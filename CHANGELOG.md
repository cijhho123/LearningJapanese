# Changelog

All notable changes to this repository are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning follows
[Semantic Versioning](https://semver.org/spec/v2.0.0.html). For an archive of study material rather
than software, those numbers mean:

- **MAJOR** - the layout changes in a way that breaks existing paths or links.
- **MINOR** - material or a guide is added, or a guide gains a new section.
- **PATCH** - corrections, clarifications and fixes that leave the structure alone.

## [Unreleased]

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

[Unreleased]: https://github.com/cijhho123/LearningJapanese/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/cijhho123/LearningJapanese/releases/tag/v1.0.0
