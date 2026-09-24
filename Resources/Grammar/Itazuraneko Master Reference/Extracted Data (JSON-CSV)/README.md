# DJT / Itazuraneko archive - extracted datasets

Five datasets pulled out of the local Itazuraneko "DJT guide" mirror at
`Resources/Grammar/Itazuraneko Master Reference/djtguide.github.io-main/djtguide.github.io-main/`.
Source and image paths below are relative to that directory. Every JSON file is a flat array,
UTF-8, **one record per line**; a key whose value would be null/empty is omitted - absent means
absent. The three CSVs mirror the slimmed JSON and are UTF-8 with BOM, LF endings. Rebuild with
`python slim.py <dir-holding-the-original-verbose-JSONs>`.

## Licence

**No licence is recorded anywhere.** The mirror has no LICENSE/COPYING file and no copyright
statement, and this repo records none for it. The underlying works are commercial (A Dictionary
of Basic / Intermediate / Advanced Japanese Grammar; 日本語表現文型辞典) and the mirror is an
unauthorised scan. Treat the whole archive as all-rights-reserved and keep it local.

## dojg.json - 629 entries - `grammar/dojg/dojgall.html`

A Dictionary of Basic/Intermediate/Advanced Japanese Grammar, one record per grammar point.

- `id` - unique key, volume + headword; cross-references elsewhere point at this
- `volume` - `basic` | `intermediate` | `advanced`; `grammar_point` - headword as printed
- `part_of_speech`, `page` - page number in the printed volume
- `definition`, `keyword` - the one-word English gloss
- `formation[]` - `{rows: grid of cell strings ("" = empty cell, positions matter), note}`
- `key_sentences[]`, `examples[]` - `{label, ja, hl, en}`
- `hl` - `[[start, end], ...]` character offsets into the sibling `ja` / `text` / `lead`
- `related[]`, `antonyms[]` - `{text as printed, refs: [target id, ...]}`
- `notes[]` - blocks `{kind: p|list|table|img|a|h3, text, hl, refs, lead, lead_hl, items, src}`;
  `refs` = `[[start, end, target id], ...]`, `items[]` = `{text, hl}`, `src` = inline image
- `note_image` - present instead of `notes` when the note is a scanned image
- `anomalies[]` - extraction warnings, on 20 entries

Caveats: **the notes are scanned images for 416 of the 629 entries and no OCR was attempted** -
212 entries have text `notes`, 416 have `note_image`, 1 has neither. One concept image
(`intermediateに関して/関する`) names a file that is not in the mirror. Two entries had a broken
anchor in the source and were given a synthetic `id` of volume + grammar point. One cross-ref
target (`basicも(1)`) does not exist in the dataset and is kept as a bare name.

## donnatoki.json - 1032 records - `grammar/donnatoki/` (41 kana pages)

日本語表現文型辞典 ("Donna Toki"). **631 real entries plus 401 redirect stubs.**

- `id` - headword; the 29 headwords that occur twice get a `__1` / `__2` suffix
- `reading`, `seg` - present only where the headword carries furigana
- `redirect[]` - stub marker: ids this headword forwards to. A stub has nothing else.
- `gloss_en`; `gloss_ja` + `gloss_ja_reading` + `gloss_ja_seg`
- `formation[]` - `{rule, rule_reading, rule_seg, markers}` (the source labels every one 接続)
- `explanation_ja[]`, `explanation_en[]` - `{text, reading, seg}`
- `examples[]` - `{n, text, reading, seg}`, or `{n, lines: [...]}` for multi-speaker dialogue
- `see_also[]` - cross-reference target ids
- `images[]` - illustration paths, on 23 entries

`seg` is the furigana alignment: a list whose elements are either a plain run (string) or a ruby
pair `[base, rt]`. `text` is the concatenation of the bases, `reading` of `rt`-or-base. `reading`
and `seg` appear only on fields that actually carry ruby; where a field has none, only the plain
text is stored. Multi-line examples carry no top-level text: join `lines` with `\n`. Example
numbers `n` are printed on the page as ❶..⓫.

Caveats: **35 cross-references dangle in the source** (4 in `see_also`, 31 in `redirect`); those
keep the name the page linked to, which matches no `id`. One entry (`うえは`) had a second
cross-reference surviving only as malformed markup; the target it names (`からには`) was recovered.

## masterreference.json / .csv - 2628 rows - `grammar/masterreference.html`

Index mapping each grammar point to the book that covers it, and to the entry in this archive.

- `grammar_point`, `ruby` - `[[base, reading], ...]` where the headword has furigana
- `reference` - the book, as printed in the source column
- exactly one of `dojg` (629, a dojg.json id), `donnatoki` (1031, a donnatoki.json id),
  `hjg` (968, an entry number at `https://core6000.neocities.org/hjgp/entries/{hjg}.htm`)

Caveats: **the source HTML was missing every `<tr>` opener**; it was structurally repaired (a
`<tr>` inserted after each `</tr>`, adding no content) before parsing, and the result was then
verified cell-for-cell against a parser-free regex split. 57 `donnatoki` values name a headword
that occurs twice in Donna Toki - the source href was equally ambiguous, so no `__N` is asserted.

## kanji-ichiranhyou.json / .csv - 27506 rows - `horon/kanji/ichiranhyou.html`

Every character on the page, with its Kanken (漢字検定) level, in page order.

- `kanji` - one character; `level` - `10級` 80, `9級` 160, `8級` 200, `7級` 200, `6級` 185,
  `5級` 181, `4級` 316, `3級` 285, `準2級` 333, `2級` 196, `準1級` 904, `1級` 2618, `以外` 21848

The page linked every character out. Those URLs are constructible and were dropped:
`http://jisho.org/kanji/details/{kanji}` for the twelve graded levels,
`https://en.wiktionary.org/wiki/{kanji}` for `以外`.

## radicals.json / .csv - 321 rows - `learn/radicals.html`

The 214 traditional radicals and their variants. `learn/radicalseng.html` holds a byte-identical
main table (it differs only in quiz direction) and was merged, not duplicated.

- `strokes`, `meaning`, `reading`, `note` (variant notes, on 106 rows)
- `image` - **the RADICAL cell is an image, never text**, so this path is the only identifier
  the source gives for the radical glyph itself. No OCR was attempted.
- `position` - legend name of the POSITION cell image (`kana/{position}.png`), absent on 198 rows:
  `hen` left, `tsukuri` right, `kanmuri` top, `ashi` bottom, `tare` hangs down, `nyou` wraps the
  bottom, and the enclosing かまえ variants `kunigamae`, `gyougamae`, `keigamae`, `hakogamae`,
  `tsutsumigamae`, `kigamae`, `mongamae`.
