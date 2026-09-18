"""Japanese Tutor knowledge base.

The single place that owns learner state. Skills call the named functions here
(or the CLI below) and never touch SQL themselves.

Two stores, deliberately:
  * SQLite  (state/tutor.db)     - structured, queryable: items, cards, reviews,
                                   errors, resources, plans
  * Markdown(state/memory/*.md)  - prose you should be able to read and edit by
                                   hand: preferences, feedback, goals

Standard library only. Every query is parameterized.

CLI:
    python kb.py brief                       one-screen state dump for a skill
    python kb.py due --limit 10
    python kb.py know kanji <char>
    python kb.py add-item vocab <word> --reading <kana> --meaning <gloss>
    python kb.py answer --kind vocab --key <word> --direction recognition --correct
    python kb.py error --type particle-wa-ga --output "..." --correction "..."
    python kb.py weak
    python kb.py stats
    python kb.py remember preference "Hates romaji" --body "..."
    python kb.py recall [name]
    python kb.py resources [--status active] [--topic Grammar]
    python kb.py scan-resources
"""

from __future__ import annotations

import argparse
import json
import os
import re
import hashlib
import sqlite3
import sys
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fsrs  # noqa: E402

# Japanese text must survive being piped. When stdout is a pipe rather than a
# terminal, Python on Windows falls back to the ANSI code page and raises
# UnicodeEncodeError on the first kana it meets - and skills always capture
# output. Force UTF-8 here so no caller has to remember -X utf8.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):  # pragma: no cover - very old Python
        pass

SCHEMA_VERSION = 1

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = Path(os.environ.get("JAPANESE_TUTOR_STATE") or (PLUGIN_ROOT / "state"))
DB_PATH = STATE_DIR / "tutor.db"
MEMORY_DIR = STATE_DIR / "memory"
MEMORY_INDEX = MEMORY_DIR / "MEMORY.md"

ITEM_KINDS = ("vocab", "kanji", "grammar", "phrase", "counter")
DIRECTIONS = ("recognition", "recall", "reading", "listening", "production")
MEMORY_KINDS = ("user", "feedback", "preference", "goal")
RESOURCE_STATUSES = ("active", "ignored", "unseen")

# Which directions get a card the moment an item is added. Deliberately narrow:
# creating all five up front multiplies the workload by five for no benefit.
# The rest unlock once the primary direction is genuinely stable.
PRIMARY_DIRECTIONS = {
    "vocab": ("recognition",),
    "kanji": ("reading",),
    "grammar": ("recognition",),
    "phrase": ("recognition",),
    "counter": ("reading",),
}
UNLOCKABLE = {
    "vocab": ("recall", "listening"),
    "kanji": ("recognition",),
    "grammar": ("production",),
    "phrase": ("production",),
    "counter": ("recall",),
}

DEFAULT_PROFILE = {
    "method": "mixed",
    "daily_minutes": "30",
    "new_per_day": "5",
    # 0.85 rather than 0.90: for vocabulary breadth, a lower target buys more
    # new items per unit time, which is what actually gates comprehension.
    "desired_retention": "0.85",
    "romaji": "off",
    "emoji": "off",
    "bluntness": "high",
    "unlock_after_days": "21",
    "leech_threshold": "5",
    "onboarded": "no",
}


# --------------------------------------------------------------------------
# plumbing
# --------------------------------------------------------------------------

def _now():
    return datetime.now(timezone.utc)


def _iso(dt):
    if dt is None:
        return None
    if isinstance(dt, str):
        return dt
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds")


def _parse(value):
    if not value:
        return None
    if isinstance(value, datetime):
        return value
    dt = datetime.fromisoformat(value)
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def connect():
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    # WAL lets one session read state while another is mid-write (a resource
    # scan, say) instead of blocking on it.
    try:
        conn.execute("PRAGMA journal_mode = WAL")
    except sqlite3.DatabaseError:       # network filesystem - not fatal
        pass
    return conn


def init_db():
    """Create the database and memory directory. Safe to re-run."""
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    schema = (Path(__file__).resolve().parent / "schema.sql").read_text(encoding="utf-8")
    conn = connect()
    with conn:
        conn.executescript(schema)
        conn.execute(
            "INSERT OR IGNORE INTO meta (key, value) VALUES (?, ?)",
            ("schema_version", str(SCHEMA_VERSION)),
        )
        conn.execute(
            "INSERT OR IGNORE INTO meta (key, value) VALUES (?, ?)",
            ("created", _iso(_now())),
        )
        for key, value in DEFAULT_PROFILE.items():
            conn.execute(
                "INSERT OR IGNORE INTO profile (key, value, updated) VALUES (?, ?, ?)",
                (key, value, _iso(_now())),
            )
    conn.close()
    if not MEMORY_INDEX.exists():
        _rebuild_memory_index()
    return {"db": str(DB_PATH), "memory": str(MEMORY_DIR)}


def repo_root():
    """Where Resources/ lives. Configurable, because the plugin can be
    installed outside the repo it teaches from."""
    configured = get_profile("repo_root")
    if configured:
        return Path(configured)
    env = os.environ.get("JAPANESE_TUTOR_REPO")
    if env:
        return Path(env)
    return PLUGIN_ROOT.parent


# --------------------------------------------------------------------------
# profile
# --------------------------------------------------------------------------

def get_profile(key=None, default=None):
    conn = connect()
    try:
        if key is None:
            return {r["key"]: r["value"] for r in conn.execute("SELECT key, value FROM profile")}
        row = conn.execute("SELECT value FROM profile WHERE key = ?", (key,)).fetchone()
        return row["value"] if row else default
    finally:
        conn.close()


def set_profile(key, value):
    conn = connect()
    with conn:
        conn.execute(
            "INSERT INTO profile (key, value, updated) VALUES (?, ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated = excluded.updated",
            (key, str(value), _iso(_now())),
        )
    conn.close()
    return {key: str(value)}


def _profile_number(key, default, cast=float):
    """Profile values are free-form text set by a model. Never let a typo in
    one of them raise out of a review or a state dump."""
    try:
        return cast(get_profile(key, default) or default)
    except (TypeError, ValueError):
        return cast(default)


def _retention():
    return _profile_number("desired_retention", "0.85", float)


# --------------------------------------------------------------------------
# items and cards
# --------------------------------------------------------------------------

def add_item(kind, key, reading=None, meaning=None, source=None, directions=None, **extra):
    """Register something learnable. Idempotent on (kind, key).

    Creates cards only for the primary direction(s) unless told otherwise.
    """
    if kind not in ITEM_KINDS:
        raise ValueError("kind must be one of %s" % (ITEM_KINDS,))
    conn = connect()
    with conn:
        conn.execute(
            "INSERT OR IGNORE INTO items (kind, key, reading, meaning, extra, source, first_seen) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (kind, key, reading, meaning, json.dumps(extra, ensure_ascii=False) if extra else None,
             source, _iso(_now())),
        )
        row = conn.execute(
            "SELECT id, extra FROM items WHERE kind = ? AND key = ?", (kind, key)
        ).fetchone()
        item_id = row["id"]
        # Fill in blanks on a re-add without clobbering what is already there.
        if reading or meaning or extra or source:
            merged = json.loads(row["extra"]) if row["extra"] else {}
            merged.update(extra or {})
            conn.execute(
                "UPDATE items SET reading = COALESCE(reading, ?), "
                "meaning = COALESCE(meaning, ?), source = COALESCE(source, ?), "
                "extra = ? WHERE id = ?",
                (reading, meaning, source,
                 json.dumps(merged, ensure_ascii=False) if merged else None, item_id),
            )
        for direction in (directions or PRIMARY_DIRECTIONS.get(kind, ("recognition",))):
            conn.execute(
                "INSERT OR IGNORE INTO cards (item_id, direction, state, due) VALUES (?, ?, 'new', ?)",
                (item_id, direction, _iso(_now())),
            )
    conn.close()
    return item_id


