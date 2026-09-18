# Teaching methods

Five profiles. A profile **biases what the tutor suggests** - it never forces a
session shape, and switching is free because progress is stored
method-independently.

```
/japanese-tutor:configure switch to immersion
python japanese-tutor/scripts/kb.py profile method immersion
```

Full text for each is in `references/methods/`.

---

## mixed *(default)*

No single philosophy driving things. Each session picks from what your state
actually says is needed - overdue items, confusable pairs, your top recurring
mistake, whichever direction is lagging.

This is the default because most of the others are complementary rather than
competing, and committing on day one is a decision made with the least
information you will ever have.

## immersion

AJATT/Refold-shaped. Vocabulary first, kanji readings acquired through words
rather than in isolation, grammar skimmed once and then learned from exposure,
sentences mined from real material.

**Deliberately skips:** isolated kanji courses, textbook ordering, grammar as a
standalone subject.

**Watch out for:** review load creeping up until spaced repetition eats the
session it was meant to serve; mining only content words and never particles or
collocations; and the fact that this trains no output at all.

## structural-grammar

Work through a grammar guide, parsing before being told. Uses the
organic/Cure-Dolly lens - が marks the subject, は is a topic marker hiding
whatever case it replaced, relative clauses are sentences used as adjectives,
zero pronouns everywhere.

**One caveat the tutor is instructed to hold onto:** "が always marks the actor"
does not hold. With stative predicates the が-argument is the thing known,
wanted or liked, not the one doing it - 水が飲みたい, 日本語が分かる,
猫が好き. (Whether you call that an object or a subject is a live analytical
question; the tutor is told not to teach either label as settled.) The lens is
excellent for explaining why a sentence parses and bad for generating natural
output, so the tutor shows the underlying structure and then immediately the
natural surface form.

**Watch out for:** explanation is addictive and feels like progress. If a
session becomes all explanation and no retrieval, the tutor is told to stop and
make you produce something.

## comprehensible-input

Generated passages just above your level - constrained to your known-word set
plus three to five new items, in a genre you choose. Free retell rather than
comprehension questions. Low friction, high volume.

This is where an AI tutor has a genuine advantage: no static graded reader can
be built for one learner's exact vocabulary.

**Deliberately skips:** grammar drilling, production demands, SRS grinding.

**Be honest about the limits:** kanji does not come free from listening, the
strong form of the input hypothesis is not well supported, and incidental
acquisition is slow - roughly 5-15% per unknown word on an immediate test, and
much less at three months unless a word is met eight or more times.
Good as the high-volume layer, slow as the whole programme.

## output-drilling

Forced production targeting your logged mistakes. Translation, guided
composition, roleplay, explain-it-back.

Exists as its own profile because almost every self-study setup - and the entire
JLPT - tests recognition only. You can clear N2 and be unable to hold a
five-minute conversation, and nothing in your routine or score report will flag
it. This makes production a scheduled thing rather than something started three
years late in an interview.

**Watch out for:** production without enough input becomes fluent wrong Japanese,
fossilised early. If you're producing confidently from a small vocabulary, the
bottleneck is input and more drilling entrenches errors.

---

## What actually conflicts

Most of these stack. A few genuinely don't:

| Conflict | The call |
|---|---|
| Isolated kanji course vs vocab-first | Vocab-first, teaching components reactively when a confusion fires. Doing both is doing kanji twice. |
| Frequency ordering vs JLPT/textbook ordering | Sequence by frequency, *tag* by JLPT. You can only sequence by one. |
| "Study is useless, only acquisition counts" vs running an SRS | Be honest and take the interface position: study can become acquisition. |
| Delayed output vs early production | Against a machine the anxiety objection largely evaporates. Earlier than Refold says, later than a classroom would. |

## Choosing

If you don't have a strong opinion, stay on `mixed`. It reads your state and
picks, and you can switch the moment you do have an opinion.

Pick a single profile when you want the tutor to stop offering things you've
decided against - someone committed to immersion doesn't want textbook drills
suggested every session.
