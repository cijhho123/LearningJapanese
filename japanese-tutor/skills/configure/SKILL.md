---
name: configure
description: Changes the Japanese tutor's settings - teaching method, daily time and new-item budget, romaji and emoji preferences, correction bluntness, retention target - and manages what the tutor remembers about the learner. Use when the user runs /japanese-tutor:configure, wants to change how the tutor behaves, asks to switch teaching methods, or wants to view, edit or delete the tutor's memories about them.
argument-hint: [what to change, e.g. "switch to immersion" or "forget that I wanted N2"]
disable-model-invocation: true
allowed-tools: Bash(python *), Bash(python3 *), Read, AskUserQuestion
---

# Configure

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" profile 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" profile 2>&1 || echo '{"error":"not set up"}'`

## Memories

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" recall 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" recall 2>&1 || echo "[]"`

Request: **$ARGUMENTS**

---

**Before anything else, read `${CLAUDE_PLUGIN_ROOT}/references/teaching-rules.md`.** Those rules bind every turn of this skill - especially rule 1, be brief.


If `$ARGUMENTS` says what they want, just do it and confirm in one line. Only
show the full settings list if they asked to see it.

## Settings

| key | values | what it does |
|---|---|---|
| `method` | `mixed`, `immersion`, `structural-grammar`, `comprehensible-input`, `output-drilling` | Biases what the tutor suggests. See `references/methods/` |
| `daily_minutes` | number | Session length target |
| `new_per_day` | number | New items introduced per day |
| `desired_retention` | 0.80-0.95 | FSRS target. Lower means more new material per unit time |
| `romaji` | `on` / `off` | Default off |
| `emoji` | `on` / `off` | Default off |
| `bluntness` | `high` / `normal` | How directly mistakes get called |
| `unlock_after_days` | number | Stability at which harder directions (recall, production) open up |
| `leech_threshold` | number | Lapses before an item is treated as a leech |
| `level_estimate` | free text | Written by `assess` and `onboard` |

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" profile <key> <value>
```

### Worth saying once, when relevant

- **Lowering `desired_retention`** (say 0.90 -> 0.85) means seeing each item
  slightly less reliably but getting through more material per hour. FSRS
  recommends 0.80-0.95, so 0.85 is well inside the sane range. Workload climbs
  steeply **above 0.90** and becomes punishing above 0.97. Don't quote a speedup
  figure - it depends on their own review history.
- **Raising `new_per_day`** raises the review load roughly in proportion:
  Anki's rule of thumb is about 10x the new rate (20 new/day -> ~200
  reviews/day). It is not a fixed constant - expect ~6-7x after a few months,
  drifting higher over a year as cards accumulate. The release valve when it
  gets heavy is cutting new items, not extending sessions.
- **Switching method** changes nothing about stored progress - the state is
  method-independent. Switching is cheap; say so.

## Memories

```
kb.py recall                    # list
kb.py recall <name>             # read one in full
kb.py forget <name>             # delete
kb.py remember <kind> "<title>" --body "..." --why "..." --how "..."
```

Kinds: `user` (durable facts), `feedback` (how the tutor should behave),
`preference` (observed habits), `goal` (targets with dates).

Memories are plain markdown in `japanese-tutor/state/memory/` - the learner can
edit them directly in an editor, and should be told that if they ask.

To **correct** a memory, rewrite it with the same `--name` rather than adding a
near-duplicate.

## Reset

Full wipe of progress, mistakes and memories. **Do not run this yourself** - it
needs a typed confirmation and will refuse when invoked by a tool. Give the
command to the learner to run in their own terminal:

```
python japanese-tutor/scripts/setup.py --reset
``` Warn them it cannot be undone and that state is
gitignored, so there is no commit to recover from. Offer to copy
`japanese-tutor/state/` somewhere first.
