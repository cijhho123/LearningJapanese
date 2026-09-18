# Resources

This repository holds hundreds of catalogued resources across thirteen topics.
The tutor teaches **only** from ones you have switched on.

That restriction is the point. Teaching from everything is the same as teaching
from nothing: the tutor wanders, never builds continuity in any one guide, and
never knows where you got to.

## Three statuses

| Status | Meaning |
|---|---|
| `active` | The tutor teaches from this |
| `ignored` | Catalogued, deliberately not used |
| `unseen` | Catalogued, you haven't decided yet |

New entries always arrive as `unseen`, so nothing joins your study material
without you saying so.

## Using it

```
/japanese-tutor:resources                        the catalogue, by topic
/japanese-tutor:resources use Tae Kim            switch on
/japanese-tutor:resources ignore KanjiDamage     switch off
/japanese-tutor:resources scan                   pick up newly added guides
/japanese-tutor:resources add <https url>        download something new
```

Or directly:

```
python japanese-tutor/scripts/kb.py resources --summary
python japanese-tutor/scripts/kb.py resources --topic Grammar
python japanese-tutor/scripts/kb.py resource-status "<path or title>" active
python japanese-tutor/scripts/kb.py resource-status "<path>" ignored --priority 5
```

Matching accepts a unique title fragment as well as a full path, since the paths
are long. It refuses rather than guessing when a fragment matches several
things.

Higher `priority` sorts first when the tutor picks material.

## How the catalogue is built

`scan_resources()` walks `Resources/`, registering each topic folder, its
immediate contents, and anything linked from that topic's `readme.md`.

It is **additive and idempotent**. Re-running after new guides are written picks
up the new entries and leaves your existing choices, priorities and positions
alone. Run it whenever the topic guides change:

```
python japanese-tutor/scripts/kb.py scan-resources
```

It reports how many entries are new so you can decide on them.

## Tracking where you are

The tutor records your position in a resource as it goes, so "continue where I
left off" works across months:

```
python japanese-tutor/scripts/kb.py resource-position "Yokubi" "Lesson 12"
```

Shown in `brief`, so every skill knows.

## Adding something new

### Already on disk

```
python japanese-tutor/scripts/kb.py resource-add "Resources/Grammar/Thing" "Title" --topic Grammar
```

### From the web

```
python japanese-tutor/scripts/fetch_resource.py <https-url> --topic Grammar --title "Name"
```

Saves it under `Resources/<topic>/<name>/`, writes a `SOURCE.txt` recording
where it came from, and registers it as `active`.

**HTTPS only, with certificate verification on, re-checked across every
redirect.** A plain-HTTP link is refused rather than silently downgraded - if a
site has no HTTPS version, save the page by hand and register it with
`resource-add`. Downloads are capped at 200 MB.

Use `--dry-run` to see where something would land before fetching it.

### It does not edit the topic guides

`Resources/*/readme.md` are maintained separately from this plugin. The tutor
reads them, never writes them. After adding something it will tell you, and
suggest mentioning it in the guide yourself.

## Choosing a starting set

Start with about **three or four**, not thirty: roughly one grammar guide, one
kanji source, one vocabulary source, matched to your method.

Everything else stays catalogued and one command away. Switching everything on
at the start reliably results in opening none of it.

## Why the tutor never searches the whole repo

The tree holds tens of thousands of files, including scraped site mirrors with
thousands of images. An unbounded search would hang or flood the context window.

So every search is scoped to active resource paths, and anything broader is
delegated to the `resource-scout` agent, which works in its own context and
returns short quoted excerpts rather than file dumps.

If you ask about something no active resource covers, the tutor will say so
rather than quietly answering from memory. That is deliberate: the most common
way an AI tutor teaches you something wrong is by producing a plausible reading
it was never given.
