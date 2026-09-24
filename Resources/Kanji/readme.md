# Kanji

![Kanji](<../../Assets/Kanji-logo.jpg>)

> **TL;DR**
>
> - Kanji are the logographic characters Japanese borrowed from Chinese. They carry the content words (nouns, verb and adjective stems); kana carry the grammar. You cannot read Japanese without them.
> - The real goal is not a kanji count. It is **kanji fluency**: the point where characters stop being visual noise and become distinguishable units, the way faces are. Everything below is in service of that.
> - Start kanji once you can read kana comfortably and have begun grammar - roughly week 2 to week 6, not month 6.
> - Recommended path: a **fast isolated pass with a component-based, mnemonic-driven system (KanjiDamage)** run *in parallel* with vocabulary and immersion. Not RTK-then-nothing, not pure vocabulary-only.
> - Budget ~3 to 8 months for the isolated pass at 10-20 new characters a day, then delete the deck and let reading carry you. The first ~1,000 characters buy you most of the text you will ever meet.

---

## What this is and why it matters

Japanese is written with three scripts at once, interleaved in the same sentence:

- **Hiragana** - the grammatical glue: particles, verb and adjective endings (okurigana), words with no common kanji.
- **Katakana** - loanwords, onomatopoeia, emphasis, some names.
- **Kanji** - the content: nouns, the stems of verbs and adjectives, most proper nouns.

Look at a real sentence and the division of labour is obvious:

```
私 は 新しい 本 を 買った
わたし は あたらしい ほん を かった
```

Every character carrying *meaning* is a kanji (私, 新, 本, 買). Everything gluing them together is kana. That is the whole system in one line.

Kanji are usually called "logographic" or "ideographic", but the more accurate word is **morphographic**: a kanji writes a *morpheme* - a minimal unit of meaning - not a whole word and not a sound. 本 is the morpheme "book / origin / this very". It is pronounced ほん in 本 and 本当, もと in 本 as "origin", and it takes part in dozens of words. The character is a stable meaning-unit with unstable pronunciation. This is the single most important structural fact about kanji, and it is why "how do you pronounce this kanji" is often the wrong question.

**How many do you need?** The **joyo kanji** (常用漢字, "regular-use kanji") list is **2,136 characters** as of the 2010 revision. That is the set a Japanese newspaper assumes an educated adult knows. Underneath it sits the **kyouiku kanji** (教育漢字), the subset taught in elementary school grades 1-6 - a bit over a thousand characters. Alongside it sits the **jinmeiyou kanji** (人名用漢字), a separate list of several hundred additional characters permitted in personal names.

But raw kanji count is the wrong metric, and chasing it is the most common beginner failure mode:

1. **You read words, not characters.** Knowing 気 and 持 does not mean you know 気持ち. Knowing 大 and 人 does not get you 大人 (おとな). Character knowledge is scaffolding for word knowledge, and word knowledge is what reading actually consumes. Word learning belongs to [Vocabulary](../Vocabulary/readme.md).
2. **Frequency is brutally skewed.** A small set of characters dominates ordinary text. The first several hundred characters you learn cover the overwhelming majority of the kanji tokens you will meet, and the returns fall off hard after the first thousand or so. Learning character #1,900 is worth a tiny fraction of learning character #200.
3. **The tail never ends anyway.** Names, place names, older literature, manga that likes archaic flavour (Berserk-style fantasy vocabulary is a great offender) and food menus will all throw non-joyo characters at you forever. You will never "finish" kanji, so stop framing it as a finish line.

Frame it as: **the first ~1,000 characters buy you most of the text you will meet; the next ~1,100 buy you comfort and speed; everything after that you pick up by reading.**

### Kanji fluency - the actual goal

This is the part worth internalising before you choose a method. It reframes the whole problem.

Jumping right into learning words at the beginning is not easy. Similar characters often look the same and remembering words takes many repetitions. You have to somehow force the words into your brain and there are no mental anchors to help you. However, if you do this enough, eventually you arrive at the point where kanji stop being foreign anymore. Once you reach this point, your brain starts to recognise each kanji as a whole without paying attention to its component parts. You start distinguishing them easily from each other, and learning new kanji becomes effortless. This point is called **kanji fluency**.

When you reach kanji fluency, recognising a kanji becomes just like recognising someone's face. It takes an instant to remember the face of a person. Later, if you just look at the person again, you immediately know if you have met them before - even if you might forget their name or why you know them.

With kanji, you are not analysing the component parts but taking the whole character as one unit. When you see a new kanji, it will look like *something* to you. When you encounter that character again, you will instantly recognise it as the same exact character.

If you wanted to test whether you have kanji fluency, you could run this experiment:

1. Randomly select one kanji you have never seen before in your life, and look at it. Example: 賃
2. Wait a couple of days.
3. Take a number of randomly selected kanji that you have also never seen before. The kanji you saw in step 1 can be among them. Example: 責 魔 歓 賃 脅 - and ask yourself, "which of these is the one I saw a couple of days ago?"
4. Guess whether the kanji you saw in step 1 is among the others.

If you could easily pass that test, you have kanji fluency. It means that just by looking at a kanji you can remember it. Maybe you do not remember its exact strokes, maybe you do not remember its readings, maybe you do not remember its meanings - but you can still tell characters apart and recall which kanji you saw the other day. You do not have to actually run this test. It is an imaginary algorithm that demonstrates what kanji fluency *is*.

Once you have it, kanji stops being a subject you study and becomes a channel you read through. Every method argument below is really an argument about the fastest, cheapest route to this one state.

Framed this way, "learn 2,136 kanji" - an open-ended grind with no natural stopping point - becomes "reach the point where characters look distinct from each other," a bounded problem with a clear exit condition. That reframing also says exactly what to *stop* doing: there is no need to be able to write 2,136 characters from an English keyword, and no need for every reading of every character. What is needed is discrimination plus enough anchoring that words stick.

---

## Where it fits in the journey

**Prerequisites:**

- **Hiragana and katakana, comfortably.** Not perfectly, but you should not be decoding letter by letter. See [Kana](../Kana/readme.md). Kanji readings are written in kana everywhere, so kana is load-bearing.
- **Grammar started.** You do not need much - particles, basic verb forms, the shape of a sentence. See [Grammar](../Grammar/readme.md). Without it you cannot tell where a word ends and okurigana begins, which makes the kun/on heuristic useless.
- **Anki set up with sane settings.** Deck configuration, FSRS, add-ons and dictionary tooling are covered in [General content](<../General content/readme.md>). Get this right *before* you start, because a badly configured kanji deck is the number one cause of abandonment.
- **Not required:** romanisation. Drop romaji before you touch kanji. See [Romaji](../Romaji/readme.md).

**What kanji unlocks:**

- **Reading anything at all.** Graded readers, manga, visual novels, news. See [Reading](../Reading/readme.md).
- **Fast vocabulary acquisition.** Once characters are distinct, new words have hooks. 経済 is not a random blob, it is a familiar 経 plus a familiar 済. This is the compounding return.
- **Dictionary lookups that actually work.** Hovering an unknown word with a popup dictionary only helps if you can tell which word you looked up from the one you looked up yesterday.
- **Mining native material.** The whole sentence-mining loop in [AJATT](../AJATT/readme.md) presupposes you can visually parse a line of Japanese.

**What kanji does NOT unlock:** listening, speaking, or pitch accent. Kanji is a *writing system*. A person who has finished RTK and done no listening understands nothing spoken. Keep [Listening](../Listening/readme.md) and [Speaking](../Speaking/readme.md) running in parallel from day one.

**When to start:** as soon as kana is comfortable and grammar has begun. Typically week 2 to week 6. Delaying kanji "until my grammar is solid" is a trap - grammar study without kanji means studying romaji or furigana-crutched text, and you will pay the transition cost later anyway.

---

## The schools of thought

This is the heart of the guide. These five approaches genuinely disagree, and the disagreement is not about taste - it is about what you optimise and what you are willing to lose.

### 1. RTK - Remembering the Kanji (James Heisig)

