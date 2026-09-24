# KanjiDamage Plus dataset

`kanji.json` is a flat extraction of `Resources/Kanji/KanjiDamage Plus/KanjiDamage
Plus+.html` (one `div.Card` per kanji), plus one field from the sibling `.apkg` deck.
**2,136 records**, flat JSON array, one compact record per line, UTF-8, nulls and empties
omitted. Field names match `temp/kanjidamage/kanji.json` where they mean the same thing.

| field | meaning | fill |
|---|---|---|
| `id` | position in the file, 1..2136; the stable join key | 2136 |
| `meaning` | English keyword (`span.keyword-big`) | 2136 |
| `character` | text of the kanji slot; absent on the 61 image cards | 2075 |
| `mnemonic` | the story prose | 2063 |
| `onyomi` | katakana readings, split on the source's own separators | 1924 |
| `components` | the red-highlighted component names inside the mnemonic | 1911 |
| `stars` | usefulness 0..5; **from the `.apkg`, not the HTML** - see below | 1627 |
| `kunyomi` | `{reading, before, after}`; `before`/`after` hold particles | 1356 |
| `description` | the card's `DESCRIPTION:` block | 151 |
| `used_in` | characters from the card's `USED IN:` block, as characters | 73 |
| `image` | artwork path, relative to the source folder (62 images total) | 61 |
| `number` | the printed number, **only where it differs from `id`** | 50 |
| `visual_aids` | extra artwork printed beside the number | 1 |

**`number` is absent on 2,086 records, meaning `number == id`.** Two of those - `id` 2042
(軸) and 2092 (丑) - print no number at all; the slot is blank and the `.apkg` agrees.
**`stars` is the one field not in the HTML:** the page renders no rating, so it is read
from the deck, the same archived resource by the same author. Range is **0..5** (11 cards
genuinely rate 0) against 0..6 in the original. Okurigana is marked `*` (`ひと*つ`), though
213 readings use the source's `・`; particles: `{"reading":"い*れる","before":"に / を"}`.

## Licence

**No licence is recorded for KanjiDamage Plus anywhere in this repo, and neither source
file carries a copyright or licence statement at all** - not the page, not the deck
description (which only links to AnkiWeb deck 2467137374); `Resources/Kanji/readme.md`
and `sources.md` describe it but state no terms. A community derivative of KanjiDamage,
itself unlicensed here beyond a site footer: treat as all-rights-reserved.

## Compared with the original KanjiDamage dataset (`temp/kanjidamage/kanji.json`)

- Records 2,136 vs 1,768; distinct single characters 2,065 vs 1,644; shared 1,636.
- **438 characters are in Plus but not the original** - mostly radicals and lower
  frequency kanji: 丑 且 串 丷 丹 乃 也 亠 享 仁 仙 伐 伯 但 佐 佳 併 俵 倣 傍 傑 傲 債 儿 冂 冠 ...
- **8 are in the original but not Plus:** ク テ ノ ホ メ ユ 丶 喧 (喧 only inside 喧嘩 in Plus).
- **264 of the 1,636 shared characters (16%) carry a different keyword.**
- Renamed: オ `katakana 'o'`->`Oprah`; ラ `katakana 'ra'`->`rambo`; ネ `NEcrophilia`->
  `Necromancer`; 丙 `t-bone steak`->`third`; 丼 `beef bowl`->`bowl of food`; 丈 `robust`->
  `height`; 純 `epitome`->`purity`.
- Component names: 581 distinct in the original, 1,201 in Plus, 322 shared. Image
  radicals 121 vs 61, and **no image file name is shared** - the artwork was redrawn.
- Both carry `stars`, so the two are comparable on usefulness; Plus prints nothing
  equivalent to `strokes`, `tags`, `jukugo`, `lookalikes`, `mutants` or `synonyms`.

## Caveats

- **The HTML has lost a tag label.** 18 cards carry an empty `<a href=".../tags/24">`
  where the `.apkg` has `STRONG` - the *only* field-level disagreement between the two
  copies. HTML is source of truth for text, so the label is absent here.
- Three deck ratings are malformed and were **left out rather than guessed**: `id` 321
  (4 glyphs), 644 (6 glyphs), 2008 (the kana `はく`). The deck's 287 Anki tags are also
  left out - deck-management metadata, printed on no card, mostly repeating the on-yomi.
- 12 cards have no single character in the kanji slot (`4`, `L`, `x`, `key`, `WHEAT`, `China`,
  `pi`, `thick pie`, `sentry`, `喧嘩`, `⺌+⺍`, `庶 席 度`); stored verbatim in `character`.
- `components` are highlighted runs *inside* the mnemonic, so they repeat text that
  `mnemonic` also holds; each was checked to be a verbatim substring. One card colours
  its mnemonic with `<font>`, off the page's own scheme, so it yields none - not guessed.
- Dropped as chrome or duplication: card 1's colour-code legend; four `span.words`
  fragments (verified duplicates of their own mnemonic); 7 external URLs (6 tag links,
  1 Wikipedia) whose anchor text is retained inline. `mnemonic`/`description`/`used_in`
  split on the card's own labels, so a label before the story pulls tail prose with it.
  Image paths are folder-relative: without `KanjiDamage Plus+_files/` there are no images.
