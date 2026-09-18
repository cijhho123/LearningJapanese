---
name: mine
description: Analyses a piece of Japanese text against what the learner already knows - reports the percentage of known words, whether the text is at a usable difficulty, and which sentences contain exactly one unknown word (i+1) worth turning into study items. Use when the user runs /japanese-tutor:mine, pastes Japanese text and asks how hard it is or what they don't know, asks to mine vocabulary from something, or asks whether they are ready to read a particular thing.
argument-hint: [paste text, or a path to a file]
allowed-tools: Bash(python *), Bash(python3 *), Read, Glob, Grep
---

# Mine

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" stats 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" stats 2>&1 || echo "{}"`

Input: **$ARGUMENTS**

---

**Before anything else, read `${CLAUDE_PLUGIN_ROOT}/references/teaching-rules.md`.** Those rules bind every turn of this skill - especially rule 1, be brief.


## Getting the text

- If they gave a file path, use `--file`.
- If they pasted text, pipe it in on stdin - do not pass long Japanese as a
  command-line argument, it breaks on quoting.
- If they gave neither, ask for the text. One line.

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/coverage.py" --file <path>
printf '%s' '<their text>' | python "${CLAUDE_PLUGIN_ROOT}/scripts/coverage.py"
```

## Reading the output

`coverage_pct` is the share of words already known. The rough bands:

| coverage | what it means |
|---|---|
| 98%+ | readable unassisted |
| 95-98% | the usual target for reading volume |
| 90-95% | intensive study only - tiring to read at length |
| below 90% | a source of mining targets, not a reading text |

These are conventions, not cliffs. 98% is the extrapolated threshold for
comfortable unassisted reading and 95% the "minimally acceptable" one; Schmitt
et al. (2011) found the coverage-comprehension relationship is essentially
linear, with no point where reading suddenly works. Quote them as targets, and
say so.

**Important caveat about the segmentation.** Unless `engine` says `sudachipy`,
word boundaries are approximated by matching against the learner's known words.
The *known* side is exact; the *unknown* side is a rough guess that can split or
merge words. So:

- Trust the coverage percentage and the known-word matches.
- Treat `top_unknown` and `unknown` as **candidates**, and use your own reading
  of the sentence as the authority. If the script says `います` is unknown,
  recognise that as grammar and skip it.
- Never present the script's segmentation to the learner as fact.

## What to report

Four lines plus the sentence list - not forty:

1. Coverage percentage and the verdict in plain words - "about 83%, so this is
   mining material rather than something to read for pleasure yet".
2. How many genuinely unknown words there are.
3. The i+1 sentences - **at most five**, the ones with exactly one real unknown.
4. Ask which they want to add.

Do not paste back the whole JSON. Do not list thirty unknown words.

## Mining rules

Only add an item if:

- The sentence has **exactly one** genuinely unknown element. Two is tolerable;
  three or more teaches nothing and should be skipped.
- The word is likely to recur. Skip hyper-specific proper nouns and one-off
  technical terms unless the learner wants them.
- They don't already half-know it - check with `kb.py know vocab <word>`.

For each one they pick:

```
kb.py add-item vocab <word> --reading <kana> --meaning <gloss> --source "mined:<title>"
```

Store the sentence it came from, so later reviews can show it in context:

```
kb.py add-item vocab <word> --reading <kana> --meaning <gloss> \
  --source "mined:<title>" --sentence "<the full sentence>"
```

Look the reading up rather than producing it from memory. If you cannot confirm
it, follow the ladder in teaching rule 4 and **omit `--reading`** rather than
storing a guess.

## If the text is far too hard

Say so directly. Below about 90% coverage, working through it is decoding rather
than reading; below 80% it is not even useful for mining, because a card whose
sentence you cannot read has no context to anchor it.

Offer the alternative: a generated `graded-passage` at their actual level
covering the same topic or vocabulary, which they can read now, and come back to
the real text later.

## If the text is easy

Above ~98%, say it and suggest they just read it. Nothing to mine is a good
result, not a failure.
