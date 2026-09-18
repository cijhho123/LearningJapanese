---
name: resources
description: Manages which Japanese learning resources the tutor teaches from - browse the catalogue, switch resources on or off, set priorities, rescan the repo for newly added guides, and download a new resource into the repo. Use when the user runs /japanese-tutor:resources, asks what materials are available or in use, wants to change or add study materials. Also use when the tutor needs to find which local resource covers a topic.
argument-hint: [list | scan | use <name> | ignore <name> | add <https-url>]
allowed-tools: Bash(python *), Bash(python3 *), Read, Glob, Grep
---

# Resources

!`python "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" resources --summary 2>&1 || python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kb.py" resources --summary 2>&1 || echo "(not set up - run scripts/setup.py)"`

Request: **$ARGUMENTS**

---

**Before anything else, read `${CLAUDE_PLUGIN_ROOT}/references/teaching-rules.md`.** Those rules bind every turn of this skill - especially rule 1, be brief.


## What this is for

This repo holds hundreds of catalogued resources. Teaching from all of them is
the same as teaching from none of them, so the tutor only ever draws material
from ones with status `active`.

Three statuses: `active` (teach from this), `ignored` (don't offer it),
`unseen` (catalogued, never decided on).

## Operations

### list
Show the table above. If they want detail on one topic:
`kb.py resources --topic Grammar`

Group by topic, lead with what's active. **Don't print 200 rows.** If a topic has
more than about a dozen entries, summarise and offer to show the rest.

### scan
`kb.py scan-resources`

Rebuilds the catalogue from `Resources/*/readme.md` and the folder tree. It is
additive - existing choices, priorities and positions survive, and anything new
arrives as `unseen` so it surfaces for a decision rather than joining silently.

Run this when the topic guides have been updated. Report new entries and ask
whether to switch any on.

### use / ignore
```
kb.py resource-status "<path or unique title fragment>" active
kb.py resource-status "<path or unique title fragment>" ignored --priority 10
```
Matching falls back to a title fragment when the path is long, but it must be
unique - the command says so if it isn't.

Higher priority sorts first when the tutor picks material.

### add
For something already on disk:
`kb.py resource-add "<repo-relative path>" "<title>" --topic <Topic>`

To download something new - **only when the user has asked for this specific
resource in this turn.** Never fetch on your own initiative, and never as a
side effect of looking for teaching material. Show them the URL and the target
topic, and wait for a yes:
```
python "${CLAUDE_PLUGIN_ROOT}/scripts/fetch_resource.py" <https-url> --topic <Topic> --title "<name>" --dry-run
python "${CLAUDE_PLUGIN_ROOT}/scripts/fetch_resource.py" <https-url> --topic <Topic> --title "<name>"
```

The fetcher is HTTPS-only with certificate verification on, including across
redirects, and caps downloads at 200 MB. If a site has no HTTPS version it will
refuse - tell the user to save the page by hand and register it with
`resource-add`, rather than trying to work around it.

**It does not edit any `Resources/*/readme.md`.** Those topic guides are
maintained separately. Say what was added and suggest they mention it there.

### Helping another skill find material

When a teaching skill needs the right resource for a topic:

1. `kb.py resources --status active --topic <Topic>`
2. Consult that topic's `Resources/<Topic>/readme.md` if it exists - those
   guides are opinionated about what each resource is good for. **Grep it, do
   not read it:** they run 40-270 KB. `grep -n "<keyword>" <path>` then
   `sed -n '<start>,<end>p'`.
3. Search **only within active resource paths**.

**Never glob or grep from the repo root.** It holds tens of thousands of files
and will flood the context. For anything broader than a couple of files,
delegate to the `resource-scout` agent.

## Recommending a starting set

When someone has nothing active, don't hand them a list of thirty. Recommend
about three or four - roughly one grammar guide, one kanji source, one
vocabulary source - matched to their method, and say in one line why each.

They can always add more. Starting with everything switched on means never
actually opening any of it.
