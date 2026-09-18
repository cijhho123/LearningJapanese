# Usage

Nine commands, plus one skill that fires on its own. You will mostly use two
of them.

---

## `/japanese-tutor:study`

Open a session. It loads what you know, what's due, what you keep getting wrong,
and what you're partway through - then asks what you feel like.

```
> /japanese-tutor:study

12 vocab items are due, and に/で has tripped you up four times this week.
You're also midway through Yokubi lesson 12.
What do you feel like? Or say "you pick".

> just kanji today

Fine. Six due, starting with the one you're closest to forgetting.

Read the kanji in this word:  食事
```

Say **"you pick"** and it chooses using your actual state - nearly-forgotten
items first, then any confusable pair it has spotted, then your top recurring
mistake.

There is no routine, no day counter, and nothing to fall behind on. Come back
after three months and it picks up exactly where the data left off.

## `/japanese-tutor:drill [topic]`

Focused practice on one thing.

```
/japanese-tutor:drill particles
/japanese-tutor:drill te-form
/japanese-tutor:drill kanji readings
/japanese-tutor:drill output
/japanese-tutor:drill              (it picks your weakest area)
```

About ten items, mixed formats, then a short summary. If something has lapsed
five or more times it repairs the item - checks what it's colliding with, builds
a mnemonic with you, or parks it - rather than making you grind it again.

## `/japanese-tutor:mine`

Paste Japanese text, or give a file path. It tells you how much you already
know and which sentences are worth learning from.

```
> /japanese-tutor:mine
> [paste a paragraph]

About 83% known - mining material rather than something to read for pleasure yet.
Three genuinely new words. Two sentences have exactly one unknown each:

  1. 卒業してから、ずっと連絡を取っていない。  <- 連絡
  2. 彼の説明はどうも曖昧だった。              <- 曖昧

Want either of those added?
```

It only suggests adding a word when the sentence around it is otherwise known -
a card with three unknowns in it teaches nothing. Grammar that the segmenter
mistakes for vocabulary (`います`, `ます`) is discarded rather than offered.

## `/japanese-tutor:resources`

Control what the tutor teaches from.

```
/japanese-tutor:resources                     show the catalogue
/japanese-tutor:resources use Tae Kim         switch something on
/japanese-tutor:resources ignore KanjiDamage  switch something off
/japanese-tutor:resources scan                pick up newly added guides
/japanese-tutor:resources add https://...     download something new into the repo
```

See [RESOURCES.md](RESOURCES.md).

## `/japanese-tutor:progress`

Where you are, what's weak, and whether your current pace actually reaches your
goal. This is the blunt one - it does the arithmetic and tells you when it
doesn't work out.

## `/japanese-tutor:assess`

Full adaptive placement: vocabulary size, kanji, grammar, reading against
listening, and production. Around 20 minutes. Worth re-running every few months.

Reports a range per skill rather than one JLPT number, because a single number
hides exactly the imbalances that matter.

## `/japanese-tutor:plan`

Optional. Builds a staged plan from a goal and a deadline, and checks the
arithmetic before writing anything. If the numbers don't reach the goal it says
so first.

```
/japanese-tutor:plan            create, or show the current one
/japanese-tutor:plan advance    move to the next step
/japanese-tutor:plan off        deactivate
```

Having a plan doesn't make the tutor prescriptive - `study` mentions where you
are in it as one suggestion among others.

## `/japanese-tutor:configure`

Change any setting, or manage what it remembers about you.

```
/japanese-tutor:configure switch to immersion
/japanese-tutor:configure 20 minutes a day
/japanese-tutor:configure forget that I wanted to take N2
```

See [STATE.md](STATE.md) for every setting and [MEMORY.md](MEMORY.md) for the
memory side.

## `/japanese-tutor:onboard`

First-run setup. Re-runnable any time you want to redo your preferences.

## Just asking

You don't need a command. Ask about anything Japanese in normal conversation:

```
> what's the difference between wa and ga here?
> how do you read 生憎?
> why is it が and not を after 好き?
```

It answers **and records it**, so something you asked about once in passing
enters your review schedule and comes back around. This is how the loose,
no-routine mode still accumulates.

---

## Using the scripts directly

Everything the tutor does is available from the command line. `kb.py` prints
JSON.

```
python japanese-tutor/scripts/kb.py brief        one-screen summary
python japanese-tutor/scripts/kb.py stats
python japanese-tutor/scripts/kb.py due --limit 20
python japanese-tutor/scripts/kb.py weak
python japanese-tutor/scripts/kb.py know kanji 待
python japanese-tutor/scripts/kb.py recall       what it remembers about you
python japanese-tutor/scripts/kb.py resources --summary
python japanese-tutor/scripts/kb.py known-words       every word you know
python japanese-tutor/scripts/kb.py confusables       pairs you mix up
```

Useful for scripting, exporting, or checking what the tutor actually recorded
after a session.
