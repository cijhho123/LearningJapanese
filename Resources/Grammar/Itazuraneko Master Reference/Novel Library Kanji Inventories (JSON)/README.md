# Itazuraneko shousetu kanji inventories

Per-volume kanji inventories for the Itazuraneko/DJT novel library, joined to their works.
Nothing else in this repo maps a specific book to the exact set of kanji it uses.

## Source
`Resources/Grammar/Itazuraneko Master Reference/djtguide.github.io-main/djtguide.github.io-main/library/shousetu/`
- `kanji/satuNNNNNN.html` (8,160 volume inventories), `shoukanji.html` (work -> volume pages,
  titles, authors), `shouall.html` (work -> `sakuhinNNNNNN` id, title, author, volume count)
- `library/shousetu.html` is a *different* page (裏小説, 790 books) and is **not** used here

## Files
**volumes.json** - 8,160 records, flat array, one record per line.
- `id` - `satuNNNNNN`, the volume's natural key
- `work` - `sakuhinNNNNNN` it belongs to (present on all 8,160)
- `n` - kanji count; kept because a UTF-8 string's *character* length is neither its byte
  length nor free to compute in every consumer
- `k` - the kanji as one concatenated string (omitted on the single empty inventory)

**titles.json** - 5,456 records, flat array, one record per line.
- `id` - `sakuhinNNNNNN`
- `title`
- `author` - omitted where the source leaves it blank (3,451 of 5,456)
- `vols` - `satuNNNNNN` ids in the source's volume order

## Representation and ordering
Each inventory is **one concatenated string**, not an array of one-character strings: at
~11.3M kanji an array costs 6 bytes per kanji instead of 3, roughly doubling the file.

**Ordering is first appearance in the book (document order)** - determined, not assumed. Title
kanji sit at median relative position 0.002 and author kanji at 0.004, while corpus-rare kanji
sit at 0.784; under frequency ordering rare author-name kanji could not come first. Inventories
open with title, author and colophon text. The order is meaningful; do not re-sort.

Filtered to Unicode script `Han`; 29,461 non-Han characters removed (kana, `〒` x3695, `ヶ`
x2739, fullwidth punctuation, symbols; 661 distinct). 5 astral-plane kanji survive, so count by
codepoint, never by UTF-16 unit or byte. `〻` (U+303B, x7) is script Han but an iteration mark.

## Licence
**No explicit licence is recorded for the DJT/Itazuraneko mirror anywhere in this repo** - treat
reuse terms as unknown. This catalogues a piracy-adjacent library; what is reproduced here is
bibliographic metadata and character inventories, not book text, but be accurate about what the
underlying collection is.

## Caveats
- **313 volumes have under 50 kanji: source-side stubs, not parse failures.** The source's
  extractor only saw a cover or contents page. One work accounts for 215 (title words + author
  name), 46 hold only the author name `松亜樹`, others only `目次` or `本文`; 25 of the 31
  affected works are stubbed throughout.
- `satu004829` has an empty inventory (marker reads `漢字＃-`): `n` is 0, `k` absent.
- 13 referenced volumes have no kanji page and are absent (11 use an undocumented letter-suffixed
  id like `satu000573A`); `sakuhin004180` and `sakuhin004181` therefore have no `vols`.
- 8 works' stated volume count disagrees with the pages present; the stated count is not carried.
- 22 files hold a corrupted 4-byte sequence (stray +0x40 on byte 2) that almost certainly encoded
  a rare astral kanji; these 32 characters are **dropped, not repaired** - reconstructing them
  would be inventing data.
- 2 volumes contain one duplicated kanji each, where a stray BOM defeated the source's own
  deduplication; inventories are otherwise deduplicated sets.
- The source's stated count matches its emitted entries for 8,158 of 8,160 files (`satu000001`
  and `satu000136` are off by 1 and 2 in the source itself).
- 7,392 distinct kanji corpus-wide across 11,348,387 total inventory entries.
