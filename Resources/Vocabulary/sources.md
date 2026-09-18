# Sources and provenance - machine-readable vocabulary data

This file covers the **six structured-data folders** in `Resources/Vocabulary/`. It does not cover the Anki decks,
PDFs and site mirrors also in this folder - those are described in [`readme.md`](./readme.md).

Everything here was downloaded from its canonical upstream: every JSON parses, every CSV/TSV has a sane header
and plausible row count, every archive passes an integrity test, and the entry counts in the table below are
counted from the installed files rather than copied from a README.

**Total size added to this folder: 207.5 MB.** See the [note on packed and unpacked files](#working-with-the-packed-and-unpacked-files)
for why JMdict and the Tanaka Corpus are shipped the way they are.

---

## The attribution chain you actually have to carry

Six of the seven datasets below are **CC-BY-SA 4.0** or the near-identical **EDRDG licence**, and both are
*share-alike with mandatory attribution*. If this repo is ever published, or if any of this data ends up
inside the local Japanese-tutor tool's output, the following notices have to travel with it:

- **EDRDG** (JMdict, JMnedict, Tanaka Corpus, and - in `../Kanji/` - KANJIDIC2 and KRADFILE/RADKFILE):
  > "This publication has included material from the JMdict (EDICT, etc.) dictionary files in accordance
  > with the licence provisions of the Electronic Dictionary Research and Development Group."

  Licence text: <https://www.edrdg.org/edrdg/licence.html>. Project started 1991 by Jim Breen.
- **Kanjium** (pitch accent, jukugo, phonetics, homonyms):
  > "The pitch accent notation, verb particle data, phonetics, homonyms and other additions or modifications
  > to EDICT, KANJIDIC or KRADFILE were provided by Uros O. through his free database."

  This exact wording is what the author asks for. It is not optional.
- **jmdict-simplified** - the JSON conversion is released under the same licence as the source, so the EDRDG
  notice covers it; crediting Timur Gagiev (scriptin) for the conversion is polite and costs nothing.
- **BCCWJ** - "Copyright National Institute for Japanese Language and Linguistics".

The one dataset with **no stated licence at all** is the JPDB frequency list. See the flag on it below.

---

## Downloaded

| Dataset | Source URL | Retrieved | Licence + attribution requirement | Format | Verified entry count | Why it is worth having |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[JMdict (jmdict-simplified JSON)](<./JMdict (jmdict-simplified JSON)>)** - `jmdict-eng-3.6.2.json.gz`, 10.7 MB (gunzip to 112.5 MB) | <https://github.com/scriptin/jmdict-simplified/releases> (tag `3.6.2+20260914172325`) | 2026-09-17 | **CC-BY-SA 4.0 / EDRDG licence. Attribution mandatory** (see above). Conversion by scriptin, released under the same terms | JSON, single minified line | **218,776 word entries**; 233,458 kanji forms; 265,663 kana forms; 253,596 senses. `version 3.6.2`, `dictDate 2026-09-14` | **The single most valuable file in this folder.** JMdict is the dictionary that Jisho, Yomitan, jpdb and essentially every other tool in this repo are built on top of - having it locally means you own the layer they all sit on. This is the `jmdict-simplified` JSON rather than the raw EDRDG XML, and the difference matters if you are going to script against it: every field is present on every record with a regular shape, no "same as previous entry" implicit values, no DTD entity decoding, no XML parser. Each entry carries kanji and kana forms with `common` flags, per-sense part-of-speech, `appliesToKanji`/`appliesToKana` scoping, cross-references, `misc` tags (`uk`, `arch`, `col`, `vulg`, ...), field-of-use tags and language-of-origin. Note it also carries the **EDICT priority tags** - `news1/news2` (Mainichi Shimbun newspaper corpus), `ichi1/ichi2`, `spec1/spec2`, `gai1/gai2`, `nf01`-`nf48` - so a **newspaper frequency signal is already inside this file**, a seventh corpus on top of the six below. Also: **266 entries are tagged part-of-speech `ctr`**, which is your counter-word list, extractable with one filter |
| **[JMnedict (jmdict-simplified JSON)](<./JMnedict (jmdict-simplified JSON)>)** - `jmnedict-all-3.6.2+20260914172325.json.zip`, 12.8 MB | <https://github.com/scriptin/jmdict-simplified/releases> (same tag) | 2026-09-17 | **CC-BY-SA 4.0 / EDRDG licence. Attribution mandatory** | JSON inside ZIP (see the compression note) | **743,661 name entries**. `version 3.6.2`, `dictDate 2026-09-14` | Proper names - surnames, given names, place names, company names, station names, works of fiction - each with its reading and a `type` classification (`surname`, `fem`, `masc`, `place`, `station`, `company`, `product`, `work`, ...). This is the direct answer to the complaint in the Reading guide that **name readings are unpredictable**: they are unpredictable, the only fix is a lookup table, and this is the lookup table. 743k entries is roughly 3.4x the size of JMdict itself, which is a decent illustration of how much of written Japanese is proper nouns you cannot derive |
| **[JmdictFurigana](./JmdictFurigana)** - `JmdictFurigana.txt`, 11.6 MB | <https://github.com/Doublevil/JmdictFurigana/releases> (release `2.3.1+2026-08-25`) | 2026-09-17 | **CC-BY-SA** - "distributed under the same licence as JMDict". Attribute Doublevil **and** EDRDG | Pipe-delimited text, one word per line | **236,255 furigana mappings** | Solves a problem that looks trivial and is not: JMdict tells you 一時間 reads いちじかん, but **not which kana belong to which character**. This file does - the record is `word`, `reading`, then `0:いち;1:じ;2:かん`. That character-level alignment is what you need to render real furigana, to build cards where only the unknown character's reading is hidden, or to detect that a word uses an irregular reading. It is built by an actual matching algorithm with a hand-maintained exception list for special readings, so it is genuinely hard to reproduce. Parsing is two `split()` calls; note the file starts with a UTF-8 BOM (read it as `utf-8-sig`). The upstream also ships a 33 MB JSON of the same data and a 78 MB JmnedictFurigana - neither included, see below |
| **[Tanaka Corpus (JP-EN example sentences)](<./Tanaka Corpus (JP-EN example sentences)>)** - `examples.utf`, 31.5 MB | <http://ftp.edrdg.org/pub/Nihongo/examples.utf.gz> | 2026-09-17 | **CC-BY-SA 4.0 / EDRDG licence. Attribution mandatory.** Sentence contributions also credited to the Tatoeba project | Plain text, alternating `A:`/`B:` line pairs | **147,836 aligned Japanese-English sentence pairs**, each with a matching `B:` word-index line (147,836 of those too) | The aligned sentence corpus, and the one behind the example sentences you see on Jisho and in WWWJDIC. The `A:` line is the Japanese sentence, a tab, and its English translation. The `B:` line is what makes this better than a plain bitext: it is a **hand-checked index of every dictionary word in the sentence**, giving the dictionary form, the reading, a sense number and the inflected surface form. So you can answer "give me sentences where 見る is used in sense 3" - a query a raw sentence dump cannot answer at all. For a local tutor tool that wants to show a real example of a word in use, this is the file. Lineage note: Tatoeba's Japanese corpus was **seeded from** this corpus, so the two are not independent - see the declined section |
| **[Kanjium (pitch accent, jukugo, proverbs)](<./Kanjium (pitch accent, jukugo, proverbs)>)** - 8 data files, 11.2 MB | <https://github.com/mifunetoshiro/kanjium> (`data/source_files/`) | 2026-09-17 | **CC-BY-SA 4.0. Attribution mandatory, with specific wording** - see above. Underlying EDICT/KANJIDIC/KRADFILE material is EDRDG | Tab-delimited text | `accents.txt` **124,137 words**; `jukugo.txt` **16,599**; `kotowaza.txt` **3,153**; `compverbs.txt` **430**; `homonyms.txt` **690**; `antonyms.txt` **521**; `novels_freq.txt` **285,718**; `wikipedia_freq.txt` **20,000** | **`accents.txt` is the reason this folder exists.** It is *the* pitch-accent dataset - the one every pitch-accent Anki deck and Yomitan pitch dictionary is ultimately built from - giving the mora position of the accent drop for 124,137 words (`0` = heiban/flat, `2` = drop after mora 2, and comma-separated alternatives where a word has more than one accepted accent). Pitch accent is the most commonly skipped feature of Japanese and the hardest to retrofit later, and this is 3 MB. Alongside it: `jukugo.txt` (compound words with readings and frequency), `kotowaza.txt` (3,153 proverbs and set phrases), `compverbs.txt` (compound verbs), `homonyms.txt` (which words collide in sound - the leech source the vocabulary guide warns about), `antonyms.txt`, and two more frequency corpora (`novels_freq.txt`, from an analysis of 5,000+ novels - the Innocent Corpus lineage; `wikipedia_freq.txt`, top 20,000) |
| **[Word Frequency (JPDB and BCCWJ)](<./Word Frequency (JPDB and BCCWJ)>)** - 2 files, 27.9 MB | <https://github.com/Kuuuube/yomitan-dictionaries> (`data/` and `dictionaries/`) | 2026-09-17 | **JPDB list: no stated licence** - see the flag below. **BCCWJ: (c) National Institute for Japanese Language and Linguistics**, free use for research and education per NINJAL's terms; Yomitan packaging by toasted-nutbread and Kuuube | `jpdb_v2.2_freq_list.csv` is **tab**-separated despite the extension; BCCWJ is a Yomitan dictionary ZIP | JPDB: **278,946 rows**, header `term / reading / frequency / kana_frequency`. BCCWJ: **1,000,219 frequency entries** | The two frequency lists worth having next to each other, because they disagree in an instructive way. **JPDB** is derived from jpdb.io's corpus of anime, drama, light novels, visual novels and web novels - i.e. what you will actually be immersing in - and it gives both a surface-form and a kana-form frequency, which matters for words usually written in kana. **BCCWJ** is the Balanced Corpus of Contemporary Written Japanese, NINJAL's 100-million-word academically balanced corpus spanning books, magazines, newspapers, white papers, blogs and Diet minutes - the closest thing to an authoritative answer, and the one cited in linguistics papers. Compare a word's rank in the two and the corpus-dependence point the [vocabulary guide](./readme.md) makes stops being abstract |

### Counting the frequency corpora

The guide argues that frequency is corpus-dependent and that no single list is "the" list. After this drop you
can demonstrate that across **seven independent corpora**, six of them from local files:

| Corpus | File | Text type |
| :--- | :--- | :--- |
| Newspaper (Mainichi Shimbun) | the `news1`/`news2`/`nf01`-`nf48` tags inside `jmdict-eng-3.6.2.json` | Journalistic |
| Balanced written Japanese | `Word Frequency (JPDB and BCCWJ)/BCCWJ_SUW_LUW_combined.zip` | Books, magazines, papers, blogs, Diet minutes |
| Anime / drama / LN / VN / web novels | `Word Frequency (JPDB and BCCWJ)/jpdb_v2.2_freq_list.csv` | Entertainment media |
| Novels (5,000+) | `Kanjium (pitch accent, jukugo, proverbs)/novels_freq.txt` | Literary prose |
| Wikipedia | `Kanjium (pitch accent, jukugo, proverbs)/wikipedia_freq.txt` | Encyclopedic |
| Aozora Bunko, online news, Twitter, Wikipedia | `../Kanji/Kanji Frequency (multi-corpus)/` | Four more, at the character rather than word level |
| Netflix subtitles | the `NetfilxFreq` field in the online AnkiDrone Core10k (extra) deck - see [`readme.md`](./readme.md#online) | Subtitles |

---

## Working with the packed and unpacked files

JMdict's unpacked JSON is 112.5 MB - over GitHub's 100 MB single-file limit - so it is stored as
`jmdict-eng-3.6.2.json.gz` (10.7 MB) instead. `gunzip -k` it to work unpacked locally, or stream it directly -
`gzip.open()` in Python and `zcat ... \| jq` both read it without unpacking. Note that the unpacked JSON is
**one single minified line**, so `head` and `grep -n` are useless on it and `json.load` needs roughly 1.5 GB
of RAM. Use `jq`, a streaming parser such as `ijson`, or scriptin's own `@scriptin/jmdict-simplified-loader`.

If you want the Tanaka Corpus compressed too: `gzip -9 "Tanaka Corpus (JP-EN example sentences)/examples.utf"`
shrinks it from 31.5 MB to 22.2 MB.

### What is kept compressed, and why

| File | Compressed | Unpacked | Reason |
| :--- | ---: | ---: | :--- |
| `JMnedict (jmdict-simplified JSON)/jmnedict-all-...json.zip` | 12.8 MB | 167.1 MB | 743,661 name entries in one minified line. `unzip` it if you want it on disk; a Python `zipfile` plus `json.load` on the member streams it without extracting. |
| `Word Frequency (JPDB and BCCWJ)/BCCWJ_SUW_LUW_combined.zip` | 17.8 MB | 81.3 MB | This is an **installable Yomitan dictionary** - the ZIP is the artifact you drag into Yomitan, so it stays a ZIP. Its unpacked form is a single 81.3 MB `term_meta_bank_1.json`, one `unzip` away if you want it on disk. |

---

## Flagged licence issues

1. **The JPDB frequency list has no stated licence.** It is a scrape of jpdb.io's frequency data, redistributed
   by Kuuuube with a source link and nothing else. jpdb.io itself publishes no licence for it. It is
   universally used in the immersion-learning community and nobody has objected, but that is convention, not
   permission. **Fine for personal use; do not redistribute it or ship it inside a tool.**
2. **Share-alike is contagious.** JMdict, JMnedict, the Tanaka Corpus, JmdictFurigana and Kanjium are all
   CC-BY-SA or EDRDG-licensed. If the local tutor tool ever emits this data to anyone other than you, the
   output inherits share-alike and needs the attribution notices at the top of this file.
3. **BCCWJ's terms are "research and educational purposes", not a standard open licence.** Personal study is
   squarely inside that. Commercial use is not.
4. **Kanjium's attribution wording is prescribed by the author**, not generic. Use his sentence verbatim.

---

## Not included here

### Not included: size or redundancy

| Resource | URL | Why not |
| :--- | :--- | :--- |
| **`JmdictFurigana.json`** (33.1 MB) | <https://github.com/Doublevil/JmdictFurigana/releases> | Identical information to the 11.6 MB `.txt` included here, at 2.9x the size. The `.txt` is pipe-delimited with a semicolon-separated index list - two `split()` calls. Fetch the JSON separately if you would rather not write the parser |
| **`JmnedictFurigana.txt`** (26.8 MB) / **`.json`** (78.2 MB) | same | Character-level furigana alignment for ~750k proper names. Genuinely useful, but JMnedict already gives you the full reading of every name, and the per-character split matters far less for names than for vocabulary - you look names up, you do not decompose them. Not included here; a good candidate to add if this folder grows |
| **Raw `JMdict_e.gz` XML** (10.6 MB, ~85 MB unpacked) | <http://ftp.edrdg.org/pub/Nihongo/JMdict_e.gz> | `jmdict-simplified` is a faithful conversion of exactly this file and is far easier to script against. Keeping both would be ~85 MB of duplicate data. Note: unlike KANJIDIC2 - where the XML is kept, because its DTD documents field meanings the JSON drops - jmdict-simplified publishes a full schema at <https://scriptin.github.io/jmdict-simplified/>, so nothing is lost by skipping the XML here |
| **`jmdict-all`** (all 11 gloss languages, 23.9 MB zip) | same release | 2.2x the size of the English-only build, for translations into Dutch, Hungarian, Slovenian and so on. Took `jmdict-eng`. Note `jmdict-eng-common` (1.4 MB zip) also exists if you ever want only the common vocabulary |
| **`jmdict-examples-eng`** (13.5 MB zip) | same release | JMdict with Tatoeba example sentences pre-attached to each sense. Elegant, but it overlaps both the plain JMdict and the Tanaka Corpus already here, and would have been a third copy of JMdict's 218k entries |
| **Tatoeba raw exports** | <https://downloads.tatoeba.org/exports/per_language/jpn/> | Tatoeba publishes `jpn_sentences.tsv.bz2` (3.4 MB) and `jpn-eng_links.tsv.bz2`, but the links file holds only sentence-ID pairs - to get usable JP-EN pairs you must also pull `eng_sentences.tsv.bz2` (24.9 MB) and join them yourself. The Tanaka Corpus is included instead: pre-joined, and it is the corpus **Tatoeba's Japanese side was originally seeded from**, plus it adds per-word sense indices Tatoeba has no equivalent of. If you want the modern, larger Tatoeba set, <http://www.manythings.org/anki/jpn-eng.zip> (4.8 MB) is the pre-joined pair export |
| **Kanjium `particles.txt`** (12.3 MB) and **`conjugations.txt`** (6.8 MB) | <https://github.com/mifunetoshiro/kanjium> | `particles.txt` is verb+particle pairs with example sentences - good data, but it is grammar rather than vocabulary; see `Resources/Grammar/` instead. `conjugations.txt` is a pre-expanded conjugation table with a search-tokenisation hack; any morphology library generates it on demand |
| **Kanjium `kanjidb.sqlite`** (35.8 MB) | same | A single SQLite database containing everything above plus stroke-order images, etymology composites and readability scores - genuinely tempting if you would rather write SQL than parse TSV. Declined only on size: the plain-text `source_files/` give the same data at a third of the cost. **If you want one queryable file instead of 20 text files, fetch this** |
| **Yomitan JPDB / BCCWJ dictionary variants** (kana, display-only; ~5 MB each) | <https://github.com/Kuuuube/yomitan-dictionaries> | Presentation variants of frequency data already here. The raw CSV is the scriptable form, and one BCCWJ dictionary is enough |

### Not included: licence or provenance

| Resource | URL | Why not |
| :--- | :--- | :--- |
| **Core 2k / 6k / 10k word lists** | various AnkiWeb mirrors | The Core series derives from the **iKnow! / Smart.fm** word lists, which are commercially owned. Every "Core 10k" in circulation is an unlicensed redistribution and there is no clean licensed version to fetch. Skipped deliberately. You lose little: it was always a *frequency-ordered list*, and you now have seven frequency corpora to build an equivalent from, plus `Kaishi 1.5k` - explicitly "in the spirit of Core 2k" - linked from [`readme.md`](./readme.md#online) |
| **NINJAL BCCWJ frequency lists, canonical** (`BCCWJ_frequencylist_suw_ver1_0.zip` and friends) | <https://clrd.ninjal.ac.jp/bccwj/freq-list.html> | The canonical upstream would be preferable to a repack, but the documented download host `pj.ninjal.ac.jp` **no longer resolves**, and the `clrd.ninjal.ac.jp` and `repository.ninjal.ac.jp` paths for the ZIPs both 404 - only the manual PDF is still served. The maintained Yomitan repack is used instead, and carries NINJAL's copyright notice in its `index.json`. Worth retrying occasionally |
| **jiten.moe frequency dictionaries** (12 per-media corpora plus a kanji list, CC-BY-SA 4.0) | <https://jiten.moe/frequency-dictionaries> | The **best-licensed multi-corpus frequency set found** - separate lists for anime, drama, manga, movies, novels, non-fiction, video games, visual novels, web novels, YouTube and audio works, built from 3.2 billion characters across 16,368 titles, in both Yomitan and CSV form, explicitly CC-BY-SA 4.0. Not included here because the site is a JavaScript app and the download URLs are not present in the served HTML, so it cannot be fetched non-interactively. **Strong recommendation: grab the CSVs from a browser.** It would do the corpus-comparison job better than anything here |
| **`gokan-dev/gokan-dataset`** (35,814 words, 31,355 sentence sets) | <https://github.com/gokan-dev/gokan-dataset> | Flat static JSON and nicely cross-linked, but a new single-maintainer project with no track record and unclear provenance for its glosses. Everything it offers is covered by JMdict plus the Tanaka Corpus, from sources with 30-year histories. Not worth the verification risk |
| **Jitendex** | <https://github.com/stephenmk/Jitendex> | Excellent, actively maintained, CC-BY-SA - JMdict cleaned up and enriched for Yomitan by the author of the JLPT tag dictionary already in `../JLPT/`. Declined as a **presentation layer over data you now have raw**: it is built for Yomitan popups rather than scripting, and would be a third copy of JMdict's entries. Install it in Yomitan; do not store it here |
| **Thematic and counter word lists from teaching sites** | various | Every well-built site checked (JapanesePod101, Tofugu, SakuraMani, 90DayJapanese) is copyrighted site content with no bulk export, so nothing was scraped. Counters specifically are already solved: **266 JMdict entries carry part-of-speech `ctr`** - filter for it and you have a licensed counter list with readings and glosses |

---

## Additional resources

This section covers five more resources: Japanese-facing (not English-gloss-first) vocabulary research,
domain-specific vocabulary, collocation data, counters, and a source for the guide's "~95%/~98% coverage"
claim.

**Total size: 9.9 MB** across the five folders below.

### Downloaded

| Resource | Source | Retrieved | Licence | Format | Verified count | Why it is worth having |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[NINJAL Basic Vocabulary Survey](<./NINJAL Basic Vocabulary Survey (nihongo kyouiku kihongoi)>)** - 3 files, 1.3 MB | <https://mmsrv.ninjal.ac.jp/bvjsl84/> (DOI `10.15084/00001268`) | 2026-09-17 | **CC-BY 4.0**, stated on the page | 3 `.xlsx` files (zip-integrity tested, `xl/worksheets` parsed directly) | `2_nihongokyoiku01.xlsx`: **6,896 headwords** (見出し語), gojuon order, each cross-referenced against 7 other historical Japanese-teaching word lists (対照資料1-7). `2_nihongokyoiku02.xlsx`: **6,942 words** classified into ~180 semantic categories from the 『分類語彙表』 thesaurus scheme by 22 expert judges, each with an importance code (e.g. `A1`/`A2`/`A3`/`V3`/`O3`). `3_bunrui01.xlsx`: **855 rows** (832 carrying a classification code) - the category-number-to-category-name index those codes point into | This is the item the guide's own gap list asked for by name: a **Japanese-language, NINJAL-produced** vocabulary reference, not another English-gloss frequency deck. It is the digitised data behind NINJAL Report 78 (1984), 『日本語教育のための基本語彙調査』, one of the foundational vocabulary surveys in the field - and the semantic classification file is a genuinely different organising principle from every list already here: grouped by *meaning* (体の類, 抽象的関係, ...) rather than by frequency or JLPT level, which is exactly the kind of thematic clustering the [thematic vocabulary section](./readme.md#3-thematic--textbook-vocabulary) of the guide discusses in the abstract without a real dataset behind it |
| **[Marugoto Starter Wordbook (Japan Foundation)](<./Marugoto Starter Wordbook (Japan Foundation)>)** - 2 PDFs, 2.8 MB | <https://marugoto.jpf.go.jp/en/download/starter_a/> and `/starter_c/` | 2026-09-17 | (c) 2017 The Japan Foundation. Freely published for download by the rights holder; **no open/CC licence stated - see the flag below** | PDF | `MarugotoStarterWordbook_EN.pdf`, 82 pages: self-states **1,000 words** across 18 Can-do topics (700 drawn from the Starter A1 *Katsudoo*/*Rikai* coursebooks, 300 added) - not independently recounted, since the words are laid out across 82 illustrated topic pages rather than a table. `MarugotoStarterCompetencesVocabularyIndex_EN.pdf`: **577 entries, verified by table extraction** (`pdfplumber`, page by page: 50+59+59+58+57+59+59+59+59+58), full 「あ」-「わ」 gojuon range, columns 「ことば」/pitch accent/romaji/English/topic-number | The Japan Foundation is the body that produces the **JF Standard** framework already represented in `../Grammar/JF Standard Guidebook (Japan Foundation)` - but that guidebook is the *framework document*, not a word list. This is the actual **Marugoto** coursebook vocabulary: organised by Can-do topic rather than frequency (a genuinely different ordering principle from Kaishi/Ankidrone/Core10k), and it carries **pitch accent marks** on every entry, which most beginner vocabulary resources skip |
| **[Vocabulary Size and Text Coverage (Matsushita PhD Thesis)](<./Vocabulary Size and Text Coverage (Matsushita PhD Thesis)>)** - 1 PDF, 4.1 MB | Te Herenga Waka - Victoria University of Wellington Open Access repository, via Figshare DOI `10.26686/wgtn.17011514` (`https://ndownloader.figshare.com/files/31466030`) | 2026-09-17 | **"Author Retains Copyright"** per the repository's own metadata - freely downloadable from the university's official open-access archive, but not a CC licence. **See the flag below** | PDF, 388 pages | Tatsuhiko Matsushita, *In What Order Should Learners Learn Japanese Vocabulary? A Corpus-based Approach* (PhD thesis, Victoria University of Wellington, 2012; supervised by Paul Nation and Peter Gu). **This is a source for the guide's own "~95%/~98% coverage" claim** - see the note below. Built the Vocabulary Database for Reading Japanese (VDRJ) from NINJAL's BCCWJ 2009 monitor corpus (33M words) |
| **[Reading Basic Vocabulary 10k (Honda 2019 Paper)](<./Reading Basic Vocabulary 10k (Honda 2019 Paper)>)** - 1 PDF, 632 KB | J-STAGE: <https://www.jstage.jst.go.jp/article/nihongokyoiku/172/0/172_118/_pdf> | 2026-09-17 | Standard J-STAGE / society-journal copyright (発行: 公益社団法人日本語教育学会). Freely downloadable; **no CC mark found on the article - see the flag below** | PDF, 16 pages | 本田ゆかり (HONDA Yukari), 「コーパスに基づく『読解基本語彙1万語』の選定」["Compiling a Corpus-based Educational Word List... Basic Vocabulary of 10,000 Words for Reading Japanese Text"], 『日本語教育』172号 (2019.4), pp.118-133 | A second, independent, **Japanese-side** academic source for the coverage question, built from NINJAL's BCCWJ rather than Matsushita's SLA-literature review. Tables 7-9 (pp.128-129) give measured text-coverage percentages at the 2,000/4,000/6,000/8,000/10,000-word bands, separately for four JLPT reading-exam levels and for four general-register text types (newspaper, web, novel, spoken corpus) - real Japanese coverage data, not an English-language approximation applied to Japanese |
| **[Kyoto Free Translation Task (KFTT dev-tune-test)](<./Kyoto Free Translation Task (KFTT dev-tune-test)>)** - 6 text files + upstream readme, 797 KB | <https://www.phontron.com/kftt/> (Graham Neubig); original text from NICT's Japanese-English Bilingual Corpus of Wikipedia's Kyoto Articles | 2026-09-17 | **CC-BY-SA 3.0**, stated in the upstream `README.txt` (kept here as `upstream-README.txt`) | Plain UTF-8 text, one sentence per line, `.ja`/`.en` files line-aligned | **`kyoto-dev`: 1,166 pairs. `kyoto-test`: 1,160 pairs. `kyoto-tune`: 1,235 pairs. Total 3,561 aligned sentence pairs**, counted with `wc -l` on both sides of each split and confirmed equal | A second aligned parallel corpus, deliberately in a *different register* from the Tanaka Corpus already here: professionally translated and checked Wikipedia articles on Kyoto's history, religion and geography, rather than short dictionary example sentences. Only the three small, hand-checked splits were taken - see the size note below for why the fourth file was left out |

### Why the KFTT training split was left out

The full KFTT release is 99.2 MB, almost entirely the `kyoto-train.ja`/`.en` pair (49.1 MB + 59.9 MB) - automatically
sentence-aligned and not independently hand-checked the way `dev`/`tune`/`test` are documented to be. Taking it
would have been 5x the size of everything else in this section, for the least-curated part of the corpus. `dev`, `tune` and `test`
are the standard small evaluation splits used in the machine-translation literature and are complete, coherent,
professionally-translated documents in their own right.

### Flagged licence issues (additional resources)

1. **Three of these five resources are freely downloadable from their rights holder but are not under an open
   licence**: the Marugoto Starter Wordbook/Index (c) The Japan Foundation, the Matsushita thesis ("Author
   Retains Copyright" on the VUW/Figshare open-access repository), and the Honda (2019) journal article (society
   copyright via J-STAGE). All three are published by the rights holder specifically for free public download -
   which is a meaningfully different situation from an unlicensed scrape - but none of the three grants
   redistribution rights the way CC-BY/CC-BY-SA does. Treat all three as **fine for personal study; do not
   present them as openly-licensed if this repo is redistributed**.
2. The NINJAL Basic Vocabulary Survey and the KFTT data are both **unambiguous CC licences** (CC-BY 4.0 and
   CC-BY-SA 3.0 respectively) and carry no such caveat.

### The guide's 95%/98% coverage claim

The Matsushita thesis added above is a primary source for the coverage thresholds cited in the
[readme's coverage section](./readme.md#coverage-and-comprehension):

- **pp.31-33** review the English-language SLA literature: Laufer & Ravenhorst-Kalovski (2010) propose "two
  thresholds... an optimal one at 98% and a minimal one at 95%", and Matsushita's own conclusion is "98% (one
  unknown word out of 50 words on average) seems enough for independent reading and 95-96% (one unknown word
  out of 20-25 words on average) will be enough for some cases" - with a citation that Komori et al. (2004),
  working on **Japanese** texts specifically, found a threshold around 96%.
- **pp.42-44** give real cumulative-coverage-by-frequency-rank tables for Japanese corpora that closely match the
  guide's own "Top 1,000/2,000/5,000..." table: NLRI magazine data puts the top 1,000 words at ~60%, top 2,000 at
  ~70%, top 5,000 at ~81.7% coverage; NLRI newspaper data is higher - 73.5% / 79.9% / 87.6% at the same bands.

Matsushita is explicit that the figure is corpus- and register-dependent, which is itself the guide's own point,
so this does not hand the guide a single clean "X words = 95%" number for Japanese - but it is a real, citable,
peer-reviewed source for the shape of the claim.

### Not included here (additional resources)

| Resource | URL | Why not |
| :--- | :--- | :--- |
| **IPA "情報技術に関する用語・プログラム言語など Ver.5.0"** | <https://www.ipa.go.jp/shiken/syllabus/ps6vr7000000i9dp-att/shiken_yougo_ver5_0.pdf> | Expected to be an IT-vocabulary glossary; it is not. It is a notation/standards-conformance spec for IT certification exams (which JIS standard applies to which pseudocode construct, which Java/C++/SQL spec version is examinable), with no term-and-definition glossary content, despite being a genuine government-affiliated (IPA) document |
| **DMiME medical term dictionary** | `osdn.net/projects/dmime/` | Reported elsewhere as an open-licence, 40,000+-term medical-Japanese conversion dictionary - exactly the "medical domain vocabulary" gap - but `osdn.net` does not resolve. Not a quality or licence problem; worth retrying |
| **日本語教育語彙表 Ver 2.8.3** (jhlee.sakura.ne.jp/JEV, jreadability.net/jev) | <https://jreadability.net/jev/> | The single best collocation/synonym/usage-range dataset found - ~8,000 headwords with co-occurring-word and synonym data, exactly the "collocation data" gap. Not included on licence grounds: the site's own terms state "secondary distribution of database content is prohibited". Worth revisiting only with direct permission from the maintainers (日本語学習辞書支援グループ) |
| **かりん (karin) collocation search system** | <https://iikaeru.susi.oita-u.ac.jp/karin/index.html> | NINJAL-adjacent noun+verb collocation search tool for learners. Web search interface only; no bulk export found, so nothing to fetch as a file |
| **Matsushita's own lab database page** (which may host the VDRJ word-list data itself, not just the thesis prose) | `http://www17408ui.sakura.ne.jp/tatsum/database.html` | Not reachable. If reachable, this would be a better source than the thesis PDF for machine-readable data |
| **Counters (josuushi) as a dedicated list** | various | JMdict already carries 266 part-of-speech-tagged `ctr` entries (noted above). Tofugu's list is not institutional and has no bulk export; a Yomitan "数え方辞典オンライン" dictionary is a presentation-layer scrape of a commercial site with unclear licence. Nothing found clears the bar of "genuinely better than filtering JMdict" |
| **JETRO Business Japanese Proficiency Test (BJT) vocabulary** | jetro.go.jp | BJT publishes no open word list; its vocabulary materials are commercial textbooks ("BJT Vocabulary" official textbook). No free institutional business-Japanese list found |
| **MEXT 学術用語集 (情報工学編)** | mext.go.jp / jglobal.jst.go.jp | The standalone print glossary series was folded into J-GLOBAL's "オンライン学術用語集" search interface in 2016; no bulk download found for the information-engineering volume specifically |
| **Onomatopoeia, gairaigo/loanwords, verb-particle collocation** | - | Grammar already has an Onomatopoeia and Manga SFX Dataset and Kanjium's Verb Particle Collocations; Kana already has NINJAL's 外来語言い換え提案 and a gairaigo/wasei-eigo list. No materially different, better-licensed alternative was found for any of the three, so none were added, to avoid duplicating those folders |
| **JParaCrawl** | NTT | Gigabyte-scale web-crawled MT corpus; even a modest slice would be noisy auto-aligned pairs with research-only usage terms, a worse fit than KFTT's small, professionally-translated, clearly CC-BY-SA-licensed splits for the same "aligned parallel corpus beyond Tanaka" gap |
