# Sources and provenance - machine-readable data and academic literature in `Resources/Speaking/`

This file covers the **structured data sets** in this folder - three pitch accent data sets - and
the **academic literature** on pitch accent instruction, sentence intonation, mora timing and
shadowing that supports several guide chapters. The audio courses and PDFs that make up the rest
of `Resources/Speaking/` are documented in [readme.md](./readme.md).

The three data sets in the first section below are all **pitch accent** data, since the guide has
a full pitch accent chapter.

**Total size of the three pitch-accent data sets: 9.1 MB. Total size of the academic literature: 14.8 MB.**

---

## Known duplication with `Resources/Vocabulary/`

Flagging this rather than hiding it: **`accents.txt` (3.1 MB) and `homonyms.txt` (32 KB) in
[Pitch Accent Data (Kanjium)](<./Pitch Accent Data (Kanjium)>) are byte-identical to copies filed
under `Resources/Vocabulary/`** (in its Kanjium folder - see that folder's own `sources.md`). Both
copies were fetched independently from the same upstream at the same time; the md5s match.

They are kept here anyway, deliberately. This guide has a full pitch accent chapter and that is
where someone looking for accent data will look; `homonyms.txt` in particular is used here as a
**pitch minimal-pair list**, which is a pronunciation use rather than a vocabulary use. If you want
to dedupe, delete one side and leave a pointer - nothing here depends on the file's location.

For completeness, the Kanjium split across folders is: pitch accent (`accents.txt`, `homonyms.txt`)
here; conjugation tables and verb-particle collocations in
[../Grammar](<../Grammar/sources.md>); jukugo, kotowaza, antonyms, compound verbs and the two word
frequency lists in `Resources/Vocabulary/`. Kanjium's `compverbs.txt` was fetched into Grammar and
then deleted once the Vocabulary copy appeared.

---

## Read this before you trust any pitch accent number

Pitch accent data is the one area of open Japanese data where provenance is genuinely murky, and it
is worth being blunt about why.

There is no free, openly-licensed, authoritative Japanese accent dictionary. The authoritative works
are commercial: the **NHK 日本語発音アクセント新辞典** (2016), **新明解日本語アクセント辞典**, and the accent
marks inside 大辞林 / 大辞泉. Every free accent data set is therefore in one of three positions:

1. **It documents an independent source.** Wadoku is in this position - it is a real, long-running
   Japanese-German dictionary project with its own editorial accent marks.
2. **It is compiled from a free, citable community source.** The Wiktionary extract is in this
   position.
3. **It asserts the data as the compiler's own addition without saying where the judgements came
   from.** Kanjium is in this position, and that gap matters - see its entry below.

Yomitan users also circulate pitch dictionaries built straight from NHK 2016 and 新明解. Those are
**verbatim extracts of commercial dictionaries** and are not included here; see "Declined" below.

Practical consequence: when two of these files agree on a word, that is weak corroboration at best,
because nobody can show the chain back to a primary source. Where they disagree, you cannot resolve
it from the data alone. Use them to *notice* accent, not to settle arguments.

---

## Downloaded

| Data set | Source URL | Retrieved | License + attribution | Format | Verified entry count | Why it is worth having |
| :--- | :--- | :--- | :--- | :--- | ---: | :--- |
| **[Pitch Accent Data (Kanjium)](<./Pitch Accent Data (Kanjium)>)** - `accents.txt` plus `homonyms.txt` | <https://github.com/mifunetoshiro/kanjium> (`data/source_files/raw/accents.txt`, `data/source_files/homonyms.txt`) | 2026-09-17 | **CC-BY-SA 4.0** per the repo's own `LICENSE.txt` and README. The README asks for this specific credit: *"The pitch accent notation, verb particle data, phonetics, homonyms and other additions or modifications to EDICT, KANJIDIC or KRADFILE were provided by Uros O. through his free database."* The repo also carries **EDRDG** material (EDICT/KANJIDIC/KRADFILE) which requires the EDRDG notice - see <https://www.edrdg.org/edrdg/licence.html>. **Provenance caveat: the repo claims the accent notation as its compiler's own addition and never states which reference works the accent judgements were taken from.** Treat the licence as asserted rather than verified. | TSV, 3 columns (`word`, `reading`, `mora positions`) | **124,137** accent entries; **690** homonym groups of which **231** are explicitly marked "Different pitch accents" | The single most-used open accent data set in the ecosystem - the Anki PitchAccent add-on, the Yomichan pitch dictionary and most "add pitch to my cards" scripts all read this file. Three columns, one word per line, trivially greppable and joinable against any word list you already have. `homonyms.txt` is the unexpected prize: **231 homophone groups that differ only by pitch**, i.e. a ready-made minimal-pair list, which is exactly what the guide's pitch chapter asks you to drill and what nothing else here supplies. |
| **[Wadoku Pitch Accent (Yomitan dictionary)](<./Wadoku Pitch Accent (Yomitan dictionary)>)** - `wadoku-pitch.zip` | <https://github.com/classicsc/wadoku-pitch-dictionary-for-yomitan> (release `v20260705.01`) | 2026-09-17 | **Murky and stated as such by the packager.** The build script and README are CC0; the *data* is governed by the **WaDoku-Datei-LIZENZ** (Copyright © 1998-2007 Ulrich Apel, <https://www.wadoku.de/wiki/display/WAD/Wörterbuch+Lizenz>), and the upstream `LICENSE` file is literally a pair of URLs rather than licence text. Required attribution, taken verbatim from the dictionary's own `index.json`: *"This dictionary incorporates data from the Wadoku Japanese-German dictionary, which is used under the WaDoku-Datei-LIZENZ. Copyright (C) 1998-2007 Ulrich APEL."* The terms of that licence are not published in a readable form - **do not assume it permits redistribution.** | Yomitan dictionary zip (41 minified JSON `term_meta_bank_*.json` files + `index.json`) | **409,568** pitch entries, of which **29,013** also carry devoicing positions | Three times the coverage of Kanjium, from a genuinely independent editorial source (a real German-Japanese dictionary project, not a repackage of Kanjium), and the **only** data set here with **devoicing (無声化) positions** - which the guide's phonetics section discusses and had no data for. Build is current (July 2026) and the dictionary declares `isUpdatable`, so Yomitan will refresh it in place. |
| **[Pitch Accent from Japanese Wiktionary](<./Pitch Accent from Japanese Wiktionary>)** - `pitch-accent-wiktionary.json` | <https://github.com/jkindrix/japanese-language-data> (`data/enrichment/pitch-accent-wiktionary.json`), extracted from Japanese Wiktionary via <https://kaikki.org> | 2026-09-17 | **CC-BY-SA 4.0** - clean, and the only one of the three with a fully traceable chain (Wiktionary contributors → kaikki.org extract → this repo). Attribution requirements for all of that repo's upstreams are reproduced in the bundled `upstream-ATTRIBUTION.md`. | JSON: `{metadata, entries[]}`, each entry `{word, reading, pitch_positions[], mora_count}` | **12,788** entries | The gap-filler with the cleanest licence. Kanjium has not been updated since 2024 and was largely frozen well before that, so recent vocabulary is simply absent from it; this set was assembled specifically to cover words Kanjium misses. It also carries an explicit `mora_count`, which saves you writing a mora counter just to interpret a bare accent position. |

---

## Downloaded - academic literature

Six papers, split across two folders by topic. None of these is a data file - they are the
scholarship behind chapters that otherwise rest on community consensus and a primer link. Full
citations, abstracts and per-paper notes are in each folder's own `info.txt`;
this table is the short version. **None of the six carries an explicit redistribution licence** -
they are freely downloadable from J-STAGE, a university publication server, or the author's own
university page, but "free to read" and "licensed for redistribution" are not the same thing. That
is flagged per-paper in `info.txt` and is the same posture this folder already takes with the
Bunkacho Keigo Guidelines in `Resources/Grammar` and the Wadoku pitch dictionary above: treat as an
official/scholarly document, credit the author, do not assume blanket reuse rights.

| Folder | Papers | Why it is worth having |
| :--- | :--- | :--- |
| **[Pitch Accent, Prosody and Intonation Scholarship](<./Pitch Accent, Prosody and Intonation Scholarship>)** | Matsuzaki et al. (1994) - a controlled comparison showing a visual "Prosody Table" teaching method beat bare accent-nucleus notation for 12 Korean learners; Kanamura (2020) - a teacher-facing survey on what phonetic training would most help teachers teach pitch accent; Kohno (1998) - a psycholinguistic account of mora timing as two distinct neural rhythm-processing systems; Kori (2013) - the acoustic and perceptual characteristics of plain yes/no question intonation in Tokyo Japanese (rise timing, range, tempo - the sentence-level prosody the guide's word-pitch chapter does not cover) | **This directly answers the guide's "should you study pitch accent deliberately?" question with data, not just community opinion**: Matsuzaki et al. found explicit, visualised prosody instruction outperformed the bare-notation method. Kori's paper is the closest thing here to scholarship on sentence-level intonation, a gap the guide otherwise had nothing for |
| **[Shadowing Scholarship](<./Shadowing Scholarship>)** | Sakoda (n.d.) - a research-synthesis talk connecting SLA theory to the shadowing literature, from a leading Japanese-SLA researcher; Mochizuki (2006) - a full journal article situating shadowing within the wider family of interpreter-training techniques (paraphrasing, sight translation, dictation, slash reading, etc.) and its correlation with learner ability | The guide's shadowing section is a detailed 7-step procedure with **zero citations**. These two put a research basis under it: what shadowing is theorised to train, what the broader technique family looks like, and what the (thin, still-developing) evidence says about transfer to general proficiency |

---

## Not included here

| Not taken | Why |
| :--- | :--- |
| **NHK 2016 pitch accent Yomitan dictionary** (`NHK2016`), **新明解 (Shinmeikai) 8 pitch accents**, **大辞林 pitch accents** - widely circulated in the community Yomitan dictionary drives | These are **verbatim extracts of in-copyright commercial dictionaries**, redistributed without any licence. There is no licensing grey area to discuss: NHK 2016 is a book you can buy. They are also not on GitHub - they live in a Google Drive folder that is not fetchable from here. These are not filed in this repo under an honest licence line, because there is no honest licence line to write. If you want them, they are easy to find; the Kanjium and Wadoku files above cover the same ground with a story you can at least tell out loud. |
| **OJAD** (Online Japanese Accent Dictionary, Tokyo Institute/University group, <https://www.gavo.t.u-tokyo.ac.jp/ojad/>) | **No bulk download exists.** OJAD is the best pitch resource for *learners* - 9,000+ nouns, 3,500 declinable words and ~42,300 conjugated forms, which is precisely the conjugated-form accent data that learners lack - but it is served only through its web interface and Suzuki-kun. There is no data file, no API and no dump. Scraping it would produce a data set with no licence and no upstream to point at. **This is the single biggest remaining gap in this folder** and it cannot be closed by downloading. Note the partial substitute: the Kanjium `conjugations.txt` in [../Grammar/Conjugation Tables with Pitch Accent (Kanjium)](<../Grammar/Conjugation Tables with Pitch Accent (Kanjium)>) carries accent annotations for a dozen conjugated forms of 1,407 words, which is the closest thing here to OJAD's central feature. |
| **kotu.io minimal pairs data** | The minimal-pair trainer's word lists are not published as a data file. `homonyms.txt` above (231 pitch-distinguished homophone groups) covers the same idea with a real licence. |
| **Kanjium `phonetics.txt`** | Name trap: despite the filename this is **kanji phonetic components (声符)**, not speech phonetics. It belongs to kanji study, not this folder. |
| **Kanjium `pitch-accent.json` from `japanese-language-data`** | A re-serialisation of the same Kanjium `accents.txt` already taken above. Duplicate. |
| **Mora inventory / devoicing environment tables as standalone data** | No such structured data set appears to exist openly. The nearest things are here anyway: the mora inventory is in [../Kana/Kana and Mora Inventory (JSON)](<../Kana/Kana and Mora Inventory (JSON)>), and per-word devoicing positions are in the Wadoku dictionary above (29,013 entries). Prose treatments of devoicing rules are in the in-repo IMABI phonology lessons. |
| **Karasawa/唐澤麻里(?) "シャドーイングが日本語学習者にもたらす影響"**, hosted at `teapot.lib.ocha.ac.jp` (Ochanomizu University repository, record 34266) | A real, legitimate-looking PDF from an official university repository, but its citation is ambiguous: a same-or-similar title is attributed elsewhere to a 2010 paper in a *different* numbered volume than the file's own name implies. Rather than publish a guess at authorship on a public repo, this one was left out. The two papers in [Shadowing Scholarship](<./Shadowing Scholarship>) cover the same ground with citations that could be verified. |
| **Matsuzaki (2016), "Nihongo onsei kyouiku ni okeru inritsu shidou - CALL system wo mochiita kyouzai kaihatsu no doukou -"**, Journal of the Acoustical Society of Japan 72(4), pp.213-220 | A real, substantial (8-page) review article by the same lead author as the Prosody Table study taken above, on 20 years of CALL-based prosody teaching tool development. Not taken because it is largely a literature review of the same research programme already represented by the 1994 paper, and six papers already covers this gap without it. Free at <https://www.jstage.jst.go.jp/article/jasj/72/4/72_213/_pdf> if you want the deeper history. |
| **Hotei (2022), "The Effects of Shadowing on Japanese Listening Comprehension Learning"** and **Chang (2022), "Questionnaire Survey of Japanese Language Learners in China Regarding Shadowing Practice"**, both *Journal of Japanese Language Teaching Methods* 29(1) | Two more J-STAGE shadowing papers, both genuine and free, both declined for thinness: this journal's "research report" format is 2 pages, and both are narrow single-cohort findings (no significant L2-vs-L3 difference in listening gains from shadowing; a majority-anxious reaction to shadowing practice in a Chinese-learner survey) that add little once the fuller Sakoda and Mochizuki papers are already in. Free at <https://www.jstage.jst.go.jp/article/jlem/29/1/29_26/_pdf> and <https://www.jstage.jst.go.jp/article/jlem/29/1/29_80/_pdf/-char/ja> if the narrower findings are useful to you. |
| **"母音の無声化・弱化が知覚に与える影響"** (effects of vowel devoicing/weakening on perception), *Journal of the Phonetic Society of Japan* 11(3), 2007 conference abstract | Real and on-topic (devoicing perception), but only a 2-page conference-presentation abstract, and thinner than the mora-timing and prosody-instruction papers already taken. Free at <https://www.jstage.jst.go.jp/article/onseikenkyu/11/3/11_KJ00007631873/_pdf> |
| **NINJAL "語のプロソディーと文のプロソディー" (word and sentence prosody) project page** | A promising NINJAL cross-linguistic prosody research project, but the domain (`crosslinguistic-studies.ninjal.ac.jp`) does not resolve, so what (if anything) it makes downloadable could not be checked. |
| **NHK, 文化庁 or NINJAL-authored "発音指導" (pronunciation-teaching) material aimed at teachers** | Plenty of *bibliographic* trail exists - NINJAL's historical 日本語教育指導参考書 series, various 文化庁 teacher-training curricula - but no confirmed open PDF of a dedicated pronunciation-teaching booklet, only administrative/curriculum documents that mention pronunciation as one line item among many. The Kanamura and Matsuzaki papers above are the closest thing found: Japanese-authored, peer-reviewed research specifically about how to teach pronunciation/pitch, even though not a Bunkacho/NINJAL institutional booklet. |

---

## Notes for actually using these

- `accents.txt` mora positions are **1-based mora indices of the accent nucleus**, and `0` means
  **heiban** (no drop). Multiple comma-separated values mean multiple accepted accents, e.g.
  `１ ひと 0,2`. The bundled `accent.css` is upstream's example stylesheet for rendering the
  notation, kept because it documents the intended display.
- Kanjium's `accents.txt` keys words by their **written form**, including full-width digits
  (`１０月`), so normalise before joining against a dictionary.
- The Wadoku dictionary is kept **as a zip on purpose**, and it is the one thing in these three
  folders that is not unpacked. Yomitan installs from the zip, and unpacking expands 4.2 MB to
  **38 MB** of minified JSON - 8.6x - for no gain beyond greppability. To unpack it anyway:
  `unzip "wadoku-pitch.zip" -d "wadoku-pitch (unpacked)"`. Its `index.json` is already unpacked
  beside the zip so the attribution and format version are readable without extracting.
- Yomitan pitch positions use the same convention as Kanjium (`position`, plus an optional
  `devoice` array of mora indices).
