---
name: onboard
description: Sets up a new learner for the Japanese tutor - goals, teaching method, time budget, format preferences, which resources to study from, and a short level check. Use when the user runs /japanese-tutor:onboard, says they want to set up or configure the Japanese tutor for the first time, or when any other tutor skill reports that onboarding is incomplete.
disable-model-invocation: true
allowed-tools: Bash(python *), Bash(python3 *), AskUserQuestion, Read, Glob, Grep
---

# Onboarding

## Current state

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" profile 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" profile 2>&1 || echo '{"error":"not set up - tell the user to run: python japanese-tutor/scripts/setup.py"}'`

## Resource catalogue by topic

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" resources --summary 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" resources --summary 2>&1 || echo "(catalogue unavailable - run setup.py)"`

---

## How to run this

Read `${CLAUDE_PLUGIN_ROOT}/references/teaching-rules.md` first. Rule 1 applies
hardest here: **onboarding is where every tool turns into a wall of text.** Do not.

- **One step per turn.** Ask, stop, wait. Never batch questions.
- **Use `AskUserQuestion`** for the multiple-choice steps. It is compact and
  beats writing out option lists in prose.
- **Write each answer immediately** with `kb.py`. If they quit halfway and come
  back, the profile already holds what they said and you skip those steps.
- **Skip what's answered.** Check the injected profile above. Only run steps
  whose keys are missing or still at their default.
- Total should feel like ~10 minutes, not an interrogation.

Open with two lines, maximum. Something like: what this does, how long it takes,
and that they can stop any time. Then go straight to step 1.

---

## The steps

### 1. Goal and timeline
Open question, conversational. What do they want to be able to do, and by when?

Write it: `kb.py remember goal "<short title>" --body "<what they said>"`
If they mention constraints (job, study time, a move abroad, an exam date),
that's a second memory of kind `user`.

### 2. Teaching method
`AskUserQuestion`, single select. Options - keep the descriptions to one line each:

- **Mixed (recommended)** - tutor picks per session from what your state needs
- **Immersion / sentence mining** - vocab-first, mine real material, grammar from exposure
- **Structural grammar** - work through a grammar guide, parse before you're told
- **Comprehensible input** - generated passages just above your level, low friction
- **Output drilling** - forced production targeting your logged mistakes

Then: `kb.py profile method <value>`

If they pick a single method, read the matching file in
`${CLAUDE_PLUGIN_ROOT}/references/methods/` and tell them **in one sentence**
what it deliberately won't do. They should know the tradeoff they just took.

### 3. Time budget
`AskUserQuestion` with two questions in one call (minutes/day, new items/day):

- Minutes: 15 / 30 / 60 / 90
- New items per day: 3 (slow and certain) / 5 / 10 / 20 (fast, heavy review load)

Write: `kb.py profile daily_minutes <n>` and `kb.py profile new_per_day <n>`

If they pick a high new-item rate, say once - one sentence - that daily reviews
settle at roughly ten times the new rate (Anki's rule of thumb) and keep
drifting up over the first year, and that the release valve is cutting new cards
rather than extending sessions.

### 4. How you want to be taught
`AskUserQuestion`, multi-select, one call. **These are all already on by
default** - say that in the question, and treat unticking as turning one off:

- Never show romaji (on by default)
- No emoji (on by default)
- Correct me bluntly, no cushioning (on by default)

Then write **both branches explicitly** - ticked gives `romaji off` /
`emoji off` / `bluntness high`, unticked gives `romaji on` / `emoji on` /
`bluntness normal`. Do not leave a key unwritten and assume the default: blunt
correction should be something they actually chose.

Anything they say beyond the options - save as a `preference` memory.

### 5. Resources
This repo holds hundreds of catalogued resources. Studying from all of them is
the same as studying from none.

Show the **topic counts** from the injection above, then recommend a **small**
starting set - about one grammar guide, one kanji source, one vocabulary source,
matched to their chosen method. Name three or four specific ones, not a list of
thirty.

To find candidates: `kb.py resources --topic Grammar` (and Kanji, Vocabulary).
Prefer entries whose `kind` is `guide` or `folder`.

The topic guides in `Resources/*/readme.md` are opinionated about what is worth
using, so they are the best signal available - but **never read one whole.**
They run 40-270 KB (Culture alone is 1,800 lines) and a single one will fill the
context window. Locate, then extract narrowly:

```
grep -n "<keyword>" "Resources/<Topic>/readme.md"
sed -n '<start>,<end>p' "Resources/<Topic>/readme.md"
```

Confirm with them, then for each: `kb.py resource-status "<path>" active`

Tell them they can change this any time with `/japanese-tutor:resources`, and
that everything else stays catalogued but switched off.

### 6. Level check
Say what this is first, in one line: about 15 quick questions, no wrong answers
matter, it just calibrates where to start.

Run it **adaptively and conversationally** - a few items per turn, not all 15 at
once. Stop early on any strand that's clearly at floor or ceiling.

- **Kana** (1-2 items) - read a short kana-only word. If they stumble, stop the
  whole assessment here and record beginner; there is nothing below this.
- **Vocabulary** (5-6 items) - words spread across the frequency range, from very
  common to rare. Ask for meaning. Binary-search: right -> rarer, wrong -> commoner.
- **Kanji** (3-4 items) - readings of kanji **inside a word**, spread across
  school grades. Never a bare kanji in isolation.
- **Grammar** (3-4 items) - `grammar-judgment` format: two sentences, one
  correct, which and why. Spread across levels. The "why" matters more than the
  pick.
- **Production** (1-2 items) - one short English-to-Japanese prompt. This is the
  single most informative item in the whole check, because it is the only one
  that tests the direction most self-study neglects.

Pull the exact items from an active resource where you can. Do not invent
readings - see teaching rule 4.

As you go:
- `kb.py add-item` for anything they clearly know (gives you a starting corpus)
- `kb.py answer` for each response
- `kb.py error --type <slug>` for each mistake, classified against
  `${CLAUDE_PLUGIN_ROOT}/references/error-taxonomy.md`

Then write a **range, not a point**:
`kb.py profile level_estimate "<e.g. N5 vocab, N4 grammar, kanji lags, production untested>"`

Report per strand, and call out any gap between strands - especially
reading-versus-production. A single "you are N4" is both less useful and less
honest.

### 7. Finish
`kb.py profile onboarded yes`

Then a summary that **fits on one screen**: method, budget, active resources,
level estimate, and the single thing you'd suggest doing first. Close with
`/japanese-tutor:study` and the note that they can just say what they feel like
working on - there's no routine to keep up with.

---

## If they want to skip

Fine. Set sensible defaults (`method mixed`, 30 min, 5 new/day, romaji off),
activate two or three obvious resources, mark `onboarded yes`, and say the tutor
will calibrate as it goes and they can run `/japanese-tutor:assess` whenever.
Don't argue about it.
