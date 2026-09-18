"""One-time setup for the Japanese Tutor plugin.

Deliberately mechanical: it creates the database, wires the plugin into Claude
Code, and catalogues the repo's resources. It asks you nothing. Every decision
that needs a human - your goals, method, budget, which resources to use, your
level - belongs to `/japanese-tutor:onboard`, where the tutor can react to what
you say instead of reading from a list.

Usage:
    python japanese-tutor/scripts/setup.py
    python japanese-tutor/scripts/setup.py --check    health check, changes nothing
    python japanese-tutor/scripts/setup.py --reset    wipe learner state and start over
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlunsplit

MIN_PYTHON = (3, 9)

SCRIPTS_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPTS_DIR.parent
REPO_ROOT = PLUGIN_ROOT.parent

GITIGNORE_BLOCK = [
    "# Japanese Tutor - personal learner state, deliberately not committed",
    "japanese-tutor/state/",
]

# AnkiConnect listens on loopback and speaks plain HTTP - it has no TLS mode and
# the traffic never leaves this machine, so transport security does not apply.
# Built through urlunsplit so the loopback-only intent is explicit in the code.
ANKI_HOST = "127.0.0.1"
ANKI_PORT = 8765
ANKI_URL = urlunsplit(("http", "%s:%d" % (ANKI_HOST, ANKI_PORT), "", "", ""))

OK, WARN, FAIL, INFO = "[ ok ]", "[note]", "[FAIL]", "[ .. ]"

# See kb.py: piped stdout on Windows defaults to the ANSI code page and cannot
# encode Japanese. Resource titles contain plenty of it.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):  # pragma: no cover
        pass


def say(marker, message, detail=None):
    print("%s %s" % (marker, message))
    if detail:
        for line in str(detail).splitlines():
            print("       %s" % line)


def check_python():
    if sys.version_info < MIN_PYTHON:
        say(FAIL, "Python %d.%d or newer is required." % MIN_PYTHON,
            "You are running %s.\n"
            "Install a newer Python from https://www.python.org/downloads/ and run this again."
            % sys.version.split()[0])
        return False
    say(OK, "Python %s" % sys.version.split()[0])
    return True


def check_repo():
    resources = REPO_ROOT / "Resources"
    if not resources.is_dir():
        say(WARN, "No Resources/ folder found next to the plugin.",
            "Looked in: %s\n"
            "The tutor works without it, but it will have no local material to teach from.\n"
            "If your library lives elsewhere, set it later with:\n"
            "  python %s/kb.py profile repo_root <path>" % (REPO_ROOT, SCRIPTS_DIR))
        return False
    topics = sorted(p.name for p in resources.iterdir() if p.is_dir())
    say(OK, "Found Resources/ with %d topics" % len(topics), ", ".join(topics))
    return True


def setup_state(kb):
    paths = kb.init_db()
    kb.set_profile("repo_root", str(REPO_ROOT))
    say(OK, "Learner database ready", paths["db"])
    say(OK, "Memory folder ready", paths["memory"])


def update_gitignore():
    # Only touch a .gitignore that belongs to an actual checkout. If the plugin
    # was installed somewhere else and setup.py is run from there, REPO_ROOT is
    # a stranger's directory and we have no business writing to it.
    if not (REPO_ROOT / ".git").exists():
        say(WARN, "Not a git checkout - skipping .gitignore.",
            "%s\nYour learner state is still local; just make sure it is not "
            "committed anywhere." % REPO_ROOT)
        return
    path = REPO_ROOT / ".gitignore"
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    # Line-exact: a substring test would be satisfied by a negation such as
    # "!japanese-tutor/state/keep" and then quietly commit the learner's state.
    if any(line.strip() == GITIGNORE_BLOCK[-1] for line in existing.splitlines()):
        say(OK, "State folder already excluded from git")
        return
    text = existing.rstrip("\n")
    text = (text + "\n\n" if text else "") + "\n".join(GITIGNORE_BLOCK) + "\n"
    path.write_text(text, encoding="utf-8")
    say(OK, "Added japanese-tutor/state/ to .gitignore",
        "Your progress, mistakes and notes stay on this machine only.")


def register_plugin():
    """Best effort. If the CLI is missing we just print what to type."""
    claude = shutil.which("claude")
    manual = (
        "Register it yourself with either of these:\n"
        "  claude plugin marketplace add %s\n"
        "  claude plugin install japanese-tutor@learning-japanese\n"
        "or start Claude Code with:  claude --plugin-dir %s" % (REPO_ROOT, PLUGIN_ROOT)
    )
    if not claude:
        say(WARN, "Could not find the 'claude' command on PATH.", manual)
        return False
    try:
        subprocess.run([claude, "plugin", "marketplace", "add", str(REPO_ROOT)],
                       check=False, capture_output=True, text=True, timeout=120)
        result = subprocess.run(
            [claude, "plugin", "install", "japanese-tutor@learning-japanese"],
            check=False, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as exc:
        say(WARN, "Could not register the plugin automatically (%s)." % exc, manual)
        return False
    installed = subprocess.run([claude, "plugin", "list"], check=False,
                               capture_output=True, text=True, timeout=120)
    if "japanese-tutor" in (installed.stdout or ""):
        say(OK, "Plugin registered with Claude Code")
        return True
    say(WARN, "Plugin did not register automatically.",
        (result.stderr or result.stdout or "").strip() + "\n" + manual)
    return False


def catalogue(kb):
    result = kb.scan_resources()
    if result.get("error"):
        say(WARN, "Could not catalogue resources.", result["error"])
        return
    say(OK, "Catalogued %d resources (%d new)" % (result["total"], result["added"]),
        "Nothing is switched on yet - you pick what to study from during onboarding.")


def probe_anki(kb):
    """Anki is a bonus, never a requirement. Absence is not an error."""
    import urllib.error
    import urllib.request

    try:
        request = urllib.request.Request(
            ANKI_URL,
            data=json.dumps({"action": "version", "version": 6}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request, timeout=3) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if payload.get("result"):
            kb.set_profile("anki", "connect")
            say(OK, "Anki is running and reachable (AnkiConnect v%s)" % payload["result"],
                "The tutor can read your decks and add cards, if you want it to.")
            return
    except (urllib.error.URLError, OSError, ValueError, json.JSONDecodeError):
        pass

    appdata = os.environ.get("APPDATA") or ""
    candidates = [Path(appdata) / "Anki2", Path.home() / ".local/share/Anki2",
                  Path.home() / "Library/Application Support/Anki2"]
    collection = next(
        (c for base in candidates if base.is_dir()
         for c in base.glob("*/collection.anki2")), None)
    if collection:
        kb.set_profile("anki", "collection")
        kb.set_profile("anki_collection", str(collection))
        say(OK, "Found an Anki collection on disk (Anki itself is not running)",
            "%s\nThe tutor can read it, but cannot add cards until Anki is open." % collection)
        return

    kb.set_profile("anki", "none")
    say(OK, "Anki not found - skipping",
        "Not a problem. The tutor has its own scheduler and needs nothing external.")


def reset_state(assume_yes=False):
    """Delete all learner state. Refuses unless a human confirms."""
    from kb import STATE_DIR
    if not STATE_DIR.exists():
        say(OK, "Nothing to reset.")
        return True
    print("This deletes ALL your tutor progress, mistakes and remembered notes:")
    print("  %s" % STATE_DIR)
    if assume_yes:
        shutil.rmtree(STATE_DIR)
        say(OK, "State deleted (--yes was given).")
        return True

    # Do not trust sys.stdin.isatty() here: on Windows it reports true for
    # character devices including NUL, so a redirected stdin still looks
    # interactive. Catching EOFError is the only reliable signal that there is
    # nobody there to answer - which is the case when a tool runs this.
    try:
        answer = input("Type 'delete' to confirm: ")
    except (EOFError, KeyboardInterrupt):
        print()
        say(FAIL, "Refusing to reset with nobody there to confirm.",
            "Nothing was deleted.\n"
            "Run it yourself in a terminal, or pass --yes if you are certain:\n"
            "  python japanese-tutor/scripts/setup.py --reset --yes")
        return False
    if answer.strip().lower() != "delete":
        say(OK, "Cancelled. Nothing was changed.")
        return False
    shutil.rmtree(STATE_DIR)
    say(OK, "State deleted.")
    return True


def health_check(kb):
    problems = 0
    if not kb.DB_PATH.exists():
        say(FAIL, "No database yet.", "Run this script without --check to create it.")
        problems += 1
    else:
        try:
            kb.connect().execute("SELECT 1 FROM profile LIMIT 1").fetchone()
        except Exception as exc:
            say(FAIL, "The database exists but is not initialised.",
                "%s\nRun this script without --check to rebuild it." % exc)
            return False
        say(OK, "Database present", kb.DB_PATH)
        prof = kb.get_profile()
        if prof.get("onboarded") == "yes":
            say(OK, "Onboarding complete", "method=%s, %s min/day"
                % (prof.get("method"), prof.get("daily_minutes")))
        else:
            say(WARN, "Not onboarded yet.", "In Claude Code, run: /japanese-tutor:onboard")
        active = len(kb.active_resources())
        total = len(kb.list_resources(limit=5000))
        if active:
            say(OK, "%d of %d catalogued resources are switched on" % (active, total))
        else:
            say(WARN, "No resources switched on.",
                "The tutor has nothing to teach from. Run: /japanese-tutor:resources")
        s = kb.stats()
        say(OK, "%d items tracked, %d reviews in the last 30 days"
            % (s["items_total"], s["reviews_30d"]))
    return problems == 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="setup.py", description="Set up the Japanese Tutor plugin.")
    parser.add_argument("--check", action="store_true",
                        help="report on the current setup without changing anything")
    parser.add_argument("--reset", action="store_true",
                        help="delete all learner state and start over")
    parser.add_argument("--yes", action="store_true",
                        help="skip the confirmation prompt for --reset")
    parser.add_argument("--no-register", action="store_true",
                        help="skip registering the plugin with Claude Code")
    args = parser.parse_args(argv)

    print()
    print("Japanese Tutor setup")
    print("=" * 60)

    if not check_python():
        return 1

    sys.path.insert(0, str(SCRIPTS_DIR))
    try:
        import kb
    except ImportError as exc:
        say(FAIL, "Could not load the tutor's code.",
            "%s\nThe plugin files may be incomplete - try re-cloning the repository." % exc)
        return 1

    if args.reset:
        if not reset_state(args.yes):
            return 1
        print()
        say(INFO, "Rebuilding an empty database so the tutor still works.")
        print()

    if args.check:
        print()
        ok = health_check(kb)
        print()
        return 0 if ok else 1

    check_repo()
    setup_state(kb)
    update_gitignore()
    catalogue(kb)
    probe_anki(kb)
    if not args.no_register:
        register_plugin()

    print()
    print("=" * 60)
    if kb.get_profile("onboarded") == "yes":
        print("Setup is complete and you are already onboarded.")
        print()
        print("  Start a session:   /japanese-tutor:study")
        print("  Change anything:   /japanese-tutor:configure")
    else:
        print("Setup is complete. One thing left, and the tutor does it with you:")
        print()
        print("  1. Open Claude Code in this folder:   %s" % REPO_ROOT)
        print("  2. Type:                              /japanese-tutor:onboard")
        print()
        print("That walks you through your goals, how you want to be taught, which")
        print("resources to use, and a short check of your current level. Takes")
        print("about ten minutes and you can stop and resume any time.")
    print()
    print("If a command is not recognised, restart Claude Code first.")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