def _item_row(conn, kind=None, key=None, item_id=None):
    if item_id is not None:
        return conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    return conn.execute("SELECT * FROM items WHERE kind = ? AND key = ?", (kind, key)).fetchone()


def know(kind, key):
    """What do we know about the learner's grasp of this thing?

    Returns None if never seen, else a dict with per-direction card state and a
    plain-language `grasp` summary.
    """
    conn = connect()
    try:
        row = _item_row(conn, kind, key)
        if not row:
            return None
        cards = conn.execute(
            "SELECT * FROM cards WHERE item_id = ? ORDER BY direction", (row["id"],)
        ).fetchall()
        now = _now()
        out = {
            "id": row["id"], "kind": row["kind"], "key": row["key"],
            "reading": row["reading"], "meaning": row["meaning"],
            "source": row["source"], "first_seen": row["first_seen"],
            "extra": json.loads(row["extra"]) if row["extra"] else {},
            "directions": {},
        }
        for card in cards:
            elapsed = None
            if card["last_review"]:
                elapsed = (now - _parse(card["last_review"])).total_seconds() / 86400.0
            out["directions"][card["direction"]] = {
                "state": card["state"],
                "stability_days": round(card["stability"], 2) if card["stability"] else None,
                "difficulty": round(card["difficulty"], 2) if card["difficulty"] else None,
                "due": card["due"],
                "overdue": bool(card["due"] and _parse(card["due"]) <= now),
                "reps": card["reps"], "lapses": card["lapses"],
                "suspended": bool(card["suspended"]),
                "retrievability": round(fsrs.retrievability(card["stability"], elapsed), 3),
            }
        out["grasp"] = _grasp(out["directions"])
        return out
    finally:
        conn.close()


def _grasp(directions):
    """One honest word for how well this is known."""
    if not directions:
        return "untracked"
    stabilities = [d["stability_days"] or 0 for d in directions.values() if d["reps"]]
    if not stabilities:
        return "introduced, never tested"
    best = max(stabilities)
    lapses = sum(d["lapses"] for d in directions.values())
    if lapses >= _profile_number("leech_threshold", "5", int):
        return "leech - keeps slipping"
    if best >= 180:
        return "solid"
    if best >= 30:
        return "sticking"
    if best >= 7:
        return "shaky"
    return "fresh"


def check_kanji(char):
    return know("kanji", char)


def check_vocab(word):
    return know("vocab", word)


def check_grammar(point):
    return know("grammar", point)


def known_words(min_stability=1.0):
    """Every vocab item with any real traction. Used for i+1 coverage maths."""
    conn = connect()
    try:
        rows = conn.execute(
            "SELECT DISTINCT i.key FROM items i JOIN cards c ON c.item_id = i.id "
            "WHERE i.kind = 'vocab' AND c.reps > 0 AND COALESCE(c.stability, 0) >= ?",
            (min_stability,),
        ).fetchall()
        return {r["key"] for r in rows}
    finally:
        conn.close()


def set_item_note(kind, key, **fields):
    """Merge free-form fields into an item's `extra` JSON.

    Used for mnemonics built with the learner during leech repair, and for the
    source sentence of a mined word - both things that are worthless if they
    have to be rebuilt from scratch next session.
    """
    fields = {k: v for k, v in fields.items() if v is not None}
    if not fields:
        return {"error": "nothing to store"}
    conn = connect()
    try:
        row = _item_row(conn, kind, key)
        if not row:
            raise LookupError("no such item: %s/%s" % (kind, key))
        merged = json.loads(row["extra"]) if row["extra"] else {}
        merged.update(fields)
        with conn:
            conn.execute("UPDATE items SET extra = ? WHERE id = ?",
                         (json.dumps(merged, ensure_ascii=False), row["id"]))
        return {"item": key, "extra": merged}
    finally:
        conn.close()


def _like(text):
    """Escape LIKE wildcards. Without this, a title fragment containing _ or %
    silently matches the wrong resource."""
    escaped = (text or "").replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    return "%" + escaped + "%"


def search_items(query=None, kind=None, limit=50):
    conn = connect()
    try:
        sql = "SELECT id, kind, key, reading, meaning FROM items WHERE 1 = 1"
        params = []
        if kind:
            sql += " AND kind = ?"
            params.append(kind)
        if query:
            sql += (" AND (key LIKE ? ESCAPE '\\' OR reading LIKE ? ESCAPE '\\' "
                    "OR meaning LIKE ? ESCAPE '\\')")
            like = _like(query)
            params.extend([like, like, like])
        sql += " ORDER BY first_seen DESC LIMIT ?"
        params.append(limit)
        return [dict(r) for r in conn.execute(sql, params)]
    finally:
        conn.close()


# Sub-day learning steps must fire on the clock, but a card scheduled for a
# given day should be available all of that day in the learner's own timezone.
# Comparing review cards on an exact instant means someone who studies at 13:00
# sees an empty queue for a card scheduled at 15:00 the same day.
_DUE_PREDICATE = (
    "((c.state IN ('new', 'learning', 'relearning') "
    "  AND c.due <= strftime('%Y-%m-%dT%H:%M:%S+00:00', 'now')) "
    " OR (c.state = 'review' "
    "  AND date(c.due, 'localtime') <= date('now', 'localtime')))"
)


def due_items(limit=10, kind=None, direction=None, include_new=True):
    """What should be practised right now, most-overdue first."""
    conn = connect()
    try:
        sql = (
            "SELECT c.id AS card_id, c.direction, c.state, c.due, c.stability, c.difficulty, "
            "       c.reps, c.lapses, c.last_review, "
            "       i.id AS item_id, i.kind, i.key, i.reading, i.meaning "
            "FROM cards c JOIN items i ON i.id = c.item_id "
            "WHERE c.suspended = 0 AND c.due IS NOT NULL AND " + _DUE_PREDICATE
        )
        params = []
        if kind:
            sql += " AND i.kind = ?"
            params.append(kind)
        if direction:
            sql += " AND c.direction = ?"
            params.append(direction)
        if not include_new:
            sql += " AND c.state != 'new'"
        sql += " ORDER BY c.due ASC LIMIT ?"
        params.append(limit)
        now = _now()
        out = []
        for r in conn.execute(sql, params):
            elapsed = None
            if r["last_review"]:
                elapsed = (now - _parse(r["last_review"])).total_seconds() / 86400.0
            d = dict(r)
            d["retrievability"] = round(fsrs.retrievability(r["stability"], elapsed), 3)
            out.append(d)
        return out
    finally:
        conn.close()


