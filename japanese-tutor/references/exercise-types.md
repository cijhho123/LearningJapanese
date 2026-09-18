# Exercise catalogue

Every practice format the tutor can run, grouped by what it trains. `drill`
dispatches from here; `study` picks from here when the learner says "you pick".

Each entry gives the presentation, the scoring rule, and what to log. Keep every
exercise to **one item per turn** - present, stop, wait.

Direction names map to `kb.py answer --direction`:
`recognition | recall | reading | listening | production`

---

## Kanji

### kanji-reading-in-word
Show the kanji **inside a word they already know**, ask for the reading.
Never test a bare kanji's reading in isolation - nobody reads bare kanji, and
multi-reading characters make it meaningless out of context.
> 「食**事**」- how do you read this?

Score: exact kana match. Log `direction=reading`. Wrong -> `kanji-reading-wrong-on`
or `kanji-reading-onkun` depending on which way they went.

### kanji-meaning
Show the character, ask what idea it carries. Accept any reasonable paraphrase -
a keyword is a pointer, not a definition.
Log `direction=recognition`.

### kanji-component-breakdown
Ask them to name the parts before you give the breakdown. Use only when a
resource supplies the real decomposition - do not invent components.
Not scored. Use as a repair tool after a visual confusion.

### kanji-discrimination  **(high value)**
Present two or more confusable characters **side by side** and ask which fits a
context.
> Which goes in 「電車を___つ」 - 待 / 持 / 特 ?

This is the one exercise SRS structurally cannot produce: it schedules
confusables independently and so hides the collision. List every known pair with
`kb.py confusables` (no arguments), or check one item with
`kb.py confusables <kind> <key>`. Log both the answer and, on failure,
`kanji-visual-confusion`.

### kanji-on-reading-family
Give a component and ask which reading it tends to carry across characters
(青/晴/清/静 -> セイ). Teaches the generalisation instead of N separate facts.
Only run when an active resource confirms the family.

---

## Vocabulary

### vocab-recognition
Japanese -> meaning. The baseline. `direction=recognition`.

### vocab-recall
Meaning or English -> Japanese. Harder, and the direction that actually matters
for speaking. Unlocks automatically once recognition is stable.
`direction=recall`. Wrong -> `vocab-production-failure`.

### vocab-cloze
Blank the word inside a sentence, supply the gloss as a hint.
> 毎朝コーヒーを___。(drink)

Better than a bare card because it tests the word *and* its particle and
conjugation. `direction=recall`.

### vocab-listening
Give the word or sentence in kana only, framed as "you hear this", ask for
meaning. A stand-in for audio when none is available.
`direction=listening`.

### vocab-collocation
Which verb goes with this noun? 傘を___ (さす), 写真を___ (撮る).
Attacks the "knows the word, can't use it" gap. Log
`near-synonym-confusion` on failure.

### vocab-from-kanji
Before glossing a new compound, ask them to guess from the characters. Free
generation-effect practice, costs one line.

---

## Grammar

### grammar-judgment  **(preferred)**
Two sentences, one correct. Ask which, **and why**.
> A: 私は日本語が分かる  B: 私は日本語を分かる - which, and what's the rule?

The "why" is what separates rule knowledge from pattern matching. A right answer
with a wrong reason is a fail - log it.

### grammar-cloze
Blank the grammatical element, not the vocabulary.
> 食べ___いる (ordering: te-form)

`direction=recognition`.

### grammar-transformation
Give a sentence, ask for a specific change: plain -> polite, active -> causative,
present -> conditional. Targets the conjugation machinery directly.
`direction=production`.

### grammar-error-correction
Show a sentence containing a mistake from *their own* error log and ask them to
fix it. Self-generated material is more motivating and better targeted than
anything invented.

### grammar-produce-with-target
"Give me a sentence using ～ておく about your morning."
The hardest and most valuable grammar exercise. `direction=production`.

### grammar-parse
Give a real sentence from an active resource and ask them to identify the
subject (including a dropped one), the clause boundaries, and what each particle
is doing. This is where structural explanation earns its keep.

---

## Reading

### graded-passage  **(high value)**
Delegate to the **passage-writer** agent: give it the target items and the
domain, and it returns a 100-300 word passage built from `kb.py known-words`
plus those items, having already verified the constraint. Keeping it out of the
main thread matters because the known-word list is large and only the writer
needs it.

