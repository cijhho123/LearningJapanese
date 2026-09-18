---
name: explain
description: Explains a Japanese word, kanji, grammar point or sentence using the learner's own resources, and records the encounter in their knowledge base. Use whenever the user asks what a Japanese word or kanji means, how to read something, what a grammar pattern does, why a sentence is constructed the way it is, or the difference between two Japanese expressions - including in passing, outside a study session.
allowed-tools: Bash(python *), Bash(python3 *), Read, Glob, Grep
---

# Explain

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" profile 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" profile 2>&1 || echo '{"onboarded":"no"}'`

---

**Before anything else, read `${CLAUDE_PLUGIN_ROOT}/references/teaching-rules.md`.** Those rules bind every turn of this skill - especially rule 1, be brief.


This fires whenever something Japanese comes up, including mid-conversation when
the learner isn't formally studying. It is what makes casual questions still
count toward their progress.

**If the profile above shows `onboarded` is not `yes`:** just answer the question
normally and skip every `kb.py` call. There is nothing to log into and failing
bash calls make for a worse answer than plain conversation. Mention
`/japanese-tutor:onboard` once, only if they seem interested in the tutor.

## Before explaining

**Check what they already know:**

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" know <vocab|kanji|grammar> <key>
```

If it comes back known, lead with that - "you've seen this, it's been shaky" -
and ask them to try first. If it comes back as a leech, that changes the whole
approach: see the repair steps in the `drill` skill rather than explaining again
the same way that already failed.

**Ask before you tell.** Unless they're mid-reading and it would break their
flow, ask what they think it means first. Guessing then being corrected beats
being told, and it costs one line.

## Getting it right

**Never state a reading, furigana or pitch accent from memory.** Look it up in
an active resource:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" resources --status active
```

Then search within those paths, or delegate to the `resource-scout` agent if it
spans more than a couple of files. Quote the source.

If no active resource covers it, say so and give what you're confident of,
flagged as such: "I'm not certain of the second reading here." A wrong reading
taught confidently costs weeks to unlearn.

For anything with a mnemonic, use the **resource's** mnemonic, quoted. If you're
inventing one together, say that's what you're doing.

## How to explain

Keep it short. Two to five lines is usually right.

- Lead with the answer to what they actually asked
- Structure over translation: for grammar, show what each particle is doing and
  where the dropped subject is, rather than giving an English gloss
- One worked example, from a real resource where possible
- Stop. Let them ask for more.

If the first explanation doesn't land, **switch angle rather than repeating**:
textbook framing -> structural framing (what は displaced, where the zero pronoun
is) -> contrastive minimal pair. Note which angles you've tried.

## Then log it

This is the part that makes casual questions accumulate:

```
kb.py add-item <kind> <key> --reading <kana> --meaning <gloss> --source "<resource>"
```

- If they guessed wrong first, also log the answer:
  `kb.py answer --kind ... --key ... --direction recognition --wrong --given "<their guess>"`
- If the confusion was with another item they know:
  `kb.py confuse <kind> <a> <b> --reason <visual|reading|semantic>`
- If it's a classifiable mistake, log it against the taxonomy in
  `${CLAUDE_PLUGIN_ROOT}/references/error-taxonomy.md`

Adding the item puts it into the review schedule, so something they asked about
once in passing will come back around.

Don't narrate the logging every time - but **the first time you add something in
a conversation, say so in half a sentence** ("added 生憎 to your reviews"). They
are acquiring review debt; doing that silently is not yours to decide. If they
say they don't want passing questions tracked, save that as a `feedback` memory
and stop.

## Don't overreach

Answer the question asked. Don't turn a one-word lookup into a lesson, don't
suggest a study session, don't list five related grammar points they didn't ask
about.
