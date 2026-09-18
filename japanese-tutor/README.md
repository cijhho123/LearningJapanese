# Japanese Tutor

A Claude Code plugin that teaches you Japanese from the resources in this
repository, and remembers everything between sessions.

It is not a flashcard app with a chat interface. It tracks what you know and how
well, notices what you keep getting wrong, adapts to how you like to be taught,
and teaches only from material you chose. It has no daily routine and no streak
to protect - you open it and say what you feel like working on.

```
python japanese-tutor/scripts/setup.py
```

then, in Claude Code:

```
/japanese-tutor:onboard      once, to set up
/japanese-tutor:study        any time after that
```

Requires **Python 3.9+ and nothing else.** No pip installs, no accounts, no
services. Your learner state is a SQLite file and a folder of markdown notes,
both kept out of git.

---

## What it does

| Command | What it's for |
|---|---|
| `/japanese-tutor:onboard` | First-run setup: goals, method, budget, resources, level check |
| `/japanese-tutor:study` | Open a session. Asks what you want to work on |
| `/japanese-tutor:drill` | Focused practice on one thing - particles, readings, conjugation, output |
| `/japanese-tutor:mine` | Paste Japanese text: how much do you know, what's worth learning |
| `/japanese-tutor:resources` | Choose what the tutor teaches from; add new material |
| `/japanese-tutor:assess` | Full adaptive placement check |
| `/japanese-tutor:progress` | Where you are, what's weak, whether your pace reaches your goal |
| `/japanese-tutor:plan` | Optional staged study plan |
| `/japanese-tutor:configure` | Change settings; view and edit what it remembers about you |

Ask about a word or grammar point in ordinary conversation and it explains it
**and quietly records it**, so casual questions still add up.

## What makes it different

**It tracks five directions separately.** Recognition, recall, reading,
listening and production each get their own schedule. Almost every self-study
setup - and the entire JLPT - tests recognition only, so you can look fluent on
every metric and be unable to speak. Here that gap is a number you can see.

**It drills things you confuse.** Spaced repetition schedules similar items
independently, so it shows you one in April and the other in July and you never
work out which pair is causing the trouble. This builds a confusable graph from
your actual wrong answers and presents the pair side by side.

**It generates reading material at your exact level.** A passage built from your
known-word set plus a handful of new items, in a genre you care about. No static
graded reader can do that.

**It does the uncomfortable arithmetic.** If your current pace doesn't reach the
goal you stated, `progress` says so with the numbers rather than praising your
consistency.

## Documentation

- [Setup](docs/SETUP.md) - installing, step by step, assuming nothing
- [Usage](docs/USAGE.md) - every command, with examples
- [Methods](docs/METHODS.md) - the five teaching profiles and their tradeoffs
- [Resources](docs/RESOURCES.md) - choosing and adding study material
- [State](docs/STATE.md) - what's stored, how to inspect, export, back up or reset
- [Memory](docs/MEMORY.md) - what it remembers about you, and how to edit it
- [Anki](docs/ANKI.md) - the optional Anki bridge

## Layout

```
japanese-tutor/
  scripts/      kb.py (the knowledge base), fsrs.py (scheduler), setup.py, and
                optional helpers for coverage analysis, downloads and Anki
  skills/       the nine commands above, plus explain, which fires on its own
  references/   teaching rules, error taxonomy, exercise catalogue, method profiles
  agents/       resource-scout, for searching the library without flooding context
  state/        your data. gitignored. never leaves this machine
```

## Privacy

Everything - progress, mistakes, goals, the notes it keeps about you - lives in
`japanese-tutor/state/`, which `setup.py` adds to `.gitignore`. Nothing is
uploaded and nothing is committed. Delete the folder and it's gone.

## Licence

MIT. It reads the resources in this repository but bundles no dictionary data.
