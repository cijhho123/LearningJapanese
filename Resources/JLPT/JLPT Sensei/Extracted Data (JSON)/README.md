# JLPT Sensei lesson data (extracted)

Structured extraction of the local mirror at
`Resources/JLPT/JLPT Sensei/jlptsensei.com/`. Flat JSON arrays, UTF-8, one
compact record per line. Empty keys are omitted, so records vary in shape.

| File | Records | Lines | Source pages |
| :-- | --: | --: | :-- |
| `grammar.json` | 848 | 850 | `learn-japanese-grammar/*/index.html` |
| `vocabulary.json` | 625 | 627 | `learn-japanese-vocabulary/*/index.html` |

## grammar.json fields (fill rate)

- `id` 100% - the grammar point as the page writes it
- `reading` 33% - kana reading, only where the page states one
- `romaji` 99.9%, `level` 100% (`N1`..`N5`), `tags` 59% - page's topic tags
- `meaning` 100% - English gloss from the definition line
- `formation` 100% - the "How to use" table, as rows of cells
- `notes` 69% - explanation prose; inner tables become `cell | cell` rows
- `examples` 99.6% - list of `{jp, kana, romaji, en}`
- `vocab` 34% - the page's vocabulary table, as `{w, kana, en}`
- `related` 99.9% / `kanji` 27% - cross-refs, named by the target's own id

## vocabulary.json fields

Same conventions plus `type` 100% (part of speech) and `senses` 12%
(multi-sense list). `reading` 70%, `tags` 30%, `notes` 27% - low because these
pages are mostly structured fields, not prose. `related` points at vocabulary,
`grammar` at grammar points, `kanji` at kanji.

## Where the JLPT level comes from

An explicit on-page statement, never inferred: the `Level:` line in the lesson
header (grammar) or info box (vocabulary). Cross-checked against the heading
banner and the per-level index tables: 0 disagreements across all 1,473 records.

## Licence

**All rights reserved - not redistributable.** jlptsensei.com's terms prohibit
reproduction and redistribution. `Resources/JLPT/sources.md` records the mirror
as a private offline copy for personal study only; there is no licence file in
the mirror. These files are a local reformatting of that private copy and
inherit the same restriction: personal use, do not publish or commit publicly.

## Caveats

- **Vocabulary is materially incomplete.** The index tables list 1,523
  vocabulary lessons but only 625 detail pages were mirrored (898 absent), so
  only 68% of `related` vocabulary refs resolve within this file. Grammar is
  complete: 848 index rows, 848 detail pages, reconciled both directions.
- **Kanji lessons were not mirrored**, so `kanji` values are names that resolve
  to nothing here. The index tables hold 2,495 kanji rows if ever needed.
- **Four upstream errors are reproduced verbatim** (nothing is invented or
  corrected): 2 examples whose `kana`/`romaji` holds the wrong script, 1 whose
  `en` holds the Japanese sentence, 1 English gloss legitimately quoting
  Japanese. Found by checking all 9,152 examples. Examples are paired by DOM
  element id, not document order, so no off-by-one pairing is possible.
- `formation` stays a grid, not a flattened "A + B" string: 394 of 848 tables
  use row/colspans, so flattening would invent unstated relationships.
- Site chrome (ads, nav, Patreon/e-book/flashcard cross-sell, share and comment
  widgets) is stripped; 27 banned markers asserted absent from every output
  string. No proxy-injected content was present in this mirror.
