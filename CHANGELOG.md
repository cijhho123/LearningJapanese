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

One new dataset, plus JSON/CSV extractions of material the repo already held only as HTML mirrors.
Each extraction sits in an `Extracted Data` folder beside its untouched original, with a `README.md`
stating every field, every known gap and the licence.

### Datasets

- **[KanjiVG r20260714](<Resources/Kanji/KanjiVG project>)** - stroke-order SVGs for 6,703 characters, every stroke a numbered path inside the character's component tree, plus 4,959 variant forms. No readings or meanings. CC BY-SA 3.0.

### Extracted data

- **[KanjiDamage](<Resources/Kanji/Kanji Damage/Extracted Data (JSON)>)** and **[KanjiDamage Plus](<Resources/Kanji/KanjiDamage Plus/Extracted Data (JSON)>)** - 1,768 and 2,136 character records with 68 tags, filterable by star rating, tag or look-alike pair. Not duplicates: 438 characters are Plus-only, 8 original-only.
- **[Itazuraneko reference shelf](<Resources/Grammar/Itazuraneko Master Reference/Extracted Data (JSON-CSV)>)** - 2,628 grammar points keyed into 629 DoJG and 1,032 Donna Toki entries, plus 27,506 kanji by Kanken level and 321 radicals.
- **[Novel kanji inventories](<Resources/Grammar/Itazuraneko Master Reference/Novel Library Kanji Inventories (JSON)>)** - the exact kanji used in each of 8,160 volumes across 5,456 works, so "can I read this yet" becomes a diff.
- **[JLPT Sensei lessons](<Resources/JLPT/JLPT Sensei/Extracted Data (JSON)>)** - 848 grammar and 625 vocabulary lessons with 9,152 example sentences, each carrying kana, romaji and English.
- **[Kansai-ben primer](<Resources/Listening/Kansai-ben Primer (kansaibenkyou.net, CC BY-SA 3.0)/Extracted Data (JSON)>)** - 231 aligned Kansai/standard/English dialogue lines, 280 dialect words, 61 topics. The only dialect parallel corpus here. CC BY-SA 3.0.
- **[Coto JLPT mega list](<Resources/AJATT/Reference Spreadsheets/Coto JLPT Mega List (JSON-CSV)>)** - 8,411 vocabulary, 2,211 kanji and 287 grammar entries with levels, for coverage diffing.

Known gaps, stated in full in each folder's `README.md`: DoJG's notes are a scanned image on 416 of
629 entries and no OCR was attempted; JLPT Sensei's vocabulary is 625 of the 1,523 lessons the site
indexes, though grammar is complete at 848; Coto's grammar file is bare pattern strings, a checklist
rather than a reference.

## [1.0.0] - 2026-09-18

Initial release: the topic guides, the archived resources they index, and a tutor plugin that
teaches from both.

### Guides

A guide per topic, each stating what the topic is, comparing the competing approaches with their
honest costs, recommending one, laying out a phased plan with checkpoints, and indexing the material
in its folder: [Kana](Resources/Kana/readme.md), [Romaji](Resources/Romaji/readme.md),
[Grammar](Resources/Grammar/readme.md), [Kanji](Resources/Kanji/readme.md),
[Vocabulary](Resources/Vocabulary/readme.md), [Listening](Resources/Listening/readme.md),
[Speaking](Resources/Speaking/readme.md), [Reading](Resources/Reading/readme.md),
[Writing](Resources/Writing/readme.md), [AJATT](Resources/AJATT/readme.md),
[General content](<Resources/General content/readme.md>), [JLPT](Resources/JLPT/readme.md),
[Culture](Resources/Culture/readme.md). Grammar is the largest, and adds reference sections on
particles, conjugation, transitivity and keigo.

### Saved sites

