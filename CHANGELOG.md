# Changelog

All notable changes to this repository are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning follows
[Semantic Versioning](https://semver.org/spec/v2.0.0.html). For an archive of study material rather
than software, those numbers mean:

- **MAJOR** - the layout changes in a way that breaks existing paths or links.
- **MINOR** - material or a guide is added, or a guide gains a new section.
- **PATCH** - corrections, clarifications and fixes that leave the structure alone.

## [Unreleased]

## [1.1.0] - 2026-09-24

One new resource, plus JSON/CSV extractions of material the repo already held only as HTML mirrors.

### Datasets

- **KanjiVG `r20260714`** at [`Resources/Kanji/KanjiVG project/`](<Resources/Kanji/KanjiVG project>) -
  one SVG per character across 6,703 characters, every stroke a numbered path nested inside the
  character's own component tree, so you can ask which strokes make up a component and which one
  carries the reading. Adds 4,959 variant forms (楷書, 表外字, stroke-order) that the older release
  under `Resources/Writing/Stroke order/` does not carry. No meanings or readings - join it to
  KANJIDIC2. CC BY-SA 3.0, attribution mandatory.

### Extracted data

Seven mirrors and one spreadsheet are now queryable as JSON, and CSV where the source was tabular.
Each sits in an `Extracted Data` folder beside its untouched original, with a `README.md` stating
every field, every known gap and the licence - which for most is "none recorded, keep it local".
About 47 MB, 33 MB of that the novel inventories. All indexed in their topic guide and recorded in
that folder's `sources.md`; nothing existing was moved, renamed or edited.

| Dataset | Records | What it gets you |
| :--- | :--- | :--- |
| [KanjiDamage](<Resources/Kanji/Kanji Damage/Extracted Data (JSON)>) + [Plus](<Resources/Kanji/KanjiDamage Plus/Extracted Data (JSON)>) | 1,768 + 2,136 characters, 68 tags | Filter what you could only scroll - by star rating, tag, or look-alike pair. Not duplicates: 438 characters are Plus-only, 8 original-only |
| [Itazuraneko reference shelf](<Resources/Grammar/Itazuraneko Master Reference/Extracted Data (JSON-CSV)>) | 2,628 grammar points, 629 DoJG, 1,032 Donna Toki, 27,506 kanji, 321 radicals | "What is this pattern called and where is it explained" becomes one join instead of five HTML searches |
| [Novel kanji inventories](<Resources/Grammar/Itazuraneko Master Reference/Novel Library Kanji Inventories (JSON)>) | 8,160 volumes across 5,456 works | Diff a book against your known-kanji list to see if it is readable yet. Nothing else here maps a book to the kanji it uses |
| [JLPT Sensei lessons](<Resources/JLPT/JLPT Sensei/Extracted Data (JSON)>) | 848 grammar, 625 vocabulary, 9,152 example sentences | Every sentence carries kana, romaji and English. Levels read from the page, never inferred |
| [Kansai-ben primer](<Resources/Listening/Kansai-ben Primer (kansaibenkyou.net, CC BY-SA 3.0)/Extracted Data (JSON)>) | 231 aligned dialogue lines, 280 dialect words, 61 topics | The only aligned dialect/standard parallel corpus here. Each line carries Kansai, standard, English and resolved notes |
| [Coto JLPT mega list](<Resources/AJATT/Reference Spreadsheets/Coto JLPT Mega List (JSON-CSV)>) | 8,411 vocabulary, 2,211 kanji, 287 grammar | Turns the N5-N1 coverage check into a diff |

Known gaps, stated in full in each folder's `README.md`: **DoJG's notes are a scanned image rather
than text on 416 of its 629 entries** and no OCR was attempted; **JLPT Sensei's vocabulary is
materially incomplete** - the site indexes 1,523 lessons and only 625 were ever mirrored, though
grammar is complete at 848; **Coto's grammar file is bare pattern strings**, a level and a pattern
and nothing else, so it is a checklist rather than a reference. Kansai-ben is the only extraction
carrying an explicit licence (CC BY-SA 3.0, share-alike inherited).

## [1.0.0] - 2026-09-18

Initial release. The repository holds three layers: the topic guides, the archived resources they
index, and an optional tutor plugin that teaches from both.

### Guides

A guide per topic at `Resources/<Topic>/readme.md`, thirteen in total - Kana, Romaji, Grammar,
Kanji, Vocabulary, Listening, Speaking, Reading, Writing, AJATT, General content, JLPT and Culture.
Each one states what the topic is, compares the competing approaches with their honest costs,
recommends one and says why, lays out a phase-by-phase plan with concrete checkpoints, names the
common pitfalls, and indexes the material in its folder.

Grammar is the largest: nine approaches compared, plus reference sections covering particles with a
full is-vs-ga treatment, a conjugation map, transitivity pairs and a keigo primer.

### Resources

Roughly 4.3 GB across about 54,000 files, all usable offline:

- **Site mirrors** - Tae Kim, Cure Dolly, Yokubi, Imabi, Sakubi, Ixrec, Itazuraneko/DJT,
  KanjiDamage, Tofugu, Tatsumoto, TheMoeWay, Maggie Sensei, and Khatzumoto's original AJATT site.
- **Books and courses** - grammar and textbook sets, four audio courses with full audio, Tanoshiku
  Yomou and Tadoku graded readers, Japan Foundation Kansai readers, a curated Aozora Bunko
  selection.
- **Anki decks** - Kaishi 1.5k, Ankidrone Essentials and Foundation, Core10k, JP1K, kana decks, RTK
  volumes 1-3, KanjiDamage.
- **Official documents** - Cabinet and Bunkacho orthography notifications including the joyo kanji
  table, keigo guidelines, romanization tables (ALA-LC, BGN/PCGN, GSI, MLIT, MOFA), W3C Japanese
  text-layout requirements.
- **JLPT material** - official practice workbooks for every level, the guidebook, the Can-do list,
  scoring methodology, past exams N1-N5, and the statistics archive back to 2009.

### Datasets

Machine-readable data alongside the reading material, as plain JSON, CSV and XML with no accounts or
API keys: JMdict, JMnedict, JmdictFurigana, the Tanaka Corpus, KANJIDIC2, KanjiVG stroke data,
radical and component decomposition, Kanken levels, several frequency corpora, pitch-accent sets
including devoicing data, conjugation and deconjugation rules, transitivity pairs, and a keigo
corpus.

### Tutor

[`japanese-tutor/`](japanese-tutor/README.md), a Claude Code plugin that runs study sessions from
the two layers above. It tracks recognition, recall, reading, listening and production on separate
schedules, records answers with the learner's exact wording so it can report which contexts a
particle actually fails in, and follows whichever of five teaching methods is selected. Python 3.9+,
standard library only, no accounts. Learner state under `japanese-tutor/state/` is gitignored.

### Provenance

Every folder holding downloaded material carries a `sources.md` recording, per file, where it came
from, when it was retrieved, its licence, and why it is worth having. Several datasets are
share-alike, so anything built on them and published inherits those terms.

[Unreleased]: https://github.com/cijhho123/LearningJapanese/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/cijhho123/LearningJapanese/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/cijhho123/LearningJapanese/releases/tag/v1.0.0
