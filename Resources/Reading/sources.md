# Sources and provenance

Everything in this folder that was fetched from the web, where it came from, what licence it
carries, and what level it is actually at. **All levels below are the publisher's own grading
where one exists**; the honesty notes about real difficulty are in
[Difficulty: honest notes](#difficulty-honest-notes).

Retrieved dates are the date the file was downloaded.

---

## Size situation - read this first

| | Size |
| :--- | :--- |
| *Tanoshiku Yomou* PDF scans (image scans with no text layer) | **67 MB** (4 files) |
| Everything else in this folder | **31 MB** (76 files: 33 PDFs, 39 HTML texts, 3 plain-text files, this file) |
| **Folder total** | **98 MB** |

The folder sits **well over a nominal 50 MB budget**, entirely due to the four pre-existing
*Tanoshiku Yomou* scans (67 MB for 4 files - they are image scans with no text layer). Everything
else here was kept deliberately lean:

- Every PDF here is **the smallest acceptable file at its level**. Tadoku's free readers
  range from 0.35 MB to 36 MB at the same nominal level, because they are full-colour
  illustrated picture books. The Tadoku books here average 0.8 MB against a catalogue
  average of 3.3 MB.
- The 39 Aozora texts are HTML and total **2.8 MB for 39 complete works** - about a tenth of one
  *Tanoshiku Yomou* scan.
- Irodori, the JLPT N2/N1 reading sections, and the rest of the Tadoku catalogue were **skipped
  on size grounds**, with URLs recorded below so they are one curl away.

---

## Downloaded

| Resource | Source URL | Retrieved | Licence / status | Level | Why it is worth having |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tadoku free graded readers** (23 books) | [tadoku.org free books](https://tadoku.org/japanese/en/free-books-en/) | 2026-09-17 | **CC BY-NC-ND 4.0** - explicitly free to download, print and share non-commercially | **Start, 0, 1, 2, 3, 4** (publisher's own 7-band scale) | The single highest-value legitimate beginner download that exists. NPO 多言語多読 is the organisation that established 多読 in Japanese teaching; these are purpose-built, illustrated, furigana'd, and genuinely graded rather than genre-guessed. Rung 1 material - the scarcest rung on the ladder. Flattened illustrated PDFs with no text layer: they cannot be searched or read with a pop-up dictionary, but that fits how rung 1 is meant to be read anyway (no dictionary). Titles include あんこ〜季節のお菓子〜, キツネとツル（イソップ）and 肉じゃが at Level 0; 山に行きました and 柴犬ディナちゃん、秋の京都へ行く！ at Level 1; やせうま and わたしとともだちのほしちゃんとねこのどのちゃん at Level 2. That last one is worth calling out: it is a cumulative, kana-heavy "this is the X that Y" sentence-building book, i.e. it drills the exact nested-relative-clause structure the guide's [parsing wall](./readme.md#i-know-every-word-but-not-the-sentence---the-parsing-wall) section explains (私が昨日買った本 pattern) - at a genuinely beginner level. |
| **KC よむよむ** (7 books) | [JF Kansai KC よむよむ](https://www.jpf.go.jp/j/kansai/clip/yomyom/) | 2026-09-17 | **CC BY-NC 2.1 JP** - the cleanest licence of anything here; redistributable non-commercially | **A1, A2, A2/B1** (CEFR, publisher's own) | Japan Foundation Kansai's own free 多読 series. Distinct from Tadoku: contemporary, Osaka-centred, everyday-life topics (a zoo, an emergency exit, local vegetables, an idol quitting). The Anh-san pair (024 then 025) is a self-introduction followed by an interview with the same person, so vocabulary repeats across the two - unusually good early value. |
| **JLPT Official Practice Workbook 2018, reading sections** (3 PDFs) | [jlpt.jp sample questions](https://www.jlpt.jp/e/samples/sampleindex.html) | 2026-09-17 | **Official free download. Copyright JF / JEES; reproduction and reprinting prohibited without permission.** Downloading for personal study is the intended use. *Not* redistributable - see the caution below. | **N5, N4, N3** (official JLPT calibration) | The only reading passages anywhere that are *officially* level-calibrated rather than someone's opinion. Best used as a **ruler**, not as reading practice: read an N4 passage cold to find out whether you are actually at N4. The 言語知識・読解 section only; the vocabulary and grammar PDFs were skipped as out of scope for a reading folder. |
| **Aozora Bunko, curated selection** (39 works) | [aozora.gr.jp](https://www.aozora.gr.jp/) | 2026-09-17 | **Public domain** - all 39 confirmed against Aozora's own index as 作品著作権フラグ = なし (copyright expired). Aozora's transcriptions are free to use. | **Genuinely mixed - see the honesty notes.** Roughly: folk tales ~N4-N3, Niimi ~N4-N3, Miyazawa ~N3-N2, Akutagawa ~N2, Dazai and Soseki ~N2-N1 | Japan's Project Gutenberg. Selected using Aozora's own 文字遣い種別 (orthography) field so that **every text taken is 新字新仮名** - modern kanji forms *and* modern kana usage. That one filter is what makes this set usable: the same works also exist in 旧字旧仮名 editions that are dramatically harder for no benefit. Taken as the XHTML edition, so **furigana is preserved as ruby tags**, then converted from Shift-JIS to UTF-8. |
| **Project Sugita Genpaku** (3 works) | [genpaku.org](https://www.genpaku.org/) | 2026-09-17 | **Creative Commons share-alike** (the file header grants free use, reproduction and modification, *including commercially*, provided attribution is kept and the same terms are passed on). **The most permissive licence in this folder.** | **~N2.** Intermediate-plus, no furigana | The acknowledged translation counterpart to Aozora: foreign works rendered into **modern** Japanese. Valuable for one specific reason - **you already know the story**, and background knowledge is the cheapest comprehension aid there is, which makes a familiar plot in unfamiliar language much more tractable than unfamiliar prose of the same raw difficulty. Taken as plain `.txt` (converted from Shift-JIS), so fully greppable and Yomitan-able. Note the project stopped adding texts in 2008. |

### Caution on the JLPT PDFs

These are free to download but their terms **prohibit reproduction without permission**. They are
fine sitting on a personal machine, which is what the JF publishes them for. If this repository is
ever made public, remove that folder. The Tadoku, KC よむよむ and Aozora material has no such
problem - all three are explicitly redistributable.

---

## What is in each folder

### Tadoku Free Graded Readers - 23 books, 22 MB

Filenames keep Tadoku's own catalogue code (f0019, w0012 and so on) so each file traces back to
its page at tadoku.org. All have furigana. These are flattened illustrated PDFs with no text
layer, so they cannot be searched or read with a pop-up dictionary.

| Level | Books |
| :--- | :--- |
| Start | あれは何？ / 何を飲みますか？ / 白い？黒い？ |
| 0 | かまきり / よむ？？？ / チワワの花すけ / 夜の空で / カラスと水さし（イソップ）/ たまご / 肉じゃが / あんこ〜季節のお菓子〜 / キツネとツル（イソップ）|
| 1 | メキシコの犬 / チワワの花すけ２ / 山に行きました / 柴犬ディナちゃん、秋の京都へ行く！ |
| 2 | ヴィトリアレジア / 吉四六さんの話 / やせうま / わたしとともだちのほしちゃんとねこのどのちゃん |
| 3 | ふしぎだな / フェリパ |
| 4 | 日本のバレンタインデー |

Levels Start and 0 are deliberately over-weighted (12 of the 23 books): that is the scarcest
material on the whole ladder, and also the cheapest per megabyte. 山に行きました is by an
international learner of Japanese (Tadoku's catalogue includes learner-written entries, not just
native-teacher ones) and reads accordingly - simple, direct sentences describing a trip to the
Sierra Nevada, not a folk-tale register. やせうま and 吉四六さんの話 both draw on Oita-region folk
culture, forming a small regional pair. わたしとともだちのほしちゃんとねこのどのちゃん is a
cumulative, kana-heavy "the X that Y bought/likes/owns" sentence-building book - a real,
beginner-level worked example of the nested-relative-clause structure the guide's parsing-wall
section explains with an invented sentence.

### KC Yomuyomu (Japan Foundation Kansai) - 7 books, 5.0 MB

| Level | Books |
| :--- | :--- |
| A1 | 太郎くんの夏休み / 天王寺動物園 / はじめまして、私はアインです / アインさんインタビュー |
| A2 | 非常口 / 泉州野菜 |
| A2/B1 | アイドルやめたい |

The site also publishes a print-imposition variant of every title (the _bind files); those were
skipped as duplicates of the same content.

### JLPT Official Practice Workbook 2018 - Reading - 3 PDFs, 1.6 MB

N5, N4 and N3 言語知識・読解 sections. N2 and N1 were skipped on size grounds and live at
https://www.jlpt.jp/samples/sample2018/pdf/N2R.pdf and .../N1R.pdf (0.8 MB and 0.9 MB).

### Aozora Bunko - 39 works, 2.8 MB

Grouped by author and numbered in **rough ascending difficulty**, which is the useful ordering:

| Folder | Works | Honest level |
| :--- | :--- | :--- |
| 01 - Folk Tales (Kusuyama Masao) | 桃太郎, 花咲かじじい, 猿かに合戦, ねずみの嫁入り, 舌切りすずめ, かちかち山, 浦島太郎, 一寸法師, 金太郎, 瘤とり, くらげのお使い, 文福茶がま | **The genuinely easy end.** ~N4-N3 |
| 02 - Childrens Stories (Niimi Nankichi) | 飴だま, 去年の木, 二ひきの蛙, がちょうのたんじょうび, くまのこ, たけのこ, こぞうさんのおきょう, 手袋を買いに, ごん狐, おじいさんのランプ | **Easiest individual texts here.** ~N4-N3 |
| 03 - Miyazawa Kenji | 注文の多い料理店, どんぐりと山猫, セロ弾きのゴーシュ, やまなし, オツベルと象, 虔十公園林, 銀河鉄道の夜, 風の又三郎 | ~N3-N2, and deceptive - see notes |
| 04 - Akutagawa Ryunosuke | 蜘蛛の糸, 杜子春, 蜜柑, 羅生門 | ~N2. Short but not easy |
| 05 - Dazai Osamu | 走れメロス, 人間失格 | ~N2 / ~N1 |
| 06 - Natsume Soseki | 夢十夜, 坊っちゃん, こころ | **~N1. The hardest material in the folder** |

### Project Sugita Genpaku - 3 works, 780 KB

不思議の国のアリス (Alice in Wonderland), 鏡の国のアリス (Through the Looking Glass) and
タイムマシン (The Time Machine), as plain UTF-8 text converted from the site's Shift-JIS `.txt`
editions. Each file retains its own licence notice in the header, which is the attribution the
licence asks for - do not strip it. 鏡の国のアリス also exists in an `alice03j` variant that adds
the suppressed Wasp episode; that was skipped as a near-duplicate.

---

## Difficulty: honest notes

The point of this section is that the bottom rungs of the ladder must not be populated with Meiji
literary prose mislabelled as easy. So, bluntly, per group:

**Genuinely beginner-accessible - safe for rungs 1 to 3:**

- **Tadoku Start / 0 / 1** - yes, genuinely. Some Level 0 books are a dozen words a page. This is
  real graded material, not famous material relabelled.
- **KC よむよむ A1** - yes. Short, contemporary, high picture support.
- **Niimi Nankichi's short pieces** - Kuma no Ko, Gachou no Tanjoubi, Takenoko and
  Kozou-san no Okyou are **written almost entirely in kana** for very young children, 4-6 KB of
  HTML each. These are the easiest *native* texts in the folder - a real find: native prose
  a beginner can actually finish. Amedama (5 KB) and Kyonen no Ki (4 KB) are
  the standard learner entry points for this author and deserve the reputation.
- **The Kusuyama Masao folk tales** - retold for children in modern orthography, with a plot most
  readers already know from general culture, and heavy ruby furigana. Nezumi no Yomeiri (14 KB)
  and Urashima Taro (27 KB) are the gentlest. One caveat: they use a **storytelling register**
  with archaic-flavoured flourishes (ございました, おりました) and onomatopoeic set pieces
  (ドンブラコッコ, スッコッコ) that no textbook teaches. Easy to *read*, occasionally odd Japanese
  to *learn from*.

**Famous, and harder than the fame suggests - do NOT treat as beginner material:**

- **Miyazawa Kenji.** The most commonly mis-sold author for learners. It is children's literature,
  it is in modern orthography, and people therefore assume it is easy. It is not: Miyazawa invents
  words, uses Tohoku dialect, writes synaesthetic nature description, and has an idiosyncratic
  private vocabulary. Yamanashi (14 KB) is short but is almost pure invented onomatopoeia.
  Kaze no Matasaburo is **dialect-heavy**, and Ginga Tetsudo no Yoru (162 KB) is long, unfinished
  and dreamlike. The two that are fairly approachable are Chumon no Oi Ryoriten and
  Donguri to Yamaneko. This is rung 4 to 6 material, not rung 1.
- **Akutagawa.** Kumo no Ito (17 KB) is the classic learner first story and is genuinely short -
  but it is Taisho literary prose with ございます narration and vocabulary like 蠢く, 極楽, 水晶.
  Short is not the same as easy. Mikan (18 KB) is the shortest thing he wrote. Early rung 8.
- **Dazai.** Hashire Merosu is a Japanese school set text, which makes it *culturally* accessible
  and heavily supported by online commentary - but the prose is declamatory and long-sentenced.
  Ningen Shikkaku (247 KB) is a full novel and thematically bleak.
- **Soseki.** Bocchan (456 KB) and Kokoro (780 KB) are **the hardest things in this folder**, full
  stop. Meiji-era prose, dense idiom, long paragraphs, and Bocchan additionally carries heavy
  period slang and Matsuyama dialect. They are here because the ladder's top rung needs a target,
  not because they are reading practice. Yume Juya is short per piece and often recommended for
  that reason, but it is oneiric and syntactically strange.

- **Project Sugita Genpaku** is intermediate-plus and has **no furigana**, so it is not a low-rung
  option. Its one real advantage is that you already know the plot. Of the three, **タイムマシン is
  the gentler start**: Wells in translation is plain declarative prose, whereas both Alice books
  are built on puns, invented words and nonsense verse, and a translator forced to reproduce
  wordplay produces Japanese that is *harder*, not easier, than the original's reading level.

**The JLPT PDFs carry the only officially calibrated level numbers in this folder.** Everything
else is a publisher's own scale (Tadoku 0-5, CEFR for KC よむよむ) or an estimate.

---

## Not included here

| Resource | Why not |
| :--- | :--- |
| **NHK News Web Easy** | Wanted badly - it is rung 3 of the ladder. But the article-list endpoint www3.nhk.or.jp/news/easy/news-list.json now returns **HTTP 401**, and NHK content is all-rights-reserved with no redistribution grant. Read it live at [www3.nhk.or.jp/news/easy](https://www3.nhk.or.jp/news/easy/). Third-party mirrors and scraper archives exist on GitHub; they are redistributing NHK's copyright and were not used. |
| **Rest of the Tadoku catalogue** (125 more free books) | Size only, not licence - they are CC BY-NC-ND and free to take. The full catalogue is roughly 470 MB of illustrated PDFs. The 141-book catalogue is trivially re-derivable: the listing page carries a data-level attribute per book, and the PDF URL is tadoku.org/japanese/wp-content/uploads/CODEe-SLUG.pdf, where CODEt-SLUG is the thumbnail filename (e = screen, p = print). |
| **Tadoku Level 5** | All four Level 5 books are 2.5-22 MB. The two most interesting, 夢十夜 and まだらの紐 (the Sherlock Holmes "Speckled Band"), are adaptations of texts free elsewhere - and 夢十夜 is already in this folder from Aozora. |
| **Irodori: Japanese for Life in Japan** (Japan Foundation) | Terms explicitly *permit* saving for personal study, so this was a pure size decision: lessons are **4.5-16 MB each** and the full set is **151 MB**. It is also a course textbook rather than a reader. Free at [irodori.jpf.go.jp](https://www.irodori.jpf.go.jp/). |
| **JLPT N2 and N1 reading sections** | Size. URLs recorded above; 1.7 MB for the pair. |
| **yomujp** | Well-regarded and graded N6-N1, but articles are **free only for their first four weeks**, and the footer states 許可なく転載することを禁じます - reproduction without permission prohibited. Read online at [yomujp.com](https://yomujp.com/). |
| **Hukumusume 福娘童話集** (366 folk tales with audio) | Frequently recommended and genuinely large, but the site is All rights reserved with no reuse grant, and the stories **have no furigana**. Read online at [hukumusume.com/douwa](http://hukumusume.com/douwa/). |
| **Watanoc** | Free N5-N4 web magazine, often recommended, but apparently **unmaintained since around 2016** and it states no reuse terms. [watanoc.com](https://watanoc.com/) |
| **Project Gutenberg Japanese-language books** (22 titles) | A trap: the ja collection is largely **pre-war 旧字旧仮名** (刺靑, 惡魔, 何處へ) or classical (奥の細道), and its one overlap with this folder, 羅生門, exists on Aozora in a strictly easier modern-orthography edition. Aozora dominates it for this purpose. |
| **Tatoeba / ManyThings JP-EN sentence pairs** | CC BY 2.0 FR and legitimately free, but the exports are 4.5-4.8 MB compressed for **isolated sentences, not texts** - poor value per megabyte against graded readers, with the folder already over budget. [tatoeba.org/downloads](https://tatoeba.org/en/downloads) |
| **Satori Reader** | Commercial subscription. Genuinely the best paid answer to the rung-3-to-4 gap, so it is worth the money rather than worth pirating. Pointer only. [satorireader.com](https://www.satorireader.com/) |
| **Commercial graded-reader series** (にほんご多読ブックス, レベル別日本語多読ライブラリー, the ASK sets) | Sold commercially. Note that a scanned set circulates on the Internet Archive under a "Tadoku" title - **that is not the free NPO material and was not used.** The name collision causes real confusion. |
| **Syosetu and Kakuyomu web novels** | Free to *read*, but individual authors retain copyright and neither site grants redistribution. Read online. |
| **Itazuraneko and Anna's Archive book collections** | Pirated. Excluded. |
| **Japan Foundation Kuala Lumpur - マレーシアの先生が作った読み物** (18 books, Levels 0-3) | A genuine Japan Foundation tadoku series - teacher- and student-written, furigana throughout, at [jfkl.org.my/language/resources-collaboration/malaysiabooks](https://www.jfkl.org.my/language/resources-collaboration/malaysiabooks/) (the old `/language/tadoku/malaysiabooks` URL 301s to the homepage - it moved). Unlike KC よむよむ (explicit CC BY-NC 2.1 JP) or Tadoku (a CC BY-NC-ND badge on every book), these carry **no book-specific licence grant** - only the site's blanket footer "Copyrights ©2022. The Japan Foundation, Kuala Lumpur. All Rights Reserved." Declined on the same no-reuse-grant grounds as Hukumusume, even though the content itself is a good fit. |
| **多読 日本語学習読本** (nihongotokuhon.jimdofree.com) | A portal of easy readers for learners and for deaf/hard-of-hearing children, Levels 0-4. Explicit footer: "Copyright (C) 2017 ... All Rights Reserved." No reuse grant. |
| **読み物いっぱい** (Yomimono Ippai, advertised as copyright-free graded readers with audio) | The host (`www17408ui.sakura.ne.jp`) appears to be defunct and is unreachable - the same category as Watanoc. |
| **Easy-Japanese-news alternatives to NHK Easy** - Yasashii Asahi Shimbun (yasashii.asahi.com), Nishinippon Shimbun me (nishinippon.co.jp/theme/easy_japanese), Kahoku Shimpo (kahoku.news/easyjapanese) | All three genuinely have furigana and a simplified register, matching the NHK Easy format - but all three are **view-only, all-rights-reserved newspaper content with no redistribution grant**, exactly the problem that already rules out NHK Easy. Rung 3 stays online-only. |
| **多読 (extensive reading) scholarship on J-STAGE**, e.g. Kumada 2016 and Mizuno 2023 in 日本語教育方法研究会誌ジャストステージ (jstage.jst.go.jp/article/jlem/...) | Freely downloadable practice reports on Japanese-as-L2 extensive reading exist, but the Japanese body text in these PDFs has no usable Unicode mapping in the embedded CID fonts - a known issue with this era of J-STAGE/NII-hosted Japanese academic typesetting (the English abstract extracts fine; the Japanese body does not) - so it cannot be extracted as real, searchable text. One candidate (日本語教育176号, 淺津 2020) also carries an explicit `copy:no` permission flag in the PDF itself, a harder stop than a copyright notice. Not included here on verification and rights grounds, not on topical relevance. |
| **Japanese Text Initiative** (University of Virginia; parallel 原文 / modern-Japanese / English text, including 源氏物語) | A genuine academic parallel-text project. Not included here because its Japanese-language texts are classical/pre-modern (古文) - the same reason Project Gutenberg's Japanese shelf is excluded above: this is a different grammar system, not simply harder modern Japanese, and does not fit the modern-orthography-only principle this folder follows throughout. |
| **レベル別日本語多読ライブラリー / ASK-style commercial sets** | Also mirrored behind a University of Iowa library guide (dsps.lib.uiowa.edu/tadoku) - the same commercially-sold series already listed above (see "Commercial graded-reader series"). Being behind a university's own licensed access does not make it free or redistributable. |
| **Vertical-text (縦書き) sample** | Aozora Bunko's own XHTML/HTML renders **horizontally** by default; genuine vertical rendering exists only via JS-based online viewers (e.g. "縦書きで読む青空文庫") or third-party conversion tools (AozoraEpub3, pyaozora) that transform existing text into a vertical-mode EPUB. Those are software tools, not standalone downloadable text resources, and producing one would mean standing up a conversion toolchain to hand-produce a single demo file - out of proportion for one sample. No ready-made, freely licensed, genuinely novel vertical-mode text file exists to add here. |
