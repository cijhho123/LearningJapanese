---
name: plan
description: Builds or manages an optional staged Japanese study plan from the learner's goal, deadline, available time and current level - and tracks progress through it. Use when the user runs /japanese-tutor:plan, asks for a study plan or roadmap, asks how to get from where they are to a specific goal, or wants to check, change or turn off an existing plan.
argument-hint: [nothing to view or create | off to deactivate | advance]
disable-model-invocation: true
allowed-tools: Bash(python *), Bash(python3 *), Read, Glob, Grep
---

# Plan

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" plan-show 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" plan-show 2>&1 || echo "{}"`

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" brief 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" brief 2>&1 || echo "not set up"`

Request: **$ARGUMENTS**

---

**Before anything else, read `${CLAUDE_PLUGIN_ROOT}/references/teaching-rules.md`.** Those rules bind every turn of this skill - especially rule 1, be brief.


**Plans are opt-in.** The tutor's default is free-flowing - it asks what you
feel like working on. A plan does not change that; it just gives `study`
something to suggest. Never guilt anyone about falling behind one.

## If a plan already exists

Show where they are in two or three lines: goal, current step, what's left.
Then ask if they want to advance it, change it, or turn it off.

```
kb.py plan-advance            # next step
kb.py plan-advance --step 4   # jump
kb.py plan-off                # deactivate, keeps the record
```

## Building one

Ask for what's missing, **one question at a time**. Check the state above first -
goals may already be on record from onboarding.

1. **The goal.** Specific and checkable. "Read Yotsuba unassisted", "pass N3",
   "hold a work conversation". Not "get better".
2. **The deadline**, if there is one.
3. **Hours per week** they will actually do, not aspire to.

Then check their current level from the state above. If there's no estimate,
say a plan built on a guess is worth little and offer `/japanese-tutor:assess`
first - but build it anyway if they'd rather.

### Do the arithmetic out loud, before writing the plan

This is the part that makes a plan worth having. Work out whether the goal is
reachable in the time, with numbers:

- Current new-items/day rate -> items per year
- Items needed for the goal (rough vocabulary and kanji counts for the target)
- Hours needed vs hours available

If it does not add up, **say so before building anything**. Then offer the real
options: extend the deadline, increase the hours, narrow the goal, or accept a
lower target. Let them choose.

A plan whose arithmetic fails is worse than no plan, because it takes two years
to find out.

Be specific about where volume actually comes from. There is no intrinsic
ceiling on spaced repetition - the binding constraint is minutes per day they
will actually sustain. So budget reviews first, set new-items/day from what is
left, and be honest that the remainder of the vocabulary has to come from
reading and listening volume. "Be more consistent" is not a plan.

### Surveying the material

Delegate this to the **curriculum-planner** agent. It counts lessons across the
active resources, finds where the learner currently is, does the goal arithmetic,
and returns a ready-to-store step list - all without pulling tables of contents
into this conversation.

Give it: the goal, the deadline, hours per week, and the current level estimate.
Relay its arithmetic verdict honestly, including when it says the goal does not
fit.

### Writing it

Four to eight steps. Each needs:

- a **title**
- a **detail** line saying what to do and which active resource to use
- a **done when** condition that is checkable, not a feeling

```
kb.py plan-create "<goal>" --horizon "<timeframe>" --steps '[
  {"title":"...","detail":"...","done_when":"..."},
  ...
]'
```

Build steps around the **active resources** (see state above). A plan that
references material they don't have switched on is fiction. If the plan needs
something they don't have, say so and offer `/japanese-tutor:resources`.

Include at least one **production** step. Plans built purely from recognition
material are how people arrive at an exam able to read and unable to speak.

### After creating

Show the steps compactly - title and done-when only, not the full detail - and
say that `study` will surface the current step as one suggestion among others,
and that they can ignore it whenever they like.

## Reviewing an existing plan

If they've drifted well off it, don't moralise. Ask whether the plan is still
what they want. Plans made three months ago are often just wrong now, and
rewriting one is cheaper than feeling bad about it.
