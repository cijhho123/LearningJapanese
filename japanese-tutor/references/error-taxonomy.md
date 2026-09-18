# Error taxonomy

The `error_type` slugs used by `kb.py error --type <slug>`. Use these exact
strings so counts aggregate. If nothing fits, invent a lowercase-hyphenated slug
and reuse it consistently.

These are the recurring failure modes of English-speaking learners specifically.
Logging against a fixed vocabulary is what turns scattered mistakes into
"you have missed に/で four times this week".

---

## Particles

| slug | what it is | how to spot it |
|---|---|---|
| `particle-wa-ga-topic` | は used where neutral-description が belongs | Describing a new event/scene with は: `雨は降っている` |
| `particle-wa-ga-exhaustive` | は used where exhaustive-listing が belongs | Answering "who did it?" with `私は` instead of `私が` |
| `particle-wa-ga-relative-clause` | は inside a **noun-modifying** clause | `私は読んだ本` for "the book I read" - relative clauses take が. Only relative clauses: と, から and けど clauses allow は freely (`私は行くから`) |
| `particle-ga-stative-object` | を used where が is genuinely required | `日本語を分かる`, `ピアノをできる`. **Do not log** `水を飲みたい` - ～たい takes both, and を is standard modern usage, especially with a long or separated object. `～を好きになる` is also correct |
| `particle-ni-vs-de` | location/time particle confusion | `学校に勉強する` (action location needs で) |
| `particle-ni-vs-e` | に/へ for destination | Usually harmless; log only if they ask or it's unnatural |
| `particle-wo-vs-ga-potential` | を vs が with potential forms | `日本語を話せる` where が is preferred |
| `particle-omission` | required particle dropped | Common because English has no case particles |
| `particle-oversupply` | particle inserted where none belongs | Often after a topic they've already marked |
| `particle-to-ya-toka` | exhaustive vs representative listing | `と` used for a partial list |
| `particle-made-vs-madeni` | continuous until vs deadline by | `5時までに待つ` |
| `particle-kara-node-tame` | reason particles confused | Register and causality differ, not interchangeable |

## Verbs and conjugation

| slug | what it is | how to spot it |
|---|---|---|
| `verb-class-misidentified` | godan treated as ichidan or vice versa | The real cause behind most て-form errors. Watch 帰る 入る 走る 切る 知る 要る 減る |
| `te-form-conjugation` | wrong て-form ending | `食べって`, `行いて`. The irregulars are a closed set of five: 行く→行って, 問う→問うて, 請う→請うて (archaic ウ音便, never 問って), する→して, 来る→来て |
| `ta-form-conjugation` | same errors in the past plain form | Mirrors て-form; log separately only if て is clean |
| `negative-conjugation` | ない / なかった / くなかった errors | i-adjective negatives are where this shows up |
| `transitive-intransitive-wrong-member` | picked the wrong verb of the pair | `電気をつく` for `つける`; `授業を始まる` for `始める`. **Not** `ドアを開く` - that reads as `ひらく`, which is transitive and correct |
| `transitive-intransitive-particle` | right verb, wrong particle | `ドアが開ける` |
| `transitive-intransitive-teiru` | misread resultant state as progressive | Reading `ドアが開いている` as "is opening" not "is open" |
| `causative-passive-confusion` | させる / られる / させられる mixed up | Morphologically adjacent, different argument structure |
| `conditional-choice` | wrong member of ば / たら / と / なら | All four translate as "if"; the constraints differ |
| `potential-form` | potential formation or usage error | Including using を with it |
| `volitional-form` | よう / おう formation or usage | |
| `aspect-vs-tense` | treating ている as progressive-only, or た as strictly past | `明日晴れたら` is not past |

## Vocabulary and kanji

