# Anki - install and setup guide

This page is the practical install-and-verify checklist: where to get Anki, platform
notes, first-run setup, and how to confirm it is configured correctly. For *why* any of
this matters - how spaced repetition works, FSRS vs the legacy SM-2 scheduler, the full
deck-options table tuned for Japanese, add-on recommendations, sync/backup discipline,
and backlog recovery - see [the Anki chapter](../readme.md#anki) in this folder's main
guide. That chapter is the canonical reference; this page does not repeat its reasoning.

## Why this folder does not ship an installer

This folder deliberately holds no Anki installer binary. A pinned installer in a git
repo is worse than a link in every respect:

- Anki releases frequently, and updates carry real security and scheduler fixes.
- A mirrored binary goes stale within weeks and silently encourages installing an old,
  unpatched build.
- Any single binary only ever covers one platform, while this folder is used by people on
  Windows, macOS, Linux, iOS and Android alike.

Always take the current build straight from the source below. It is one click away.

## Where to get Anki

| Source | URL | What it is for |
| :--- | :--- | :--- |
| Official site | <https://apps.ankiweb.net/> | The download hub for desktop Anki (Windows, macOS, Linux), with links to AnkiMobile and AnkiDroid at the bottom of the page. Always has the current release. |
| GitHub releases | <https://github.com/ankitects/anki/releases> | Same builds as above, plus changelogs and older versions if you ever need to roll back. |
| AnkiWeb | <https://ankiweb.net/> | Free account for sync and off-device backup of your collection. Not a download - a service. |
| AnkiMobile | <https://apps.apple.com/us/app/ankimobile-flashcards/id373493387> | iOS/iPadOS app, one-time paid purchase ($24.99 at time of writing). Made by the same developer as desktop Anki; sales fund development of both. |
| AnkiDroid | <https://play.google.com/store/apps/details?id=com.ichi2.anki> (also on F-Droid: <https://f-droid.org/packages/com.ichi2.anki/>) | Android app, free. **Not made by the same developer as Anki desktop** - it is built and maintained by an independent volunteer community ([github.com/ankidroid/Anki-Android](https://github.com/ankidroid/Anki-Android)), based on Anki but a separate codebase. |

## Platform notes

- **Windows.** Current releases ship a standard `.msi` installer, one for x64 (Windows
  10+) and one for ARM64 (Windows 11). If you encounter references elsewhere to a
  separate self-updating "launcher" `.exe`, that was specific to Anki versions 25.07
  through 25.09.4 - current releases do not need it; just run the `.msi` for your
  architecture.
- **macOS.** Separate `.dmg` builds for Apple Silicon and Intel - pick the one matching
  your Mac, not just "any Mac build". Requires a reasonably recent macOS version; check
  the download page for the current minimum.
- **Linux.** The official download is a `.tar.zst` archive (x86_64 or aarch64) that runs
  without installation via its own bundled Python environment. **Prefer this over your
  distro's package.** Distro-packaged Anki (apt, dnf, AUR, etc.) is frequently several
  major versions behind, which matters more than usual here because FSRS and its
  optimizer have improved significantly release over release.

## First-run setup checklist

1. **Create or log into an AnkiWeb account**, then enable sync (`Tools > Preferences >
   Syncing` on desktop, or press `Y`). This is what makes your collection available on
   other devices and gives you an off-device copy if your machine dies.
2. **Enable FSRS.** Go to any deck's Options, scroll to the **FSRS** section near the
   bottom, and turn it on. This is global - you cannot enable it for some presets and not
   others. Recent Anki versions turn it on by default for new collections; older or
   migrated collections may still have it off.
3. **Set a deliberate new-cards/day limit and a high (effectively uncapped) reviews/day
   limit.** See [the deck-options table](../readme.md#anki) in the main chapter for exact
   numbers and the reasoning - the short version is: throttle new cards, never reviews.
4. **Set your desired retention.** Default is 90% and that is a reasonable starting
   point; do not raise it just because a higher number looks better.
5. **Install the Japanese-specific add-ons** you intend to use (AnkiConnect, AJT
   Japanese, etc.) - the full table with codes and verdicts is in the main chapter's
   add-on section.
6. **Confirm backups are being written.** `Tools > Preferences > Backups` on desktop.
   Anki takes these automatically, but they live on the same machine - see the main
   chapter for why you still need an off-machine `.colpkg` export on top of this.

## Recommended settings, in short

The full table (new cards/day, review limits, learning steps, leech thresholds, sibling
burying, FSRS retention, and why each value is set that way) lives in
[the Anki chapter's deck-options section](../readme.md#anki) - it is tuned specifically
for a Japanese-learning workload and is not repeated here. In one line: **FSRS on,
desired retention 0.9, new cards/day at a number you can sustain on a bad week, maximum
reviews/day uncapped.**

## Verifying your install

- **Check the version.** `Help > About` (desktop). If it looks old, redownload from
  [apps.ankiweb.net](https://apps.ankiweb.net/) rather than trusting an auto-updater to
  have caught it.
- **Confirm FSRS is actually active.** Open any deck's `Options`, scroll to the **FSRS**
  section, and check the toggle - not just that you clicked it once, but that it is still
  on. Click **Optimize** once you have a few hundred reviews; if you see "The FSRS
  parameters currently appear to be optimal", scheduling is working as intended.
- **Confirm scheduling behaviour.** `Stats > True Retention Table` should start showing
  numbers once you have mature cards (interval >= 21 days). If that table stays empty
  indefinitely or retention looks wildly off from your target, FSRS is not fitting
  correctly - re-check that FSRS is enabled and that you have enough review history.
- **Confirm sync actually round-trips.** Create a throwaway test card on one device,
  sync, and check it appears on another device (or on AnkiWeb's card browser). Delete the
  test card afterward.

## Local material in this folder and nearby

- [Anki Manual (docs.ankiweb.net, CC BY-SA 4.0).html](<./Anki Manual (docs.ankiweb.net, CC BY-SA 4.0).html>) - the complete official manual, offline. The authoritative reference for anything not covered here or in the main chapter.
- [`../FSRS research and benchmark (open-spaced-repetition)/`](<../FSRS research and benchmark (open-spaced-repetition)>) - the FSRS algorithm's own documentation (CC0) and the public SRS Benchmark comparing FSRS against SM-2 and other schedulers over ~727 million real Anki reviews. Start with [ABC of FSRS.md](<../FSRS research and benchmark (open-spaced-repetition)/ABC of FSRS.md>) for a beginner-friendly explanation, or [SRS Benchmark Results (README).md](<../FSRS research and benchmark (open-spaced-repetition)/SRS Benchmark Results (README).md>) for the evidence itself.
- [`../Spaced repetition and memory research (open access papers)/`](<../Spaced repetition and memory research (open access papers)>) - the underlying cognitive-psychology papers on the spacing effect and the testing effect, i.e. why spaced repetition works at all, independent of which algorithm does the scheduling.
- [the Anki chapter](../readme.md#anki) - the canonical guide this page defers to for everything conceptual.