Then ask for a free retell in English - not multiple choice. The retell shows
exactly which clause broke. If the agent reports words it could not write
around, remember that a comprehension failure there is a material problem, not a
learner problem.

No static graded reader can be personalised to one learner's known-word set.
This is the thing an LLM tutor can do that nothing else can. Use it often.

Log comprehension as a `reading` answer on the target items, and log any
construction that broke as an error.

### sentence-mining-parse
Take one sentence from real material, check it is genuinely i+1 (exactly one
unknown element), have them parse it, then offer to add the unknown as an item.
Skip sentences with 3+ unknowns - they teach nothing.

### resource-reading
Work through the next section of an active resource at their stored position.
Ask before explaining, one section per turn. Update `resource-position` after.

---

## Listening

### dictation
Write a sentence in kana, have them tell you what it means and where the word
boundaries are. Approximates listening when no audio exists.

### minimal-pair-length
Contrast おばさん/おばあさん, ここ/こうこう, きた/きった in context.
Targets `vowel-length` and `gemination`, which English speakers under-perceive
rather than under-produce.

### audio-resource
If an active resource has audio, point them at a specific track and debrief
afterwards. Log what they missed.

---

## Output / production

### translate-to-japanese
English -> Japanese, with the prompt deliberately chosen to require a
construction from their current error profile.
`direction=production`. This is the direction every recognition-only deck skips.

### guided-composition
"Write three sentences about what you did yesterday." Then correct **one thing**
- the most important one - and ask them to redo it. Correcting everything at once
teaches nothing.

### roleplay
Short scenario in Japanese: ordering, asking directions, a work exchange. Stay
in role, keep turns short, debrief at the end rather than interrupting.

### explain-back
"Explain ～ば vs ～たら to me as if I were the student."
The strongest test of real understanding, and the direct answer to
"that makes sense".

---

## Pitch accent *(optional - off unless the learner asked for it)*

### pitch-minimal-pairs  *(requires an active audio resource)*
**Cannot be run in text.** With no sound there is nothing to perceive: a written
forced choice tests whether they remember which pattern goes with which word,
which is vocabulary knowledge wearing a phonetics costume. Say so and point them
at an audio minimal-pair tool instead.

If you do probe accent knowledge in text, be accurate about it:
- Present items in **kana** - 箸/橋/端 are orthographically distinct, so showing
  the kanji hands over the answer.
- 箸/橋/端 is a **three**-way set, so chance is **33%**, not 50%.
- 橋 and 端 are **both LH in isolation** and only separate once a particle
  follows (はしが: LHL vs LHH). Test the `-が` form or the contrast does not exist.
- Do **not** conclude that production training is wasted from a low score.
  Perception and production gains are uncorrelated at the individual level
  (Bradlow et al. 1997), so there is no gate here to enforce.

### pitch-pattern-id
Name the pattern of a known word: 平板 / 頭高 / 中高 / 尾高.
Only with a resource that supplies verified accent data. Never state pitch from
memory.

---

## Choosing what to run

In rough priority order, when the learner says "you pick":

1. Anything **overdue** with low retrievability - a nearly-forgotten item is
   worth far more than a fresh one.
2. A **discrimination drill** if `confusables` has an unaddressed pair.
3. The **top recurring error** from `weak_points` - via `grammar-error-correction`
   or a targeted judgment exercise.
4. **Production** on items whose recognition is far ahead of their recall.
5. New material from the highest-priority active resource.

**Block, then interleave - in that order.** This is narrower than the usual
advice and the nuance matters:

- When *introducing* a new pattern, **block** it. Practise it repeatedly until
  there is a representation to work with. Brunmair & Richter's meta-analysis
  (2019, 238 effect sizes) found blocking outright *better* for word learning
  (g = -0.39) and no reliable interleaving benefit for expository text - the
  authors explicitly decline to recommend interleaving for foreign-language
  material.
- Once the learner has the pattern and the problem is **telling similar things
  apart**, interleave. That is where the benefit is real and large (overall
  g = 0.42, paintings g = 0.67): high between-category similarity, low
  within-category similarity. Confusable kanji, transitive/intransitive pairs,
  は/が - exactly the discrimination drills.

So: do not shuffle formats for its own sake. Mix when the goal is
discrimination; block when the goal is acquiring something new.

Cap a drill at around 10 items unless they ask to keep going. Reviews expanding
to fill all available time is how SRS eats the study habit it was meant to serve.
