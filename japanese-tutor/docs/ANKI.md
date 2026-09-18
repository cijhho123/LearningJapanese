# Anki (optional)

**The tutor does not need Anki.** It has its own FSRS scheduler and its own
knowledge base, and works identically with Anki uninstalled, closed, or never
heard of. Everything here is a bonus.

If you already have Anki with decks you've studied, the one genuinely valuable
thing is **import**: it tells the tutor which words you already know, so it
doesn't spend a month re-teaching you vocabulary you learned last year.

## Check what's available

```
python japanese-tutor/scripts/anki.py status
```

Three possible answers:

| Mode | Means |
|---|---|
| `connect` | Anki is running. Decks readable, cards can be added. |
| `collection` | Anki is closed. Decks readable, nothing writable. |
| `none` | No Anki found. Nothing is broken. |

Reading works in both of the first two, because the collection file is opened
read-only and immutable - safe even with Anki open, and it never takes a lock or
modifies anything.

## Import what you know

```
python japanese-tutor/scripts/anki.py decks
python japanese-tutor/scripts/anki.py import --deck "Kaishi 1.5k" --dry-run
python japanese-tutor/scripts/anki.py import --deck "Kaishi 1.5k"
```

Always dry-run first. It reports what it would do:

```
{
  "deck": "Kaishi 1.5k",
  "imported": 5,
  "skipped_not_mature": 1495,
  "note": "Only cards with an interval of 21 days or more were treated as known."
}
```

### Why it imports so little by default

Only cards with an interval of **21 days or more** count as known - Anki's own
definition of a mature card.

This is deliberate and conservative. Importing all 1500 cards in a deck you're
200 cards into would tell the tutor you know 1500 words. It would then stop
teaching them, skip them in coverage analysis, and build reading material on the
assumption you can read words you've seen once. Under-importing costs you a few
easy reviews; over-importing corrupts the model of what you know.

Use `--all` to override, if you genuinely know the whole deck.

### What carries across

Anki's interval becomes the tutor's initial **stability**, and review counts and
lapses carry over. That's an approximation - the two systems don't define
intervals identically - but it's far better than starting a well-known word from
scratch.

Only the `recognition` direction is seeded, because that is all a standard Anki
card tests. Recall, production and listening start unmeasured, which is honest:
your deck never tested them.

## After importing

```
python japanese-tutor/scripts/kb.py stats
```

Imported words immediately improve `/japanese-tutor:mine` coverage figures and
the level of generated reading passages, since both work off your known-word
set.

## Licensing

Anki is AGPL-licensed and AnkiConnect is GPL. This bridge only speaks to them
over a local socket and reads a SQLite file - it vendors no code and imports no
Anki module, which keeps it at arm's length.

If you extend it: **do not `pip install anki`** and do not copy code out of
AnkiConnect. Both would pull copyleft obligations into this plugin. The HTTP and
read-only-file boundary is the defensible line.

## Troubleshooting

**"no such collation sequence: unicase"** - already handled; the bridge
registers a stand-in for Anki's custom collation. If you see it, your Python is
older than the script expects.

**Deck not found** - run `anki.py decks` for exact names. Subdecks use `::`.

**Nothing imported** - almost always means nothing in that deck is mature yet.
Check with `--dry-run`; `skipped_not_mature` tells you.

**Adding cards to Anki** requires Anki to be running, since the collection file
is only ever opened read-only.
