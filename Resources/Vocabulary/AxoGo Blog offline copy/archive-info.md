# AxoGo Blog (Japanese section) - offline mirror

Source: <https://axogo.app/en/japanese/blog/> (AxoGo, by Achoq Software Inc.)

A two-post blog attached to a commercial Japanese-learning app. Both posts present an in-house
quantitative analysis built on a proprietary "120 million sentence" corpus. The corpus itself and
the analysis methodology are not published and are not independently reproducible from anything on
the site.

- `japanese-full-homonyms` - "Is Japanese Full of Homonyms? A Quantitative Comparison" (2025-10-08):
  compares homonym/homophone density between Japanese and Spanish, measured in mora-equivalent
  units, reporting roughly a 7x higher reading-collision rate for Japanese, with a secondary
  discussion of how pitch accent would partially offset the count.
- `kanji-needed-understand` - "Beyond the Average: How Many Kanji and Vocabulary Do You Really Need
  to Understand Japanese?" (2025-10-03): argues that running-word frequency-coverage percentages
  overstate real comprehension, and reports its own full-sentence comprehension thresholds -
  75% comprehension at ~1,568 kanji / 3,986 words, 85% at ~1,926 kanji / 6,255 words, 95% at
  ~2,570 kanji / 13,157 words.

## Licence / terms status

No open licence is stated anywhere on the site. The footer carries a plain copyright notice
("(c) 2026 AxoGo by Achoq Software Inc. All rights reserved."). `robots.txt` does not exist on the
site (returns 404), and no other crawl restriction is published. This mirror is a personal
archival/reference copy, not a redistributable or citable dataset - the underlying corpus behind
the numbers is never published, so none of the reported figures can be independently verified.

## Caveat - marketing content, not research

Every page ends in a "GET STARTED FOR FREE" call to action and carries Google Analytics conversion
tracking (including a script that copies the current URL to the clipboard on click, purely for
attribution). This is content marketing for the AxoGo app, not an academic source. Its specific
numeric claims (corpus size, comprehension thresholds, homonym-density ratios) rest entirely on an
unpublished, unreviewed internal methodology and should be read as one company's marketing argument,
not as a citable figure - unlike the peer-reviewed thesis and paper sources already in
`Resources/Vocabulary/` (Matsushita's PhD thesis, Honda 2019). The comprehension-threshold numbers
in `kanji-needed-understand` also use a different metric (percentage of whole sentences fully
understood) than the running-word lexical-coverage figures already cited in the Vocabulary guide
(95%/98% coverage of running words), so the two sets of numbers answer different questions and
should not be read as directly comparable, consistent, or contradictory without accounting for that
difference.

## Contents

17 files, 333 KB total:

- 3 HTML pages: the blog index (`en/japanese/blog/index.html`) and the two posts above.
- 14 page-requisite files needed to render the pages offline: one CSS bundle, 8 web-font files
  (woff/woff2), 2 logo/icon PNGs, an app-store badge SVG and PNG, and one web manifest.

## Scope of the mirror

Captured with `wget --mirror --no-parent`, scoped to `https://axogo.app/en/japanese/blog/` and
restricted to the `axogo.app` domain. The site's other sections (about, forum, the paid platform/app,
careers, privacy policy, terms) were not crawled and are not part of this mirror.