def due_counts():
    conn = connect()
    try:
        rows = conn.execute(
            "SELECT i.kind, c.state, COUNT(*) AS n FROM cards c "
            "JOIN items i ON i.id = c.item_id "
            "WHERE c.suspended = 0 AND c.due IS NOT NULL AND " + _DUE_PREDICATE +
            " GROUP BY i.kind, c.state"
        ).fetchall()
        out = {}
        for r in rows:
            bucket = out.setdefault(r["kind"], {"new": 0, "review": 0})
            bucket["new" if r["state"] == "new" else "review"] += r["n"]
        return out
    finally:
        conn.close()


def record_answer(direction, correct, kind=None, key=None, item_id=None, rating=None,
                  given=None, expected=None, latency_ms=None, session_id=None):
    """Log one answer and reschedule the card.

    `rating` is the FSRS 1-4 scale. If omitted it is derived from `correct`,
    which is the common case for a conversational tutor that is judging
    right/wrong rather than asking the learner to self-grade.
    """
    if direction not in DIRECTIONS:
        raise ValueError("direction must be one of %s" % (DIRECTIONS,))
    if rating is not None:
        # An explicit rating is the stronger signal - derive correctness from it
        # so the review log cannot record "correct" on a card FSRS just lapsed.
        rating = int(rating)
        correct = rating >= fsrs.GOOD
    else:
        correct = bool(int(correct)) if not isinstance(correct, bool) else correct
        rating = fsrs.GOOD if correct else fsrs.AGAIN

    conn = connect()
    try:
        item = _item_row(conn, kind, key, item_id)
        if not item:
            raise LookupError("no such item: %s/%s" % (kind, key))
        with conn:
            conn.execute(
                "INSERT OR IGNORE INTO cards (item_id, direction, state, due) "
                "VALUES (?, ?, 'new', ?)",
                (item["id"], direction, _iso(_now())),
            )
        card = conn.execute(
            "SELECT * FROM cards WHERE item_id = ? AND direction = ?",
            (item["id"], direction),
        ).fetchone()

        updated = fsrs.review(
            {
                "stability": card["stability"], "difficulty": card["difficulty"],
                "last_review": card["last_review"], "reps": card["reps"],
                "lapses": card["lapses"], "state": card["state"],
            },
            rating,
            desired_retention=_retention(),
        )
        with conn:
            conn.execute(
                "UPDATE cards SET stability = ?, difficulty = ?, due = ?, last_review = ?, "
                "reps = ?, lapses = ?, state = ? WHERE id = ?",
                (updated["stability"], updated["difficulty"], _iso(updated["due"]),
                 _iso(updated["last_review"]), updated["reps"], updated["lapses"],
                 updated["state"], card["id"]),
            )
            conn.execute(
                "INSERT INTO reviews (card_id, ts, rating, correct, given, expected, "
                "latency_ms, elapsed_days, stability_after, session_id) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (card["id"], _iso(updated["last_review"]), rating, 1 if correct else 0,
                 given, expected, latency_ms, updated["elapsed_days"],
                 updated["stability"], session_id),
            )
    finally:
        conn.close()

    unlocked = _maybe_unlock(item["id"], item["kind"])
    return {
        "item": item["key"], "direction": direction, "rating": rating,
        "correct": correct,
        "stability_days": round(updated["stability"], 2),
        "next_due": _iso(updated["due"]),
        "next_in_days": round((updated["due"] - updated["last_review"]).total_seconds() / 86400, 2),
        "state": updated["state"],
        "lapses": updated["lapses"],
        "unlocked": unlocked,
    }


def _maybe_unlock(item_id, kind):
    """Open up harder directions once the primary one is genuinely stable.

    Production is the direction that matters and the one every recognition-only
    deck neglects - but unlocking it on day one just multiplies the workload.
    """
    threshold = _profile_number("unlock_after_days", "21", float)
    candidates = UNLOCKABLE.get(kind, ())
    if not candidates:
        return []
    conn = connect()
    try:
        primary = conn.execute(
            "SELECT MAX(stability) AS s FROM cards WHERE item_id = ? AND direction IN (%s)"
            % ",".join("?" * len(PRIMARY_DIRECTIONS.get(kind, ("recognition",)))),
            (item_id,) + tuple(PRIMARY_DIRECTIONS.get(kind, ("recognition",))),
        ).fetchone()
        if not primary or not primary["s"] or primary["s"] < threshold:
            return []
        opened = []
        with conn:
            for direction in candidates:
                exists = conn.execute(
                    "SELECT 1 FROM cards WHERE item_id = ? AND direction = ?",
                    (item_id, direction),
                ).fetchone()
                if not exists:
                    conn.execute(
                        "INSERT INTO cards (item_id, direction, state, due) VALUES (?, ?, 'new', ?)",
                        (item_id, direction, _iso(_now())),
                    )
                    opened.append(direction)
        return opened
    finally:
        conn.close()


def suspend(kind, key, direction=None, suspended=True):
    conn = connect()
    try:
        item = _item_row(conn, kind, key)
        if not item:
            raise LookupError("no such item: %s/%s" % (kind, key))
        with conn:
            if direction:
                conn.execute(
                    "UPDATE cards SET suspended = ? WHERE item_id = ? AND direction = ?",
                    (1 if suspended else 0, item["id"], direction),
                )
            else:
                conn.execute("UPDATE cards SET suspended = ? WHERE item_id = ?",
                             (1 if suspended else 0, item["id"]))
        return {"item": key, "suspended": suspended}
    finally:
        conn.close()


# --------------------------------------------------------------------------
# errors, weak points, interference
# --------------------------------------------------------------------------

def record_error(error_type, learner_output=None, correction=None, kind=None, key=None,
                 item_id=None, context=None, session_id=None):
    """Log a classified mistake. error_type comes from references/error-taxonomy.md."""
    conn = connect()
    try:
        if item_id is None and kind and key:
            row = _item_row(conn, kind, key)
            item_id = row["id"] if row else None
        with conn:
            conn.execute(
                "INSERT INTO errors (ts, error_type, item_id, learner_output, correction, "
                "context, session_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (_iso(_now()), error_type, item_id, learner_output, correction,
                 context, session_id),
            )
        return {"logged": error_type, "item_id": item_id}
    finally:
        conn.close()


def weak_points(n=10, days=60):
    """The recurring mistakes and the items that keep slipping.

    This - not the review queue - is what should drive what gets re-taught.
    """
    since = _iso(_now() - timedelta(days=days))
    threshold = _profile_number("leech_threshold", "5", int)
    conn = connect()
    try:
        patterns = [
            dict(r) for r in conn.execute(
                "SELECT error_type, COUNT(*) AS hits, MAX(ts) AS last_seen FROM errors "
                "WHERE ts >= ? GROUP BY error_type ORDER BY hits DESC, last_seen DESC LIMIT ?",
                (since, n),
            )
        ]
        leeches = [
            dict(r) for r in conn.execute(
                "SELECT i.kind, i.key, i.reading, i.meaning, c.direction, c.lapses "
                "FROM cards c JOIN items i ON i.id = c.item_id "
                "WHERE c.lapses >= ? ORDER BY c.lapses DESC LIMIT ?",
                (threshold, n),
            )
        ]
        lagging = [
            dict(r) for r in conn.execute(
                "SELECT i.kind, i.key, c.direction, c.stability FROM cards c "
                "JOIN items i ON i.id = c.item_id "
                "WHERE c.direction IN ('production', 'recall') AND c.reps > 0 "
                "ORDER BY c.stability ASC LIMIT ?",
                (n,),
            )
        ]
        return {"patterns": patterns, "leeches": leeches, "weakest_production": lagging}
    finally:
        conn.close()


