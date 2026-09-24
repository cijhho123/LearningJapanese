# Coto Academy JLPT Mega List - extracted data

Extracted from `Resources/AJATT/Reference Spreadsheets/Coto JLPT Grammar and Vocab Mega List.xlsx`
(15 sheets, N5-N1 x Grammar/Vocab/Kanji). The source is unmodified; this folder is derived data only.

| File | Records | Per level |
| :-- | --: | :-- |
| `grammar.json` / `.csv` | 287 | N5 40, N4 50, N3 63, N2 63, N1 71 |
| `vocabulary.json` / `.csv` | 8,411 | N5 669, N4 634, N3 1,835, N2 1,797, N1 3,476 |
| `kanji.json` / `.csv` | 2,211 | N5 79, N4 166, N3 367, N2 367, N1 1,232 |

Total 10,909 records = every data row in the workbook; nothing was dropped. Split by content type
rather than by sheet, so `level` is a field. JSON is a flat array, one compact record per line,
UTF-8, `ensure_ascii=False`, ordered N5 -> N1 then by original sheet row. CSV is UTF-8 **with BOM**
(so Excel on Windows renders Japanese), LF endings.

## Fields (keys are omitted when the source cell is blank; CSV writes an empty column)

- `level` - one of `N5 N4 N3 N2 N1`. From the sheet name; the only field not read from a cell.
- `grammar_point` - the pattern, as written. The grammar sheets have **no other column** - no
  meaning, no example sentence. This is a checklist, not a reference.
- `kanji` (vocabulary) - kanji spelling. Absent for the 1,099 kana-only entries (13.1%).
- `kana` (vocabulary) - the reading. The source header says "Hiragana" but the column also holds
  katakana (`ブルー`), so the field is named `kana`. Absent on 1 row (N2 `けれど/けれども`).
- `english` (vocabulary) - gloss, verbatim. Absent on 13 N3 rows. Kept as one string: the source
  separates senses with commas, but 39 cells have commas *inside* a gloss
  (`band (e.g. conduction, valence)`), so splitting would corrupt them.
- `kanji` (kanji) - the character; all 2,211 are exactly 1 character.
- `readings` (kanji) - list, split on the source's `・` (U+30FB). Lossless: rejoining restores the cell.
- `meanings` (kanji) - list, split on the source's `"; "`. Lossless; no bare `;` occurs anywhere.

CSV list separator is **` | `** (space-pipe-space) for `readings` and `meanings`. Verified: that
sequence occurs nowhere in the 10,909 records, so the join is unambiguously reversible.

## Licence

**Copyright (C) 2025 Coto Japanese Academy**, stated in cell B1 of every sheet. That is the only
licence signal that exists: the workbook carries no `docProps` metadata, and
`Resources/AJATT/sources.md` has **no entry for this file at all** (it appears only in
`Resources/AJATT/readme.md`). No open licence, no permission to redistribute, no terms beyond that
line. Treat it as a personal study copy, attributed to Coto Academy. B1 also says the sheet is a
read-only progress tracker and to contact info@cotoacademy.com; it documents the tracker, not the columns.

## Caveats

- **No merged cells exist in this workbook** (verified across all 15 sheets), so nothing was filled
  down and every value is one the source cell literally holds.
- **Dropped columns**: `Mastered?` / `Progress` (a checkbox, `FALSE` on all 10,909 rows) and
  `Percent Completed` / `* Mastered` (two tracker formulas per sheet) - UI, not data. The single
  hyperlink per sheet points at cotoacademy.com from the B1 notice, not per-record data.
- **Duplicates kept, not silently dropped**: `～が早いか` appears twice within N1 Grammar. Four
  grammar points are listed at two levels each (`～ないで`, `～のような`, `～ても` N4+N3;
  `～ことにする` N4+N2), and two N5 vocabulary entries repeat (`たいへん`, `あの`).
- **Source artefacts preserved verbatim**: N3 `ノー` has `（no）` in the reading column; N2
  `けれど/けれども` has kana in the kanji column. Not corrected - no content was added or inferred.
- The workbook's own progress formulas disagree with its own row counts on two sheets: N5 Kanji
  divides by 81 (79 rows exist), N4 Kanji by 165 (166 rows). Coto's arithmetic, not an extraction bug.
- `Resources/AJATT/readme.md` undercounts this workbook: its "~7,300 vocabulary" counts only rows
  with a kanji spelling, omitting the 1,099 kana-only words; it also lists N4 Kanji as 167, not 166.
