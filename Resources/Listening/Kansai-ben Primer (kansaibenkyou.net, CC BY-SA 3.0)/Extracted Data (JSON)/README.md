# Kansai-ben Primer - extracted data

Source (read-only, unmodified): `Resources/Listening/Kansai-ben Primer (kansaibenkyou.net, CC BY-SA 3.0)/`
599 HTML pages mirrored from <https://kansaibenkyou.net/>, written by Keiko Yukawa.

Split by *thing a learner queries* rather than by source directory: a conversation, a word,
an explanation, a piece of jargon - so phonology folds into grammar and the audio-only "real
conversations" fold into conversations, distinguished by a `kind` field.

## Files

- **conversations.json** - 48 records. 12 scripted example conversations (231 stanzas total)
  plus 36 audio-only "real conversations".
  `kind=example`: `n` 1-12, `ja`, `en`, `desc`, `chars`, `uses`, `elements`, `lines[]`.
  `lines[]`: `sp` speaker, `k` Kansai-ben, `s` standard Japanese, `e` English,
  `g[]` grammar annotations, `w[]` word annotations; each annotation is
  `{x: the annotated span of k, id, name}` (`name` omitted when equal to `x`).
  `kind=real`: `id`, `title`, `summary`, `tags`, `hints[]`, `expr[]`.
- **grammar.json** - 61 records: 45 grammar points (`kind=grammar`) + 16 phonology topics
  (`kind=phonology`). `id`, `title`, `romaji`, `uses`, `elements`, `body[]`, `sections[]`
  (`h` + `body[]`), `refs[]` bibliographic footnotes.
  A `body[]` block is one of `{p}`, `{h}`, `{ul:[]}`, `{table:{caption,head,rows}}`.
- **words.json** - 280 dialect word entries. `id`, `word`, `romaji`, `meaning`, `type[]`,
  `std`, `std_kanji`, `kanji`, `usage[]` (register warnings), `ex[]`, `note[]`.
- **glossary.json** - 62 terms. `term`, `def`. The linguistic jargon and speaker/tag
  definitions the other three files use.

Flat arrays, one record per line, UTF-8, keys omitted when empty. The remaining 112 taxonomy
pages are navigation listings (their tag names already appear on the records) and are dropped.

## Licence

Quoted verbatim from `kansaibenkyou.net/copyright/index.html`:

> Unless otherwise noted on this page, the contents of this site, and the media contained,
> is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License.

**CC BY-SA 3.0 Unported**, attribution to kansaibenkyou.net / Keiko Yukawa. The exception on
that page covers the site's banner photographs only; no photographs are in this dataset.

## Caveats

- 6 of 550 grammar cross-references dangle: ids 258, 264 and 358 have no page in the mirror.
  They are emitted with `id` but no `name`. All 315 word cross-references resolve.
- `skit-g`/`skit-w` are not stored verbatim. They are the Kansai line with `(<id>span)`
  markers inline; storing the markers as `g[]`/`w[]` spans is lossless (verified by
  reconstructing 461 of 462 tracks byte-exactly; the one exception is cosmetic whitespace
  inside a marker in `06-at-karaoke`).
- Two source typos, reproduced as-is: in `10-on-a-break` one `skit-k` line is missing a
  comma its annotated tracks have; in `11-at-a-pub` one `skit-w` line has a stray `)` where
  an opening `(166` is missing, so that span carries no word reference.
- Audio was excluded from the mirror, so 28 tables in grammar.json have label-only rows
  (`["Standard",""]`) where a clip sat. Real conversations are summaries, not transcripts.
- `phonology/360` mistypes closing `</table>` tags as `<table>`; five example sentences were
  being swallowed and are recovered here by walking the document in reading order.
- Dropped as presentation, with the text kept: `<em>`/`<strong>` emphasis, the inline `?`
  glossary popups (see glossary.json), and footnote superscript numbers (see `refs`).
- The 12 top-level `NN - Title.html` files duplicate `example-conversations/` exactly
  (verified by hash) and are extracted once.
