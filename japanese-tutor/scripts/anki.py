"""Optional Anki bridge.

Entirely optional. The tutor has its own scheduler and knowledge base and works
with Anki absent, closed, or never installed. This only adds two things:

  * import - seed the tutor's knowledge base from decks you have already
    studied, so it does not re-teach you 2000 words you know
  * add - push a mined word into Anki, if that is where you prefer to review

Two access paths, tried in order:
  1. AnkiConnect over loopback HTTP  - works while Anki is running, can write
  2. collection.anki2 opened read-only and immutable - works while Anki is
     closed, cannot write

Licensing note: Anki is AGPL and AnkiConnect is GPL. This file only speaks to
them over a socket and reads a SQLite file - it vendors no code and imports no
Anki module, which keeps it at arm's length. Do not `pip install anki` here.

Usage:
    python anki.py status
    python anki.py decks
    python anki.py import --deck "Kaishi 1.5k" --limit 2000
    python anki.py import --deck "Kaishi 1.5k" --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlunsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb  # noqa: E402

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):  # pragma: no cover
        pass

# AnkiConnect binds to loopback and has no TLS mode. This traffic never leaves
# the machine, so transport security does not apply.
ANKI_HOST = "127.0.0.1"
ANKI_PORT = 8765
ANKI_URL = urlunsplit(("http", "%s:%d" % (ANKI_HOST, ANKI_PORT), "", "", ""))

FIELD_SEP = "\x1f"
DECK_SEP = "\x1f"

# Anki's own convention: an interval of three weeks or more means "mature".
MATURE_DAYS = 21

_TAG = re.compile(r"<[^>]+>")
_SOUND = re.compile(r"\[sound:[^\]]*\]")


def _clean(text):
    text = _SOUND.sub("", text or "")
    text = _TAG.sub("", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", text).strip()


# ---------------------------------------------------------------- AnkiConnect

def _invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params})
    request = urllib.request.Request(
        ANKI_URL, data=payload.encode("utf-8"),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=15) as response:
        body = json.loads(response.read().decode("utf-8"))
    if body.get("error"):
        raise RuntimeError(body["error"])
    return body.get("result")


def connect_available():
    try:
        return bool(_invoke("version"))
    except (urllib.error.URLError, OSError, ValueError, RuntimeError):
        return False


# ------------------------------------------------------------ collection file

def find_collection():
    configured = kb.get_profile("anki_collection")
    if configured and Path(configured).exists():
        return Path(configured)
    bases = [
        Path(os.environ.get("APPDATA") or "nonexistent") / "Anki2",
        Path.home() / ".local" / "share" / "Anki2",
        Path.home() / "Library" / "Application Support" / "Anki2",
    ]
    for base in bases:
        if base.is_dir():
            found = sorted(base.glob("*/collection.anki2"))
            if found:
                return found[0]
    return None


def _unicase(a, b):
    """Stand-in for Anki's custom collation.

    Anki registers a `unicase` collation inside its own process, so indexes that
    use it are unreadable from plain sqlite3 without an equivalent. Casefolded
    comparison is close enough for the lookups here, and we only ever read.
    """
    a, b = (a or "").casefold(), (b or "").casefold()
    return (a > b) - (a < b)


def _open_readonly(path):
    """Immutable mode: no locks taken, safe to read while Anki has the file open."""
    # as_uri() percent-escapes # and %, which a hand-built URI does not - a
    # profile directory called "User#1" would otherwise silently open a
    # different (empty) database and report that there is nothing to import.
    uri = Path(path).resolve().as_uri() + "?immutable=1"
    conn = sqlite3.connect(uri, uri=True)
    conn.create_collation("unicase", _unicase)
    return conn


def status():
    if connect_available():
        return {"mode": "connect", "writable": True,
                "detail": "Anki is running; decks readable and cards can be added."}
    collection = find_collection()
    if collection:
        return {"mode": "collection", "writable": False, "path": str(collection),
                "detail": "Anki is closed. Decks readable, but nothing can be added "
                          "until you open Anki."}
    return {"mode": "none", "writable": False,
            "detail": "No Anki found. Nothing here is required - the tutor has its "
                      "own scheduler."}


def decks():
    if connect_available():
        names = _invoke("deckNames")
        counts = {}
        for name in names:
            try:
                ids = _invoke("findCards", query='deck:"%s"' % name)
                counts[name] = len(ids)
            except RuntimeError:
                counts[name] = None
        return [{"name": n, "cards": counts.get(n)} for n in sorted(names)]

    collection = find_collection()
    if not collection:
        return []
    conn = _open_readonly(collection)
    try:
        rows = conn.execute(
            "SELECT d.name, COUNT(c.id) AS n FROM decks d "
            "LEFT JOIN cards c ON c.did = d.id GROUP BY d.id ORDER BY d.name"
        ).fetchall()
        return [{"name": name.replace(DECK_SEP, "::"), "cards": n} for name, n in rows]
    finally:
        conn.close()


def _rows_from_collection(collection, deck, limit):
    conn = _open_readonly(collection)
    try:
        like = deck.replace("::", DECK_SEP)
        deck_ids = [r[0] for r in conn.execute(
            "SELECT id FROM decks WHERE name = ? OR name LIKE ?",
            (like, like + DECK_SEP + "%"))]
        if not deck_ids:
            return None
        placeholders = ",".join("?" * len(deck_ids))
        return conn.execute(
            "SELECT n.flds, MAX(c.ivl) AS ivl, SUM(c.reps) AS reps, SUM(c.lapses) AS lapses "
            "FROM cards c JOIN notes n ON n.id = c.nid "
            "WHERE c.did IN (%s) AND c.queue != -1 "
            "GROUP BY n.id LIMIT ?" % placeholders,
            deck_ids + [limit],
        ).fetchall()
    finally:
        conn.close()


def _rows_from_connect(deck, limit):
    note_ids = _invoke("findNotes", query='deck:"%s"' % deck)[:limit]
    if not note_ids:
        return []
    infos = _invoke("notesInfo", notes=note_ids)
    card_ids = [cid for info in infos for cid in info.get("cards", [])]
    intervals = {}
    if card_ids:
        for card in _invoke("cardsInfo", cards=card_ids):
            intervals[card["cardId"]] = (card.get("interval", 0), card.get("reps", 0),
                                         card.get("lapses", 0))
    rows = []
    for info in infos:
        fields = [f["value"] for f in sorted(
            info["fields"].values(), key=lambda v: v["order"])]
        stats = [intervals.get(cid, (0, 0, 0)) for cid in info.get("cards", [])]
        ivl = max((s[0] for s in stats), default=0)
        reps = sum(s[1] for s in stats)
        lapses = sum(s[2] for s in stats)
        rows.append((FIELD_SEP.join(fields), ivl, reps, lapses))
    return rows


def import_deck(deck, limit=5000, mature_only=True, kind="vocab", dry_run=False):
    """Seed the knowledge base from a deck you have already studied.

    Only imports what the Anki data says you actually know - by default, cards
    with an interval of three weeks or more. Importing everything would tell the
    tutor you know 1500 words when you have seen 200 of them once.
    """
    if connect_available():
        rows, source_mode = _rows_from_connect(deck, limit), "connect"
    else:
        collection = find_collection()
        if not collection:
            return {"error": "No Anki found. Nothing to import - and nothing is "
                             "required; the tutor works without it."}
        rows, source_mode = _rows_from_collection(collection, deck, limit), "collection"
        if rows is None:
            available = ", ".join(d["name"] for d in decks()) or "(none)"
            return {"error": "No deck named %r. Available: %s" % (deck, available)}

    imported, skipped_immature, skipped_blank = 0, 0, 0
    samples = []
    for flds, ivl, reps, lapses in rows:
        fields = [_clean(f) for f in (flds or "").split(FIELD_SEP)]
        key = next((f for f in fields if f), None)
        if not key or len(key) > 40:
            skipped_blank += 1
            continue
        ivl = int(ivl or 0)
        if mature_only and ivl < MATURE_DAYS:
            skipped_immature += 1
            continue
        reading = fields[1] if len(fields) > 1 else None
        meaning = next((f for f in fields[2:5] if f), None)
        if len(samples) < 8:
            samples.append(key)
        if dry_run:
            imported += 1
            continue
        item_id = kb.add_item(kind, key, reading=reading or None, meaning=meaning,
                              source="anki:%s" % deck)
        if not _seed_card(item_id, kind, ivl, int(reps or 0), int(lapses or 0)):
            skipped_blank += 1
            continue
        imported += 1

    return {
        "deck": deck, "mode": source_mode, "dry_run": dry_run,
        "imported": imported,
        "skipped_not_mature": skipped_immature,
        "skipped_unusable": skipped_blank,
        "sample": samples,
        "note": "Only cards with an interval of %d days or more were treated as known."
                % MATURE_DAYS if mature_only else "All cards imported.",
    }


def _seed_card(item_id, kind, interval_days, reps, lapses):
    """Carry Anki's interval across as FSRS stability.

    Anki's interval is, by construction, roughly the point where recall drops to
    the target retention - which is what FSRS stability means. It is not an
    exact translation, but it is far better than starting a known word from zero
    and drilling it for a month.
    """
    import datetime

    stability = max(float(interval_days), 1.0)
    due = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=max(stability * 0.5, 1.0))
    # Seed whichever direction add_item actually created - it is `reading` for
    # kanji and counters, not `recognition`, and targeting the wrong one updates
    # nothing while still reporting a successful import.
    directions = kb.PRIMARY_DIRECTIONS.get(kind, ("recognition",))
    placeholders = ",".join("?" * len(directions))
    conn = kb.connect()
    with conn:
        cur = conn.execute(
            "UPDATE cards SET stability = ?, difficulty = COALESCE(difficulty, 5.0), "
            "state = 'review', due = ?, reps = ?, lapses = ? "
            "WHERE item_id = ? AND direction IN (%s)" % placeholders,
            (stability, due.isoformat(timespec="seconds"), reps, lapses, item_id)
            + tuple(directions),
        )
        updated = cur.rowcount
    conn.close()
    return updated > 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="anki.py", description="Optional Anki bridge")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    sub.add_parser("decks")
    g = sub.add_parser("import")
    g.add_argument("--deck", required=True)
    g.add_argument("--limit", type=int, default=5000)
    g.add_argument("--kind", default="vocab", choices=list(kb.ITEM_KINDS))
    g.add_argument("--all", action="store_true",
                   help="import every card, not only mature ones")
    g.add_argument("--dry-run", action="store_true")
    a = p.parse_args(argv)

    if a.cmd == "status":
        out = status()
    elif a.cmd == "decks":
        out = decks() or {"decks": [], "note": "No Anki found."}
    else:
        out = import_deck(a.deck, a.limit, not a.all, a.kind, a.dry_run)

    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
