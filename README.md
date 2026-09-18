# Learning Japanese

A working archive of resources for learning Japanese, plus a detailed guide to each part of the
language. Continuously updated.

**Version 1.0.0** - what changed, and when, is in the [changelog](CHANGELOG.md).

The repo has three layers:

- **Guides** - one per topic, at `Resources/<Topic>/readme.md`. Each one covers what the topic is,
  the competing schools of thought with honest pros and cons, an opinionated recommended path, a
  phase-by-phase plan with concrete checkpoints, the common pitfalls, and a complete index of the
  material in that folder.
- **Resources** - offline material: textbooks, Anki decks, graded readers, audio courses, dozens of
  machine-readable datasets, and full mirrors of the major community guides, so nothing here depends
  on a website staying online.
- **[Tutor](japanese-tutor/README.md)** - an optional Claude Code plugin that teaches from the two
  layers above and remembers what you have learned between sessions.

The guides are opinionated on purpose. Where a topic has several legitimate approaches - and most of
them do - each guide lays the options out fairly first, then recommends one and says why.
Disagreeing with the recommendation is fine; the point is that you can see the reasoning and the
tradeoffs instead of a flat list of links.

---

## Start here

If you are on day zero, this is the order that works.

1. **[Kana](Resources/Kana/readme.md)** - hiragana and katakana first. Days to weeks, not months. Everything else assumes you can read them, so get off [romaji](Resources/Romaji/readme.md) fast.
2. **[Grammar](Resources/Grammar/readme.md)** + **[Kanji](Resources/Kanji/readme.md)** + **[Vocabulary](Resources/Vocabulary/readme.md)** - in parallel, not in sequence: one fast pass through a grammar guide, a daily kanji habit, a frequency-ordered vocabulary deck.
3. **[Immersion](Resources/AJATT/readme.md)** - start on real Japanese earlier than feels comfortable and keep [listening](Resources/Listening/readme.md) and [reading](Resources/Reading/readme.md) daily. This is where the language is acquired; the study above is what makes the input comprehensible.
4. **[Output](Resources/Speaking/readme.md)** - [speaking](Resources/Speaking/readme.md) and [writing](Resources/Writing/readme.md) once you have a base, and earlier than immersion orthodoxy says if you intend to live there.
5. **[Tooling](<Resources/General content/readme.md>)** - Anki and a pop-up dictionary on day one. It pays for itself inside a week.

[Culture](Resources/Culture/readme.md) runs alongside all of this rather than at any fixed point.

**Do not make the [JLPT](Resources/JLPT/readme.md) your goal.** It is entirely passive multiple choice, with no speaking or writing, so preparing for it and learning the language end in different places - sit it only if you need the certificate for a visa or a job.

---

## The guides