def error_log(limit=200, days=90, error_type=None):
    """Raw classified mistakes, newest first, with the learner's own wording."""
    since = _iso(_now() - timedelta(days=days))
    conn = connect()
    try:
        sql = ("SELECT e.ts, e.error_type, e.learner_output, e.correction, e.context, "
               "       i.kind, i.key, i.reading, i.meaning "
               "FROM errors e LEFT JOIN items i ON i.id = e.item_id "
               "WHERE e.ts >= ?")
        params = [since]
        if error_type:
            sql += " AND e.error_type = ?"
            params.append(error_type)
        sql += " ORDER BY e.ts DESC LIMIT ?"
        params.append(limit)
        return [dict(r) for r in conn.execute(sql, params)]
    finally:
        conn.close()


def review_log(limit=200, days=90, wrong_only=True, direction=None):
    """Raw answers. `given` vs `expected` is what makes confusable pairs findable."""
    since = _iso(_now() - timedelta(days=days))
    conn = connect()
    try:
        sql = ("SELECT r.ts, r.rating, r.correct, r.given, r.expected, r.elapsed_days, "
               "       c.direction, i.kind, i.key, i.reading, i.meaning "
               "FROM reviews r JOIN cards c ON c.id = r.card_id "
               "JOIN items i ON i.id = c.item_id WHERE r.ts >= ?")
        params = [since]
        if wrong_only:
            sql += " AND r.correct = 0"
        if direction:
            sql += " AND c.direction = ?"
            params.append(direction)
        sql += " ORDER BY r.ts DESC LIMIT ?"
        params.append(limit)
        return [dict(r) for r in conn.execute(sql, params)]
    finally:
        conn.close()


def add_confusion(kind, key_a, key_b, reason="observed"):
    conn = connect()
    try:
        a = _item_row(conn, kind, key_a)
        b = _item_row(conn, kind, key_b)
        if not a or not b:
            raise LookupError("both items must exist before linking them")
        lo, hi = sorted((a["id"], b["id"]))
        with conn:
            conn.execute(
                "INSERT INTO confusions (a_id, b_id, reason, hits, last_hit) VALUES (?, ?, ?, 1, ?) "
                "ON CONFLICT(a_id, b_id) DO UPDATE SET hits = hits + 1, last_hit = excluded.last_hit",
                (lo, hi, reason, _iso(_now())),
            )
        return {"linked": [key_a, key_b], "reason": reason}
    finally:
        conn.close()


def confusion_pairs(limit=20):
    """Every pair the learner has actually been seen to confuse, worst first.

    This is what makes the side-by-side discrimination drill possible. Spaced
    repetition schedules confusable items independently, so it never presents
    the pair together and the collision stays invisible - listing them here is
    the whole point.
    """
    conn = connect()
    try:
        rows = conn.execute(
            "SELECT a.kind AS kind, a.key AS a_key, b.key AS b_key, a.reading AS a_reading, "
            "       b.reading AS b_reading, c.reason, c.hits, c.last_hit "
            "FROM confusions c "
            "JOIN items a ON a.id = c.a_id "
            "JOIN items b ON b.id = c.b_id "
            "ORDER BY c.hits DESC, c.last_hit DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def confusables(kind=None, key=None, item_id=None, limit=10):
    """Items the learner is likely to mix up with this one.

    Two sources: pairs explicitly observed colliding, and structural overlap
    (shared kanji characters). SRS schedules confusable items independently and
    so actively hides these collisions; this is how we find them anyway.
    """
    conn = connect()
    try:
        item = _item_row(conn, kind, key, item_id)
        if not item:
            return []
        out = []
        for r in conn.execute(
            "SELECT c.reason, c.hits, i.kind, i.key, i.reading, i.meaning FROM confusions c "
            "JOIN items i ON i.id = CASE WHEN c.a_id = ? THEN c.b_id ELSE c.a_id END "
            "WHERE c.a_id = ? OR c.b_id = ? ORDER BY c.hits DESC LIMIT ?",
            (item["id"], item["id"], item["id"], limit),
        ):
            out.append({**dict(r), "source": "observed"})

        chars = {ch for ch in item["key"] if _is_kanji(ch)}
        if chars:
            seen = {c["key"] for c in out}
            for r in conn.execute(
                "SELECT kind, key, reading, meaning FROM items WHERE id != ? AND kind = ?",
                (item["id"], item["kind"]),
            ):
                if r["key"] in seen:
                    continue
                overlap = chars & {ch for ch in r["key"] if _is_kanji(ch)}
                if overlap:
                    out.append({**dict(r), "reason": "shares " + "".join(sorted(overlap)),
                                "hits": 0, "source": "structural"})
                if len(out) >= limit:
                    break
        return out[:limit]
    finally:
        conn.close()


def _is_kanji(ch):
    return "CJK UNIFIED" in unicodedata.name(ch, "")


# --------------------------------------------------------------------------
# sessions
# --------------------------------------------------------------------------

def start_session(method=None):
    conn = connect()
    with conn:
        cur = conn.execute(
            "INSERT INTO sessions (started, method) VALUES (?, ?)",
            (_iso(_now()), method or get_profile("method", "mixed")),
        )
    session_id = cur.lastrowid
    conn.close()
    return {"session_id": session_id}


def end_session(summary=None, session_id=None):
    conn = connect()
    try:
        if session_id is None:
            row = conn.execute(
                "SELECT id FROM sessions WHERE ended IS NULL ORDER BY id DESC LIMIT 1"
            ).fetchone()
            if not row:
                return {"closed": None}
            session_id = row["id"]
        with conn:
            conn.execute("UPDATE sessions SET ended = ?, summary = ? WHERE id = ?",
                         (_iso(_now()), summary, session_id))
        return {"closed": session_id}
    finally:
        conn.close()


# --------------------------------------------------------------------------
# stats
# --------------------------------------------------------------------------

def stats():
    conn = connect()
    try:
        counts = {r["kind"]: r["n"] for r in conn.execute(
            "SELECT kind, COUNT(*) AS n FROM items GROUP BY kind")}
        directions = {r["direction"]: r["n"] for r in conn.execute(
            "SELECT direction, COUNT(*) AS n FROM cards WHERE reps > 0 GROUP BY direction")}
        stability = {r["direction"]: round(r["s"] or 0, 1) for r in conn.execute(
            "SELECT direction, AVG(stability) AS s FROM cards WHERE reps > 0 GROUP BY direction")}
        since = _iso(_now() - timedelta(days=30))
        row = conn.execute(
            "SELECT COUNT(*) AS n, SUM(correct) AS ok FROM reviews WHERE ts >= ?", (since,)
        ).fetchone()
        reviewed = row["n"] or 0
        # Local days, not UTC days: otherwise an evening session in UTC+9 is
        # filed under the next day and streaks break for morning studiers.
        today = conn.execute(
            "SELECT COUNT(*) AS n FROM reviews "
            "WHERE date(ts, 'localtime') = date('now', 'localtime')"
        ).fetchone()["n"]
        days = [r["d"] for r in conn.execute(
            "SELECT DISTINCT date(ts, 'localtime') AS d FROM reviews "
            "ORDER BY d DESC LIMIT 400")]
        return {
            "items": counts,
            "items_total": sum(counts.values()),
            "cards_practised_by_direction": directions,
            "mean_stability_days_by_direction": stability,
            "reviews_30d": reviewed,
            "retention_30d": round((row["ok"] or 0) / reviewed, 3) if reviewed else None,
            "reviews_today": today,
            "streak_days": _streak(days),
            "due_now": due_counts(),
        }
    finally:
        conn.close()


def _streak(days):
    if not days:
        return 0
    today = _now().date()
    streak = 0
    for offset in range(len(days) + 1):
        day = (today - timedelta(days=offset)).isoformat()
        if day in days:
            streak += 1
        elif offset > 0 or day not in days:
            if offset == 0:
                continue          # nothing today yet; a streak can still be alive
            break
    return streak


# --------------------------------------------------------------------------
# memory - markdown, not database rows
# --------------------------------------------------------------------------

def _slug(text):
    """Filesystem-safe name for a memory.

    Japanese titles contain no ASCII, so a naive strip collapses every one of
    them to the same name and each new memory silently destroys the last. When
    nothing survives, fall back to a short digest of the title so distinct
    titles keep distinct files.
    """
    normalised = unicodedata.normalize("NFKD", text or "")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalised).strip("-").lower()
    if not slug:
        # Non-security use: this is a filename disambiguator, not a digest of
        # anything sensitive.
        digest = hashlib.sha256((text or "").encode("utf-8")).hexdigest()[:10]
        return "note-%s" % digest
    return slug[:60]