Meaning-and-writing first, readings deliberately deferred. Each character gets **one unique English keyword**, decomposes into "primitives" (Heisig's own component set, grounded in but not identical to the traditional radicals), and you **build your own mnemonic story** from the primitives to the keyword. Characters are ordered strictly by component dependency: you never meet a character before its parts. Volume 1 of the local fifth edition covers **2,042 characters**; volume 2 teaches readings; volume 3 extends toward a 3,000-character total using frequency data, the JIS character sets and the name-use list.

Heisig is explicit about the trade in his own introduction: *"You will read nothing about how kanji combine to form compounds. Nor is anything said about the various ways to pronounce the characters."* He recommends 20-25 characters per day for someone with a couple of hours, and claims 4-6 weeks full time.

**Pros**
- The most systematic component ordering that exists. Nothing arrives unprepared.
- It builds the "see components, not blobs" skill faster than anything else. That skill is the real deliverable.
- Genuine writing production: you can produce characters from a keyword, which no recognition-only method gives you.
- Huge ecosystem: pre-made Anki decks, shared community mnemonics, the RRTK cut-down variant.

**Cons**
- **Keywords are not meanings.** Heisig says so himself - they are selected to be unique and memorable, not accurate. Learners routinely fossilise the keyword as the character's definition and then mis-parse real words for years.
- **Zero readings and zero words for months.** You finish with 2,000 English keywords and cannot read a sentence. The "I finished RTK and still can't read anything" complaint is real, common, and correct.
- **High dropout.** The wall lands around 600-800 characters, when story invention gets tiring and you still have nothing to show for it. Many people quit there.
- **Poor long-term retention if you stop.** Several months after finishing an isolated deck, retention commonly collapses toward roughly half. Without reading to reinforce it, the whole thing leaks.
- Writing production is expensive and, if your goal is reading, mostly wasted effort. See [Writing](../Writing/readme.md).

**Best for:** people who want handwriting from the start; people who like heavy systems and will actually finish; people studying full time who can compress the pass into 6-8 weeks so the leak has no time to happen.

### 2. KanjiDamage

Component-first, like RTK, but with four differences that matter. It ranks characters **by usefulness and cuts the useless ones** (it merges the JLPT and joyo sets and then throws out characters whose meanings "sound like a crossword puzzle clue"), landing at roughly **1,700 kanji**. It gives you a **pre-written mnemonic for every single character** rather than making you invent one. It **teaches the on-yomi from the start**, treating each on-yomi as "just another radical - a sonic one" with its own fixed English keyword (しょう becomes SHOW, か becomes CAR). And it gives you **jukugo, look-alike discrimination hints and warning tags** alongside each character.

The ordering logic is the author's own, and it is good engineering: start with a set of simple characters, combine them every way that produces a real kanji, and only then introduce one new component - *"once you've learned around 200 kanji, you can learn 12 NEW kanji just by learning ONE SINGLE 3-stroke radical and combining it with the first 200."*

It is also the only one of these systems that is straight with you about the tooling problem. From its own [introduction](<./Kanji Damage/markdown/introduction.md>): *"even with my awesome system of jaw-dropping logic, kanji is still a motherfucker. You'll study 12 months and still not be able to read a newspaper."*

**Pros**
- **Free**, complete, and fully mirrored in this repo (including a 2,403-file markdown archive you can grep).
- **Readings and real words from character one.** This is the decisive advantage over RTK: the mnemonic bundles components + meaning + on-yomi in one sentence, so you are not building something you have to un-learn.
- **Ordering by usefulness**, with explicit permission to skip obscure characters. It respects your time.
- **Over 800 look-alike hints.** Look-alike discrimination is the actual hard part of early kanji and almost nobody else addresses it directly.
- Memorable to the point of being intrusive, which is exactly what a mnemonic is for.
- The warning-tag system (STRONG, SYMBOLIC, JERK RADICAL, 1/2 KANA, NOKURI, NP, DUH...) names problems that other resources leave you to discover alone. Naming a problem is half of solving it.

**Cons**
- **The humour is genuinely off-putting.** It is crude, dated, occasionally racist and sexist, and leans on "yo mama" jokes and slurs. Judge it yourself before committing - read the [introduction](<./Kanji Damage/markdown/introduction.md>) and a few [kanji pages](<./Kanji Damage/markdown/kanji/>) first. If it annoys you, the mnemonics will not stick, and then the whole method is worthless to you.
- **The site is dated** and the writing is undisciplined. Signal-to-noise is mediocre; you skim a lot of rant to get the fact.
- **Someone else's mnemonics are harder to recall than your own.** This is a real cost versus RTK's build-it-yourself approach. Pre-written stories feel efficient and often are not.
- **Component keywords are idiosyncratic.** "Nest", "crows", "TNT plunger", "Abe Lincoln's hat" - none of these correspond to anything a Japanese person or a dictionary would recognise. They are private scaffolding you will eventually discard.
- The ordering is *not* frequency-ordered, so you meet some uncommon characters early and some very common ones late. The deck author flags this explicitly.
- Some readings are simplified away ("A lot of textbooks list 2 ONyomi or even 3 ONyomi per kanji... So, fuck it!! Erase that shit!"). Efficient, but occasionally wrong in a way you have to repair later.

**Best for:** self-studying adults with an hour a day who want readings and words included, who are not squeamish, and who value practical ordering over academic completeness.

### 3. WaniKani

A managed, hosted SRS. Fixed pipeline: radicals, then kanji built from them, then vocabulary using those kanji. Mnemonics are provided for both meaning *and* reading, and they are well written. Levels gate: you cannot advance until you have passed the current level to a threshold. ~60 levels covering the joyo set plus about 6,000 vocabulary words.

**Pros**
- **Zero setup.** No Anki configuration, no deck hunting, no add-ons. For a lot of people this alone is decisive.
- **Excellent mnemonic quality** - consistently better written and more consistent than KanjiDamage, and better integrated than DIY RTK.
- **Forced pacing prevents both burnout and cramming.** The gating is the product. You cannot pile up 400 new cards and then quit.
- **Real vocabulary integrated** from level one, and reading is drilled, not deferred.
- Good, active community with shared mnemonics and user scripts.

**Cons**
- **Subscription.** Free for the first three levels, then paid monthly or lifetime.
- **You cannot accelerate.** The gating that saves the average learner actively obstructs the fast one. If you can absorb 25 characters a day, WaniKani will not let you.
- **Fixed order that ignores what you are reading.** If you are working through Chainsaw Man, WaniKani has no idea and will not prioritise its characters.
- **~2 years at the intended pace.** For anyone on a timeline, that is a long time to spend not reaching kanji fluency.
- Closed platform: your review history is not yours in any portable sense, and it does not compose with the rest of an Anki-based workflow.

**Best for:** people who will not maintain their own tooling, people who need external structure to stay consistent, people not in a hurry.

### 4. No isolated kanji study - kanji through vocabulary only

The immersion-community position: never study a character alone. Learn *words*, with their readings and meanings, and let character knowledge accrete as a side effect. In its softest form (Tatsumoto's **JP1K**) you learn ~1,000 common words from cards where the furigana is hidden but revealable on hover - "training wheels" that let you peek at a reading rather than fail the card - and after 1,000 words you remove the wheels and mine normally.

**Pros**
- **Everything you learn is immediately useful.** No English keywords, no private component vocabulary, nothing to discard later.
- **No keyword/meaning confusion**, ever. You learn that 大人 is おとな meaning "adult", not that 大 is "big" and 人 is "person".
- **Matches how natives and all advanced learners actually operate.** Past the beginner stage, everybody learns this way. The only question is whether the beginner stage needs a different tool.
- Readings are learned where they belong: inside words, with their actual voicing and gemination.
- No retention cliff, because the knowledge is the knowledge you use.

**Cons**
- **The first few weeks are a wall.** Every word is an undifferentiated cluster of unfamiliar shapes with no anchors. 議 and 護 and 穫 are the same smudge. This is the exact problem kanji fluency solves, and vocabulary-only gives you no tool for it other than raw repetition.
- **Slower to reach reliable character discrimination.** You will get there, but through brute force rather than through component awareness.
- **Look-alikes stay confusable longer**, because you never explicitly compared them.
- Requires more discipline: without a finite deck to finish, there is no visible milestone.

**Best for:** people who have already tried an isolated deck and bounced off it; people with unusually high tolerance for early ambiguity; anyone restarting Japanese after a failed RTK attempt.

### 5. Textbook / school order (kyouiku kanji by grade)

What Japanese children do: characters ordered by school grade, grades 1-6, then junior high. Genki, Minna no Nihongo and most classroom courses approximate this.

**Pros**
- Official and standardised; aligns with school materials and with some [JLPT](../JLPT/readme.md) prep books.
- Graded and gentle; each stage is small.
- If you are in a class, this is the order you are getting whether you like it or not.

**Cons**
- **It is ordered for six-year-old native speakers who already speak fluent Japanese.** They need the characters for words they already know and say. You do not have that base, so the ordering optimises for the wrong constraint entirely.
- **Badly mis-ordered by complexity.** KanjiDamage's central complaint is exactly this: students bust their heads on common-but-complex characters like 館 and 裂, and only a year later learn 官 and 列 - *which are the components of 館 and 裂*. Learning the parts second is pure waste.
- **Frequency and complexity barely correlate.** 顔 (face) and 鼻 (nose) are kid-words and visually horrible; 丹 (cinnabar) and 后 (dowager empress) are simple and useless. Grade order mixes these freely.

**Best for:** people in a formal class, people teaching children, people whose goal is specifically to follow Japanese school curriculum.

### Also worth knowing

- **KanjiDamage Plus** - a modernised, extended community version of KanjiDamage with roughly **200 additional kanji** and some component names renamed. One flashcard per kanji, pre-made mnemonic stories, and each story includes the character's most common reading. There is a single-page online reference and, locally, both an Anki deck and a saved HTML export (over 2,100 cards including component entries). See [its readme](<./KanjiDamage Plus/readme.md>) and [the local export](<./KanjiDamage Plus/KanjiDamage Plus+.html>). If you like KanjiDamage's method but want a cleaner, more complete list, this is the better starting point.
- **Kodansha Kanji Learner's Course (KKLC)** by Andrew Scott Conning - a graded, component-ordered course covering the joyo set with a single English keyword per character *plus* readings and example vocabulary. It is the sober, well-edited alternative to both RTK's reading-free austerity and KanjiDamage's chaos. Not mirrored in this repo; if you want a paper book and RTK's discipline without RTK's blind spot, this is the one to look at.
- **Frequency-ordered KanjiDamage** - the author of the official Anki deck also published a frequency-ordered variant of the same content ([AnkiWeb](https://ankiweb.net/shared/info/1917095458)). If the "uncommon characters early" complaint bothers you, that is the fix.
- **RRTK (Recognition RTK)** - an RTK-derived Anki deck cut down to roughly the 1,000 most common characters, recognition-only (kanji on the front, meaning on the back), no writing. It exists precisely because the goal is kanji fluency, not 2,042 keywords. If you want the shortest possible isolated pass, this is it.
- **Kanji Koohii** (<https://kanji.koohii.com/>) - a free SRS specifically for RTK with a large database of community-shared mnemonic stories. Even if you are not doing RTK, its story database is a useful mnemonic quarry.

### The real debate: should you study kanji in isolation at all?

This is the only question that actually matters, and it is worth resolving honestly rather than tribally.

**The case against isolated study** is strong. Isolated decks teach you English keywords that have a loose and sometimes false relationship to Japanese. The component names are private inventions that no Japanese person uses. Retention collapses once you stop reviewing, because nothing in your real reading reinforces "the crows get warm in the sun". And you can point at plenty of people who reached fluency without ever touching RTK.

**The case for isolated study** is also strong, and it is a different claim than the one its critics attack. The claim is not "keywords are useful knowledge". The claim is "**a fast pass through component-decomposed characters is the cheapest way to buy visual discrimination**". Two weeks in, a vocabulary-only learner sees 復 and 複 as the same thing. A learner 300 characters into KanjiDamage sees 彳+复 and 衤+复 and can tell them apart instantly even if both English keywords are garbage. The keywords are disposable; the decomposition habit is not.

**The synthesis, and the position this guide takes:**

> A **fast** isolated pass (measured in weeks, not years) whose purpose is component-awareness and character-discrimination, run **in parallel** with vocabulary learning and immersion from day one, beats either pure extreme.

- "Fast" matters because the retention cliff is real. If your pass takes 18 months, the characters you learned in month 2 are gone by the time you finish. Speed is not impatience here, it is the mechanism.
- "In parallel" matters because immersion is what converts scaffolding into knowledge. Isolated study with zero reading is the single most wasteful thing you can do with kanji time.
- "Component-awareness, not meaning" matters because it tells you what to grade yourself on. If you recall a character's shape and can tell it from its look-alikes, that card is a pass even if you fumbled the keyword.
- And critically: **the isolated deck is disposable**. When you notice its retention sliding and you can read, delete it. It was a ladder, not a house.

---

## Recommended path (opinionated)

**Do the KanjiDamage (or KanjiDamage Plus) Anki deck at 10-20 new cards a day, in parallel with a frequency vocabulary deck and daily immersion. Grade yourself on recognition and discrimination, not on production. Finish in 3-6 months. Then delete it and read.**

The reasoning, in order of weight:

1. **It includes readings and jukugo.** This is the thing that kills RTK for reading-focused learners. KanjiDamage's mnemonic bundles components, meaning and on-yomi in one sentence, so the very first day of study produces something that helps you read. The on-yomi-as-a-sonic-radical idea is genuinely clever: there may be a hundred characters sharing コウ the same way there are a hundred sharing 木, so treat the sound as a component with a keyword.
2. **It is ordered by usefulness and it cuts dead weight.** ~1,700 instead of 2,042, with the crossword-puzzle characters removed. That is 300+ characters of your life back.
3. **It addresses look-alikes explicitly.** 800+ discrimination hints. Look-alike confusion is the actual bottleneck in months 1-4 and almost nothing else takes it seriously.
4. **It is free and completely mirrored offline here.** No subscription, no dependency, works on a plane.
5. **It composes with everything else.** An Anki deck sits next to your vocabulary deck and your mined sentences with one shared review queue and one shared scheduler. WaniKani does not.

**Ignore this recommendation if:**

- **The humour is a dealbreaker.** This is not a small caveat. If you find it repellent, the mnemonics will not stick and the method is actively worse than the alternatives. Use **WaniKani** instead - it gives you the same readings-included, component-first structure with professional writing and no setup cost. Pay the subscription; it is cheaper than a failed method.
- **You want handwriting from day one.** Then do **RTK volume 1** with pad and pencil as Heisig intends, and accept that you will not be reading for a few months. Also read [Writing](../Writing/readme.md) first and be honest about whether handwriting is actually one of your goals.
- **You have already bounced off an isolated deck once.** Do not try again with a different one. Go **vocabulary-only / JP1K**: learn 1,000 words from hover-furigana cards and let the characters accrete. A method you will actually execute beats a better method you will abandon.
- **You are in a class or prepping a specific JLPT level on a deadline.** Follow your course's order for the exam and run a general deck underneath it. See [JLPT](../JLPT/readme.md).
- **You have unlimited time and no deadline.** WaniKani's gating is genuinely pleasant if you are not in a hurry.

---

## Phase-by-phase plan

### Phase 0 - Prerequisites and tooling

- **Goal:** be ready to start, with no setup friction left to blame.
- **Time:** 1-2 weeks, overlapping with kana study.
- **Daily routine:** kana drills; install and configure Anki; install a popup dictionary; read this guide's method section and pick one.
- **Materials:** [Kana](../Kana/readme.md), [General content](<../General content/readme.md>) for Anki/FSRS/Yomitan/dictionaries/fonts, the [KanjiDamage introduction](<./Kanji Damage/markdown/introduction.md>) and [kanji facts](<./Kanji Damage/markdown/kanji_facts.md>) pages, [Introduction to Kanji.pdf](<./General Introduction/Introduction to Kanji.pdf>) for the linguistic background.
- **Done when:** you can read a hiragana sentence aloud without decoding letter by letter; Anki is installed with FSRS on and a review cap you have chosen deliberately; you can hover a Japanese word in your browser and get a definition; and you have read enough of your chosen method to explain in one sentence why you picked it over the other four.

### Phase 1 - Component literacy

- **Goal:** stop seeing blobs. Learn to look at an unknown character and automatically decompose it.
- **Time:** 2-3 weeks (roughly the first 150-250 characters of your deck).
- **Daily routine:** 10-20 new kanji cards; all due reviews; 15 minutes reading anything with furigana. When a new character appears, say its component keywords out loud before reading the mnemonic.
- **Materials:** your chosen deck ([Official KanjiDamage deck](<./Kanji Damage/Official_KanjiDamage_Anki_deck.apkg>) or [KanjiDamage Plus](<./KanjiDamage Plus/KanjiDamage Plus+.apkg>) or [RTK 6th edition deck](<./Remembering the Kanji/Heisigs RTK 6th Edition [Stories, Stroke Diagrams, Readings].apkg>)); the [radicals list](<./Kanji Damage/markdown/radicals.md>); the [component table below](#reference-how-kanji-are-built).
- **Done when:** given an unfamiliar 12-stroke character you have never studied, you can break it into 2-4 named parts within a few seconds, and at least three of the parts are ones you can name. You do not need to know what the character means.

### Phase 2 - The isolated pass

- **Goal:** get through your chosen character set and reach kanji fluency.
- **Time:** 3-6 months at 10-20 new/day. (At 5/day, budget closer to a year and accept the retention cost.)
- **Daily routine:** 10-20 new kanji cards; all reviews (expect 20-40 minutes once the deck matures); 5 new vocabulary cards in parallel from a frequency deck; 30+ minutes of immersion, ideally something you can also read. Once a week, spend 10 minutes on the look-alike pairs you have been failing.
- **Materials:** your deck; [illpairs appendix](<./Kanji Damage/markdown/appendix/illpairs.md>) for look-alikes; [onyomi keywords](<./Kanji Damage/markdown/appendix/onyomikeywords.md>); [long/short vowel appendix](<./Kanji Damage/markdown/appendix/longshortvowels.md>); [Vocabulary](../Vocabulary/readme.md) for the parallel word deck; [AJATT](../AJATT/readme.md) for the immersion schedule.
- **Done when:** you pass the kanji fluency test in [Measuring progress](#measuring-progress) - shown 5 unfamiliar characters, you can reliably pick out the one you saw days earlier. Concretely: you can open a random manga page and point at every character you do not know, as *individual characters*, instead of seeing a wall of noise.

### Phase 3 - Readings inside words

- **Goal:** convert character recognition into actual reading ability. Stop learning readings as lists; learn them as words.
- **Time:** continuous from roughly the midpoint of Phase 2 onward; the dedicated push is 2-3 months.
- **Daily routine:** reduce or stop new kanji cards; 10-20 new vocabulary or mined sentence cards per day; 45+ minutes reading with a popup dictionary. Every time you meet a new word, check whether its on-yomi matches a phonetic family you already know - and note when it does, because that is the accelerator compounding.
- **Materials:** [Vocabulary](../Vocabulary/readme.md) for deck choice and card formats; [AJATT](../AJATT/readme.md) for sentence mining; [Reading](../Reading/readme.md) for graded material; the [readings reference](#reference-readings) and [phonetic series](#reference-phonetic-series---the-single-biggest-accelerator) sections below.
- **Done when:** given a two-kanji compound you have never seen, built from characters you know, you can guess its on-yomi reading correctly more often than not, and guess its meaning correctly more often than not. This is the point where kanji starts paying you back.

### Phase 4 - Delete the scaffolding

- **Goal:** get off the isolated deck before it becomes a treadmill.
- **Time:** whenever Phase 2 is complete and retention starts sliding - typically a few months after finishing the deck.
- **Daily routine:** vocabulary and mined sentences only; heavy reading; no isolated kanji cards. Keep reviewing the old kanji deck for a few months after finishing it, *but stop when its retention drops* - at that point the cards are costing you more than they return, and your reading has taken over the job.
- **Materials:** [Reading](../Reading/readme.md), [AJATT](../AJATT/readme.md), [Vocabulary](../Vocabulary/readme.md).
- **Done when:** you have deleted or suspended the isolated kanji deck and your character knowledge is *still improving*, because reading is now doing the work. New characters get learned as part of new words, the way they will be for the rest of your life.

---

## Daily and weekly routine

A concrete 60-90 minute weekday schedule for Phase 2, sized for someone working full time. Copy it and adjust the numbers, not the structure.

| Slot | Time | What | Why this slot |
| :--- | :--- | :--- | :--- |
| Morning, before work | 15 min | Kanji deck: all due reviews, no new cards yet | Reviews are the load-bearing part. Do them when your discipline is highest. |
| Commute / walk | 20-30 min | Passive immersion: anime, podcast, music. No study. | Zero-friction, zero-willpower volume. Keeps the language in your ear. |
| Lunch break | 10 min | Kanji deck: today's new cards (10-20) | New cards need attention, not much time. Splitting them from reviews stops the session feeling endless. |
| Evening block | 20 min | Vocabulary deck reviews + 5 new words | Runs in parallel from day one. This is where readings actually get learned. |
| Evening block | 20-30 min | Active reading: manga with a popup dictionary, or graded reader | Non-negotiable. This is what converts the deck into knowledge. |
| Before sleep | 5 min | Clear any stragglers; look up one character that annoyed you today | Cheap, and the annoyance is a free mnemonic hook. |

Weekly:

| Day | Extra | Purpose |
| :--- | :--- | :--- |
| Mid-week (e.g. Wednesday) | 10 min: review the look-alike pairs you failed this week, side by side | Look-alike confusion does not fix itself through normal SRS. It needs explicit comparison. |
| Weekend, day 1 | 45-60 min: extended reading session on real material you care about | Longer sessions build reading stamina, which short daily blocks do not. |
| Weekend, day 2 | 20 min: audit the deck. Suspend leeches. Check retention and new-card rate against your target finish date. | Engineering discipline applied to your own pipeline. Do the arithmetic: characters remaining / new per day = days left. |
| Monthly | 15 min: run the fluency self-test and the manga-page test in [Measuring progress](#measuring-progress) | Vibes lie. Tests do not. |

Two rules that matter more than the schedule:

1. **Reviews before new cards, always.** If you cannot finish reviews, you cannot afford new cards. Lower the new-card rate; do not skip reviews.
2. **Never study kanji on a day you do zero immersion.** If you only have 20 minutes, spend it reading, not on the deck. The deck without reading is the failure mode.

---

## Common pitfalls

**1. Chasing the kanji count as a score.**
*The mistake:* treating "I know 1,200 kanji" as the measure of progress, and optimising your study to make that number go up.
*Why it feels right:* it is the only number available, it goes up monotonically, and it feels like progress. Engineers are especially vulnerable - it looks like a metric.
*The fix:* replace the metric. Measure "can I read this page and identify exactly which words I do not know" instead. Count *words* if you must count something, since words are what text is made of. A person with 800 characters and 3,000 words reads far better than one with 2,000 characters and 400 words.

**2. Learning keywords and believing they are meanings.**
*The mistake:* concluding that 生 means "life", 手 means "hand", full stop - and then being baffled by 生ビール, 苦手, 生憎.
*Why it feels right:* the deck asked you for one keyword and rewarded you for producing it. The reward signal trained you to treat the keyword as the truth. Heisig says outright that keywords are chosen for uniqueness, and KanjiDamage says outright that component keywords are arbitrary nicknames - but the card does not remind you of that at review time.
*The fix:* hold keywords as *labels*, not definitions. When you meet a real word, learn the word's meaning from the word, never by adding up its characters. Treat every keyword as provisional and expect to overwrite it.

**3. Trying to memorise every reading of every character up front.**
*The mistake:* front-of-card 生, back-of-card せい・しょう・い・う・お・は・き・なま and eight more. Failing it forever.
*Why it feels right:* the dictionary lists them, so they look like the thing to learn. Completeness feels like rigour.
*The fix:* **learn readings inside words.** Learn 人生 and 生活 and you have せい twice, in context, with a meaning attached. Learn 生まれる and you have う. Nobody, including natives, holds a per-character reading list in their head; they hold words. A character's reading inventory is an *emergent* property of the words you know. At most, learn the one dominant on-yomi per character, which is exactly what KanjiDamage and WaniKani do.

**4. Neglecting look-alike discrimination.**
*The mistake:* passing 給 and 絵 on separate days, never noticing you cannot tell them apart when they appear together.
*Why it feels right:* SRS shows cards in isolation, so you are never actually tested on discrimination. You pass both cards and conclude you know both.
*The fix:* explicitly drill pairs side by side. Every week, take the characters you have been failing and find their look-alikes in the [illpairs appendix](<./Kanji Damage/markdown/appendix/illpairs.md>) or the [look-alike table below](#reference-look-alike-confusion-sets). Ask "which single component is the difference?" and memorise *that*, not the whole character again. 待 / 持 / 特 share 寺; the answer is entirely in the left side.

**5. Writing-production obsession when your goal is reading.**
*The mistake:* spending half your kanji time producing characters by hand from an English keyword.
*Why it feels right:* writing feels rigorous and deep, and school taught you that writing is how you learn. Also, writing a character *does* strengthen memory of its shape - that part is true.
*The fix:* be explicit about your goal. If it is reading and typing, handwriting is optional, because Japanese typing is phonetic - reading ability yields typing ability for free. Recognition-first, then handwriting later if you want it, is strictly cheaper than both at once. Stroke order mechanics and handwriting as a discipline belong to [Writing](../Writing/readme.md). What *is* worth borrowing from writing practice: occasionally sketching a character you keep confusing, as a diagnostic for which component you are actually failing to see.

**6. Letting reviews pile up.**
*The mistake:* 40 new cards on a good day, then a bad week, then 600 due cards and a decision to "start fresh later".
*Why it feels right:* adding new cards is the fun part and feels like progress. Reviews feel like maintenance. SRS debt is invisible until it is fatal.
*The fix:* new-card rate is a *commitment to future review load*, roughly ten times over. Pick a rate you can sustain on your worst day, not your best. Cap reviews. When you fall behind, reduce new cards to zero until the backlog clears - never delete the deck. Deck settings and leech handling are covered in [General content](<../General content/readme.md>).

**7. Abandoning at the 700-character wall.**
*The mistake:* quitting somewhere between 600 and 900 characters, usually while doing RTK, usually with the thought "this is not helping me read anything".
*Why it feels right:* because at that point **it genuinely is not helping you read anything**, if you have been doing isolated study with no immersion. The complaint is accurate; the conclusion is wrong.
*The fix:* two things. First, run immersion in parallel from day one so you get visible wins alongside the grind - recognising 魔 in a manga panel is worth fifty flashcards of motivation. Second, pick a method that pays out earlier: a system that teaches readings and jukugo from character one gives you something usable in week two, which is exactly why reading-free RTK is not recommended for someone working alone.

**8. Studying kanji with zero immersion.**
*The mistake:* the deck is the whole practice. No reading, no listening, no native material.
*Why it feels right:* the deck gives clean, measurable, gradable feedback. Native material gives confusion and no score. Of course you prefer the deck.
*The fix:* accept that the deck is scaffolding and immersion is the building. Nothing you learn in isolation gets consolidated until you meet it in the wild. If you have to choose, choose immersion - a learner who reads daily and does no deck will beat a learner who decks daily and reads nothing, every time. See [AJATT](../AJATT/readme.md).

---

## Measuring progress

Self-tests, not feelings. Run these monthly and write down the results.

**1. The kanji fluency test** (from the [section above](#kanji-fluency---the-actual-goal)). Pick one character you have never seen. Look at it once. Wait two or three days. Then look at five unfamiliar characters, one of which may be it, and identify which. Pass = you can do this reliably. This tests raw visual discrimination, independent of meaning or reading, which is exactly what you want to isolate.

**2. The manga page test.** Open a page of native manga you have not read. Can you point at every character you do not know, *as individual characters*? Early on you will see an undifferentiated wall and be unable to answer. Later you will be able to say "I don't know these four" with confidence. The transition from "wall of noise" to "inventory of specific gaps" is the single clearest progress signal in kanji study, and it usually arrives before you expect it.

**3. The decomposition test.** Take an unfamiliar character from a dictionary. Within five seconds, name its parts. Score: how many of the parts can you name? Track this over months. It should go from 0-1 to 3-4.

**4. The compound-guessing test.** Find ten two-kanji compounds you have never seen, built from characters you know. For each, write down your guess at the on-yomi reading and the meaning before looking. Score both. Target: 60%+ on readings and 60%+ on meanings by the end of Phase 3. This directly measures whether your phonetic-series knowledge and your component knowledge are actually generalising, which is the entire point of studying characters at all.

**5. The look-alike gauntlet.** From the [look-alike table below](#reference-look-alike-confusion-sets) or the [illpairs appendix](<./Kanji Damage/markdown/appendix/illpairs.md>), take 20 pairs. Cover the labels. For each pair, state which is which and name the distinguishing component. Score out of 20. This catches the failure that SRS structurally hides.

**6. Lookup rate while reading.** Read a fixed amount of native material - say one manga chapter - and count how many times you needed the dictionary. Log it. The absolute number matters less than the trend across months. This is the only test on the list that measures the thing you actually want, so weight it heavily.

**Deliberately not on this list:** "how many kanji do you know", "what JLPT level are you", and "how does it feel". The first is the wrong metric, the second belongs to [JLPT](../JLPT/readme.md) and measures test-taking, and the third is systematically miscalibrated in both directions.

---

## Reference: the groundwork - the facts a beginner needs first

This is the orientation brief, and it is deliberately the first of the reference chapters: everything after it goes deeper, and very little after it makes sense without it. It exists because the largest avoidable cost in early kanji study is not effort, it is **operating on a wrong model of what the writing system is** and then spending months asking questions the system does not answer.

Its shape is borrowed from the two pages that still do this job best for free - KanjiDamage's [introduction](<./Kanji Damage/markdown/introduction.md>) and its [kanji facts](<./Kanji Damage/markdown/kanji_facts.md>) chapter. The difference is that where those pages assert, this section checks: **every count below was computed from the datasets in this folder or read out of the government document in `../Writing/`, and the numbers are reported as found rather than as remembered.** Provenance and attribution for the datasets are in [`sources.md`](./sources.md).

Boundaries, so nothing is said twice: [how kanji are built](#reference-how-kanji-are-built) owns the radical/component distinction and the component tables; [readings](#reference-readings) owns the on/kun mechanics, the borrowing layers and the full exception lists; [phonetic series](#reference-phonetic-series---the-single-biggest-accelerator) owns predicting a reading from a shape; [Writing](../Writing/readme.md#reference-stroke-order) owns the stroke-order rules and [which script to use](../Writing/readme.md#reference-choosing-kanji-hiragana-or-katakana); [Vocabulary](../Vocabulary/readme.md#how-new-words-are-built) owns how compound *meanings* are assembled. This section gives the compact version of each, plus the figures none of them state.

### Basic terms

The vocabulary you will meet in dictionary tags, in Japanese-language resources, in this folder's datasets and in the rest of this guide. Learn the terms; they are how you look things up.

| Term | Reading | What it means |
| :--- | :--- | :--- |
| 漢字 | かんじ | "Han characters". The logographic script borrowed from China. One character writes a **morpheme**, not a word and not a sound. |
| 部首 | ぶしゅ | **Radical** - strictly, the *one* component a dictionary files a character under. Loosely (and confusingly) used for any component. The distinction is worth getting right; see [radical vs component](#radical-vs-component---a-distinction-that-confuses-everyone). |
| 偏 / 旁 / 冠 / 脚 / 構 / 垂 / 繞 | へん / つくり / かんむり / あし / かまえ / たれ / にょう | The seven **positions** a component can occupy: left, right, top, bottom, enclosing, hanging over the top-left, wrapping the bottom-left. 氵 is さんずいへん; 辶 is しんにょう. All 321 rows of [Kanji Alive](<./Kanji Alive (radicals and kanji data)>)'s radical file carry one of these. |
| 画数 | かくすう | **Stroke count.** A lookup key, and the only objective measure of how complex a character is. |
| 筆順 / 書き順 | ひつじゅん / かきじゅん | **Stroke order.** A taught convention, not a property of the character. |
| 音読み | おんよみ | **On-yomi** - the reading derived from a Chinese pronunciation at the time of borrowing. Written in カタカナ in dictionaries. Dominant inside 熟語. |
| 訓読み | くんよみ | **Kun-yomi** - the native Japanese word mapped onto the character. Written in ひらがな in dictionaries. Dominant when the character stands alone or takes 送り仮名. |
| 名乗り | なのり | Readings a character takes **only in names**. 924 of the 2,136 常用漢字 have at least one in [KANJIDIC2](./KANJIDIC2). This is why you cannot read a Japanese name you have not been told. |
| 熟語 | じゅくご | A **compound word** written with two or more kanji and no kana between them: 漢字, 経済, 洗濯機. Normally read with 音読み. |
| 熟字訓 | じゅくじくん | A compound whose reading attaches to the **whole word** and cannot be split across its characters. 大人 = おとな. |
| 当て字 | あてじ | A character used for its **sound** (or occasionally its vibe) with its meaning disregarded: 珈琲, 出鱈目. |
| 送り仮名 | おくりがな | The kana **tail** after a kanji stem: the べる in 食べる. It marks where the inflecting part of the word begins. |
| 振り仮名 / ルビ | ふりがな | A small kana **reading gloss** printed above or beside kanji. |
| 常用漢字 | じょうようかんじ | The **2,136 characters** of the 2010 cabinet list - the set general-audience writing assumes. |
| 教育漢字 | きょういくかんじ | The **1,026 characters** taught in elementary school, assigned to grades by the 学年別漢字配当表. |
| 人名用漢字 | じんめいようかんじ | The extra characters legally permitted in **personal names**, beyond 常用漢字. |
| 表外字 | ひょうがいじ | A character **outside** the 常用漢字表. Not rare, not wrong, just unlisted - which is why newspapers gloss or avoid them. |
| 漢検 | かんけん | 日本漢字能力検定, the native-oriented kanji exam. Its levels run far past JLPT; see [the level data](<./Jinmeiyou and Kanken Kanji (names and difficulty levels)>). |
| 旧字体 / 新字体 | きゅうじたい / しんじたい | **Pre-reform / post-reform** character shapes. 國 became 国, 氣 became 気. |
| 異体字 | いたいじ | A **variant form** of the same character. 島 / 嶋. |
| 国字 / 和製漢字 | こくじ / わせいかんじ | A character **invented in Japan** rather than borrowed: 峠, 畑, 込, 塀, 枠, 腺, 働, 丼. |
| 六書 | りくしょ | The classical **six-way classification** of characters by how they were formed or used. Table in [semantic vs phonetic components](#semantic-vs-phonetic-components). |
| 象形 / 指事 / 会意 / 形声 | しょうけい / しじ / かいい / けいせい | Pictograph / ideograph / compound-ideograph / **phono-semantic**. The last one is the majority class by a wide margin - see [below](#the-two-myths-and-what-the-data-actually-says). |
| 音符 / 声符 | おんぷ / せいふ | The **phonetic component** of a 形声 character - the part that predicts the 音読み. 448 of them in [Kanjium](<./Kanjium (phonetic components and kanji elements)>)'s `phonetics.txt`. |
| 連濁 | れんだく | **Voicing** of a later element's initial consonant inside a compound: 手 + 紙 = てがみ. |
| 促音便 | そくおんびん | **Gemination** inside a compound: 学 + 校 = がっこう. |
| 連声 | れんじょう | A final ン **linking** into a following vowel: 因縁 いんえん becomes いんねん, 順応 じゅんおう becomes じゅんのう. |
| 重箱読み / 湯桶読み | じゅうばこよみ / ゆとうよみ | The two mixed-reading compounds: **on + kun** and **kun + on**. Named after themselves. |

Vocabulary keeps a parallel [word-level glossary](../Vocabulary/readme.md#basic-terms) and Writing keeps an [orthography glossary](../Writing/readme.md#reference-terms-for-written-japanese). There is deliberate overlap on three or four terms and no contradiction.

### The three levels: 部首, 漢字, 熟語

The system has exactly three levels, and knowing which level you are looking at answers most beginner questions by itself.

| Level | Japanese | What it is | KanjiDamage's analogy | Where the analogy breaks |
| :--- | :--- | :--- | :--- | :--- |
| **Component** | 部首 | A recurring sub-shape. Some are characters in their own right (木, 日, 口), some only ever appear inside others (宀, 艹, 疒), some are bare strokes. | "letters" | Letters encode sound systematically. Components mostly do not - and the ones that do (音符) predict only the 音読み, not the whole word. |
| **Character** | 漢字 | One character. Carries a **meaning-unit**, has one or more readings. | "words" | A kanji is a **morpheme**, not a word. 経 is not a word. Treating characters as words is the root of the keyword confusion in [pitfall 2](#common-pitfalls). |
| **Compound** | 熟語 | Two or more characters forming one word. | "compound words" | This one holds up well. It is also where the leverage is. |

The analogy is worth keeping despite the cracks, because it produces the single best piece of advice on the KanjiDamage site: **do not ask what a component inside a character means; ask what a character inside a compound means.** The first question usually has no answer. The second almost always does.

**How big is the component inventory, actually?** This is the question that decides whether component study is worth it, and it is answerable:

| Question | Answer | How it was counted |
| :--- | ---: | :--- |
| Traditional Kangxi radicals | **214** | `radicals.txt` in [Kanjium](<./Kanjium (phonetic components and kanji elements)>) is exactly 214 lines; [Kanji Alive](<./Kanji Alive (radicals and kanji data)>)'s file has 214 rows marked `Kangxi` out of 321 including variants. Two independent sources agree. |
| ...of which actually index a 常用漢字 | 198 | KANJIDIC2 `rad_value type="classical"` over the 2,136 |
| ...plus recognised variant forms | +73 | Kanjium `radicals_variants.txt` |
| Distinct components needed to build the **whole** 常用漢字 set | **241** | KRADFILE decomposition of the 2,136 (2 characters absent from the file) |
| Parts per 常用漢字 character | median **4**, mean 3.78 | same |
| Characters that are a single indivisible part | 80 | same |
| Phonetic components (音符) | 448 | Kanjium `phonetics.txt` |

**241 components for 2,136 characters.** That is the whole argument for component-first study on one line, and it is why [the recommended path](#recommended-path-opinionated) looks the way it does.

Now the deflation. Courses sell this as "learn N radicals and X% of kanji open up" - the [Mastering Kanji 1500](<./japanesepod101 Kanji course/Mastering_Kanji_1500.pdf>) book in this folder claims 48 radicals cover over 75% of the 常用漢字. Checked against KANJIDIC2's classical radical field:

| Top N radicals by how many 常用漢字 they index | Share of the 2,136 |
| ---: | ---: |
| 6 | 25.6% |
| 12 | 40.7% |
| 20 | 53.2% |
| 30 | 62.8% |
| **48** | **75.0%** |
| 100 | 91.4% |

So the headline claim is exactly right, and its intermediate steps are not: the book's 12-radicals-to-50% and 30-radicals-to-75% do not reproduce (41% and 63%). More importantly, **"indexes" is a much weaker verb than the marketing implies**. 75% of 常用漢字 being filed under one of 48 radicals tells you nothing about whether you can read them; it tells you a lexicographer picked one of those 48 as the filing key. Useful for looking a character up on paper, close to useless for recognising it.

### The two myths, and what the data actually says

KanjiDamage names two beliefs that every beginner arrives with and that both need killing on day one:

1. **"Every component means something."** Most do not. 青 in 清 晴 請 静 精 contributes sound, not blue. Asking what it means there is the same question as asking what the "r" in "fire" means - not a hard question, a **malformed** one. The mechanism is in [semantic vs phonetic components](#semantic-vs-phonetic-components).
2. **"Kanji look like the things they describe."** Almost none do.

The second myth is the more expensive one, because it sends people looking for pictures that are not there. Here is the actual composition of the 常用漢字 set, taken from `ids-analysis.txt` in [CJKVI IDS](<./CJKVI IDS (component decomposition)>) - a scholarly classification in the 說文解字 tradition, with redirects from 新字体 to their traditional forms resolved:

| Class | Japanese | Characters | Share |
| :--- | :--- | ---: | ---: |
| **Phono-semantic** | **形声** | **1,618** | **76.4%** |
| Compound ideograph | 会意 | 289 | 13.7% |
| Pictograph | 象形 | 188 | 8.9% |
| Ideograph | 指事 | 11 | 0.5% |
| Invented in Japan | 国字 | 6 | 0.3% |
| Other or uncertain | - | 5 | 0.2% |

2,117 of the 2,136 resolved; 19 had no classification in the file.

**Fewer than one character in ten is a picture of anything.** Three quarters are sound-plus-meaning compounds, which is a completely different object and rewards a completely different reading strategy. Two honest caveats: the classification is **Chinese etymology**, so it says what a character was built as roughly two thousand years ago, not how it behaves in modern Japanese - a component can be historically phonetic and no longer predictive - and the 說文解字 tradition is itself contested. Take 76.4% as "the overwhelming majority" rather than as a precise measurement.

### How many kanji there actually are

The [opening section](#what-this-is-and-why-it-matters) gives the headline lists. Here are the exact figures and the layers above them, because "how many kanji are there" has about six defensible answers depending on where you draw the line.

| Set | Japanese | Count | Verified from |
| :--- | :--- | ---: | :--- |
| Elementary school | 教育漢字 | **1,026** | KANJIDIC2 `grade` 1-6 |
| The general-use list | 常用漢字 | **2,136** | KANJIDIC2 `grade` 1-6 and 8; and the official table states 字種2136字 in its own preface |
| ...plus name-use characters | 人名用漢字 | **+863** | KANJIDIC2 `grade` 9-10. The Ministry of Justice list, as CSV, gives 652 non-jouyou plus 212 permitted jouyou variants = 864, one more than KANJIDIC2 flags |
| The standard character encoding | JIS X 0208-1997 | **6,355** | KRADFILE is one line per JIS X 0208 kanji, and it has 6,355 |
| Everything 漢検 examines | - | **6,244** | Kanken CSV: 6,787 rows, of which 537 have an empty 漢字テキスト field (398 of those carry a glyph image instead), leaving 6,250 text values and **6,244 distinct** characters |
| A serious Japanese dictionary file | - | **13,108** | KANJIDIC2 character count |
| Everything with a structural decomposition, CJK-wide | - | **88,937** | CJKVI `ids.txt` |

KanjiDamage's "over 5,000 of them, but you only need around 2,000 to read a newspaper" is therefore a fair summary. The important number is not on that list, though:

**The grade split inside 教育漢字:**

| Grade | 1 | 2 | 3 | 4 | 5 | 6 | Total |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Characters | 80 | 160 | 200 | 202 | 193 | 191 | 1,026 |

That total is 1,026 rather than the 1,006 older books give because the 2017 curriculum revision added 20 prefecture-name characters (茨 媛 岡 潟 岐 熊 香 佐 埼 崎 滋 鹿 縄 井 沖 栃 奈 梨 阪 阜), in force from 2020. If a resource says 1,006, it predates that.

**The lists are guidelines, not law.** The 常用漢字表 opens by calling itself a 目安 - a guide for 法令, official documents, newspapers, magazines and broadcasting - and explicitly says it does not reach into specialist fields, personal writing, or proper nouns beyond prefecture names, and does not invalidate older writing. 人名用漢字 is the one place where the list really is a legal restriction, because a registrar can refuse a name. Everything else is convention.

**And the set you are learning is partly a 1946 redesign.** The 当用漢字表 of 1946 restricted everyday use to 1,850 characters and simplified many shapes; the 1981 常用漢字表 raised it to 1,945; the 2010 revision landed on 2,136. Of the current 2,136, **362 have a distinct pre-reform 旧字体 form** (`shinjitai.json` in [the simplification folder](<./Kanji Simplification History (1946 reform and kyuujitai-shinjitai)>): 2,136 keys, 362 non-null). That is not trivia - it is why pre-war literature looks subtly wrong, and it is the single largest source of the "characters I have never seen" feeling in [Aozora Bunko](https://www.aozora.gr.jp/) texts.

### How many you actually need, measured

The guide asserts above that frequency is brutally skewed. It is, and here is the size of the skew. Cumulative share of **kanji tokens** covered by the top N characters, in three corpora from [Kanji Frequency](<./Kanji Frequency (multi-corpus)>):

| Characters known (most frequent first) | Online news | Aozora Bunko (literature) | Japanese Wikipedia |
| ---: | ---: | ---: | ---: |
| 100 | 45.1% | 37.0% | 38.0% |
| 200 | 61.1% | 50.7% | 53.7% |
| **500** | **83.3%** | **71.1%** | **76.9%** |
| **1,000** | **95.4%** | **86.3%** | **91.9%** |
| 1,500 | 98.8% | 93.1% | 96.9% |
| 2,000 | 99.7% | 96.4% | 98.7% |

Read the 500 row twice. **Five hundred characters is over four fifths of the kanji in a newspaper.** Character number 1,800 is worth a rounding error by comparison, which is the entire justification for KanjiDamage cutting its list and for [measuring words rather than characters](#measuring-progress).

Two things that table is **not** saying. First, this is coverage of kanji *tokens*, not of text and not of words: knowing every character in 気持ち does not give you 気持ち. Second, the rows are the top N *by frequency in that corpus*, which is not the 常用漢字 set. Measured as a set, the 2,136 常用漢字 account for **99.2% of newspaper kanji tokens, 98.1% of Wikipedia's and only 93.8% of Aozora's**.

That 93.8% is the interesting one, and the composition of the remainder tells you exactly what the endless tail is made of:

| Corpus | Distinct 表外字 appearing | Their share of tokens | Most frequent of them |
| :--- | ---: | ---: | :--- |
| Online news | 869 | 0.81% | 伊 幌 龍 彦 讀 賣 靖 阿 也 苫 智 之 |
| Japanese Wikipedia | 6,348 | 1.92% | 伊 之 彦 也 弘 龍 阿 智 澤 浩 乃 幌 |
| Aozora Bunko | 5,782 | 6.24% | 云 其 此 之 來 或 廻 於 氣 伊 貰 吾 |

The news and Wikipedia tails are **names** - 伊 and 幌 and 彦 and 苫 are place and person characters, and 讀 賣 is a newspaper masthead. The Aozora tail is **old forms and classical function words** - 來 and 氣 are pre-reform 旧字体, 云 其 此 於 或 are classical usage. Neither tail is learnable as a list, both are learnable in context, and 65 常用漢字 characters do not appear in the news corpus at all. That is the honest version of "you will never finish kanji": you will finish the useful part quite quickly, and then the tail is names and history forever.

### 画数 - stroke counts, and what they are for

A stroke is one unbroken contact of pen on paper. 画数 is how many of them a character takes, and the count is a **convention with edge cases** - KANJIDIC2 records an accepted count *plus* commonly accepted miscounts for exactly that reason.

Distribution across the 常用漢字, from KANJIDIC2:

| Strokes | Characters | Share |
| :--- | ---: | ---: |
| 1-4 | 113 | 5.3% |
| 5-8 | 571 | 26.7% |
| **9-12** | **838** | **39.2%** |
| 13-16 | 487 | 22.8% |
| 17-20 | 116 | 5.4% |
| 21+ | 11 | 0.5% |

Mean 10.5, **median 10**, range 1 (一, 乙) to 29 (鬱). Half the set is ten strokes or fewer and only one character in two hundred is above twenty, so the "wall of dense scribbles" impression is mostly an artefact of not yet seeing components. The visually terrifying characters are a rounding error.

**Two practical uses, and only two.** 画数 plus 部首 is how you look up a character in a paper dictionary or a radical-search tool when you do not know its reading - that is what the index was built for. And stroke count is the input to component decomposition: a 21-stroke character is never 21 things, it is three or four things.

**Does complexity predict usefulness?** KanjiDamage's "terrible secret" says almost not at all, and the guide repeats that when it [criticises school ordering](#5-textbook--school-order-kyouiku-kanji-by-grade). Now with a number: the Spearman correlation between stroke count and frequency rank across the 常用漢字 is **0.23 in news, 0.26 in Wikipedia, 0.32 in Aozora**. Weakly positive - so complex characters really are somewhat rarer - but weak enough to be useless as a guide. The top 100 characters by news frequency average 8.0 strokes; the rarest band of 常用漢字 averages 11.5. **The whole effect is about three and a half strokes across the entire frequency range**, which is why you meet 顔 (18 strokes) in grade 2 and 丹 (4 strokes) never.

### 筆順 - stroke order, the short version

[Writing](../Writing/readme.md#reference-stroke-order) owns this properly: 14 rules, the exceptions, and the question of who is even authoritative. Three things belong here, in the groundwork, because they change how you *read* a character even if you never handwrite one.

**1. Why it matters, minus the moralising.** The strong argument is not calligraphy and not legibility. It is that **a fixed order gives your hand a routine**, so recall becomes "run the sequence" instead of "reproduce the picture". The secondary argument is that 行書 and 草書 - ordinary adult handwriting and anything old - are stroke order rendered as continuous motion, so handwritten notes and signs become readable only once you know what order the strokes came in. And the honest counterweight: **stroke order is worth nothing for reading printed text**, which is what most people here actually want.

**2. The three habits, instead of 14 rules.** Writing's chapter reduces its own rule table to these, and they are enough to guess most characters correctly:

1. **Top-left to bottom-right, component by component.**
2. **Frames before contents; closing strokes last.**
3. **Piercing strokes and dots last; a dot at the very top first.**

The load-bearing word is *component*. You are not memorising 2,136 sequences; you are memorising a couple of hundred component sequences plus the order components go in. Which is the same leverage as everything else in this section.

**3. It is a taught convention, not a law.** The Japanese reference point is 筆順指導の手びき, published in 1958 as *guidance* for teaching elementary-school characters, and it covers only those. The clean proof that these are conventions rather than derivations: **左 starts with its horizontal stroke and 右 starts with its diagonal.** Two mirror-image shapes, opposite starting strokes, no principle that predicts it. When a character fights you, look it up rather than reasoning it out.

KanjiDamage's own position on stroke order is *"Psyche! I don't care about this even a little bit."* That is an overcorrection, but it is an overcorrection in the right direction for a reading-first learner. Stroke-order diagrams are in [`../Writing/Stroke order/`](<../Writing/Stroke order>) and, as raw per-stroke SVG data, in [KanjiVG](<./KanjiVG project>) below; the Anki decks in this folder ship them on the card, which is the correct way to use them: as a check, not a curriculum.

### 音読み and 訓読み - the orientation

Full mechanics, borrowing layers, heuristics and exceptions are in [Reference: readings](#reference-readings). The orientation version is three facts.

**1. Two families, because the import happened twice.** Characters arrived carrying a Chinese pronunciation, and were *also* matched to Japanese words that already existed. So most characters have a borrowed reading (音読み) and a native one (訓読み). The two-stage mechanism is in [the note on the historical import](#a-note-on-the-historical-import).

**2. The rule that gets you 80% of the way, on day one:**

> **Kanji touching kana, read it 訓. Kanji touching only kanji, read it 音.**

食べる is たべる. 食事 is しょくじ. That is the whole heuristic, and [the full table](#the-heuristics-and-they-are-good-ones) covers the cases it does not.

**3. "How do you pronounce this character" is usually the wrong question**, and here is how wrong. Counted from KANJIDIC2 over the 2,136 常用漢字:

| | 音読み | 訓読み |
| :--- | ---: | ---: |
| Characters with none at all | 6 | **359** |
| Characters with exactly one | 1,541 | 1,035 |
| Characters with two or more | **589** (27.6%) | **742** (34.7%) |

So a bit over a quarter of the set has multiple 音読み and over a third has multiple 訓読み stems, which means **for roughly half of all 常用漢字 there is no single answer to "how is this pronounced"**. 生 is the extreme case: 2 音読み and 18 訓読み entries in KANJIDIC2. The 359 characters with no 訓読み at all are the ones that only ever appear inside compounds (肉, 駅, 茶). Why this matters for [multiple borrowing layers](#why-there-are-multiple-on-yomi-the-layers-of-borrowing) is explained downstairs.

Two further numbers worth having:

- **The prescriptive and descriptive answers differ by half.** The 2010 常用漢字表 sanctions 4,388 readings for its 2,136 characters (2,352 音 and 2,036 訓), about 2.05 per character. KANJIDIC2, which is descriptive and includes rare, dialectal and obsolete readings, lists 2,854 音読み and 2,995 distinct 訓読み stems for the same characters - **roughly 33% more readings than the standard sanctions**. When a flashcard front shows you eight readings, that is why. Learn readings inside words and this problem evaporates; see [pitfall 3](#common-pitfalls).
- **The 音読み inventory is tiny, which is why Japanese is so homophonous.** All 2,136 常用漢字 are covered by just **337 distinct 音読み**. ショウ and コウ each serve **81** of them; 93 readings are shared by ten or more characters. Across all 13,108 characters in KANJIDIC2, 652 are pronounced コウ. KanjiDamage's "over 100 kanji with the same exact pronunciation (コウ, to be precise)" is true of the whole character set and an overstatement for 常用漢字, where it is 81. Either way this is a **listening** problem, not a reading one, and the writing system is the thing that solves it - see [Vocabulary on homophones](../Vocabulary/readme.md#homophones-and-what-pitch-accent-does-and-does-not-fix).

### 送り仮名, 振り仮名 and where the kana go

Two kana systems sit around kanji and do completely different jobs. Confusing them is common and costly.

**送り仮名 is part of the word.** It is the inflecting tail: 食**べる**, 食**べた**, 高**い**, 高**かった**. The kanji holds the meaning, the kana holds the grammar. Three consequences:

- **It is what makes the 訓/音 heuristic mechanically possible.** You can see okurigana. That visible kana is your signal to read the stem as 訓読み, which is why [the prerequisites](#where-it-fits-in-the-journey) insist you start grammar before kanji: without it you cannot tell a stem from its tail.
- **The boundary is partly conventional.** 行う and 行なう are the same word; 申し込み, 申込み and 申込 are the same word. Recognise the variants, write one, do not treat a spelling variant as a new vocabulary item. Rules and the official guideline document are in [Writing](../Writing/readme.md#okurigana---which-part-is-kanji-and-which-is-kana).
- **Sometimes it silently disappears.** 取引 (とりひき) and 受付 (うけつけ) are pronounced as though the kana were there. This is genuinely nasty because you cannot look up what you cannot spell; KanjiDamage tags it NOKURI.

**振り仮名 is not part of the word.** It is a reading aid printed above or beside the kanji, and it is a *publisher's decision*. Manga for younger readers glosses nearly everything, which is why manga is readable the moment kana is. Two things to know:

- **Furigana is the best crutch available and the easiest to become dependent on.** If your eye goes to the kana every time, you are practising kana recognition, not kanji recognition. The JP1K hover-furigana card design mentioned in [school 4](#4-no-isolated-kanji-study---kanji-through-vocabulary-only) exists precisely to make peeking deliberate rather than automatic.
- **It is also used expressively.** An author can gloss a word with a reading that is not its dictionary reading, saying two things at once. Manga does this constantly. Mechanics and vertical-text placement are in [Writing](../Writing/readme.md#furigana).

### 熟語 - compounds, and how their readings shift

This is where all the effort pays back, and it is the most cheerful part of the writing system. **Compounds are the logical layer**: if you know the characters, you can often guess both the reading and the meaning of a compound you have never seen. 火山 is fire plus mountain. 読書 is read plus book. KanjiDamage's promise that compounds "basically shriek their meaning at you" is the one piece of hype on that site that is close to true.

Four reasons to study compounds alongside characters rather than after them, which is the substance of KanjiDamage's argument and the reason [this guide recommends it over RTK](#recommended-path-opinionated):

1. **They show you what a character actually means**, as opposed to what its keyword says. 弾 as "play an instrument" and also "bullet" only becomes visible through 弾く and 爆弾.
2. **They drill the 音読み for free.** 本人, 本当, 本来, 本場 pound ホン into place without a single reading card.
3. **They are real vocabulary**, which a character keyword never is.
4. **They are where the compounding return lives.** New compounds get cheaper as your character stock grows, and this is the mechanism behind the [Phase 3 exit test](#phase-3---readings-inside-words).

How compound *meanings* are assembled - modifier plus head, verb plus object in Chinese word order, synonym pairs, antonym pairs, the 的/性/化 suffixes - is owned by [Vocabulary](../Vocabulary/readme.md#two-kanji-compound-patterns). What belongs here is the other half: **a compound's reading is frequently not the sum of its parts.** The 常用漢字表 says so itself, and lists its own examples in the preface under 音韻上の変化, sound changes triggered by combination:

| Compound | Parts | Reading | What moved |
| :--- | :--- | :--- | :--- |
| 納得 | ノウ + トク | ナットク | Vowel change plus gemination |
| 格子 | カク + シ | コウシ | The 音読み itself shifts in this compound |
| 手綱 | て + つな | タヅナ | Stem change (て to た) plus voicing |
| 金物 | かね + もの | カナモノ | Stem change (かね to かな) |
| 春雨 | はる + あめ | ハルサメ | 雨 takes its compounding form さめ |
| 音頭 | オン + トウ | オンド | Voicing plus shortening |
| 夫婦 | フ + フ | フウフ | Vowel lengthening |
| 順応 | ジュン + オウ | ジュンノウ | 連声: the ン links into the vowel |
| 因縁 | イン + エン | インネン | 連声 again |

Those nine are the government's own list, quoted because it is worth knowing that **the standard itself concedes the readings are irregular** and says outright that its examples are not exhaustive. The two most systematic of these changes, 連濁 and 促音便, get proper tables with their own rules in [the exceptions section](#the-exceptions-you-must-know-about); the rest are learned per word.

**熟字訓 - the compounds where per-character reading fails completely.** 大人 is おとな. Not だいじん, not おおひと. The characters supply meaning and nothing else, and no rule recovers the reading. The official list is finite and countable: the 付表 of the 常用漢字表 has **116 headwords across 123 written forms**, counted directly out of [the government PDF in this repo](<../Writing/Official orthography/joyo kanji table 2010 - 常用漢字表.pdf>). The table's own preface describes it as covering "いわゆる当て字や熟字訓など、主として1字1字の音訓としては挙げにくいもの" - the officially sanctioned irregulars, mixing 当て字 and 熟字訓 without separating them.

That 116 is a genuinely useful number, because it bounds the problem. Worth knowing about it:

- **They are front-loaded and unavoidable.** 明日, 今日, 昨日, 一日, 二日, 大人, 眼鏡, 果物, 上手, 下手, 時計, 部屋, 手伝う, 友達, 二十歳 are all on the list, and you will meet most of them in your first month.
- **They propagate into longer words.** The 付表 explicitly permits its entries inside bigger compounds: 河岸 (かし) gives 魚河岸 (うおがし), 居士 (こじ) gives 一言居士 (いちげんこじ).
- **116 is the *sanctioned* count, not the total.** The list covers what the standard chose to bless. Real text, and especially names and place names, has many more.
- **Do not try to derive them, and do not card them as characters.** They are vocabulary. The worked table is in [the exceptions section](#the-exceptions-you-must-know-about), and Vocabulary keeps [its own](../Vocabulary/readme.md#how-a-word-is-written).

**One data caveat to carry out of this section.** `waseikanji-ids.txt` in the [CJKVI folder](<./CJKVI IDS (component decomposition)>) is described as isolating the kanji invented in Japan, and it does contain the genuine 国字 - 峠 畑 込 塀 枠 腺 働 丼 are all in it. But it also lists post-reform simplified forms such as 会, 国, 読 and 気, which are borrowed characters with Japanese *shapes*, not Japanese inventions. **So it is not a clean 国字 list and a count taken from it would be wrong.** That is the general lesson for every dataset in this folder, including the ones this section leans on: check what a file actually contains before quoting a number out of it, and say which file you checked.

---

## Reference: how kanji are built

### Radical vs component - a distinction that confuses everyone

These two words get used interchangeably and they are not the same thing. Being precise here saves you real confusion later.

**The traditional radical** (部首, *bushu*) is the **one** component under which a dictionary indexes a character. There are **214** of these in the classical Kangxi system. It is a *filing* device: some ancient lexicographer looked at each character, declared one part to be "the main radical", and alphabetised the dictionary by that. Exactly one radical per character, chosen by convention, not by usefulness. The historical reason is mechanical - before you could type a reading into a phone, a paper dictionary of 5,000+ characters needed *some* index, and "main component" was the index they picked.

**The component sense** (also often called "radical", also often *bushu*, and in Heisig's terminology "**primitive**") is looser and far more useful: **any recurring recognisable sub-shape**. A character has as many of these as it has parts. KanjiDamage states its rule plainly: *"if the exact same pattern of lines is used in three or more kanji, it's a damn radical, and I made up a name for it."* Heisig notes the same thing from the other direction: *"the number of primitives is not restricted to the traditional list of radicals... Traditional etymology counts some 224 of them. We shall draw upon these freely."* Professional linguists call these *graphemes*.

The practical consequence, stated as a rule:

> The traditional 214 radicals are for **looking things up**. The looser component set - a few hundred shapes, depending on who is counting - is for **learning and remembering**. Do not confuse the index with the alphabet.

This is why a Japanese friend might insist that 暖 "has one radical, 日" - which is true in the dictionary-index sense and useless to you, because the upper-right part of 暖 appears in exactly the same shape and position in 受, 浮, 隠, 授, 妥 and 採, and the lower-right part appears in 友, 緩, 抜 and 援. Those are not coincidences; they are components, and knowing them is how you stop memorising 13 strokes as 13 strokes.

The payoff, in one example: 露 is a 21-stroke character. Memorising the placement of 21 strokes is miserable, and doing that 2,000 times is impossible. But it is three parts - 雨 (rain) + 足 (foot) + 各 - and each of those three parts is reusable: 雨 also builds 雲 霜 雪 雷; 足 also builds 踊 路 踏; 各 also builds 客 落 格 路. One decomposition buys you a dozen characters.

### Semantic vs phonetic components

Classical Chinese lexicography classifies characters six ways (六書, *rikusho*). The four formation types and two usage types are laid out in [Introduction to Kanji.pdf](<./General Introduction/Introduction to Kanji.pdf>):

| Class | Japanese | What it is | Example |
| :--- | :--- | :--- | :--- |
| Pictograph | 象形 | simplified picture of a thing | 山 (mountain), 日 (sun), 手 (hand) |
| Ideograph | 指事 | abstract concept indicated graphically | 上 (up), 下 (down), 三 (three) |
| **Phono-semantic** | **形声** | **one part gives meaning, one part gives sound** | 悲 = 心 (heart, meaning) + 非 (ヒ, sound) |
| Compound ideograph | 会意 | two or more meaning-parts combined; sound unrelated to either | 明 = 日 + 月 (bright); 休 = 人 + 木 (rest) |
| Associated meaning | 転注 | character extended to a related sense | 好 (beauty, virtue) used for 好む (to like) |
| Provisional use (ateji) | 仮借 | character borrowed purely for its *sound*, meaning ignored | 亜米利加 for アメリカ |

The row that matters operationally is **形声, phono-semantic** - and it is the majority class among complex characters. Its structure is:

- A **semantic component** narrowing the meaning domain. Usually on the **left** or the **top**.
- A **phonetic component** indicating the on-yomi. Usually on the **right** or the **bottom**.

KanjiDamage encodes exactly this as a heuristic worth burning in: *"the left side radicals are likely to be SYMBOLIC - to have to do with the meaning of the kanji. The right side radicals are more likely to be STRONG - to control the ONyomi of the kanji."*

**And here is the fact that spares you years of pointless frustration: a component is often purely phonetic and carries no meaning whatsoever.** Take the 青 family:

| Character | Meaning | On-yomi | Does 青 (blue) contribute meaning? |
| :--- | :--- | :--- | :--- |
| 清 | clear, pure | セイ | No |
| 晴 | clear weather | セイ | No |
| 請 | request | セイ | No |
| 静 | quiet | セイ | No |
| 精 | spirit, refined | セイ | No |

Not one of those has anything to do with blue. 青 is there **for its sound**. Asking "why does 'request' have 'blue' in it?" is the same category of question as asking an English speaker what the "r" in "fire" means. It is not a Japanese-is-crazy problem; it is a question that does not apply.

So the working rule is: **check the left/top component for a meaning hint, check the right/bottom component for a sound hint, and do not expect both to pay out.**

### High-value recurring components

These are the components with the best return per minute. Learn these and most characters become 2-4 familiar parts instead of a smudge. Position labels: `L` = left, `T` = top, `B` = bottom, `R` = right, `E` = enclosing.

| Component | Common name | Pos | What it signals | Example characters |
| :--- | :--- | :--- | :--- | :--- |
| 亻 (人) | person | L | people, human action | 休 体 作 使 係 侍 |
| 扌 (手) | hand | L | manual action | 持 打 押 投 指 抜 |
| 氵 (水) | water | L | liquid, flow, washing | 海 河 泳 洗 湖 清 |
| 忄 (心) | heart | L | emotion, mental state | 快 情 悩 慣 怖 忙 |
| 言 | say, speech | L | speech, language, writing | 話 語 読 記 訳 請 |
| 糸 | thread | L | string, cloth, binding | 紙 細 絵 給 練 縛 |
| 木 | tree, wood | L | plants, wooden objects | 林 森 板 松 材 格 |
| 日 | sun, day | L/T | light, time, weather | 明 時 晴 曜 暗 暖 |
| 月 | moon *or* flesh | L/R | months and time, **or** body parts | 明 朝 (moon); 肺 胸 腹 脳 (flesh) |
| 口 | mouth | L/B | speech, openings, holes | 吸 呼 唱 味 噂 品 |
| 土 | earth, soil | L/B | ground, places, building | 地 場 坂 埋 堕 |
| 女 | woman | L | women, family relations | 姉 妹 好 婦 妻 妨 |
| 子 | child | L | children, offspring | 孫 存 学 |
| 金 | metal, gold | L | metals, tools, money | 鉄 銀 針 鏡 |
| 火 / 灬 | fire | L/B | heat, burning, cooking | 焼 燃 灯 然 |
| 犭 (犬) | animal, beast | L | animals, wildness | 猫 犯 狩 独 猛 |
| 疒 | sickness | E | illness, pain | 病 痛 疲 症 |
| 艹 | grass, plant | T | plants, vegetables | 花 草 茶 葉 薄 |
| 竹 | bamboo | T | bamboo objects, writing tools | 箱 笑 筆 節 |
| 宀 | roof, house | T | dwelling, containment | 家 室 安 寒 宅 |
| 辶 | road, movement | E | going, motion, progress | 道 通 送 遠 迫 連 |
| 彳 | step, go | L | movement, conduct | 待 役 徒 得 |
| 阝 (left) | hill, mound | L | terrain, barriers, position | 防 陽 際 険 陣 |
| 阝 (right) | village, district | R | places, administrative areas | 部 郡 郊 都 郵 |
| 門 | gate | E | gates, openings, enclosure | 問 聞 間 開 閉 |
| 貝 | shell, money | B/L | money, value, trade | 買 財 貯 賃 販 |
| 車 | vehicle | L | vehicles, wheels, transport | 転 軽 輪 載 軒 |
| 目 | eye | L | sight, watching | 眼 睡 眠 |
| 心 | heart (bottom) | B | emotion, thought | 思 急 忠 恵 |
| 頁 | head, page | R | head, face, appearance | 顔 頭 願 頑 |
| 力 | strength | R/B | power, effort, work | 動 助 労 功 効 |
| 攵 | strike, action | R | acting on something | 放 政 敗 数 |
| 王 (玉) | king, jade | L | jewels, rule, refinement | 珍 現 球 理 |
| 米 | rice | L | grain, powder, materials | 粉 精 糖 料 |
| 飠 (食) | food, eat | L | food, eating, feeding | 飯 飲 館 飼 |
| 馬 | horse | L | horses, motion, commotion | 駅 験 駐 騒 |
| 雨 | rain | T | weather | 雲 雪 雷 霜 露 |
| 隹 | small bird | R | (mostly phonetic) | 唯 推 稚 維 催 |

Two traps in that table, both worth naming:

- **月 is a "jerk radical".** It means *moon* standing alone or in 明 and 朝, but *internal organ / flesh* inside 肺, 胸, 腹, 脳, 腫. Same shape, two unrelated jobs. There are a handful of these; 月 is by far the most common.
- **阝 does two different jobs depending on side.** On the left it is 阜 (hill/mound); on the right it is 邑 (village/district). Identical shape, different origin, different meaning.

The complete component inventory used by KanjiDamage, with every character that uses each one, is in [radicals.md](<./Kanji Damage/markdown/radicals.md>). Positional terminology in Japanese (へん, つくり, かんむり, あし, かまえ, たれ, にょう) is laid out in [Introduction to Kanji.pdf](<./General Introduction/Introduction to Kanji.pdf>).

For the *handwriting* side of components - stroke order rules, how to write a component correctly, handwriting as a practice - see [Writing](../Writing/readme.md). The method question "do components help recognition" is answered here: yes, decisively, and it is the main reason isolated study is worth doing at all. The mechanics question "which stroke goes first" lives there.

### A note on the historical import

Chinese characters arrived in Japan around the fourth or fifth century, carried by continental and Korean intermediaries, at a time when Japanese had **no writing system at all**. The adaptation happened in two stages, and both stages left permanent scars on the system:

1. **Phonetic use first.** Characters were used for their *sounds*, ignoring meaning. やま (mountain) was written with two characters whose Chinese readings were roughly *ya* and *ma*, with no semantic connection to mountains. This is the ancestor of both *man'yougana* and modern ateji.
2. **Semantic use second.** Characters were then matched to existing Japanese words by *meaning*, ignoring the Chinese sound. やま came to be written 山, even though 山 in Chinese was pronounced something like *shan*.

Stage 2 is why every kanji has two families of reading: the borrowed Chinese sound (**on-yomi**) and the native Japanese word that was mapped onto it (**kun-yomi**). Stage 1 is why ateji exist. It is also worth internalising that Japanese was forced onto a writing system built for a structurally unrelated language: Chinese has tones and is largely monosyllabic, Japanese has neither property. Squeezing one into the other produced most of the irregularity you are about to meet - mass homophony in on-yomi vocabulary, multiple on-yomi per character, and several characters competing for one native word.

The broader cultural and political history of Japan - the Tang embassies, Buddhist transmission, the Meiji script reforms - belongs to [Culture](../Culture/readme.md). What you need for kanji is the two-stage mechanism above.

---

## Reference: readings

### On-yomi and kun-yomi

Most kanji carry at least one of each:

- **On-yomi** (音読み, "sound reading") - derived from a Chinese pronunciation at the time of borrowing. Used predominantly in **compounds** (熟語, *jukugo*): 特定, 原案, 脂肪, 漢字.
- **Kun-yomi** (訓読み, "explanation reading") - the native Japanese word mapped onto the character. Used when the character stands **alone** or with **okurigana**: 肉 (にく), 逃げる (にげる), 苦い (にがい).

Some characters have only one kind. 肉 and 駅 are on-only in practice; 貝 and 畑 are kun-only.

### Why there are multiple on-yomi: the layers of borrowing

Characters were not borrowed once. They came in waves from different regions and centuries of China, and Japanese kept the readings from several waves side by side. The three layers, per [Introduction to Kanji.pdf](<./General Introduction/Introduction to Kanji.pdf>):

| Layer | Source | Arrived | Character |
| :--- | :--- | :--- | :--- |
| **呉音** (go-on) | the Wu region, lower Yangtze, Southern and Northern Dynasties | by the 6th century | often found in Buddhist vocabulary |
| **漢音** (kan-on) | the northwest, Tang dynasty; brought by Japanese embassies to the Tang court | 7th-9th century | the largest layer; the "default" on-yomi for most characters |
| **唐音** (tou-on, sometimes 宋音 sou-on) | Song dynasty standard; brought by monks and merchants | around the 12th-13th century | the smallest layer; scattered Zen and trade vocabulary |

So 行 has ぎょう, こう and あん sitting in different words for genuinely historical reasons: 行列 (ぎょうれつ), 旅行 (りょこう), 行灯 (あんどん). Memorising which layer a given reading came from is not the point - the useful takeaway is simply *why* one character can have several unrelated-sounding on-yomi, so it stops feeling arbitrary. Going deeper on the layer assignments is historical linguistics, not study strategy, and detailed layer claims should be treated as something to verify rather than trust.

### The heuristics (and they are good ones)

| Pattern | Reading | Example |
| :--- | :--- | :--- |
| Single kanji standing alone | **kun** | 猫 (ねこ), 雲 (くも), 肉 (にく) |
| Kanji + okurigana | **kun** | 大きい (おおきい), 殺す (ころす), 逃げる (にげる) |
| Two or more kanji together, no kana | **on** | 秘密 (ひみつ), 記者 (きしゃ), 洗濯機 (せんたくき) |
| Multi-kanji compound *with* kana inside | **kun** | 落ち着き (おちつき), 繰り返し (くりかえし), 食べ放題 (たべほうだい) |
| Proper nouns (names, places) | usually **kun**, but unpredictable | 田中 (たなか), 裏山 (うらやま) |

Two secondary observations worth keeping: no-okurigana compounds are usually **nouns**, and compounds with okurigana are usually **verbs**. Those correlations are useful when parsing a sentence you cannot fully read.

**Okurigana** (送り仮名, "accompanying letters") is the technical name for the kana hanging off the end of a kanji stem. Learn the word; you will need it constantly.

### The exceptions you must know about

The heuristics above are worth maybe 80%. Here is the rest.

**Jukujikun (熟字訓)** - a whole compound gets a single native reading that cannot be assigned to the individual characters. The characters supply the *meaning* and nothing else.

| Word | Reading | Literal characters | Meaning |
| :--- | :--- | :--- | :--- |
| 大人 | おとな | big + person | adult |
| 明日 | あす / あした | bright + day | tomorrow |
| 今日 | きょう | now + day | today |
| 一昨日 | おととい | one + last + day | day before yesterday |
| 田舎 | いなか | field + hut | countryside |
| 紅葉 | もみじ | crimson + leaf | autumn leaves / maple |
| 七夕 | たなばた | seven + evening | Tanabata festival |
| 眼鏡 | めがね | eye + mirror | glasses |
| 相撲 | すもう | mutual + strike | sumo |
| 為替 | かわせ | do + exchange | money exchange / draft |

You cannot derive these. Learn them as vocabulary. There are a few hundred that matter.

**Ateji (当て字)** - characters chosen for sound, with meaning disregarded (the 仮借 class): 亜米利加 for アメリカ, 珈琲 for コーヒー, 出鱈目 for でたらめ. Mostly historical curiosities now, since katakana does this job, but they turn up in older text, shop signs and manga.

**Rendaku (連濁) - mid-word voicing.** The initial consonant of a later element voices: か to が, は to ば, た to だ, さ to ざ.

| Compound | Parts | Result |
| :--- | :--- | :--- |
| 手紙 | て + かみ | てがみ |
| 花火 | はな + ひ | はなび |
| 昔話 | むかし + はなし | むかしばなし |
| 忍者 | にん + しゃ | にんじゃ |
| 株式会社 | かぶしき + かいしゃ | かぶしきがいしゃ |

**Gemination (促音便) - the doubled consonant.** In on-yomi compounds, a final consonant and a following consonant collapse into a small っ:

| Compound | Parts | Result |
| :--- | :--- | :--- |
| 学校 | がく + こう | がっこう |
| 日記 | にち + き | にっき |
| 失敗 | しつ + はい | しっぱい |
| 一本 | いち + ほん | いっぽん |

Note 一本 does both: gemination *and* は becoming ぽ. The counters are the worst offenders; 一本/二本/三本 is いっぽん/にほん/さんぼん.

**Mixed readings.** Two named exceptions to the on-for-compounds rule:

- **重箱読み** (juubako-yomi) - **on + kun**, named after 重箱 (じゅうばこ: 重 on + 箱 kun). Others: 台所 (だいどころ), 番組 (ばんぐみ).
- **湯桶読み** (yutou-yomi) - **kun + on**, named after 湯桶 (ゆとう: 湯 kun + 桶 on). Others: 見本 (みほん), 手本 (てほん), 消印 (けしいん).

**Nokurigana** - okurigana that stops being written but is still pronounced: 取引 (とりひき, from 取り + 引き), 受付 (うけつけ, from 受け + 付け). Genuinely nasty, because you cannot look up what you cannot spell.

**The practical response to all of this:** do not try to hold the exception lists in working memory. Read the tables once so you recognise the *categories*, then learn readings inside words and let the exceptions arrive as individual vocabulary items. Every single exception above is learnable as one word. None of them is learnable as a rule.

---

## Reference: phonetic series - the single biggest accelerator

If you take one thing from the reference sections, take this one. **A phonetic component predicts the on-yomi across a whole family of characters.** This is the highest-leverage pattern in the entire writing system, and most beginners discover it accidentally after a year instead of being told in week two.

KanjiDamage tags these components **STRONG**, defined as *"radical that usually controls the pronunciation of any kanji in which it is a component."* Once you know that 工 is コウ, you have a strong prior on 紅, 攻 and 功 without ever having met them.

Worked families (all verified against the local KanjiDamage data):

| Phonetic | Reading | Family | Notes |
| :--- | :--- | :--- | :--- |
| 青 | セイ | 清 晴 請 静 精 | Perfectly regular. None of them mean anything to do with blue. |
| 交 | コウ | 校 郊 効 絞 | Perfectly regular. |
| 白 | ハク | 泊 拍 迫 | Regular; 拍 also has ヒョウ. |
| 求 | キュウ | 救 球 | Regular. |
| 可 | カ | 何 河 歌 苛 | Regular. |
| 中 | チュウ | 虫 忠 仲 | Regular. |
| 生 | セイ | 性 星 姓 | Regular; several also carry ショウ. |
| 工 | コウ | 紅 攻 功 項 | Regular, but 空 drifted to クウ. |
| 反 | ハン | 販 飯 版 板 | 板 voiced to バン. Predict the consonant, expect voicing. |
| 方 | ホウ | 訪 放 / 防 房 妨 | Splits cleanly: ホウ or its voiced partner ボウ. Still a win. |
| 各 | カク | 格 客 | 客 has キャク and カク; but 落 went ラク and 路 went ロ. Partial family. |
| 寺 | ジ | 時 持 侍 | **But** 待 is タイ, 特 is トク, 詩 is シ. A family that visibly breaks. |
| 己 | (コ) | 記 紀 起 忌 | **Trap.** 己 alone is コ, but the family is almost all **キ**. KanjiDamage flags this explicitly. |
| 門 | - | 問 モン, 聞 ブン, 間 カン, 開 カイ, 閉 ヘイ | **Not phonetic at all.** 門 is a semantic/enclosing component. No prediction available. |

How to use this, concretely:

1. **When you meet an unknown compound, look at the right-hand or bottom component of each character.** If you recognise it as a phonetic you know, you have a guess at the reading.
2. **When you learn a new character, actively ask "what family is this in?"** Learning 請 as "the セイ family again" costs almost nothing; learning it as a fresh 15-stroke shape with a fresh reading costs a lot.
3. **Expect voicing and length variation, not identity.** ホウ/ボウ, ハン/バン, セイ/ショウ - the consonant and vowel skeleton is what is preserved.
4. **Treat exceptions as information, not betrayal.** 寺 giving ジ/タイ/トク/シ is genuinely messy. Note the mess once and move on. A heuristic that works 70% of the time is enormously valuable; demanding 100% is how people talk themselves out of using it.
5. **Use the bluffing routine.** When stuck on a compound, think of another word using the same character. *"品質 - something-shitsu. Where have I seen those three boxes? ...作品! Sakuhin! So 品 is HIN. Therefore 品質 is hinshitsu."* This is a skill; it gets fast with practice, and the "aha" is one of the genuinely satisfying parts of learning Japanese.

The complementary heuristic for *meaning*: check the left-hand or top component. If it has 火 in it, it probably concerns fire (焼 燃 爆 災). If it has 疒, it concerns illness (病 痛 疲 症). KanjiDamage tags these **SYMBOLIC**. Semantic on the left, phonetic on the right - that one sentence is most of what component analysis buys you.

Full on-yomi keyword list: [onyomikeywords.md](<./Kanji Damage/markdown/appendix/onyomikeywords.md>). Short-vs-long vowel disambiguation: [longshortvowels.md](<./Kanji Damage/markdown/appendix/longshortvowels.md>).

---

## Reference: look-alike confusion sets

The hardest part of early kanji is not memorising characters, it is **telling them apart**. SRS structurally hides this failure because it shows cards in isolation. Drill these side by side.

The discrimination technique is always the same: **do not re-memorise the whole character. Identify the one component that differs and memorise only that.**

| Set | The difference | Discrimination hook |
| :--- | :--- | :--- |
| 給 (provide) / 絵 (picture) | both 糸; right side is 合 vs 会 | 合 "fits together" = supply fits demand; 会 "meeting" = a picture is a gathering of things |
| 待 (wait) / 持 (hold) / 特 (special) | all share 寺; left is 彳 / 扌 / 牛 | step = wait by the road; hand = hold; cow = a special cow |
| 休 (rest) / 体 (body) | 亻 + 木 vs 亻 + 本 | tree = resting under it; 本 = the person's "main thing" is their body |
| 午 (noon) / 牛 (cow) | top stroke crosses or does not | the cow's horns stick out above the line |
| 未 (not yet) / 末 (tip, end) | which horizontal is longer | 末 has the long stroke on **top** - the end is at the top |
| 大 (big) / 太 (fat) / 犬 (dog) | bare / extra stroke inside / dot on top | fat has an extra roll; the dog has an ear |
| 少 (a little) / 小 (small) | extra diagonal stroke | 少 is *amount*, 小 is *size* |
| 王 (king) / 主 (master) / 玉 (ball) | dot position: none / on top / on the right | crown on top = master; the ball has a bump on the side |
| 力 (strength) / 刀 (sword) / 刃 (blade) | stroke direction; extra dot | the blade is a sword with a nick in it |
| 人 (person) / 入 (enter) | which stroke starts on top | 入 has a roof to enter under |
| 雲 (cloud) / 曇 (get cloudy) | 雨+云 vs 日+雨+云 | 曇 has a sun *behind* the cloud - the weather *becomes* cloudy |
| 原 (original) / 源 (origin, source) | 源 adds 氵 | water at the source |
| 像 (image) / 象 (elephant, phenomenon) | 像 adds 亻 | a person makes the image |
| 底 (bottom) / 低 (low) | 广 vs 亻 | a building has a floor; a person is short |
| 熟 (become skilled) / 塾 (cram school) | bottom is 灬 vs 土 | fire cooks you into skill; the cram school is a building on the ground |
| 求 (demand) / 救 (rescue) | 救 adds 攵 | rescue is demand plus *action* |
| 左 (left) / 右 (right) | bottom is 工 vs 口 | the mouth is on the right (口 for 右) |
| 復 (repeat) / 複 (multiple) | 彳 vs 衤 | step = go again; cloth = layered, multiple |
| 鳥 (bird) / 島 (island) | 島 has 山 underneath | an island is a bird sitting on a mountain |
| 手 (hand) / 毛 (hair) | direction of the top hook | hair curls the other way |

A far longer list of these - the author's "ill pairs", kanji that look as similar as their meanings, which makes them twice as hard - is in [illpairs.md](<./Kanji Damage/markdown/appendix/illpairs.md>). The related problem of *different characters for the same native word* (硬い / 固い / 堅い all かたい; 計る / 図る / 測る all はかる; 勤める / 努める / 務める all つとめる) is covered in [dupes.md](<./Kanji Damage/markdown/dupes.md>) and [synonyms.md](<./Kanji Damage/markdown/synonyms.md>).

---

## Resources

### In this repo (offline)

| Resource | Path | Format | What it is and how to use it |
| :--- | :--- | :--- | :--- |
| **Introduction to Kanji** | [link](<./General Introduction/Introduction to Kanji.pdf>) | PDF, 14 pp | Compact academic primer by Harumi Hibino Lory. Covers the history of the import, the go-on / kan-on / tou-on reading layers with their dynasties, the six-way 六書 classification, the 10 basic strokes, 12 stroke-order rules, 3 stroke endings, and the 214 historical radicals grouped into 8 positional categories with Japanese names. **Read this once, early** - it is the best short explanation of *why* kanji behave as they do. |
| **Mastering Kanji 1500** | [link](<./japanesepod101 Kanji course/Mastering_Kanji_1500.pdf>) | PDF, 537 pp | JapanesePod101's "A Radical Approach to Mastering Kanji". Front section teaches 48 radicals (+2 bonus) which it says appear in over 75% of joyo kanji, with a 6 / 12 / 30 breakdown corresponding to 25% / 50% / 75% coverage. **Checked against KANJIDIC2: the 48-radical / 75% headline is exactly right (75.0%), but the intermediate steps are not** - 12 radicals index 40.7% and 30 index 62.8%, not 50% and 75%. See the [groundwork chapter](#reference-the-groundwork---the-facts-a-beginner-needs-first) for the verified series. Bulk of the book is kanji tables: character, meaning, on/kun readings, and example vocabulary. Good as a **radical reference and a browsable vocabulary source**, weak as a primary study path (no SRS, no mnemonics). |
| **Learn Kanji in 45 Minutes (video)** | [link](<./japanesepod101 Kanji course/Learn Kanji in 45 minutes - How to Read and Write Japanese/video.mp4>) | MP4, ~61 MB | JapanesePod101 video lesson on reading and writing kanji, presented by Alicia and Risa. Decent orientation if you prefer video to text. |
| **...its subtitles** | [link](<./japanesepod101 Kanji course/Learn Kanji in 45 minutes - How to Read and Write Japanese/subs.srt>) | SRT | English subtitle track for the video above. Also greppable if you want to find a specific segment. |
| **COMPLETE_KANJIDAMAGE.md** | [link](<./Kanji Damage/COMPLETE_KANJIDAMAGE.md>) | Markdown, 5.7 MB | The **entire KanjiDamage site as one file**. This is the single most useful thing in this folder for lookups: grep it for a character, a reading, a component name or a jukugo and get every mention at once. |
| KanjiDamage - markdown archive | [link](<./Kanji Damage/markdown/>) | 2,403 .md files | The same content split into navigable files: main pages, an `appendix/` (3), `kanji/` (1,768 pages - kanji plus pure component entries), `tags/` (65), `synonyms/` (556). Use this when you want to read one page cleanly rather than grep the monolith. |
| - introduction | [link](<./Kanji Damage/markdown/introduction.md>) | Markdown | "Why most kanji textbooks suck" - the method's rationale and its four strategies (rad ordering, comprehensive mnemonics, warning tags, cutting useless kanji). **Read this before committing to KanjiDamage**, both for the argument and to check whether the tone works for you. |
| - kanji facts | [link](<./Kanji Damage/markdown/kanji_facts.md>) | Markdown | The theory chapter: bushu / kanji / jukugo, absolute vs symbolic vs kanji-as-radical, the two big myths (radicals always mean something; kanji look like what they describe), why complexity does not correlate with usefulness, on/kun and when to use which, jukugo, homophones and synonyms. **One of the best free explanations of kanji structure available.** |
| - how to use | [link](<./Kanji Damage/markdown/howto.md>) | Markdown | Decodes the site's format: sequence number, flags, breakdown, on-yomi keywords, mnemonics, usefulness ranking, tags, kunyomi, jukugo, look-alikes. Also contains an excellent **"bluffing when you can't read a kanji"** section - a genuine reading skill, not a gimmick. |
| - radicals in order | [link](<./Kanji Damage/markdown/radicals.md>) | Markdown | Every component the system uses, in teaching order, each linked to every character that contains it. The best **component-to-characters index** here. |
| - tags | [link](<./Kanji Damage/markdown/tags.md>) | Markdown | The warning-label system with counts: STRONG (90 characters - controls the on-yomi), SYMBOLIC (38 - controls the meaning), SAME ON, JERK RADICAL, PK, 1/2 KANA, NOKURI, NP, DUH, COUNTER and more. Worth reading in full once; it names problems you would otherwise hit blind. |
| - illpairs appendix | [link](<./Kanji Damage/markdown/appendix/illpairs.md>) | Markdown | Character pairs that look as similar as their meanings. **Drill this.** |
| - onyomi keywords | [link](<./Kanji Damage/markdown/appendix/onyomikeywords.md>) | Markdown | Every on-yomi with its English mnemonic keyword, alphabetical, plus the long/short vowel convention (long vowel = one word, short vowel = an abbreviation). |
| - long/short vowels | [link](<./Kanji Damage/markdown/appendix/longshortvowels.md>) | Markdown | Disambiguating しょ vs しょう, しゅ vs しゅう and friends. |
| - dupes | [link](<./Kanji Damage/markdown/dupes.md>) | Markdown | Different characters for the same native word (硬い/固い/堅い) and when to use which. |
| - synonyms | [link](<./Kanji Damage/markdown/synonyms.md>) + [dir](<./Kanji Damage/markdown/synonyms/>) | Markdown | 556 pages distinguishing Japanese near-synonyms where English has one word. Useful well past the kanji stage. |
| - japanese symbols | [link](<./Kanji Damage/markdown/japanese_symbols.md>) | Markdown | Punctuation and non-kanji symbols (々, 〜, ・ and so on). |
| - articles | [link](<./Kanji Damage/markdown/articles.md>) | Markdown | Miscellaneous essays from the site. |
| - kanji list | [link](<./Kanji Damage/markdown/kanji.md>) | Markdown | The full character list in teaching order - useful as a progress checklist. |
| KanjiDamage - website mirror | [link](<./Kanji Damage/website_mirror/index.html>) | HTML | Fully browsable offline copy **with images**. The markdown loses the component images; this does not. Open it in a browser when a mnemonic references a picture. |
| KanjiDamage - extracted data (JSON) | [dir](<./Kanji Damage/Extracted Data (JSON)>) | JSON, 2.2 MB | **The mirror above turned into queryable data.** `kanji.json` (**1,768 records**) and `tags.json` (**68 tags**), one record per line so both stay greppable. Every page's structure survives as fields: components, usefulness stars (0-6), tags, on-yomi with its keyword mnemonic, kunyomi, jukugo, look-alikes *with the distinguishing hint*, `used_in`, mutants, and the synonym word lists inlined - cross-links stored as the character they point at, not as an href. Use it when you want to **filter rather than read**: every STRONG character, every look-alike pair, everything the author rated 5 stars or better. **It inherits the mirror's gaps** - 281 internal links point at 26 pages the mirror does not contain (179 tag, 102 synonym), flagged in the data rather than dropped, so 24 of the 68 tags have no description. **No licence recorded**, see [`sources.md`](./sources.md). |
| **Official KanjiDamage Anki deck** | [link](<./Kanji Damage/Official_KanjiDamage_Anki_deck.apkg>) | .apkg, 21 MB | The deck this guide's recommended path is built around. Built by miwuc; contains all site data (mnemonics, jukugo, look-alikes, images) **plus stroke order diagrams**. Two card types by default: *reading* cards (kanji + a jukugo) and *writing* cards (meaning + on-yomi, a kunyomi and a jukugo in kana). Fully customisable - you can strip the writing cards if reading is your goal. Follows KanjiDamage order, not frequency order. |
| Official KanjiDamage deck - AnkiWeb page | [link](<./Kanji Damage/Official KanjiDamage deck - AnkiWeb.pdf>) | PDF, 20 pp | The deck's AnkiWeb page saved offline: full description, the author's own notes on the ordering trade-off, and instructions for customising the card types. **Read this before importing the deck** - the customisation section saves real time. |
| **KanjiDamage Plus - Anki deck** | [link](<./KanjiDamage Plus/KanjiDamage Plus+.apkg>) | .apkg | The extended community version: ~200 additional kanji over base KanjiDamage, some component names renamed, one flashcard per kanji with a pre-made mnemonic story that includes the character's most common reading. |
| KanjiDamage Plus - single-page reference | [link](<./KanjiDamage Plus/KanjiDamage Plus+.html>) | HTML, 1.3 MB | The whole deck as one scrollable page (2,100+ cards, kanji and component entries), saved from the neocities reference with its images. Excellent for **browsing or Ctrl+F lookup** without opening Anki. |
| KanjiDamage Plus - extracted data (JSON) | [dir](<./KanjiDamage Plus/Extracted Data (JSON)>) | JSON, 0.5 MB | The single-page reference above parsed into `kanji.json`: **2,136 records** over 2,074 distinct characters, with keyword, mnemonic, components, on-yomi, kunyomi, `used_in`, and a `stars` rating (0-5) merged in from the sibling `.apkg`, since the page itself prints no rating. **Not a duplicate of the extraction above** - counted across the two files, **438 characters appear only in Plus**, **8 only in the original**, and **264 of the 1,636 shared characters carry a different keyword** (丙 `t-bone steak` became `third`; 丈 `robust` became `height`). Plus is the wider list, the original the deeper record - it prints no `strokes`, `tags`, `jukugo`, `lookalikes` or `synonyms`. **No licence recorded**, see [`sources.md`](./sources.md). |
| KanjiDamage Plus - notes | [link](<./KanjiDamage Plus/readme.md>) | Markdown | Short description and the link to the online reference. |
| **Remembering the Kanji, Vol. 1** | [link](<./Remembering the Kanji/Remembering the Kanji  Vol. 1.pdf>) | PDF, 467 pp | Heisig, **fifth edition** (2007), **2,042 characters**. Meaning and writing only - explicitly no compounds and no readings. Part One gives full stories, Part Two gives skeletal plots, Part Three gives elements and expects you to build your own. Indexes by character, primitive, stroke order and keyword. **Read the introduction even if you do not do RTK** - it is the clearest statement of the "imaginative memory" argument that underpins every mnemonic system including KanjiDamage. |
| Remembering the Kanji, Vol. 2 | [link](<./Remembering the Kanji/Remembering the Kanji  Vol. 2.pdf>) | PDF, 199 pp | "A Systematic Guide to Reading Japanese Characters" - the readings volume for the characters in Vol. 1. **Note: this copy is a scan with no text layer**, so it is not searchable. Also note that most modern immersion advice says to skip it and learn readings in context instead. |
| Remembering the Kanji, Vol. 3 | [link](<./Remembering the Kanji/Remembering the Kanji  Vol. 3.pdf>) | PDF, 466 pp | "Writing and Reading Japanese Characters for Upper-Level Proficiency", with Tanya Sienko. Extends the method toward a **3,000-character total**, selecting the additional characters using frequency data, the JIS-1/JIS-2 character sets and the ministry's name-use list. For after Vol. 1, if you ever want the long tail. |
| RTK Flashcards (2042 Kanji) | [link](<./Remembering the Kanji/RTK Flashcards (2042 Kanji).pdf>) | PDF, 342 pp | Printable cut-out flashcards for the Vol. 1 set. Each card carries the character plus index codes (stroke count, dictionary index, RTK frame number, frequency rank, school grade). Useful if you want paper; an Anki deck is strictly better if you do not. |
| **Heisig RTK 6th Edition Anki deck** | [link](<./Remembering the Kanji/Heisigs RTK 6th Edition [Stories, Stroke Diagrams, Readings].apkg>) | .apkg, 32 MB | RTK as an Anki deck, labelled 6th edition, bundling **stories, stroke diagrams and readings**. Note this is a more generous package than the book itself, which deliberately withholds readings - so it is really "RTK ordering plus extras". If you want to do RTK without transcribing 2,000 frames by hand, start here. |
| **KANJIDIC2** | [dir](./KANJIDIC2) | XML 14.9 MB + JSON 16.8 MB | **The canonical kanji database, and the upstream of almost every other kanji dataset here** - including the `kanji-jouyou.json` in [JLPT](<../JLPT/Kanji Data by JLPT Level (KANJIDIC-derived)>), which was derived from it. **13,108 characters**, `database_version 2026-260` (created 2026-09-17). Per character: on/kun/nanori readings, English/French/Spanish/Portuguese meanings, stroke count with accepted miscounts, school grade, newspaper frequency rank 1-2500, **both** classical Kangxi and Nelson radical indices, every major dictionary index number (Nelson, Halpern, Heisig, De Roo), SKIP and Four Corner query codes, variant cross-references, Unicode/JIS codepoints. Counted from the file: **2,136 jouyou**, **1,026 kyouiku**, **863 jinmeiyou**, 2,501 with a frequency rank, 2,230 with a pre-2010 JLPT level - so the designations discussed above are one `<grade>` filter away (1-6 kyouiku by year, 8 = rest of jouyou, 9-10 jinmeiyou). Kept in **both** formats on purpose: script against the JSON, but **the XML's embedded DTD is the only place the field semantics are documented**. **CC-BY-SA 4.0 - EDRDG attribution mandatory**, see [`sources.md`](./sources.md). |
| **KRADFILE / RADKFILE** | [dir](<./KRADFILE and RADKFILE (kanji-radical decomposition)>) | text + JSON, 1.3 MB | **The "see components, not blobs" data this whole guide is built around, and it runs both ways.** KRADFILE maps **kanji to its components** (6,355 kanji; `kradfile2` 5,801); RADKFILE inverts it to **radical to every kanji containing it** (1,097 lines; `radkfile2` 1,169; extended `radkfilex` 1,888), which is what powers radical search on Jisho. The JSON conversions hold **12,156 kanji** and **253 radicals**. Bundled `kradintro`/`radkintro` files document the formats. Use this instead of trusting any one mnemonic system's component names - and pair it with `phonetics.txt` below, which tells you *which* of those components controls the reading. **EDRDG licence; `kradfile2`/`radkfile2` are copyright Jim Rose separately.** |
| **Kanji Alive (radicals and kanji data)** | [dir](<./Kanji Alive (radicals and kanji data)>) | CSV, 0.8 MB | **The 214 Kangxi radicals as proper structured data** - the thing this guide keeps needing and no other file here supplies cleanly. `japanese-radicals.csv` covers all 214 plus variants across **321 rows**, each with its **Japanese name in kana and romaji**, English meaning, stroke count, Kangxi-or-later origin, which radical it varies from, and its **positional category** (hen / tsukuri / kanmuri / ashi / tare / nyou / kamae - the same eight positions [Introduction to Kanji](<./General Introduction/Introduction to Kanji.pdf>) describes). `ka_data.csv` adds **1,235 kanji x 18 columns**: readings in kana and romaji, meaning, grade, the character's radical *with that radical's own name, meaning, strokes and position*, and a JSON list of example vocabulary with readings and translations. From the University of Chicago, **CC-BY 4.0** - a genuinely clean licence, which is rare here. |
| **Kanji Frequency (multi-corpus)** | [dir](<./Kanji Frequency (multi-corpus)>) | CSV + JSON, 1.8 MB | **The evidence for this guide's argument that raw kanji count is the wrong metric and frequency is what matters - from five corpora at once.** 2024 CSVs: Aozora Bunko **7,916 characters**, online news (Asahi/Mainichi/Yomiuri/Saga) **2,941**, Japanese Wikipedia **8,485**, each in a `_characters` (raw count) and a `_documents` (how many documents contain it) variant - a useful distinction, since a character can be frequent overall but concentrated in few documents, which marks it as specialist rather than general. Plus 2015 snapshots including **Twitter (4,517)**, which has no modern equivalent, and `jpdb_kanji_frequency.csv` (**5,112 kanji**, anime/drama/LN/VN). Read the upstream README's honest caveats: 笑 tops the Twitter list because it is used as a smiley, and ASCII-art faces inflate 个 and 皿. **CC-BY 4.0 (scriptin); the JPDB file has no stated licence - personal use only.** |
| **Kanjium (phonetic components and kanji elements)** | [dir](<./Kanjium (phonetic components and kanji elements)>) | text, 2.1 MB | **`phonetics.txt` is the single most valuable file here, and it is only 16 KB.** The phonetic-series section above (the 青 family) argues that components predict on-readings; this file is that argument as data - **448 phonetic components**, each with the on-reading(s) it produces, how many kanji it governs, and a split into `Single-reading phonetic` (reliable) versus `Mixed-reading phonetic` (not). 者 is listed as yielding シャ/ショ/チョ/ト across 24 kanji; 古 as yielding コ across 12. This is the only local source of that reliability distinction in machine-readable form. Beside it: `onyomi_statistics.txt` gives **per-kanji on-reading frequency counts** for 2,059 characters (丁 is チョウ 27 times vs テイ 24) - i.e. which reading to learn first, which almost nothing else exposes; `elements.txt` decomposes 6,813 characters with the **phonetic element as its own field** plus IDC shape code and jouyou/jinmeiyou/hyougaiji grade; `radicals.txt` is the 214 Kangxi radicals again (independent of Kanji Alive, so you can cross-check); `lookalikes.txt` is **487 confusable pairs** - the same problem as KanjiDamage's [illpairs](<./Kanji Damage/markdown/appendix/illpairs.md>) but drillable. **CC-BY-SA 4.0 with the author's prescribed attribution wording.** |
| **CJKVI IDS (component decomposition)** | [dir](<./CJKVI IDS (component decomposition)>) | text, 4.0 MB | **Decomposition that goes beyond KRADFILE: a recursive structural tree rather than a flat bag of parts.** IDS uses the Unicode Ideographic Description Characters to record *how* components are arranged - left-right, top-bottom, enclosure, overlaid - so 曜 is an explicit left-right composition whose right half decomposes again, not merely "contains 日, 羽, 隹". `ids.txt` covers **88,937 characters**. That is the difference between a component list and a real parse, and it lets you compute full breakdown trees, find characters sharing a *sub*-structure, or generate mnemonics programmatically. `ids-analysis.txt` (**18,347**) is the one to read second: it adds the traditional **六書 classification** (象形 pictographic, 形聲 phonosemantic...) and marks which component is the phonetic - a second, scholarly source on phonetic components independent of Kanjium. `ucs-strokes.txt` gives stroke counts for **89,586** characters where KANJIDIC2 covers 13,108, and `waseikanji-ids.txt` isolates the **2,749 kanji invented in Japan**. **GPLv2 / CHISE terms - the only non-Creative-Commons licence in this folder; see the flag in [`sources.md`](./sources.md).** |
| **KanjiVG (stroke and component SVGs)** | [dir](<./KanjiVG project>) | ZIP, 21.6 MB (11,662 SVG, 50.8 MB unpacked) | **Component structure with the ink attached - the decomposition data that draws itself.** **11,662 files over 6,703 characters**, one SVG per character: every stroke its own numbered `<path>` in drawing order, the paths *nested* inside `<g>` elements mirroring the character's breakdown, so 漢 is 氵 plus a right half that decomposes again into 艹, 口 and 夫. Each group is tagged: `kvg:element` names the sub-shape, `kvg:position` places it (left/right/top/bottom, tare, nyo, kamae), `kvg:radical` marks which tradition calls it *the* radical, `kvg:original` expands a reduced form (氵 → 水), and **`kvg:phon` names the phonetic component on 1,329 characters** - a third take on [phonetic series](#reference-phonetic-series---the-single-biggest-accelerator) beside Kanjium and CJKVI IDS. Most strokes also carry a `kvg:type` stroke class (147,621 of 148,292 paths), so stroke *shape* is queryable too. Coverage: **all 2,136 jouyou**, 645 of the 652 non-jouyou name kanji, both kana, and **4,959 variant files** (楷書 and 表外字 shapes, stroke-order variants). **What it is not:** no meanings, readings, frequency or grade - geometry and structure only; join KANJIDIC2 for anything semantic. It **overlaps [`../Writing/Stroke order/`](<../Writing/Stroke order>)**, which has the older `r20250816` release unpacked - go there for a single character's diagram, come here for the variant forms and newer data. **CC-BY-SA 3.0 (Ulrich Apel), attribution mandatory** - see [`sources.md`](./sources.md). |
| **Jinmeiyou and Kanken Kanji (names and difficulty levels)** | [dir](<./Jinmeiyou and Kanken Kanji (names and difficulty levels)>) | PDF + CSV, 3.7 MB | **The official name-use kanji list, plus a difficulty ordering finer than JLPT.** `jinmeiyou_kanji_moj_official.pdf` is the actual Ministry of Justice document (別表第三 of the Family Register Act Enforcement Regulations): the legal list of kanji, beyond jouyou, that a given name may use. It is a government work (free of copyright, Copyright Act Article 13) rendered with each character as an individual glyph image for typographic exactness - prose, not data, so it is paired with `name_use_kanji_mimneko.csv` (CC0, **3,000 rows**: 2,136 jouyou standard forms + 652 non-jouyou/jinmeiyou + 212 permitted jouyou variants) for the queryable version of the same list. `kanken_level_kanji_mimneko.csv` (CC0, **6,787 rows, 6,245 characters**) adds 漢字検定 (Kanken) level for each character across all ten official levels plus the two half-steps - JLPT N1 tops out around 2,000 characters, Kanken 1級 runs to roughly 6,000, so this is real headroom past JLPT. |
| **Kanji Simplification History (1946 reform and kyuujitai-shinjitai)** | [dir](<./Kanji Simplification History (1946 reform and kyuujitai-shinjitai)>) | PDF + JSON, 0.7 MB | **The 1946 当用漢字 reform itself, plus a queryable map of what it changed.** `touyou_kanji_hyou_1946_aozora.pdf` is Aozora Bunko's typeset reproduction of the 1946 cabinet order and cabinet notification that first restricted everyday kanji to 1,850 characters and introduced simplified shapes for many - public domain, since government notifications fall outside copyright. `kyujitai.json`/`shinjitai.json` (from `dahlia/shinjitai-table`; **2,138/2,136 keys, 364/362 non-null** - i.e. that many characters actually changed shape) give the old-form/new-form correspondence bidirectionally, e.g. `"亜": ["亞"]`. **Licence note: the JSON files carry no explicit licence** (see [`sources.md`](./sources.md)) - fine for personal use, flagged since this repo is public. |
| **Shuowen Jiezi (historical kanji etymology)** | [dir](<./Shuowen Jiezi (historical kanji etymology)>) | XML, 6.0 MB | **The primary source the guide's 六書 classification is ultimately built on - Xu Shen's 2nd-century dictionary, not a summary of it.** `swjz.xml` is Duan Yucai's Qing-dynasty annotated edition (經韵樓臧版) of 說文解字, digitised by the Kanji Database Project under a JSPS grant: **11,246 headword entries**, **9,426** original Han-dynasty definitions, **23,991** Duan-era commentary notes, organised into the traditional **540 radicals**, matching the structure of the original text. In Classical Chinese, which is the honest cost of going to the actual primary source; cross-reference with `ids-analysis.txt` in the CJKVI folder above for a modern structured index into the same 六書 categories. **GPLv2**, mirrored from `cjkvi/cjkvi-dict` because the original host (kanji-database.sourceforge.net) blocks scripted fetches. |
| **Phonetic Component Research (J-STAGE)** | [dir](<./Phonetic Component Research (J-STAGE)>) | PDF, 10 pp | **A Japanese-authored scholarly source on phonetic components.** Ishizawa Seiji (石沢誠司) - founder of the 漢字音符研究会 and author of the book behind the phonetic-component data this repo already carries - publishing in *JSL漢字学習研究会誌* vol. 10 (2018), pp. 46-55, DOI `10.20808/jslk.10.0_46`: how grouping kanji by shared phonetic component (the 青-family idea in [Reference: phonetic series](#reference-phonetic-series---the-single-biggest-accelerator) above) works as a teaching method, aimed at adult L2 learners specifically. **Licence note: freely readable via J-STAGE open access, but copyright is retained by the author/society and no redistribution licence is stated** - see the flag in [`sources.md`](./sources.md). |

**Two more kanji datasets sit under [Grammar](../Grammar/readme.md)**, because they came out of the Itazuraneko mirror rather than a kanji source: `kanji-ichiranhyou.json`/`.csv` (**27,506 characters** with their 漢字検定 level - 5,658 inside the twelve graded levels, the rest marked 以外) and `radicals.json`/`.csv` (the 214 traditional radicals and their variants, **321 rows**), both in [`../Grammar/Itazuraneko Master Reference/Extracted Data (JSON-CSV)/`](<../Grammar/Itazuraneko Master Reference/Extracted Data (JSON-CSV)>) and documented there.

### Online

| Name | Link | Notes |
| :--- | :--- | :--- |
| **KanjiDamage** | <https://www.kanjidamage.com/> | The live site. Component-based mnemonics, ~1,700 kanji ranked by usefulness, on-yomi keywords, jukugo, look-alike hints, warning tags. Free. Crude humour - check your tolerance first. The full site is mirrored above, so the live version mostly matters for its search box. |
| **KanjiDamage Plus** | <https://kanjidamageplus.neocities.org/> | The modernised, extended community version (~200 more kanji, some renamed components) as a single-page reference. Cleaner presentation than the original. |
| **Official KanjiDamage Anki deck** | <https://ankiweb.net/shared/info/748570187> | The AnkiWeb listing for the deck mirrored above. Use this for the current version and the comments. |
| KanjiDamage, frequency-ordered | <https://ankiweb.net/shared/info/1917095458> | Same content, reordered by character frequency, by the same author. The fix if "uncommon characters early" bothers you. |
| **WaniKani** | <https://www.wanikani.com/> | Managed SRS: radicals, then kanji, then vocabulary, with mnemonics for meaning and reading and hard level gating. Free for the first three levels, subscription after. The best choice if you will not maintain your own tooling, or if KanjiDamage's tone is a dealbreaker. |
| **Learning Kanji** (Tatsumoto) | <https://tatsumoto.neocities.org/blog/learning-kanji> | The immersion community's position, argued properly: kanji fluency as the real goal, isolated study as optional scaffolding, the JP1K compromise, and an honest account of the post-deck retention collapse. **Read this alongside the KanjiDamage introduction** - between them you have both sides of the central debate. A local mirror of this article is at [Tatsumoto: Learning Kanji](<../General content/Tatsumoto Blog offline copy/tatsumoto.neocities.org/blog/learning-kanji.html>), alongside [Learning Kanji Radicals](<../General content/Tatsumoto Blog offline copy/tatsumoto.neocities.org/blog/learning-kanji-radicals.html>). |
| Kanji Koohii | <https://kanji.koohii.com/> | Free SRS built for RTK, with a large database of community-shared mnemonic stories. The story database is worth mining even if you are not doing RTK - when a character will not stick, someone there has a better story for it than you do. |
| Jisho | <https://jisho.org/> | Dictionary with per-character pages: readings, stroke order, component breakdown, radical search, example words, JLPT level and frequency rank. The default lookup tool. |
| jpdb | <https://jpdb.io/> | Frequency data, per-media vocabulary and kanji lists, and its own SRS. Excellent for answering "which characters does *this specific anime/manga* need", which no fixed-order course can do. |
| MaruMori | <https://marumori.io> | Integrated paid curriculum covering grammar, kanji, vocabulary and reading together. Worth knowing about if you want one system rather than assembled parts. |
| Anki | <https://apps.ankiweb.net/> | The SRS everything above assumes. Setup, FSRS, deck settings and add-ons are covered in [General content](<../General content/readme.md>). |

---

## Where to go next

- **[Vocabulary](../Vocabulary/readme.md)** - the necessary counterpart. Kanji gives you characters; vocabulary gives you words, and words are what text is made of. Deck choice, card formats, frequency data and SRS vocabulary strategy live there. If you read only one sibling guide after this one, read that one.
- **[AJATT](../AJATT/readme.md)** - sentence mining, immersion scheduling, active vs passive time. This is what converts your kanji deck into actual ability. Kanji study without immersion is the most common way to waste a year.
- **[Reading](../Reading/readme.md)** - graded readers, reading ladders, what to read when. The place to go the moment you can distinguish characters.
- **[Grammar](../Grammar/readme.md)** - particles, conjugation, sequencing. You need enough of this to tell a stem from its okurigana, which is what makes the kun/on heuristic work at all.
- **[Writing](../Writing/readme.md)** - stroke order mechanics, handwriting as a discipline, IME and typing. Go there if you decided handwriting is one of your goals, and go there anyway before you decide it is not.
- **[General content](<../General content/readme.md>)** - Anki setup, FSRS, deck settings, add-ons, Yomitan, dictionaries and fonts. Do this before Phase 1, not after you have already built a bad habit.
- **[Kana](../Kana/readme.md)** - the prerequisite. If kana is still slow, go back and fix it; everything here depends on it.
- **[JLPT](../JLPT/readme.md)** - levels, test structure, strategy. Relevant if you need a certificate; not relevant to reaching kanji fluency.
- **[Listening](../Listening/readme.md)** and **[Speaking](../Speaking/readme.md)** - the abilities kanji does *not* give you. Keep them running in parallel from day one.
- **[Culture](../Culture/readme.md)** - the broader history and society behind the writing system.
