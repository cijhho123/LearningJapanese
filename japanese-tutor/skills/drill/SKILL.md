---
name: drill
description: Runs focused Japanese practice on one specific thing - kanji readings, particles, verb conjugation, counters, vocabulary recall, listening, translation, keigo, or whichever weak point the learner names. Use when the user runs /japanese-tutor:drill, asks to practise or drill a specific Japanese topic, says they want to work on a particular weakness, or asks to be quizzed or tested on something.
argument-hint: [topic, e.g. "particles" or "te-form" or "kanji readings"]
allowed-tools: Bash(python *), Bash(python3 *), Read, Glob, Grep
---

# Drill: $ARGUMENTS

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" brief 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" brief 2>&1 || echo "Tutor not set up - run: python japanese-tutor/scripts/setup.py"`

## Weak points and leeches

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" weak --limit 8 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" weak --limit 8 2>&1 || echo "{}"`

## Due now

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" due --limit 12 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" due --limit 12 2>&1 || echo "[]"`

---

## How to run this

Read `${CLAUDE_PLUGIN_ROOT}/references/exercise-types.md` and
`${CLAUDE_PLUGIN_ROOT}/references/teaching-rules.md`.

### Choosing the target

If `$ARGUMENTS` names a topic, drill that.

If it's empty, pick the highest-value target from the state above and say what
you picked in one line:

1. An unaddressed confusable pair - `kb.py confusables` with no arguments lists
   every pair on record. Run `kanji-discrimination` on the worst. This is the
   single highest-value drill available, because spaced repetition schedules
   confusable items independently and so actively hides the collision.
2. The top recurring `error_type` - run `grammar-error-correction` or
   `grammar-judgment` on it, using **their own logged mistakes** as material.
3. A leech - repair it rather than grinding it (see below).
   If the same error type keeps recurring and you cannot see *why* from the
   counts, ask the **error-analyst** agent - it reads the actual wrong answers
   and can usually name the sub-pattern to drill.
4. The direction where stability lags worst - usually production.

### Choosing the format

Map the topic to exercise types from the catalogue. Examples:

| They say | Run |
|---|---|
| "particles" | `grammar-judgment`, `vocab-cloze` with particle blanked |
| "kanji readings" | `kanji-reading-in-word`, then `kanji-discrimination` on any miss |
| "te-form" / conjugation | `grammar-transformation`, `grammar-produce-with-target` |
| "counters" | `vocab-recall` with the full alternation paradigm, not bare numbers |
| "vocab" | `vocab-recall` and `vocab-cloze`, not plain recognition |
| "listening" | `dictation`, `minimal-pair-length` |
| "speaking" / "output" | `translate-to-japanese`, `guided-composition`, `roleplay` |
| "keigo" | `grammar-judgment` on direction (sonkeigo vs kenjougo), `roleplay` |
| "reading" | `graded-passage` with free retell |

**Match the format to the goal.** If they are learning something new, stay on
one format - blocked practice is genuinely better for acquiring words and
patterns. If they are trying to tell confusable things apart, interleave the
confusable set; that is where mixing earns its keep. Do not shuffle formats just
to shuffle them.

### Running it

- **One item per turn.** Present, stop, wait for the answer.
- Confirm or correct in one or two lines, then the next item.
- Answers in a `Key` section at the bottom if the item needs one revealed.
- **Cap at about 10 items** unless they ask to keep going. Say when you stop.

### If they miss several in a row

**Three consecutive misses means the level is wrong, not the learner.** Stop the
drill, say exactly that, and drop to the prerequisite skill or an easier
direction (production -> recognition). Do not push through to ten items.

Bluntness is about being clear, not relentless. "No" five times running with no
change of approach is a failure of the drill, not honesty.

### Repairing a leech

Grinding a leech is the most reliable way to make someone quit. When an item has
lapsed 5+ times, change the item rather than repeating it. In order:

1. Check `kb.py confusables` - if something is interfering, switch to a
   side-by-side contrastive presentation of the pair. Interference, not
   difficulty, causes most leeches.
2. Build a mnemonic **with** them, using real kanji components or an on-reading
   family. Save it so next session does not rebuild it from scratch:
   `kb.py item-note <kind> <key> --mnemonic "<what you agreed>"`
3. Split it if the card is carrying too much at once.
4. Add disambiguating context to how it's tested.
5. If none of that applies, park it: `kb.py suspend <kind> <key>`, and let
   immersion handle it later. Some words are not worth the fight yet.
   (`--unsuspend` brings it back.)

### Logging

Same as `study`. Every answer, every classified error, the exact wording of what
they said when they got it wrong.

### Closing

Two or three lines: hit rate, the one pattern worth naming, and what you'd drill
next. Nothing longer.