| Topic                                                                      | What it covers                                                                                                                                                                                                                                                        |
| :------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Kana](Resources/Kana/readme.md)**                                       | Hiragana and katakana, the full sound system (dakuten, youon, long vowels, small tsu, the mora), look-alike discrimination, katakana loanword decoding, and the 2-day vs 2-week speedrun debate.                                                                      |
| **[Romaji](Resources/Romaji/readme.md)**                                   | Hepburn vs Kunrei-shiki vs Nihon-shiki vs keyboard wapuro romaji, where romanization is legitimately used, the phonetic damage it does to beginners, and a staged plan for getting off it.                                                                            |
| **[Grammar](Resources/Grammar/readme.md)**                                 | The biggest guide here. Nine approaches compared (Tae Kim, Cure Dolly, Yokubi, Imabi, Sakubi, textbooks, Bunpro, DoJG, pure immersion), plus reference sections: particles with a full は vs が treatment, a conjugation map, transitivity pairs, and a keigo primer. |
| **[Kanji](Resources/Kanji/readme.md)**                                     | RTK vs KanjiDamage vs WaniKani vs vocabulary-only, argued properly. Radicals and components, semantic vs phonetic parts, on/kun readings and their exceptions, phonetic families, look-alike sets, and what kanji fluency actually feels like.                        |
| **[Vocabulary](Resources/Vocabulary/readme.md)**                           | Two parts. A brief on what Japanese words are: the wago/kango/gairaigo strata and the register they encode, word formation and the affixes that generate thousands of words, counters, mimetics, homophones and why pitch accent only half-fixes them. Then acquisition: premade decks vs mining, card formats, the arithmetic of new-cards-per-day, leech triage, and the 10k plateau. |
| **[Listening](Resources/Listening/readme.md)**                             | The listening ladder from comprehensible input to unscripted native speech, the subtitle question answered bluntly, what passive listening does and does not buy you, and a reference table of real-speech contractions.                                              |
| **[Speaking](Resources/Speaking/readme.md)**                               | The output-timing debate (silent period vs speak from day one), a pronunciation reference, pitch accent and whether to study it deliberately, shadowing procedure, and the anime-register trap.                                                                       |
| **[Reading](Resources/Reading/readme.md)**                                 | Intensive vs extensive reading, when to look a word up and when to let it go, the ladder from graded readers through manga and visual novels to native prose, manga-specific skills, and the "I know every word but not the sentence" wall.                           |
| **[Writing](Resources/Writing/readme.md)**                                 | Two unrelated skills, separated. The marks: stroke order, printed vs handwritten forms, IME input, punctuation and orthography, okurigana, when to write a word in kanji vs kana, numbers and era-name dates, vertical text. Then composing a text: written vs spoken vocabulary, connectives, paragraph and essay structure, email, and getting corrected. Plus an honest case for whether a modern learner needs handwriting at all. |
| **[Immersion / AJATT](Resources/AJATT/readme.md)**                         | What AJATT claims, its descendants (MIA, Refold, Animecards, TheMoeWay), and its honest critiques. Active vs passive immersion, the full sentence-mining pipeline, and choosing media you actually enjoy.                                                             |
| **[Tooling and general reference](<Resources/General content/readme.md>)** | Anki properly: FSRS, deck options, add-ons, backups, digging out of a review backlog. Plus Yomitan and dictionaries, why Japanese fonts differ, and a guide to the archived site mirrors.                                                                             |
| **[JLPT](Resources/JLPT/readme.md)**                                       | N5 to N1, what the test does and does not measure, how scoring and sectional minimums actually work, what each level means in practice, whether it is worth sitting, and a 12-week prep cycle.                                                                        |
| **[Culture](Resources/Culture/readme.md)**                                 | History, geography and the 47 prefectures, dialects and regional identity, the social structure that Japanese grammar encodes, etiquette, work culture, religion and holidays, food, pop culture, and being a foreigner there long-term.                              |

---

## The tutor

[`japanese-tutor/`](japanese-tutor/README.md) is a Claude Code plugin that turns the material above
into an actual study loop. It keeps a record of what you know and how well, and teaches from the
resources you switch on.

```
python japanese-tutor/scripts/setup.py     # then, in Claude Code: /japanese-tutor:onboard
```

You say what you want to work on and it runs the session: quizzes what is due, drills a weak point,
walks you through the next section of a guide, generates a reading passage built from your own
known-word list, or takes text you paste and finds the sentences worth mining. It follows whichever
of the five teaching methods you pick - immersion, structural grammar, comprehensible input, output
drilling, or a mix - and answers anything Japanese you raise in passing, logging it as it goes.

It records every answer with your exact wording, which is what lets it tell you that your に/で
mistakes are all with motion verbs, drill the kanji pairs you genuinely confuse side by side, and
show how far your production lags your reading - recognition, recall, reading, listening and
production each get their own schedule.

Python 3.9+ and nothing else - no installs, no accounts. Your progress stays on your machine and is
gitignored. Anki is supported if you already use it and ignored if you do not.

---

## Repository layout

Every topic folder holds its guide (`readme.md`), a provenance file (`sources.md`), and sub-folders
of material.

