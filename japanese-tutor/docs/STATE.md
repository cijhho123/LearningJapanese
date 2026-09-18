# State

Everything the tutor knows lives in `japanese-tutor/state/`. It is gitignored,
local to this machine, and yours to inspect, edit or delete.

```
japanese-tutor/state/
  tutor.db      SQLite: items, schedules, review log, mistakes, resources, plans
  memory/       markdown notes about you - see MEMORY.md
```

## What's tracked

| Table | Holds |
|---|---|
| `profile` | Your settings: method, budgets, format preferences, level estimate |
| `items` | Everything learnable you've met - words, kanji, grammar points, counters |
| `cards` | Scheduling state, **one row per item per direction** |
| `reviews` | Every answer you've given, including what you said when wrong |
| `errors` | Mistakes classified against the error taxonomy |
| `confusions` | Pairs you mix up |
| `resources` | The catalogue and which entries are switched on |
| `sessions` | When you studied and what was covered |
| `plans` | Optional study plans |

### Why directions are separate

Each item can carry up to five independently scheduled cards:

| Direction | Question |
|---|---|
| `recognition` | Japanese -> meaning |
| `recall` | meaning -> Japanese |
| `reading` | how is this kanji read here |
| `listening` | kana only, no kanji support - a proxy for speech, not real audio |
| `production` | use it in a sentence |

New items start with **one** direction. Creating all five at once would
multiply your review load by five on day one. Harder directions unlock
automatically once the first is genuinely stable (default: 21 days, tunable via
`unlock_after_days`).

This is the single most important design choice in the system. A deck that only
ever tests recognition will show healthy numbers while you remain unable to
produce anything, and it will never tell you. Here, the gap between
`recognition` and `production` stability is a number you can read.

## Scheduling

FSRS-5, implemented in `scripts/fsrs.py` from the published specification.
Per card it stores two numbers - stability and difficulty - plus a timestamp.

- **Stability** is how many days until your chance of recall falls to the
  retention target.
- Intervals are derived from stability, never stored.
- A lapse does **not** reset you to zero. Forget a 600-day card and it comes
  back at around two weeks, because a forgotten mature memory is still far
  stronger than a new one.
- Intervals are fuzzed by a few percent so cards added in the same week don't
  come due together forever.

### `desired_retention`

Default **0.85**, not the more common 0.90. For building vocabulary breadth -
which is what actually gates comprehension - a slightly lower target means
seeing each item a bit less reliably but getting through considerably more
material per hour. FSRS permits 0.70-0.99 and recommends 0.80-0.95, so 0.85 is
squarely inside the sane band. Per Anki's own docs the workload rises steeply
**above 0.90** and becomes overwhelming above 0.97 - raise it for exam-critical
material, but know what you are buying. Exact time-per-item gains are
user-specific; the honest answer is to try it rather than quote a number.

## Settings

```
python japanese-tutor/scripts/kb.py profile                 show all
python japanese-tutor/scripts/kb.py profile <key> <value>   set one
```

| Key | Default | Meaning |
|---|---|---|
| `method` | `mixed` | Teaching profile - see METHODS.md |
| `daily_minutes` | `30` | Session length target |
| `new_per_day` | `5` | New items introduced per day |
| `desired_retention` | `0.85` | FSRS target |
| `romaji` | `off` | Whether romaji may be shown |
| `emoji` | `off` | Whether emoji may be used |
| `bluntness` | `high` | How directly mistakes are called |
| `unlock_after_days` | `21` | Stability at which harder directions open |
| `leech_threshold` | `5` | Lapses before an item is treated as a leech |
| `level_estimate` | - | Written by `assess` and `onboard` |
| `repo_root` | - | Where `Resources/` lives |

## Inspecting it

```
python japanese-tutor/scripts/kb.py brief      one-screen summary
python japanese-tutor/scripts/kb.py stats      counts, retention, streak
python japanese-tutor/scripts/kb.py weak       recurring mistakes and leeches
python japanese-tutor/scripts/kb.py know vocab 食べる
python japanese-tutor/scripts/kb.py search --kind kanji
```

It's an ordinary SQLite file, so any SQLite browser opens it. Read freely.
Writing by hand is possible but easy to get wrong - prefer the CLI.

## Backing up

Copy `japanese-tutor/state/`. That's the whole backup.

To move machines, copy the folder across and run `setup.py` on the new one.
`repo_root` is stored in the profile, so fix it if the repo lives elsewhere:

```
python japanese-tutor/scripts/kb.py profile repo_root /new/path
```

## Why it isn't committed

The repository is shareable; your mistakes, weak points and goals are not.
`setup.py` adds `japanese-tutor/state/` to `.gitignore` on first run.

The trade is real: no history, no sync between machines, and a fresh clone
starts empty. If you'd rather version it, remove that line from `.gitignore` -
but understand that a public repo then publishes your error log.

## Resetting

```
python japanese-tutor/scripts/setup.py --reset
```

Asks you to type `delete`. Wipes progress, mistakes and memories. There is no
undo and no commit to recover from - copy the folder first if unsure.

To reset only part of it, open the database and delete from the relevant table.
`reviews` and `errors` are append-only logs; clearing them loses your history
but leaves your schedules intact.
