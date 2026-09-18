---
name: progress
description: Reports on the learner's Japanese progress - what they know, what is weak, what is drifting, and whether their current pace actually reaches their stated goal. Use when the user runs /japanese-tutor:progress, asks how they are doing, asks what their weak points are, or asks whether they are on track.
allowed-tools: Bash(python *), Bash(python3 *), Read
---

# Progress

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" brief 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" brief 2>&1 || echo "not set up"`

## Raw numbers

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" stats 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" stats 2>&1 || echo "{}"`

## Weak points

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" weak --limit 12 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" weak --limit 12 2>&1 || echo "{}"`

## Goals and preferences on record

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" recall 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" recall 2>&1 || echo "[]"`

## Plan

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" plan-show 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" plan-show 2>&1 || echo "{}"`

---

**Before anything else, read `${CLAUDE_PLUGIN_ROOT}/references/teaching-rules.md`.** Those rules bind every turn of this skill - especially rule 1, be brief.


## What to report

The learner asked for bluntness. This is the skill where that matters most,
because it is the only place the uncomfortable arithmetic gets done.

**Keep it under about 15 lines.** A progress report that needs scrolling doesn't
get read.

Cover, in this order:

### 1. Where they are
Item counts by kind, streak, 30-day retention. One or two lines.

If retention is far above ~90%, their intervals are too short and they're
wasting reviews. Far below ~80% and they're pushing too hard or the material is
too difficult. Say which.

### 2. The recognition-production gap
Compare `mean_stability_days_by_direction`. If `recognition` or `reading` is
far ahead of `recall` and `production`, **name it explicitly**. This is the
single most common way a self-study routine quietly fails: the learner builds a
large passive vocabulary, every metric looks healthy, and they cannot speak.

If `production` has no entry at all, that's the finding. Say so.

### 3. What keeps going wrong

If there is real history to work with (say 20+ logged errors or wrong answers),
delegate the deep read to the **error-analyst** agent. It reads the raw
wrong-answer text, which the counts above throw away, and comes back with
patterns like "all six に/で misses were with motion verbs". Ask it for its
findings, then report the two or three that matter - do not paste its whole
report.
The top few recurring error types with counts, and any leeches. Frame them as
things to drill, not as failures.

If the same error type has 3+ hits, say what you'd do about it concretely -
which drill, which exercise type.

### 4. The arithmetic, when there is a goal
If a goal memory or an active plan names a target and a date, do the sums out
loud:

- current new-items/day rate -> items per year
- items needed for the target level
- whether those meet

If they don't meet, say so plainly with the numbers, and name what would have to
change (more input volume, higher mining rate, more time - not "more
consistency"). Do not soften this. A plan that doesn't add up is worth more
broken early than believed for two years.

### 5. One thing to do next
A single concrete suggestion. Not a list.

## What not to do

- No praise for showing up. No "great job staying consistent!"
- No charts, no tables of every item
- Don't report metrics that are zero or near-zero as if they were findings -
  if they've done 12 reviews total, say the data is thin and stop there
- Don't invent trends from a handful of data points