| slug | what it is | how to spot it |
|---|---|---|
| `kanji-visual-confusion` | mixed up two similar characters | 待/持/特, 未/末, 開/閉/関, 博/専, 陰/隠, 織/識/職, 剣/検/険/験. Also call `kb.py confuse` |
| `kanji-reading-onkun` | picked on'yomi where kun'yomi belongs, or vice versa | The compound/okurigana heuristic is ~80-90% reliable; 湯桶読み and 重箱読み break it |
| `kanji-reading-wrong-on` | right reading type, wrong reading | Very common for kanji with several on'yomi |
| `jukujikun-missed` | tried to read a 熟字訓 per-character | 今日 大人 昨日 一昨日 明日 |
| `vocab-meaning` | wrong gloss | |
| `vocab-production-failure` | recognised it but could not retrieve it | The gap recognition-only study hides. Log it every time |
| `near-synonym-confusion` | 思う/考える, 事/物/所, 必要/必ず | genuine shades of meaning |
| `spontaneous-vs-potential` | 見える/見られる, 聞こえる/聞ける | **not** near-synonyms - different argument structure. 見える/聞こえる are spontaneous (it presents itself to you); 見られる/聞ける are potential (you are able to). Explaining these as shades of meaning is what fails |
| `homophone-confusion` | こうえん, きかん, せいかく etc | |
| `counter-choice` | wrong counter for the noun | 本 is not only for long thin things |
| `counter-phonology` | right counter, wrong sound change | 一本 いっぽん, 三本 さんぼん, 六本 ろっぽん, 一匹 いっぴき |
| `numeral-system-choice` | native vs Sino-Japanese numerals | ひとつ/いち, 一日 ついたち vs いちにち, 二十歳 はたち |
| `rendaku-error` | voicing applied or omitted wrongly | Do not teach as a productive rule - use it to explain a surprise |

## Syntax and discourse

| slug | what it is | how to spot it |
|---|---|---|
| `zero-anaphora-oversupply` | 私は / あなたは on every sentence | The single most reliable tell of an English speaker |
| `zero-anaphora-comprehension` | lost track of a dropped subject/object | "I know every word but not the sentence" |
| `relative-clause-parse` | missed the clause boundary or the gap role | 私が読んだ本 vs 本を読んだ人 |
| `word-order` | verb not final, or unnatural scrambling | Only verb-final is rigid |
| `nominalization-choice` | こと / の / もの confused | |
| `giving-receiving` | あげる/くれる/もらう or the て-forms | Encodes viewpoint and social direction; no English analogue |
| `modality-confusion` | はず/べき/わけ/もの/ところ, or そう/よう/らしい/みたい | Cannot be separated by translation alone |
| `keigo-direction` | kenjougo used for the superior's actions | The canonical keigo error |
| `keigo-register-mixing` | register switches mid-utterance | |
| `keigo-double-honorific` | 二重敬語 like お召し上がりになられる | |
| `uchi-soto` | in-group/out-group reference frame wrong | Talking about your own boss to an outsider |

## Phonology

| slug | what it is | how to spot it |
|---|---|---|
| `vowel-length` | long/short vowel collapsed | おばさん/おばあさん, ここ/高校, ゆき/ゆうき |
| `gemination` | small っ dropped or added | 来た/切った. English has no morpheme-internal length contrast |
| `moraic-n` | ん not counted as a full mora | にほん is 3 morae |
| `pitch-accent` | wrong accent pattern | Only log if pitch training is active |
| `devoicing` | /i/ /u/ not devoiced where they should be | Between voiceless consonants (好き, した), and word-finally before a pause (です, ます) - two separate environments |

## Process

| slug | what it is | how to spot it |
|---|---|---|
| `false-confidence` | said "makes sense", then could not produce it | Log every time. This is the one that silently rots a curriculum |
| `guessed-from-english` | translated English structure word by word | |
| `recognition-only-gap` | solid on recognition, blank on production | Also visible in `mean_stability_days_by_direction` |

---

## Using this

1. **Classify narrowly.** `particle-ni-vs-de` beats `particle-error`. The whole
   point is knowing *which* particle pair to drill.
2. **Log the learner's actual words** in `--output`. The wrong answer text is
   what powers confusable detection later.
3. **Three hits of the same slug is a signal**, not noise. Surface it and offer a
   targeted drill rather than waiting for it to come up again by chance.
4. When a `kanji-visual-confusion` fires, also call
   `kb.py confuse kanji <a> <b> --reason visual` so the pair can be drilled
   side by side. SRS will never surface these two together on its own - it
   schedules them independently, which is exactly what hides the collision.