- **[Tae Kim's Guide](<Resources/Grammar/Tae Kim Guide to Learning Japanese>)** - the community-default grammar guide, as a 353-page PDF plus the newer website mirror.
- **[Cure Dolly - Organic Japanese](<Resources/Grammar/Cure Dolly - Organic Japanese Guide/cure-script-main/script.html>)** - the structural course transcribed and interlinked, ~100 lessons built on the invisible-subject model.
- **[Yokubi](<Resources/Grammar/yoku.bi grammer guide/YOKUBI_COMPLETE.md>)** - all 63 lessons in one file; the best single-file modern grammar guide here.
- **[Sakubi](<Resources/Grammar/Sakubi - Yesterdays Grammar Guide/sakubi.neocities.org/index.html>)** - 54 lessons, CC0, the minimalist ancestor of Yokubi. A weekend skim.
- **[Imabi](<Resources/Grammar/imabi.org blog offline copy/offline copy/imabi.org/imabi.org/index.html>)** - ~1,985 pages, the deepest free English grammar reference, Beginner through Classical.
- **[Ixrec's Guide](<Resources/Grammar/Ixrec Guide to Japanese/ixrec.neocities.org/index.html>)** - a four-part guide trading beginner-friendliness for accuracy, with dissected manga chapters.
- **[Maggie Sensei](<Resources/Grammar/maggiesensei.com offline copy/maggiesensei.com.zip>)** - a 2009-2026 blog archive, strongest on colloquial usage and sentence-ending particles. Zipped.
- **[Itazuraneko / DJT master reference](<Resources/Grammar/Itazuraneko Master Reference/djtguide.github.io-main/djtguide.github.io-main/index.html>)** - the DJT community library: 文型一覧表, DoJG, どんなときどう使う, HJG, 庭三郎, and the keigo and dialect shelves.
- **[A Dictionary of Japanese Grammar](<Resources/Grammar/DoJG grammer guide/日本語文法辞典.html>)** - all three DoJG volumes on one page with a clickable concept index.
- **[KanjiDamage](<Resources/Kanji/Kanji Damage>)** - component mnemonics for ~1,700 kanji: the whole site as one markdown file, 2,403 split pages, and a browsable mirror that keeps the images.
- **[KanjiDamage Plus](<Resources/Kanji/KanjiDamage Plus/KanjiDamage Plus+.html>)** - the extended community version, ~2,100 entries on one page with redrawn artwork.
- **[Tofugu](<Resources/General content/Tofugu Website offline copy/www.tofugu.com>)** - the article body plus the resource-review database.
- **[Tatsumoto](<Resources/General content/Tatsumoto Blog offline copy/tatsumoto.neocities.org>)** - speedrun-style immersion guides, and the pitch-accent primer the Speaking guide leans on.
- **[DJT guide](<Resources/General content/djtguide.neocities.org>)** - the short community starting guide with its own kana pages.
- **[AJATT, Khatzumoto's original](<Resources/AJATT/AJATT original site (Khatzumoto)/alljapanesealltheti.me>)** - 271 pages of the blog the whole immersion lineage descends from.
- **Immersion community guides** - [Animecards](Resources/AJATT/AnimecardsWebsite), [TheMoeWay](Resources/AJATT/TheMoeWay), [Donkuri](Resources/AJATT/donkuri.github.io), [Perdition](Resources/AJATT/perdition-japanese.github.io) and the [Lazy Guide](Resources/AJATT/lazyguidejp): the current mainstream setup-and-mining guides, with two [quickstart PDFs](<Resources/AJATT/Community Guides>) beside them.
- **[morg.systems](<Resources/AJATT/morg.systems (Morgawr zettel)>)** - Morgawr's zettelkasten, including four consecutive years of logged immersion hours by medium.
- **[saegusa resources](<Resources/AJATT/saegusa resources>)** - the personal hub plus difficulty-ranked media recommendations as screenshots and searchable HTML.
- **[80-20 Japanese](<Resources/Vocabulary/80-20 Japanese>)** - Richard Webb's book, cheat sheets and full site mirror; sentence structure rather than vocabulary.
- **[JLPT Sensei](<Resources/JLPT/JLPT Sensei/jlptsensei.com>)** - 848 grammar and 625 vocabulary lesson pages with their usage notes and example sentences intact.
- **[Kansai-ben Primer](<Resources/Listening/Kansai-ben Primer (kansaibenkyou.net, CC BY-SA 3.0)>)** - 12 four-track example conversations plus grammar, phonology and 280 dialect word pages. CC BY-SA 3.0.
- **[Japanese Pathway](<Resources/General content/Japanese Pathway Website offline copy>)** - a learning blog on annual events, culture and features of the language. Zipped.
- **[AxoGo blog](<Resources/Vocabulary/AxoGo Blog offline copy>)** - two quantitative posts: homonym density against Spanish, and how many kanji you actually need.
- **[NINJAL loanword site](<Resources/Kana/Loanword Paraphrase Proposals (NINJAL)>)** - the 「外来語」言い換え提案 section mirrored, plus the 176-word report and its alphabetical dictionary view.

### Books and courses

- **[Grammar books](Resources/Grammar/Books)** - Japanese the Manga Way, Jay Rubin's Making Sense of Japanese, Teach Yourself Japanese Complete Course and Japanese for You; the last two with per-lesson audio.
- **[Textbook sets](<Resources/General content/Books>)** - Nakama 1-2, Japanese for Everyone, Konomi's Beginning Japanese for Professionals 1-3 (open-licensed), and A History of the Japanese Language.
- **[A Year to Learn Japanese](<Resources/General content/A Year to Learn Japanese>)** - SuikaCider's day-0-to-output roadmap across phonetics, kana, kanji, grammar, vocabulary, input and output.
- **[Kana starter set](Resources/Kana)** - [hiragana](Resources/Kana/Hiragana) and [katakana](Resources/Kana/Katakana) charts, Tofugu's two guides, writing-practice sheets, a one-hour video per script, and a [combined worksheet](<Resources/Kana/Practice Worksheets>).
- **[Introduction to Kanji](<Resources/Kanji/General Introduction>)** - a 14-page academic primer on the import, the go-on/kan-on/tou-on reading layers, and the six character classes.
- **[Remembering the Kanji](<Resources/Kanji/Remembering the Kanji>)** - Heisig volumes 1-3, a printable 2,042-card flashcard set, and the RTK Anki deck.
- **[Mastering Kanji 1500](<Resources/Kanji/japanesepod101 Kanji course>)** - JapanesePod101's radical-first course, 537 pp, plus a 45-minute video lesson with subtitles.
- **[All About Particles](<Resources/Grammar/All About Particles>)** - Naoko Chino's 69 particles and function words as PDF, searchable HTML and an Anki deck, with a [one-page cheatsheet](Resources/Grammar/Particles) beside it.
- **[Classical Japanese Grammar](<Resources/Grammar/Classical Japanese Grammar (OpenCourseWare)>)** - a bungo reference grammar for readers who already have modern Japanese.
- **[Audio speaking courses](Resources/Speaking)** - Speak Japanese with Confidence, Nihongo Nama Chuukei, Teach Yourself Phone Japanese and Teach Yourself Instant Japanese: ~245 audio files, every one with a printed transcript.
- **[Colloquial Japanese](<Resources/Listening/Colloquial Japanese>)** - Routledge's 395-page beginner course, 15 units of business-visitor dialogue; its pronunciation chapter is the on-topic part.
- **[Preadvanced Japanese](<Resources/Listening/Preadvanced Japanese (PDXOpen, Portland State University)>)** - Portland State's open-licensed course textbook, four themed units written to be used with audio.
- **[JapanesePod101 sheets](Resources/Vocabulary/japanesepod101)** - 45 thematic cheat sheets, a 112-page conversation bundle and a seasonal writing workbook.

### Reading material

- **[Tadoku free graded readers](<Resources/Reading/Tadoku Free Graded Readers>)** - 23 illustrated, furigana'd books across levels Start to 4, weighted toward the scarce bottom rungs. CC BY-NC-ND.
- **[KC よむよむ](<Resources/Reading/KC Yomuyomu (Japan Foundation Kansai)>)** - 7 Japan Foundation Kansai readers at A1 to A2/B1 on contemporary everyday topics. CC BY-NC.
- **[Tanoshiku Yomou](<Resources/Reading/Tanoshiku Yomou Read Japanese>)** - two graded reader volumes with answer keys, as image scans with no text layer.
- **[Aozora Bunko selection](<Resources/Reading/Aozora Bunko>)** - 39 public-domain works filtered to modern orthography and kept as XHTML so ruby furigana survives, from Kusuyama's folk tales up to Soseki.
- **[Project Sugita Genpaku](<Resources/Reading/Project Sugita Genpaku>)** - Alice, Through the Looking Glass and The Time Machine in modern Japanese; you already know the plot.

### Listening material

- **[NHK World Easy Japanese](<Resources/Listening/NHK World - Easy Japanese>)** - the 48-lesson course, each lesson a skit with full script, romaji, translation and vocabulary, plus conjugation and counter tables.
- **[Erin's Challenge](<Resources/Listening/Erins Challenge - Japan Foundation>)** - the Japan Foundation's 25 lessons in basic and advanced script form, with audio for lessons 1-5.
- **[Japanese subtitles](<Resources/Listening/Japanese Subtitles (kitsunekko)>)** - 95 timed subtitle files across eight slice-of-life series, curated for narrow vocabulary rather than popularity.
- **[Contractions and phonology reference](<Resources/Listening/Contractions and Phonology Reference>)** - Wikipedia's 縮約形 and Japanese phonology articles, for mora timing, devoicing and ん assimilation.

### Anki decks

- **[KanjiDamage](<Resources/Kanji/Kanji Damage/Official_KanjiDamage_Anki_deck.apkg>)** - the whole site as cards with mnemonics, jukugo, look-alikes and images; the deck the Kanji guide's path is built around.
- **[KanjiDamage Plus](<Resources/Kanji/KanjiDamage Plus/KanjiDamage Plus+.apkg>)** - the extended version, ~200 more characters, one card each with a pre-made mnemonic.
- **[Heisig RTK 6th edition](<Resources/Kanji/Remembering the Kanji>)** - RTK as cards with stories, stroke diagrams and readings, next to the volumes it comes from.
- **[Kana decks](<Resources/Kana/Anki Decks>)** - Just Kana and Recognizing kana, the latter including the obsolete ゐ/ゑ.
- **[A Dictionary of Japanese Grammar](<Resources/Grammar/DoJG grammer guide/DoJG anki deck.apkg>)** - the dictionary as a browsable card index rather than a daily review load.
- **[All About Particles](<Resources/Grammar/All About Particles/All About Particles.apkg>)** - particle cards from the book.
- **[JLPT N1 vocabulary](<Resources/Vocabulary/JLPT N1 Vocabulary>)** - 7,861 notes with expression, reading, meaning and per-kanji meanings.
- **[Japanese locations](<Resources/Vocabulary/Japanese locations>)** - 295 notes on regions, prefectures, cities, wards and the old provinces.

### Dictionaries and datasets

- **[JMdict](<Resources/Vocabulary/JMdict (jmdict-simplified JSON)>)** - 218,776 entries of the dictionary Jisho, Yomitan and jpdb are all built on, as regular JSON with priority tags intact.
- **[JMnedict](<Resources/Vocabulary/JMnedict (jmdict-simplified JSON)>)** - 743,661 proper names with readings and a type tag; the only real fix for unpredictable name readings.
- **[JmdictFurigana](Resources/Vocabulary/JmdictFurigana)** - 236,255 character-level furigana alignments, so you know which kana belong to which character.
- **[Tanaka Corpus](<Resources/Vocabulary/Tanaka Corpus (JP-EN example sentences)>)** - 147,836 aligned JP-EN sentence pairs, each with a hand-checked per-word sense index.
- **[Kyoto Free Translation Task](<Resources/Vocabulary/Kyoto Free Translation Task (KFTT dev-tune-test)>)** - 3,561 professionally translated Wikipedia sentence pairs, a deliberately different register from Tanaka.
- **[KANJIDIC2](Resources/Kanji/KANJIDIC2)** - 13,108 characters with readings, meanings, grades, frequency ranks and dictionary indices, as XML and JSON.
- **[KRADFILE and RADKFILE](<Resources/Kanji/KRADFILE and RADKFILE (kanji-radical decomposition)>)** - kanji to components and components to kanji, the data behind every radical lookup you have used.
- **[CJKVI IDS](<Resources/Kanji/CJKVI IDS (component decomposition)>)** - recursive decomposition trees for 88,937 characters, with 六書 classification on 18,347 of them.
- **[Kanjium kanji data](<Resources/Kanji/Kanjium (phonetic components and kanji elements)>)** - 448 phonetic components with the on-readings they control, per-kanji reading frequencies, element breakdowns and 487 look-alike pairs.
- **[Kanji Alive](<Resources/Kanji/Kanji Alive (radicals and kanji data)>)** - the 214 Kangxi radicals and variants with Japanese names, positions and meanings, plus 1,235 kanji.
- **[Kanji frequency](<Resources/Kanji/Kanji Frequency (multi-corpus)>)** - character counts from Aozora, online news, Wikipedia, Twitter and JPDB, split by occurrence and by document.
- **[Word frequency](<Resources/Vocabulary/Word Frequency (JPDB and BCCWJ)>)** - jpdb's entertainment-media list against NINJAL's balanced BCCWJ, which disagree instructively.
- **[Kanjium word data](<Resources/Vocabulary/Kanjium (pitch accent, jukugo, proverbs)>)** - 124,137 pitch accents, 16,599 jukugo, 3,153 proverbs, homonyms, antonyms and two further frequency corpora.
- **Pitch accent** - [Kanjium](<Resources/Speaking/Pitch Accent Data (Kanjium)>) with 231 homophone groups that differ only by pitch, [Wadoku](<Resources/Speaking/Wadoku Pitch Accent (Yomitan dictionary)>) at 409,568 entries and the only devoicing data here, and a [Wiktionary extract](<Resources/Speaking/Pitch Accent from Japanese Wiktionary>) covering what Kanjium misses.
- **Conjugation and deconjugation** - [jconj's 1,137 generating rules](<Resources/Grammar/Conjugation Rule Tables (JMdictDB - jconj)>), [Yomitan's 808 suffix rules](<Resources/Grammar/Deconjugation Rules (Yomitan - Yomichan)>) for going backwards, [Kanjium's 1,407 words x 80 accented forms](<Resources/Grammar/Conjugation Tables with Pitch Accent (Kanjium)>), and [J-UniMorph](<Resources/Grammar/J-UniMorph Japanese Inflection Dataset>), which labels what each form means.
- **[Grammar points and expressions](<Resources/Grammar/Grammar Points and Expressions (JSON)>)** - 13,220 JMdict expression entries, 595 JLPT-levelled grammar points and 125 counters.
- **[Transitivity pairs](<Resources/Grammar/Transitivity Pairs (Jim Breen)>)** - 267 and 154 pairs grouped by formation pattern, with readings, POS codes and glosses on both halves.
- **[Verb-particle collocations](<Resources/Grammar/Verb Particle Collocations (Kanjium)>)** - 10,740 particle+word pairs over 6,012 words, each attested by a real sentence. Nothing else here covers valency.
- **[Onomatopoeia and manga SFX](<Resources/Grammar/Onomatopoeia and Manga SFX Dataset>)** - 2,644 headwords and 6,155 senses for the ドドド and ズキュウウウン that ordinary dictionaries do not carry.
- **[KeiCO keigo corpus](<Resources/Grammar/Keigo-Annotated Sentence Corpus (KeiCO)>)** - 10,007 sentences labelled for which keigo type they use and graded 1-4 for politeness, across 122 topic fields.
- **[Kana and mora inventory](<Resources/Kana/Kana and Mora Inventory (JSON)>)** - 215 kana typed by class with codepoints and stroke counts; the wall chart as something you can query.
- **Romanization as data** - [CLDR transform rules](<Resources/Kana/Romanization Rule Tables (Unicode CLDR)>) and [romkan's Kunrei/Hepburn table](<Resources/Kana/Kana-Romaji Mapping Tables (romkan)>), giving Hepburn, modified Hepburn, BGN/PCGN, Kunrei-shiki and wapuro as executable rules.
- **[Kana frequency](<Resources/Kana/Kana Frequency (Tono Frequency Dictionary)>)** - per-kana counts over ~5,000 corpus sentences, with youon digraphs counted as single units.
- **Loanword references** - NINJAL's [176 officially hard loanwords with native paraphrases](<Resources/Kana/Loanword Paraphrase Proposals (NINJAL)>) and a [gairaigo and wasei-eigo list](<Resources/Kana/Gairaigo Reference>) for the false friends.
- **[NINJAL basic vocabulary survey](<Resources/Vocabulary/NINJAL Basic Vocabulary Survey (nihongo kyouiku kihongoi)>)** - 6,896 headwords and 6,942 words grouped by meaning rather than by frequency or level.
- **[Marugoto Starter Wordbook](<Resources/Vocabulary/Marugoto Starter Wordbook (Japan Foundation)>)** - the Japan Foundation's 1,000 A1 words organised by can-do topic, with pitch accent marked.
- **[Jinmeiyou and Kanken kanji](<Resources/Kanji/Jinmeiyou and Kanken Kanji (names and difficulty levels)>)** - the Ministry of Justice name-kanji appendix, its queryable CSV, and 6,787 characters graded by Kanken level.
- **[Kanji simplification history](<Resources/Kanji/Kanji Simplification History (1946 reform and kyuujitai-shinjitai)>)** - the 1946 当用漢字表 itself plus a bidirectional kyuujitai/shinjitai map of the 364 characters that changed shape.
- **[Shuowen Jiezi](<Resources/Kanji/Shuowen Jiezi (historical kanji etymology)>)** - Duan Yucai's annotated edition of the 2nd-century dictionary the 六書 classification comes from, as structured XML.
- **[Stroke order](<Resources/Writing/Stroke order>)** - KanjiVG r20250816 as ~11,000 SVGs and one XML, plus a BSD-licensed font whose glyphs are numbered stroke-order diagrams.

### Official and standards documents

- **[Official orthography](<Resources/Writing/Official orthography>)** - the cabinet notifications themselves: the 2010 joyo kanji table and its appendix, okurigana rules, modern kana usage, loanword transcription, the 2022 official-writing guidance, and the 字体/字形 excerpt.
- **[Romanization, official](<Resources/Romaji/Japan Government - Official Notifications>)** - the 2025 Cabinet Notification that replaced Kunrei-shiki, the council report that explains it, the repealed 1954 notification, and the subcommittee minutes.
- **[Romanization standards](<Resources/Romaji/Standards - Library and Geographic>)** - ALA-LC, BGN/PCGN, GSI's toponymic guidelines and English-notation regulation, the NDL reading standard, and two UNGEGN reports.
- **[Passport and practical romanization](<Resources/Romaji/Passport and Practical>)** - MOFA's binding Hepburn table with worked surname examples, a printable second-ministry version, and Microsoft's wapuro reference.
- **Romanization background** - Hepburn's own [1867 dictionary](Resources/Romaji/Historical) as OCR text with Bunkacho papers on how his spellings changed, an [academic framing](Resources/Romaji/Academic), the [national signage guideline](<Resources/Romaji/Signage and Multilingual Guidelines>), and [general guides](<Resources/Romaji/General Guides>).
- **[Keigo Guidelines](<Resources/Grammar/Keigo Guidelines (Bunkacho)>)** - Japan's own 2007 official account of the sonkeigo/kenjougo/teineigo split, with a Q&A chapter on real usage problems.
- **CEFR-modelled frameworks** - Bunkacho's [Japanese-Language Education Reference Framework](<Resources/Grammar/Japanese-Language Education Reference Framework (Bunkacho)>) and the Japan Foundation's [JF Standard Guidebook](<Resources/Grammar/JF Standard Guidebook (Japan Foundation)>), the structure Marugoto is built around.
- **[W3C Requirements for Japanese Text Layout](<Resources/Writing/Text layout>)** - the vendor-neutral specification for 縦書き, 禁則処理, ruby placement and emphasis marks.
- **[Hentaigana code charts](<Resources/Kana/Historical Kana (Unicode Hentaigana)>)** - Unicode's two charts for 299 hentaigana with the man'yogana kanji each derives from, plus the encoding proposal that tells the story.

### JLPT material

- **[Official Practice Workbook 2018](<Resources/JLPT/Official Practice Workbook 2018>)** - 35 PDFs across all five levels: question papers, answer keys, listening scripts and answer sheets.
- **[Official Guidebook](<Resources/JLPT/Official Guidebook>)** and the **[Can-do list](<Resources/JLPT/Official Can-do Self-Evaluation List>)** - what each level means, from the organisers, including the speaking and writing the exam never tests.
- **[Scaled scoring methodology](<Resources/JLPT/Official Scaled Scoring Methodology>)** and **[CEFR correspondence](<Resources/JLPT/Official CEFR Correspondence (Standard Setting)>)** - why raw scores are not comparable across sittings, and the A1-C1 mapping introduced in December 2025.
- **[Official Statistics Archive](<Resources/JLPT/Official Statistics Archive>)** - all 33 per-sitting results pages back to 2009, split Japan versus overseas, plus score distributions for the latest sitting.
- **[New Test Sample Questions 2009](<Resources/JLPT/New Test Sample Questions 2009>)** - the official taxonomy of every question type at every level, with the intent behind each.
- **[Past Exams](<Resources/JLPT/Past Exams>)** - N1 to N5 papers from 1991 onward, with listening audio for N4 and N5.
- **Tanos lists** - the long-standing unofficial per-level [grammar and kanji PDFs](<Resources/JLPT/Tanos JLPT Lists>) and [the same data as CSV/JSON](<Resources/JLPT/Tanos Vocab and Kanji Data (CSV-JSON)>). There is no official grammar list, which is why these exist.
- **[Kanji by JLPT level](<Resources/JLPT/Kanji Data by JLPT Level (KANJIDIC-derived)>)** and **[Yomitan level tags](<Resources/JLPT/Yomitan JLPT Vocab Level Tags>)** - 2,136 jouyou kanji with meanings and frequency ranks, and level tags that show up while you read.
- **[JFT-Basic specification](<Resources/JLPT/JFT-Basic Test Specification (Comparison Test)>)** and the **[2026 registration guide](<Resources/JLPT/Official 2026 Guide (Registration and Logistics)>)** - the CBT the Specified Skilled Worker route accepts instead of N4, and this year's dates and logistics.
- **[N5 learning path](<Resources/JLPT/JLPT N5 learning path>)** - a 12-week N5 plan, an FSRS setup note, and a kanji practice sheet.

### Writing practice

- **[Practice paper](<Resources/Writing/Practice paper>)** - 原稿用紙 in three layouts and kanji grids at 20mm and 10mm, all freely redistributable.
- **[Composition prompts](<Resources/Writing/Composition prompts (JF Marugoto)>)** - Marugoto's own さくぶん worksheets for A1 and A2: a model sentence, then a blank parallel row for yours.
- **[Form filling practice](<Resources/Writing/Form filling practice>)** - the 住民異動届 residence-change form, national reference layout plus two annotated municipal variants.
- **[JapanesePod101 worksheets](<Resources/Writing/japanesepod101 Worksheets>)** - 17 thematic vocabulary-and-writing sheets, greetings through personality adjectives.

### Culture and history

- **[Primary sources and classics](<Resources/Culture/Primary sources and classics>)** - Kojiki and Nihongi in English, Genji, Hearn's Kwaidan and Glimpses, Aston on Shinto, Mitford's Tales of Old Japan, Nitobe's Bushido and Chamberlain's Things Japanese.
- **[Japanese classics from Aozora](<Resources/Culture/Japanese classics (Aozora Bunko)>)** - Hojoki, Tosa Nikki, Taketori, Tsurezuregusa and the Kojiki in Japanese, most paired with a modern-Japanese translation.
- **[Folklore studies](<Resources/Culture/Japanese folklore studies (Aozora Bunko)>)** - Yanagita's Tono Monogatari, annual-observance notes, legends, children's rhymes and regional food terms, plus Orikuchi on setsubun and higan.
- **[Meiji thought](<Resources/Culture/Meiji thought and society (Aozora Bunko)>)** - Fukuzawa's An Encouragement of Learning and The New Greater Learning for Women: modernisation argued from the inside.
- **[MIT Visualizing Cultures](<Resources/Culture/History - MIT Visualizing Cultures>)** - thirteen Dower and Miyagawa image-and-essay units, from the Opium Wars through Hiroshima to the 1960 Anpo protests.
- **[NINJAL dialect atlas](<Resources/Culture/Dialect atlas (NINJAL)>)** - three maps and legends from the Linguistic Atlas of Japan: the sentence-final copula, いる against おる, and the snail rings around Kyoto.
- **Statistics and geography** - the [Statistical Handbook of Japan 2025, the JMA shindo guide and the official holiday list](<Resources/Culture/Official statistics and government>), plus [the 47 prefectures with kana readings](<Resources/Culture/Geography and prefecture data>).
- **[Government white papers](<Resources/Culture/Government white papers (Japanese)>)** - Japanese-language 白書 on karoshi, gender equality and religion: authoritative, and dense administrative reading practice.
- **Open-access scholarship** - peer-reviewed articles on [religion as practised](<Resources/Culture/Religion as practised (JJRS)>), [festivals and everyday culture](<Resources/Culture/Festivals, folklore and everyday culture (Asian Ethnology)>), [theatre and aesthetics](<Resources/Culture/Theatre, arts and aesthetics>), [contested history](<Resources/Culture/Society and contested history>), [dialect and manga language](<Resources/Culture/Dialect and manga-language scholarship (Language in Japan)>) and [premodern diet](<Resources/Culture/Food culture and history (bioarchaeology)>).
- **Pop culture studies** - [anime and manga](<Resources/Culture/Anime and manga studies (open access)>), [JAMS and TWC fan studies](<Resources/Culture/Anime, manga and fan studies (JAMS and TWC)>), [Japanese-language animation scholarship](<Resources/Culture/Anime scholarship in Japanese (JJAS)>), [otaku and doujin](<Resources/Culture/Otaku subculture, doujin and fandom>), [idols and VTubers](<Resources/Culture/Idols, music and VTubers>), [games and visual novels](<Resources/Culture/Games and visual novels>) and [Cool Japan policy](<Resources/Culture/Cool Japan and cultural policy>).

### Research and scholarship

- **[Comprehensible input theory](<Resources/AJATT/Academic sources - comprehensible input theory>)** - Krashen's two core books free from the author, an open-access critique of them, and a study measuring what incidental reading actually retains.
- **[Spaced repetition and memory research](<Resources/General content/Spaced repetition and memory research (open access papers)>)** - Dunlosky's technique review and its practitioner digest, the two Roediger and Karpicke testing-effect papers, and Cepeda's spacing meta-analysis.
- **[FSRS documentation and benchmark](<Resources/General content/FSRS research and benchmark (open-spaced-repetition)>)** - the algorithm's complete wiki plus the cross-algorithm benchmark run over roughly 727 million real reviews.
- **Vocabulary coverage** - the [Matsushita thesis](<Resources/Vocabulary/Vocabulary Size and Text Coverage (Matsushita PhD Thesis)>) and [Honda (2019)](<Resources/Vocabulary/Reading Basic Vocabulary 10k (Honda 2019 Paper)>), the English-side and Japanese-side sources behind the 95%/98% coverage claim.
- **[Pitch accent and prosody scholarship](<Resources/Speaking/Pitch Accent, Prosody and Intonation Scholarship>)** - four papers on whether explicit prosody instruction works, mora timing, and question intonation; [two more](<Resources/Speaking/Shadowing Scholarship>) on what shadowing actually trains.
- **[Phonetic component research](<Resources/Kanji/Phonetic Component Research (J-STAGE)>)** - Ishizawa Seiji on 音符, the Japanese-authored scholarship behind the phonetic-series argument.
- **[Centering and zero pronouns](<Resources/Grammar/Centering and Zero Pronouns in Japanese Discourse (Walker, Iida, Cote)>)** - the peer-reviewed linguistics behind the は-versus-が and invisible-subject claims.
- **[Kana visual similarity](<Resources/Kana/Kana Visual Similarity (Higuchi 2022)>)** - reaction-time data over 4,278 kana pairs: which characters are measurably hard to tell apart, not which ones feel hard.

### Tooling and reference

- **[Anki setup and the official manual](<Resources/General content/Anki>)** - a first-run checklist with per-platform download links, plus the entire manual as one offline file.
- **[Yomitan documentation](<Resources/General content/Yomitan documentation (official, CC BY 4.0)>)** - all eleven pages of the official manual, including the AnkiConnect field-mapping reference the mining workflow depends on.
- **[Dictionary format documentation](<Resources/General content/Dictionary format documentation (EDRDG - JMdict, KANJIDIC)>)** - the annotated JMdict and KANJIDIC2 DTDs, the EDRDG licence, and 20 archived project wiki pages.
- **[Japanese fonts](<Resources/General content/Japanese Fonts>)** - Mincho, Gothic, Hanazono and two Kyoukasho faces, the textbook style that shows how strokes are actually taught.
- **Reference spreadsheets** - [131 podcasts with level and transcript columns, and Coto's N5-N1 checklists](<Resources/AJATT/Reference Spreadsheets>).

### Tutor

[`japanese-tutor/`](japanese-tutor/README.md) is a Claude Code plugin that runs study sessions from
the guides and the resources above. It tracks recognition, recall, reading, listening and production
on separate schedules, records answers in the learner's own wording so it can report which contexts
a particle actually fails in, and follows whichever of five teaching methods is selected. Python
3.9+, standard library only. Learner state under `japanese-tutor/state/` is gitignored.

Every folder holding downloaded material carries a `sources.md` recording each file's origin, date,
licence and reason for being there; several datasets are share-alike, so anything published on top
of them inherits those terms.

[Unreleased]: https://github.com/cijhho123/LearningJapanese/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/cijhho123/LearningJapanese/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/cijhho123/LearningJapanese/releases/tag/v1.0.0
