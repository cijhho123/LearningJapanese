# Memory

Separate from the database, the tutor keeps plain-markdown notes about **you** -
your goals, your constraints, how you want to be taught, and habits it has
noticed. These are loaded at the start of every skill, which is what stops you
re-explaining yourself every session.

```
japanese-tutor/state/memory/
  MEMORY.md          the index, loaded every time
  hates-romaji.md    one file per memory
  ...
```

Markdown rather than database rows on purpose: you should be able to open these
in any editor, read exactly what the tutor thinks about you, and change or
delete it.

## Four kinds

| Kind | For | Example |
|---|---|---|
| `user` | Durable facts | "Works full time, studies on the commute" |
| `feedback` | Corrections about how the tutor should behave | "Stop explaining before asking me" |
| `preference` | Habits it observed rather than was told | "Disengages when a drill runs past ten items" |
| `goal` | Targets, with dates | "Employable in Japanese tech within 2-4 years" |

## What a memory looks like

```markdown
---
name: hates-romaji
kind: preference
title: Hates romaji
created: 2026-09-17
---
Never use romaji, including in quiz options and hints. Kana or kanji only.

**Why:** Considers it a lossy encoding with no canonical spec.
**How to apply:** If a reading is needed, use kana in a Key section at the bottom.
```

The **Why** matters more than it looks. A rule without its reason gets applied
too literally or dropped the moment it's inconvenient.

## Managing them

```
/japanese-tutor:configure                          view them
/japanese-tutor:configure forget the N2 goal       delete one
```

Or directly:

```
python japanese-tutor/scripts/kb.py recall              list
python japanese-tutor/scripts/kb.py recall hates-romaji read one
python japanese-tutor/scripts/kb.py forget hates-romaji delete
python japanese-tutor/scripts/kb.py remember preference "Title" --body "..." --why "..."
```

Editing the files by hand is fine and expected. The index rebuilds itself on the
next write; if you want it refreshed immediately, run any `remember` or `forget`.

## What gets written, and what doesn't

**Written:** you correct how the tutor teaches; you state a durable preference;
you mention something about your goals, timeline or life that changes what makes
sense; the tutor notices a pattern in how you work.

**Not written:** anything the database already answers. Item counts, error
rates, what's due, which resources are active, how long your streak is - those
are queries, and duplicating them into memory just creates two versions of the
truth that drift apart.

If the tutor starts recording things that look like statistics, delete them and
tell it to stop. That correction is itself worth a `feedback` memory.

## Why not the built-in memory

Claude Code has its own automatic memory, and this deliberately doesn't use it.
That store is tied to your machine and your Claude install rather than to this
project, it isn't visible next to the rest of your learner state, and its
contents aren't yours to structure.

Keeping memory inside `japanese-tutor/state/` means one folder holds everything
the tutor knows, you can back it up or move it in one copy, and deleting it
genuinely deletes everything.

## Privacy

Same as the rest of your state: gitignored, local, never uploaded. These files
can be fairly personal - goals, frustrations, what you find hard - which is
exactly why they aren't committed to a shareable repository.
