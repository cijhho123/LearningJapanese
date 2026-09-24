# KanjiDamage dataset

`kanji.json` (1768 records) and `tags.json` (68 records) are a flat, self-contained
extraction of the local KanjiDamage HTML mirror in
`Resources/Kanji/Kanji Damage/website_mirror`. Everything is data: no hrefs, no slugs,
no file names. A cross-link is stored as the character it points at, or as `{"id": n}`
when that character exists in the source only as an image.

Both files are UTF-8, top level is a JSON array, and there is one record per line, so the
files stay greppable and diffable. Regenerate with `python extract.py` (parses the mirror
into a verbose intermediate) then `python slim.py` (rewrites both files in place, refusing
to run on already-slim input). `slim.py` aborts before writing unless every content atom
and every content string of the verbose shape survives into the slim shape.

## Licence

**No licence is recorded for KanjiDamage anywhere in this repo.** The only statement in
the mirror is the site footer, `(c) 2009-2025`. Treat the content as all-rights-reserved
third-party material: usable for personal study, not cleared for redistribution.

## kanji.json fields

Absent means absent - every null, empty string, empty list and empty dict is omitted, so
most records carry only a handful of keys. Stars run `0..6` and `0` is a real value.

| field | meaning |
|---|---|
| `id` | mirror page id, 1..1768; the join key that `{"id": n}` references use |
| `number` | KanjiDamage's own kanji number as printed on the page |
| `character` | the kanji; absent on the 121 radicals the site draws as images |
| `image` | mirror-relative path to the character artwork; only on those 121 records |
| `meaning` | English keyword |
| `radical_annotation` | where the page states one, e.g. `(left radical)` |
| `strokes` | stroke count |
| `stars` | usefulness rating, 0..6 |
| `tags` | kanji-level tag labels; the inline `Same-ON` label is merged in here |
| `components` | radical breakdown, `{"kanji" or "id", "meaning"}` per part |
| `description` | free prose printed under the header |
| `visual_aids` | mirror-relative paths of the comic images used by the mnemonic |
| `onyomi` | `{"reading", "mnemonic"}` |
| `mnemonic` | the kanji's mnemonic |
| `kunyomi` | `{"reading", "meaning", "stars", "before", "after", "tags"}` |
| `jukugo` | `{"word", "reading", "meaning", "stars", "before", "after", "components", "tags", "notes"}` |
| `lookalikes` | `{"kanji" or "id", "meaning", "hint", "radical", "group"}` |
| `lookalike_notes` | the notes printed under the lookalike table, in table order |
| `used_in` | kanji that use this one as a component |
| `mutants` | variant forms of the character, `{"name", "kanji" or "image"}` |
| `synonyms` | `{"meaning", "words"}` - the synonym page's word list, inlined |

`before` / `after` hold the particles that attach to a reading or compound, so
`{"word": "同時", "after": "に"}` is 同時に. Kunyomi readings keep the `*` (or full-width
`＊`) okurigana marker, e.g. `ひと*つ`. Tags on a jukugo or a kunyomi belong to that word
or reading alone and are never merged up into the kanji's `tags`. `group` appears only on
the 41 pages that print two separate lookalike tables (group 0 is omitted).

## tags.json fields

`id`, `name`, `labels` (other spellings of the label seen on kanji pages - only tag 63),
`description`, `see_also` (other tags named in the description), `kanji` (the kanji that
carry the tag, as characters or `{"id": n}`).

## Caveats

- Each tag's `kanji` list is built from the kanji pages, which the extraction's
  verification found reliable. The tag detail pages disagree: 962 edges appear only on
  tag pages, 384 only on kanji pages, and 36 of the 68 tags have mismatched counts. The
  tag-page edge lists are deliberately not in this dataset.
- 25 tags have no `kanji` list because they are only ever applied to a jukugo or a
  kunyomi (`$$$`, `KANA`, `1/2 KANA`, ...). Find their members in `kanji.json` at those
  levels.
- 281 internal links in the mirror point at pages the mirror does not contain (179 tag
  links, 102 synonym links; 26 distinct targets). No content is lost here - tag labels
  and synonym word lists are stored inline - but 24 of the 68 tags have no description.
- 148 radical pages carry no `stars` and no `strokes`; the site does not rate them.
- 67 external links in the prose (Wikipedia, YouTube, Achewood, ...) were dropped by
  request. Every one of their anchor texts still appears in the retained text; only the
  URLs are gone.
- Image paths are mirror-relative: without the mirror you have all the text but not the
  artwork for the 121 image characters, 22 mutant forms and 109 visual aids.