| Folder              | What is in it                                                                                                                                                                                                                                  |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kana**            | Charts, writing-practice sheets, Tofugu's kana books, kana Anki decks, Unicode hentaigana references, NINJAL loanword proposals, mora and romanization mapping data                                                                            |
| **Romaji**          | The Cabinet Notification that replaced Kunrei-shiki, the repealed 1954 notification, ALA-LC and BGN/PCGN tables, GSI and MLIT signage standards, MOFA passport rules, Hepburn's 1867 dictionary                                                |
| **Grammar**         | Tae Kim, Cure Dolly transcripts, Yokubi, Imabi, Sakubi, Ixrec, Itazuraneko, DoJG, All About Particles, four grammar books, 文化庁 keigo guidelines, conjugation and deconjugation rule sets, a keigo corpus                                    |
| **Kanji**           | KanjiDamage (mirror, markdown and deck), KanjiDamage Plus, Remembering the Kanji vols 1-3 with decks, KANJIDIC2, radical decomposition data, Kanken level data, the official jinmeiyou list, Shuowen Jiezi                                     |
| **Vocabulary**      | Kaishi 1.5k, Ankidrone Essentials and Foundation, Core10k, JP1K, 80-20 Japanese, JMdict, JMnedict, JmdictFurigana, the Tanaka Corpus, several frequency corpora, NINJAL's basic vocabulary survey                                              |
| **Listening**       | Japanese subtitle sets, NHK World's Easy Japanese textbook, Erin's Challenge scripts, a Kansai-ben primer, a university listening course                                                                                                       |
| **Speaking**        | Four audio courses with full audio, three pitch-accent datasets including devoicing data, and phonetics and shadowing scholarship                                                                                                              |
| **Reading**         | Tanoshiku Yomou graded readers, Tadoku free readers across levels, Japan Foundation Kansai readers, a curated Aozora Bunko selection, official JLPT reading sections                                                                           |
| **Writing**         | Five 文化庁 orthography notifications including the joyo kanji table, KanjiVG stroke data, a stroke-order font, genkouyoushi and kanji practice paper, Marugoto composition sheets, W3C Japanese text-layout requirements                      |
| **AJATT**           | Khatzumoto's original AJATT site, Animecards, TheMoeWay, Donkuri, Perdition, saegusa's media recommendations, Krashen's own books plus academic critiques, the Lazy Guide, Morgawr's zettelkasten                                              |
| **General content** | Anki and FSRS documentation with the cross-algorithm benchmark, Yomitan docs, spaced-repetition research, Japanese fonts, textbook sets, and offline mirrors of djtguide/Itazuraneko, Tatsumoto and Tofugu                                     |
| **JLPT**            | Official practice workbooks for every level, the official guidebook, the Can-do list, scoring methodology, the statistics archive back to 2009, Tanos N1-N5 lists, structured kanji and vocabulary datasets                                    |
| **Culture**         | MIT Visualizing Cultures, the JJRS religion archive, anime and manga studies, otaku and fandom scholarship, theatre and aesthetics, the NINJAL dialect atlas, the Aozora classical canon, government white papers, prefecture and holiday data |

---

## Datasets

Most folders carry machine-readable data alongside the reading material - plain JSON, CSV and XML,
with no accounts or API keys:

- **Dictionaries** - JMdict, JMnedict, furigana mappings, an aligned Japanese-English sentence corpus
- **Kanji** - KANJIDIC2, radical and component decomposition, per-character stroke SVGs, Kanken levels
- **Frequency** - several different corpora, because which words are common depends on what you read
- **Pronunciation** - pitch-accent datasets, one of them including devoicing
- **Grammar** - conjugation and deconjugation rules, transitivity pairs, a keigo corpus

Each folder's `sources.md` lists what it holds, where it came from, and its licence. Several are
share-alike, so anything you build on them and publish inherits those terms.

---

## Contributing and new resources

Suggestions and corrections are welcome - especially corrections to the Japanese itself.

- **[CONTRIBUTE.md](CONTRIBUTE.md)** - what belongs here, how to archive a resource and record its
  provenance, the licensing rules, the branching and PR workflow, and the house style the guides are
  written in.
- **[NEW_RESOURCES.md](NEW_RESOURCES.md)** - the queue of material still to be archived and folded
  in. Adding a link there is a useful contribution on its own; you do not have to archive it
  yourself.
- **[CHANGELOG.md](CHANGELOG.md)** - every release and what it added, corrected or moved. Worth a
  look before you report something as missing; it may have been renamed.

## About the offline copies

The mirrors and books here are third-party material, archived so that study does not break when a
site goes down. Credit belongs to the people who made them: Tae Kim, Cure Dolly, Tatsumoto,
KanjiDamage, Tofugu, the Yokubi and Sakubi authors, Imabi, Ixrec, itazuraneko / DJT, TheMoeWay,
Donkuri, saegusa, Khatzumoto, the Anki and Yomitan maintainers, the EDRDG volunteers, and the
Japanese-learning community at large, which has been building and freely sharing this material for
decades. If you find something useful here, go support the original.

Every folder that holds downloaded material also holds a `sources.md` recording, per file, where it
came from, when it was retrieved, its licence, and why it is here.
