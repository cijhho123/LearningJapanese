---
name: assess
description: Runs a full adaptive placement check of the learner's Japanese - vocabulary size, kanji recognition, grammar, the gap between reading and listening, and production - then writes a per-skill level estimate. Use when the user runs /japanese-tutor:assess, asks what level they are at, asks to be tested or placed, or wants to recheck their level after a stretch of study.
disable-model-invocation: true
allowed-tools: Bash(python *), Bash(python3 *), Read, Glob, Grep
---

# Assessment

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" brief 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" brief 2>&1 || echo "not set up"`

---

**Before anything else, read `${CLAUDE_PLUGIN_ROOT}/references/teaching-rules.md`.** Those rules bind every turn of this skill - especially rule 1, be brief.


This is the deep version. `onboard` runs a short one; this is for placing a
learner properly or rechecking after a few months.

Say up front, in one line, what it involves: about 30 questions, roughly 20
minutes, and they can stop any time - partial results still get saved.

## Rules

- **A few items per turn**, never a numbered list of thirty.
- **Adaptive.** Right answer -> harder. Wrong -> easier. Stop a strand once two
  consecutive items at a level are wrong, or two at the ceiling are right.
- Pull real items from active resources where possible. Never invent readings.
- No feedback on correctness until the end of a strand - correcting as you go
  changes what later items measure.

## The strands

### 1. Kana (1-2 items)
A short kana-only word. If this fails, stop everything: record absolute beginner
and recommend starting with kana. Nothing below this is worth measuring.

### 2. Vocabulary size (8-10 items)
Sample words across the frequency range - very common, common, mid, uncommon,
rare - and ask for meaning. Binary-search: right means jump rarer, wrong means
step back toward common.

**On frequency:** no frequency list ships with this plugin, so you are working
from your own sense of how common a word is. That is reasonable for the common
end and unreliable in the mid-to-rare band - so report a **wide** range and say
the estimate is rough. Do not present a word count as a measurement.

Skip non-word controls. A "plausible non-word" you invent has a real chance of
being an actual rare word, and then an honest learner gets their whole estimate
silently discounted. Instead, ask them to rate confidence ("know it / seen it /
no idea") and treat "seen it" as unknown.

This is still the highest-information strand per minute. Weight it accordingly.

### 3. Kanji (5-6 items)
Readings of kanji **inside words**, spread across school grades. Never bare
characters in isolation - nobody reads those, and multi-reading kanji make it
meaningless.

Note which way failures go: wrong reading type (on where kun belongs) is a
different problem from wrong reading within the right type.

### 4. Grammar (6-8 items)
`grammar-judgment` format: two sentences, one correct, which and why.

Walk the prerequisite structure rather than a flat level list - verb class
before te-form, te-form before its compounds. A failure low in the chain makes
everything above it untestable, so drop to the prerequisite rather than
continuing sideways.

The **why** matters more than the pick. A right answer with a wrong reason is a
fail, and worth logging as such.

### 5. Reading, with and without kanji support (2 items)
Give a short passage at the estimated level. Ask for a **free retell in
English** - not multiple choice. A retell shows exactly which clause broke.

Then give a comparable passage in kana only and do the same. The gap between
these two tells you how much of their reading is carried by kanji recognition
rather than by knowing the words - which predicts how they will cope with speech,
where there are no kanji to lean on.

**Be honest about what this is not.** It is not a listening test; nothing here
is heard. Real listening can only be assessed with an audio resource (see
`audio-resource` in the exercise catalogue). If they have no audio resource
active, say plainly that listening is unmeasured rather than inferring it.

### 6. Production (2-3 items)
Short English-to-Japanese prompts covering constructions with known high error
rates: a wa/ga contrast, a transitive-intransitive choice, a te-form chain.

Classify every error against `${CLAUDE_PLUGIN_ROOT}/references/error-taxonomy.md`.
This strand seeds the error profile that drives everything afterwards.

### 7. Pitch (optional)
Only if they have said pitch matters to them **and an audio resource is active**.

Pitch perception cannot be tested in text - the learner would be looking at the
words. Without audio, say so and skip the strand. Do not produce a score, and
never conclude "pitch training is wasted" from a written test; that conclusion
would be an artefact of the medium, not a fact about their hearing.

## Logging

Throughout:
```
kb.py add-item <kind> <key> ...          # anything they clearly know
kb.py answer --kind ... --direction ...  # every response
kb.py error --type <slug> ...            # every mistake, classified
```

At the end:
```
kb.py profile level_estimate "<per-strand summary>"
```

## Reporting

Report a **range per strand**, not a single level. For example:

> Vocabulary sits around N4, maybe 1200-1600 words. Kanji lags - solidly N5.
> Grammar is patchy N4: te-form is clean, conditionals are not. Listening is
> roughly one level behind your reading. Production is the weak strand, which
> is normal and also the thing most likely to bite you later.

Then: the single biggest gap, and one concrete thing to do about it.

Do not give one overall JLPT number. It hides exactly the imbalances that matter,
and the exam's own sectional minimums mean per-section standing is what actually
predicts a pass anyway.