def remember(kind, title, body, name=None, why=None, how=None):
    """Write a durable note about the learner.

    For things the database already answers (counts, error rates) this is the
    wrong tool - those are queries, not memories.
    """
    if kind not in MEMORY_KINDS:
        raise ValueError("kind must be one of %s" % (MEMORY_KINDS,))
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    # Always slug: a caller-supplied name must not be able to escape the
    # memory directory, and a multi-line title must not be able to forge
    # extra frontmatter keys.
    name = _slug(name or title)
    flat_title = " ".join((title or "").split())
    path = MEMORY_DIR / ("%s.md" % name)
    lines = [
        "---",
        "name: %s" % name,
        "kind: %s" % kind,
        "title: %s" % flat_title,
        "created: %s" % _now().date().isoformat(),
        "---",
        "",
        body.strip(),
    ]
    if why:
        lines += ["", "**Why:** %s" % why.strip()]
    if how:
        lines += ["", "**How to apply:** %s" % how.strip()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    _rebuild_memory_index()
    return {"saved": str(path), "name": name, "kind": kind}


def _read_memory(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        for line in fm.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta, body.strip()


def recall(name=None):
    """No name: the index. With a name: that memory's full text."""
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    if name:
        path = MEMORY_DIR / ("%s.md" % name)
        if not path.exists():
            return None
        meta, body = _read_memory(path)
        return {"name": name, **meta, "body": body}
    out = []
    for path in sorted(MEMORY_DIR.glob("*.md")):
        if path.name == "MEMORY.md":
            continue
        meta, body = _read_memory(path)
        first = next((ln for ln in body.splitlines() if ln.strip()), "")
        out.append({
            "name": meta.get("name", path.stem),
            "kind": meta.get("kind", "user"),
            "title": meta.get("title", path.stem),
            "summary": first[:160],
        })
    return out


def forget(name):
    path = MEMORY_DIR / ("%s.md" % _slug(name))
    if not path.exists():
        return {"forgot": None}
    path.unlink()
    _rebuild_memory_index()
    return {"forgot": name}


def _rebuild_memory_index():
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    entries = recall()
    lines = [
        "# What the tutor remembers about you",
        "",
        "One line per memory. Full text is in the linked file - edit or delete any of them",
        "by hand; the tutor re-reads this directory every session.",
        "",
    ]
    if not entries:
        lines.append("_Nothing yet._")
    else:
        for kind in MEMORY_KINDS:
            group = [e for e in entries if e["kind"] == kind]
            if not group:
                continue
            lines.append("## %s" % kind)
            for e in group:
                lines.append("- [%s](%s.md) - %s" % (e["title"], e["name"], e["summary"]))
            lines.append("")
    MEMORY_INDEX.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


# --------------------------------------------------------------------------
# resource catalogue
# --------------------------------------------------------------------------

_EXT_KIND = {
    ".pdf": "book", ".epub": "book", ".apkg": "deck", ".colpkg": "deck",
    ".md": "guide", ".html": "site", ".htm": "site", ".txt": "guide",
    ".xlsx": "list", ".ods": "list", ".csv": "list",
    ".mp3": "audio", ".flac": "audio", ".m4a": "audio", ".mp4": "video",
}


def _kind_for(path_str):
    lower = path_str.lower()
    for ext, kind in _EXT_KIND.items():
        if lower.endswith(ext):
            return kind
    return "folder"


def scan_resources(max_entries_per_topic=60):
    """Rebuild the catalogue from Resources/.

    Additive and idempotent: existing statuses, priorities and positions are
    never touched, and anything new lands as 'unseen' so it surfaces for a
    decision rather than silently joining what you study from.
    """
    root = repo_root()
    resources_dir = root / "Resources"
    if not resources_dir.is_dir():
        return {"error": "no Resources/ directory under %s" % root, "added": 0}

    found = []
    for topic_dir in sorted(p for p in resources_dir.iterdir() if p.is_dir()):
        topic = topic_dir.name
        found.append((
            _rel(topic_dir, root), topic, topic, "folder",
            "Topic folder",
        ))
        for sub in sorted(p for p in topic_dir.iterdir())[:max_entries_per_topic]:
            if sub.name.lower() in ("readme.md", "readme.markdown"):
                continue
            found.append((
                _rel(sub, root), sub.name, topic,
                "folder" if sub.is_dir() else _kind_for(sub.name), None,
            ))
        readme = next((p for p in topic_dir.iterdir()
                       if p.is_file() and p.name.lower() == "readme.md"), None)
        if readme:
            found.extend(_parse_readme(readme, topic, root, max_entries_per_topic))

    # Same path can be reached twice (listed as a subfolder and linked from the
    # readme). First mention wins, so the counts below mean what they say.
    deduped = {}
    for entry in found:
        deduped.setdefault(entry[0], entry)

    conn = connect()
    added = updated = 0
    with conn:
        for path, title, topic, kind, notes in deduped.values():
            cur = conn.execute(
                "INSERT OR IGNORE INTO resources (path, title, topic, kind, status, notes, added) "
                "VALUES (?, ?, ?, ?, 'unseen', ?, ?)",
                (path, title, topic, kind, notes, _iso(_now())),
            )
            if cur.rowcount:
                added += 1
            else:
                # Refresh descriptive fields only. Never status/priority/position.
                cur2 = conn.execute(
                    "UPDATE resources SET title = ?, topic = ?, kind = ?, "
                    "notes = COALESCE(?, notes), updated = ? WHERE path = ?",
                    (title, topic, kind, notes, _iso(_now()), path),
                )
                updated += cur2.rowcount
    total = conn.execute("SELECT COUNT(*) AS n FROM resources").fetchone()["n"]
    conn.close()
    return {"added": added, "refreshed": updated, "total": total,
            "unseen": len(list_resources(status="unseen"))}


def _rel(path, root):
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


_LINK = re.compile(r"\[([^\]]{1,120})\]\(([^)\s]+)\)")


def _parse_readme(readme, topic, root, cap):
    """Pull resource links out of a topic guide.

    These readmes are written by a separate process, so parse defensively:
    take what looks like a resource, ignore everything else.
    """
    out = []
    try:
        text = readme.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    for title, target in _LINK.findall(text)[: cap * 3]:
        title = title.strip()
        if not title or target.startswith("#"):
            continue
        scheme = urlsplit(target).scheme.lower()
        if scheme:
            # Only TLS-protected links are catalogued as usable. A plain-HTTP
            # link is recorded but flagged, and the fetcher refuses it.
            if scheme != "https":
                out.append((target, title, topic, "site",
                            "insecure or unsupported scheme (%s) - not fetchable" % scheme))
            else:
                out.append((target, title, topic, "site", "linked from %s" % topic))
            continue
        candidate = (readme.parent / unquote(target)).resolve()
        # A readme can link anywhere; only catalogue things inside the library.
        try:
            inside = candidate.is_relative_to(root.resolve())
        except AttributeError:            # Python 3.8
            inside = str(candidate).startswith(str(root.resolve()))
        if candidate.exists() and inside:
            out.append((_rel(candidate, root), title, topic,
                        "folder" if candidate.is_dir() else _kind_for(candidate.name),
                        "linked from %s" % topic))
        if len(out) >= cap:
            break
    return out


def list_resources(status=None, topic=None, limit=500):
    conn = connect()
    try:
        sql = "SELECT * FROM resources WHERE 1 = 1"
        params = []
        if status:
            sql += " AND status = ?"
            params.append(status)
        if topic:
            sql += " AND topic = ?"
            params.append(topic)
        sql += " ORDER BY priority DESC, topic, title LIMIT ?"
        params.append(limit)
        return [dict(r) for r in conn.execute(sql, params)]
    finally:
        conn.close()


def resource_summary():
    """Compact per-topic table for skill injection.

    Lives here rather than as a shell one-liner in a SKILL.md so it is testable
    and cannot silently break on quoting.
    """
    rows = list_resources(limit=5000)
    if not rows:
        return "No resources catalogued yet - run `scripts/setup.py`.\n"
    topics = {}
    for r in rows:
        bucket = topics.setdefault(r["topic"] or "(untopiced)", {"active": 0, "ignored": 0,
                                                                 "unseen": 0})
        bucket[r["status"]] = bucket.get(r["status"], 0) + 1
    lines = ["| topic | active | unseen | ignored |", "|---|---|---|---|"]
    for topic in sorted(topics):
        b = topics[topic]
        lines.append("| %s | %d | %d | %d |"
                     % (topic, b["active"], b["unseen"], b["ignored"]))
    total_active = sum(b["active"] for b in topics.values())
    lines.append("")
    if total_active:
        lines.append("Active right now:")
        for r in active_resources():
            pos = " (at %s)" % r["position"] if r["position"] else ""
            lines.append("- %s - `%s`%s" % (r["title"], r["path"], pos))
    else:
        lines.append("**Nothing is switched on yet.** The tutor has no material to teach from.")
    return "\n".join(lines) + "\n"


def active_resources(topic=None):
    """The only material the tutor is allowed to teach from."""
    return list_resources(status="active", topic=topic)


def set_resource_status(path, status, priority=None):
    if status not in RESOURCE_STATUSES:
        raise ValueError("status must be one of %s" % (RESOURCE_STATUSES,))
    conn = connect()
    try:
        with conn:
            cur = conn.execute(
                "UPDATE resources SET status = ?, priority = COALESCE(?, priority), updated = ? "
                "WHERE path = ?",
                (status, priority, _iso(_now()), path),
            )
            if not cur.rowcount:
                # Allow matching on a unique title fragment - paths are long.
                rows = conn.execute(
                    "SELECT path FROM resources WHERE title LIKE ? ESCAPE '\\' "
                    "OR path LIKE ? ESCAPE '\\'",
                    (_like(path), _like(path)),
                ).fetchall()
                if len(rows) != 1:
                    return {"error": "no unique match for %r (%d candidates)" % (path, len(rows))}
                conn.execute(
                    "UPDATE resources SET status = ?, priority = COALESCE(?, priority), "
                    "updated = ? WHERE path = ?",
                    (status, priority, _iso(_now()), rows[0]["path"]),
                )
                path = rows[0]["path"]
        return {"path": path, "status": status}
    finally:
        conn.close()


def add_resource(path, title, topic=None, kind=None, notes=None, status="active"):
    conn = connect()
    with conn:
        conn.execute(
            "INSERT OR IGNORE INTO resources (path, title, topic, kind, status, notes, added) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (path, title, topic, kind or _kind_for(path), status, notes, _iso(_now())),
        )
        conn.execute(
            "UPDATE resources SET title = ?, topic = COALESCE(?, topic), status = ?, "
            "notes = COALESCE(?, notes), updated = ? WHERE path = ?",
            (title, topic, status, notes, _iso(_now()), path),
        )
    conn.close()
    return {"path": path, "title": title, "status": status}


def set_resource_position(path, position, note=None):
    conn = connect()
    try:
        with conn:
            cur = conn.execute(
                "UPDATE resources SET position = ?, notes = COALESCE(?, notes), updated = ? "
                "WHERE path = ?",
                (position, note, _iso(_now()), path),
            )
            if not cur.rowcount:
                rows = conn.execute(
                    "SELECT path FROM resources WHERE title LIKE ? ESCAPE '\\'",
                    (_like(path),)).fetchall()
                if len(rows) != 1:
                    return {"error": "no unique match for %r" % path}
                conn.execute("UPDATE resources SET position = ?, updated = ? WHERE path = ?",
                             (position, _iso(_now()), rows[0]["path"]))
                path = rows[0]["path"]
        return {"path": path, "position": position}
    finally:
        conn.close()


def get_resource_progress(path=None):
    rows = [r for r in active_resources() if r["position"]]
    if path:
        rows = [r for r in rows if path in r["path"] or path in r["title"]]
    return rows


# --------------------------------------------------------------------------
# plans (opt-in)
# --------------------------------------------------------------------------

def create_plan(goal, steps, horizon=None, notes=None):
    if not isinstance(steps, (list, tuple)) or not steps:
        raise ValueError("steps must be a non-empty list")
    steps = [s if isinstance(s, dict) else {"title": str(s)} for s in steps]
    conn = connect()
    with conn:
        conn.execute("UPDATE plans SET active = 0 WHERE active = 1")
        cur = conn.execute(
            "INSERT INTO plans (created, goal, horizon, steps, notes) VALUES (?, ?, ?, ?, ?)",
            (_iso(_now()), goal, horizon, json.dumps(steps, ensure_ascii=False), notes),
        )
    plan_id = cur.lastrowid
    conn.close()
    return {"plan_id": plan_id, "goal": goal, "steps": len(steps)}


def active_plan():
    conn = connect()
    try:
        row = conn.execute(
            "SELECT * FROM plans WHERE active = 1 ORDER BY id DESC LIMIT 1").fetchone()
        if not row:
            return None
        plan = dict(row)
        plan["steps"] = json.loads(row["steps"])
        return plan
    finally:
        conn.close()


def advance_plan(step=None):
    plan = active_plan()
    if not plan:
        return {"error": "no active plan"}
    step = plan["current_step"] + 1 if step is None else int(step)
    step = max(0, min(step, len(plan["steps"])))      # never index backwards
    conn = connect()
    with conn:
        conn.execute("UPDATE plans SET current_step = ? WHERE id = ?", (step, plan["id"]))
    conn.close()
    return {"plan_id": plan["id"], "current_step": step, "of": len(plan["steps"])}


def deactivate_plan():
    conn = connect()
    with conn:
        cur = conn.execute("UPDATE plans SET active = 0 WHERE active = 1")
    conn.close()
    return {"deactivated": cur.rowcount}


# --------------------------------------------------------------------------
# brief - the one-shot state dump every skill opens with
# --------------------------------------------------------------------------

def brief():
    """Compact markdown. This lands in context on every skill invocation, so it
    stays short on purpose."""
    prof = get_profile()
    if prof.get("onboarded") != "yes":
        return ("## Tutor state\n\nNot set up yet - no profile, no level estimate, "
                "no resources chosen.\n**Run `/japanese-tutor:onboard` first.**\n")

    s = stats()
    lines = ["## Tutor state", ""]
    lines.append("Method **%s** | %s min/day | %s new/day | retention %s | romaji %s"
                 % (prof.get("method"), prof.get("daily_minutes"), prof.get("new_per_day"),
                    prof.get("desired_retention"), prof.get("romaji")))
    if prof.get("level_estimate"):
        lines.append("Level: %s" % prof["level_estimate"])
    lines.append("")

    lines.append("**Known:** " + (", ".join("%s %s" % (v, k) for k, v in
                                            sorted(s["items"].items())) or "nothing yet"))
    due = s["due_now"]
    if due:
        parts = []
        for kind, b in sorted(due.items()):
            bits = []
            if b["review"]:
                bits.append("%d due" % b["review"])
            if b["new"]:
                bits.append("%d new" % b["new"])
            if bits:
                parts.append("%s: %s" % (kind, ", ".join(bits)))
        lines.append("**Waiting:** " + ("; ".join(parts) if parts else "nothing"))
    else:
        lines.append("**Waiting:** nothing")
    lines.append("**Activity:** %d reviews today, %d in 30d, retention %s, streak %d days"
                 % (s["reviews_today"], s["reviews_30d"],
                    s["retention_30d"] if s["retention_30d"] is not None else "n/a",
                    s["streak_days"]))

    stab = s["mean_stability_days_by_direction"]
    if stab:
        lines.append("**Mean stability by direction:** "
                     + ", ".join("%s %sd" % (k, v) for k, v in sorted(stab.items())))

    w = weak_points(n=5)
    if w["patterns"]:
        lines.append("")
        lines.append("**Recurring mistakes:** "
                     + ", ".join("%s (x%d)" % (p["error_type"], p["hits"]) for p in w["patterns"]))
    if w["leeches"]:
        lines.append("**Leeches:** "
                     + ", ".join("%s" % l["key"] for l in w["leeches"][:8]))

    res = active_resources()
    lines.append("")
    if res:
        lines.append("**Active resources (%d):**" % len(res))
        for r in res[:12]:
            pos = " - at %s" % r["position"] if r["position"] else ""
            lines.append("- %s (%s)%s" % (r["title"], r["topic"] or "?", pos))
        if len(res) > 12:
            lines.append("- ...and %d more" % (len(res) - 12))
    else:
        lines.append("**Active resources:** none chosen yet "
                     "(run `/japanese-tutor:resources`)")

    unseen = len(list_resources(status="unseen"))
    if unseen:
        lines.append("_%d catalogued resources are still unreviewed._" % unseen)

    plan = active_plan()
    lines.append("")
    if plan:
        step = plan["current_step"]
        steps = plan["steps"]
        # Steps are free-form JSON from the caller, so never assume a dict here -
        # a malformed plan must not be able to break every skill's state dump.
        if 0 <= step < len(steps):
            entry = steps[step]
            current = (entry.get("title", "step %d" % (step + 1))
                       if isinstance(entry, dict) else str(entry))
        else:
            current = "finished"
        lines.append("**Active plan:** %s - step %d/%d: %s"
                     % (plan["goal"], step + 1, len(steps), current))
    else:
        lines.append("**Active plan:** none (free-flowing; `/japanese-tutor:plan` to make one)")

    mem = recall()
    if mem:
        lines.append("")
        lines.append("**Remembered about you:**")
        for m in mem[:14]:
            lines.append("- [%s] %s: %s" % (m["kind"], m["title"], m["summary"]))
        if len(mem) > 14:
            lines.append("- ...and %d more (`kb.py recall`)" % (len(mem) - 14))

    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _emit(value):
    if isinstance(value, str):
        sys.stdout.write(value)
    else:
        sys.stdout.write(json.dumps(value, ensure_ascii=False, indent=2, default=str) + "\n")


def main(argv=None):
    p = argparse.ArgumentParser(prog="kb.py", description="Japanese Tutor knowledge base")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")
    sub.add_parser("brief")
    sub.add_parser("stats")
    sub.add_parser("scan-resources")

    g = sub.add_parser("profile")
    g.add_argument("key", nargs="?")
    g.add_argument("value", nargs="?")

    g = sub.add_parser("due")
    g.add_argument("--limit", type=int, default=10)
    g.add_argument("--kind")
    g.add_argument("--direction")

    g = sub.add_parser("know")
    g.add_argument("kind")
    g.add_argument("key")

    g = sub.add_parser("add-item")
    g.add_argument("kind")
    g.add_argument("key")
    g.add_argument("--reading")
    g.add_argument("--meaning")
    g.add_argument("--source")
    g.add_argument("--directions", help="comma-separated; defaults to the primary one")
    g.add_argument("--sentence", help="the sentence it was met in - shown in later reviews")
    g.add_argument("--mnemonic")
    g.add_argument("--note")

    g = sub.add_parser("item-note")
    g.add_argument("kind")
    g.add_argument("key")
    g.add_argument("--sentence")
    g.add_argument("--mnemonic")
    g.add_argument("--note")

    g = sub.add_parser("known-words")
    g.add_argument("--min-stability", type=float, default=1.0)

    g = sub.add_parser("suspend")
    g.add_argument("kind")
    g.add_argument("key")
    g.add_argument("--direction", choices=DIRECTIONS)
    g.add_argument("--unsuspend", action="store_true")

    g = sub.add_parser("answer")
    g.add_argument("--kind", required=True)
    g.add_argument("--key", required=True)
    g.add_argument("--direction", default="recognition")
    g.add_argument("--correct", dest="correct", action="store_true")
    g.add_argument("--wrong", dest="correct", action="store_false")
    g.set_defaults(correct=True)
    g.add_argument("--rating", type=int)
    g.add_argument("--given")
    g.add_argument("--expected")
    g.add_argument("--session", type=int)

    g = sub.add_parser("error")
    g.add_argument("--type", required=True, dest="error_type")
    g.add_argument("--output", dest="learner_output")
    g.add_argument("--correction")
    g.add_argument("--kind")
    g.add_argument("--key")
    g.add_argument("--context")

    g = sub.add_parser("weak")
    g.add_argument("--limit", type=int, default=10)

    g = sub.add_parser("log-errors")
    g.add_argument("--limit", type=int, default=200)
    g.add_argument("--days", type=int, default=90)
    g.add_argument("--type", dest="error_type")

    g = sub.add_parser("log-reviews")
    g.add_argument("--limit", type=int, default=200)
    g.add_argument("--days", type=int, default=90)
    g.add_argument("--direction", choices=DIRECTIONS)
    g.add_argument("--all", action="store_true", help="include correct answers too")

    g = sub.add_parser("confusables")
    g.add_argument("kind", nargs="?", help="omit both to list every known pair")
    g.add_argument("key", nargs="?")
    g.add_argument("--limit", type=int, default=20)

    g = sub.add_parser("confuse")
    g.add_argument("kind")
    g.add_argument("key_a")
    g.add_argument("key_b")
    g.add_argument("--reason", default="observed")

    g = sub.add_parser("search")
    g.add_argument("query", nargs="?")
    g.add_argument("--kind")

    g = sub.add_parser("remember")
    g.add_argument("kind", choices=MEMORY_KINDS)
    g.add_argument("title")
    g.add_argument("--body", required=True)
    g.add_argument("--why")
    g.add_argument("--how")
    g.add_argument("--name")

    g = sub.add_parser("recall")
    g.add_argument("name", nargs="?")

    g = sub.add_parser("forget")
    g.add_argument("name")

    g = sub.add_parser("resources")
    g.add_argument("--status", choices=RESOURCE_STATUSES)
    g.add_argument("--topic")
    g.add_argument("--limit", type=int, default=500)
    g.add_argument("--summary", action="store_true",
                   help="per-topic counts as a markdown table")

    g = sub.add_parser("resource-status")
    g.add_argument("path")
    g.add_argument("status", choices=RESOURCE_STATUSES)
    g.add_argument("--priority", type=int)

    g = sub.add_parser("resource-add")
    g.add_argument("path")
    g.add_argument("title")
    g.add_argument("--topic")
    g.add_argument("--kind")
    g.add_argument("--notes")

    g = sub.add_parser("resource-position")
    g.add_argument("path")
    g.add_argument("position")
    g.add_argument("--note")

    g = sub.add_parser("session-start")
    g.add_argument("--method")
    g = sub.add_parser("session-end")
    g.add_argument("--summary")

    g = sub.add_parser("plan-create")
    g.add_argument("goal")
    g.add_argument("--steps", required=True, help="JSON array of {title, detail}")
    g.add_argument("--horizon")
    sub.add_parser("plan-show")
    g = sub.add_parser("plan-advance")
    g.add_argument("--step", type=int)
    sub.add_parser("plan-off")

    a = p.parse_args(argv)
    cmd = a.cmd

    if cmd == "init":
        return _emit(init_db())
    if not DB_PATH.exists() or DB_PATH.stat().st_size == 0:
        raise SystemExit(
            "error: no tutor database yet.\n"
            "Run: python japanese-tutor/scripts/setup.py")
    if cmd == "brief":
        return _emit(brief())
    if cmd == "stats":
        return _emit(stats())
    if cmd == "scan-resources":
        return _emit(scan_resources())
    if cmd == "profile":
        if a.key and a.value is not None:
            return _emit(set_profile(a.key, a.value))
        if a.key:
            return _emit({a.key: get_profile(a.key)})
        return _emit(get_profile())
    if cmd == "due":
        return _emit(due_items(a.limit, a.kind, a.direction))
    if cmd == "know":
        return _emit(know(a.kind, a.key) or {"known": False, "key": a.key})
    if cmd == "add-item":
        dirs = a.directions.split(",") if a.directions else None
        extra = {k: v for k, v in (("sentence", a.sentence), ("mnemonic", a.mnemonic),
                                   ("note", a.note)) if v}
        return _emit({"item_id": add_item(a.kind, a.key, a.reading, a.meaning,
                                          a.source, dirs, **extra)})
    if cmd == "item-note":
        return _emit(set_item_note(a.kind, a.key, sentence=a.sentence,
                                   mnemonic=a.mnemonic, note=a.note))
    if cmd == "known-words":
        return _emit(sorted(known_words(a.min_stability)))
    if cmd == "suspend":
        return _emit(suspend(a.kind, a.key, a.direction, not a.unsuspend))
    if cmd == "answer":
        return _emit(record_answer(a.direction, a.correct, kind=a.kind, key=a.key,
                                   rating=a.rating, given=a.given, expected=a.expected,
                                   session_id=a.session))
    if cmd == "error":
        return _emit(record_error(a.error_type, a.learner_output, a.correction,
                                  kind=a.kind, key=a.key, context=a.context))
    if cmd == "weak":
        return _emit(weak_points(a.limit))
    if cmd == "log-errors":
        return _emit(error_log(a.limit, a.days, a.error_type))
    if cmd == "log-reviews":
        return _emit(review_log(a.limit, a.days, not a.all, a.direction))
    if cmd == "confusables":
        if not a.kind or not a.key:
            return _emit(confusion_pairs(a.limit))
        return _emit(confusables(a.kind, a.key, limit=a.limit))
    if cmd == "confuse":
        return _emit(add_confusion(a.kind, a.key_a, a.key_b, a.reason))
    if cmd == "search":
        return _emit(search_items(a.query, a.kind))
    if cmd == "remember":
        return _emit(remember(a.kind, a.title, a.body, a.name, a.why, a.how))
    if cmd == "recall":
        return _emit(recall(a.name))
    if cmd == "forget":
        return _emit(forget(a.name))
    if cmd == "resources":
        if a.summary:
            return _emit(resource_summary())
        return _emit(list_resources(a.status, a.topic, a.limit))
    if cmd == "resource-status":
        return _emit(set_resource_status(a.path, a.status, a.priority))
    if cmd == "resource-add":
        return _emit(add_resource(a.path, a.title, a.topic, a.kind, a.notes))
    if cmd == "resource-position":
        return _emit(set_resource_position(a.path, a.position, a.note))
    if cmd == "session-start":
        return _emit(start_session(a.method))
    if cmd == "session-end":
        return _emit(end_session(a.summary))
    if cmd == "plan-create":
        return _emit(create_plan(a.goal, json.loads(a.steps), a.horizon))
    if cmd == "plan-show":
        return _emit(active_plan() or {"active_plan": None})
    if cmd == "plan-advance":
        return _emit(advance_plan(a.step))
    if cmd == "plan-off":
        return _emit(deactivate_plan())
    raise SystemExit("unknown command: %s" % cmd)


if __name__ == "__main__":
    try:
        main()
    except (LookupError, ValueError) as exc:
        sys.stderr.write("error: %s\n" % exc)
        raise SystemExit(1)
    except sqlite3.OperationalError as exc:
        if "no such table" in str(exc):
            sys.stderr.write(
                "error: the tutor database is not initialised.\n"
                "Run: python japanese-tutor/scripts/setup.py\n")
            raise SystemExit(1)
        raise
