# AJATT - All Japanese All The Time (Khatzumoto) - offline mirror

Source: <https://alljapanesealltheti.me/> (successor domain for the original
`alljapaneseallthetime.com`, now defunct).

A full mirror of Khatzumoto's original *All Japanese All The Time* blog, written from the
mid-2000s onward and the historical root of the immersion-learning method this repo's AJATT guide
documents. The live site itself is a static HTTrack export of the original WordPress blog,
re-hosted on GitHub Pages under the successor domain - the WordPress path structure
(`wp-content/`, `wp-includes/`, `wp-json/`) and an "Added by HTTrack" comment in the page source
are artifacts of that original export, not of this mirror.

## Contents

271 files, 15 MB: roughly 163 individual posts and pages, plus the site's archive listings,
author/category/tag/series index pages, comment threads, RSS feeds, and the `images/` and
`wp-content/`/`wp-includes/` asset folders needed to render pages offline.

Two pages central to the site were not reachable by crawling alone (nothing on the site links to
them) and were fetched directly by their known URLs:

- `table-of-contents/` - redirects to the canonical Table of Contents at
  `all-japanese-all-the-time-ajatt-how-to-learn-japanese-on-your-own-having-fun-and-to-fluency/`.
- `the-best-well-least-crappy-of-ajatt/` - the "Best of AJATT" curated index.

Because the crawl otherwise only follows discoverable links, older unlinked/orphaned posts may
exist on the live site beyond what is captured here.

## What was excluded

WordPress comment-reply URL variants (the `replytocom` query parameter) were excluded - these are
the same page content behind a different pre-filled reply form, not distinct material.

## Licence and terms

**Copyright (C) 2006-2021 AJATT, All Rights Reserved**, per the site's own footer notice. The
content is freely readable on the live site but carries no open licence. This mirror is an offline
copy for personal study only and is not for redistribution.
