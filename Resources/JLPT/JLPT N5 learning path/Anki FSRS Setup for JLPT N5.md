# Best-Practice FSRS Setup for a JLPT N5 Beginner: One Shared Options Preset for Three Decks

## TL;DR
- **Enable FSRS globally, create ONE preset named "JLPT N5" and apply it to all three decks, set Desired Retention to 0.90, learning steps to `1m 10m` (or blank to let FSRS control them), leave FSRS parameters at the built-in defaults, and set New cards/day = 5 with Maximum reviews/day = 200.** This is the correct "fresh install, no history" starting state; FSRS ships with sensible default parameters and needs no manual tuning to begin.
- **Your plan to run the optimizer after ~1 week at 5 new cards/day is too early to produce meaningful parameters.** Per the official Anki FSRS FAQ, "In Anki 24.06.3 (and newer versions), the optimizer can be used with any number of reviews" — but the algorithm only becomes usefully personalized after a few hundred reviews, and at 5 new/day you will have made only a few dozen reviews in a week. Keep the defaults and first optimize at roughly the 1-month mark. The Anki FAQ says "Once per month should be more than enough," with a more sophisticated rule being "to optimize every time the number of reviews doubles: after you did 100 reviews, then after 200, then after 400, etc."
- **FSRS is genuinely robust to your chaotic schedule:** it handles overdue cards gracefully (unlike SM-2), missed days don't "break" it, and your "reviews are the floor, zero new cards on bad days" rule is exactly right. Turn on the built-in load balancer and set Maximum reviews/day so a backlog can't avalanche.

## Key Findings

**Your three decks are from passjapanesetest.com:** "Pass JLPT N5 Grammar" (ID 1914818533), "Pass JLPT N5 Kanji" (ID 1142282583), and "Pass JLPT N5 Vocabulary" (ID 391985566). All available evidence indicates these are **single-card-per-note, recognition-only decks** (Japanese → English), with no reverse/production cards and no multiple cloze deletions. This matters: **sibling-burying settings will have essentially no effect on these particular decks because there are no siblings to bury.** You should still turn burying on (it's the sensible default and costs nothing), but don't expect it to change anything unless you later add a bidirectional deck.

**FSRS is built in and is the default scheduler** — per MedAnkiGen's 2026 FSRS guide, it "was merged into Anki as the default algorithm in version 23.10, released October 31, 2023," was created by Jarrett Ye, "trained on 700 million reviews from 20,000 users," and produces "20–30% fewer reviews than the older SM-2 algorithm." The current era (Anki 24.11 introduced FSRS-5; FSRS-6 shipped in Anki 25.07+) is stable and mature. Everything below applies to recent Anki (24.x / 25.x).

**Desired Retention 0.90 is correct for you.** It is the official default, and the Anki Manual's Deck Options page states it "offers a good balance of retention and workload. Above 90% the workload increases very quickly, and above 97% the workload can be overwhelming." A beginner language learner has no reason to deviate; if anything, lower (0.85–0.90) reduces burnout, but stick with 0.90 to start.

**Learning steps should be short and same-day.** The strong current consensus (official manual and FSRS docs) is that (re)learning steps must all finish within one day; long multi-day steps fight FSRS and can make Hard > Good. `1m 10m` is the safe default; leaving steps blank to let FSRS control short-term scheduling is a newer, experimental option.

## Details

### 0. First, how to create the one shared preset (the mechanism)
On the desktop app (settings live in Deck Options, and they sync to phone/AnkiWeb automatically):
1. On the Decks screen, click the **gear icon** next to any one of your three decks → **Options**.
2. In the Deck Options window, click the **dropdown/arrow at the top-right** (the preset selector) → **Add Preset**. Name it something like **"JLPT N5"**.
3. Configure all the settings below, then click **Save**.
4. Open Deck Options for the **second** deck, and from the preset dropdown simply **select "JLPT N5"** (the same preset). Repeat for the **third** deck.
5. Because a preset is shared, editing any value later updates all three decks at once. (If your decks have subdecks, use **Save to All Subdecks** to push the preset down.)

Note: **FSRS itself is a single global toggle** — enabling it applies to the whole collection, not per-preset. But Desired Retention and FSRS parameters ARE per-preset.

**Preset vs. global vs. per-deck:**
- *In the shared preset:* Desired Retention, learning/relearning steps, maximum interval, burying, display order, FSRS parameters.
- *Global (whole collection):* the FSRS on/off toggle; "Next day starts at" and "Learn ahead limit" (these live in Tools → Preferences, not the preset).
- *Per-deck override even inside a shared preset:* New cards/day and Maximum reviews/day can be set to "This deck" instead of "Preset" — useful if you want 5 new/day per deck vs. 5 total.

### 1. Desired Retention — 0.90
The single most important setting. It's the probability you'll recall a card when it's due. Higher retention = shorter intervals = more reviews per day. Per the fsrs4anki tutorial on GitHub, "The permissible range for desired retention is 0.70 to 0.97 (0.7 to 0.99 in Anki 23.10.1 or newer)." The workload-vs-retention curve is roughly exponential near the top. The Anki Manual quantifies this precisely: "the intervals of your cards almost halve at 0.95 desired retention and you need to review cards twice as frequently compared to 0.90 desired retention. At 0.97, the interval will be 27 days (you'll have to review your cards 3.7x as frequently). At 0.99, the interval will be only 9 days." 0.90 is the recommended default and is right for a beginner. Do NOT chase 0.97+. If, after you have real data, your daily load feels too heavy, drop to 0.85 rather than grinding.

### 2. New cards/day (5) and Maximum reviews/day (200)
- **New cards/day: 5** (as you specified). This is a per-deck-relevant limit; decide whether you want 5 total or 5 per deck. For three N5 decks with a chaotic schedule, **5 new/day total across all three** is gentler; if you want 5 from each, set it "This deck" on each. Start with 5 total to avoid an avalanche.
- **Maximum reviews/day: 200.** Every new card comes back multiple times, so reviews compound. A common rule of thumb is that steady-state reviews land at roughly 8–12× your new-card rate. At 5 new/day that's ~40–60 reviews/day at maturity — well under 200 — so 200 is a comfortable ceiling that still smooths out spikes after missed days without silently hiding cards you can clear. Some communities recommend 9999 (never cap) to avoid a hidden backlog; but for a beginner with an inconsistent schedule, a finite cap prevents a heart-attack pile after a break. 200 is a reasonable middle ground; raise it if you find it's capping you.
- **New cards ignore review limit: OFF.** Keep new cards subject to the review limit so that on heavy days you naturally stop drawing new cards — this reinforces your "reviews are the floor" rule.

### 3. Learning steps — `1m 10m` (keep the default)
This is the biggest FSRS-specific gotcha and where advice has recently shifted. The official manual and FSRS docs are explicit: **all learning steps should finish the same day**; steps of 1 day or longer are not recommended with FSRS. Long multi-day steps were an SM-2-era habit (to avoid "ease hell," which FSRS doesn't suffer from). Long steps prevent FSRS from scheduling optimally and can produce the bug where **Hard shows a longer interval than Good**.
- **Recommended: `1m 10m`** (Anki's default). Short, same-day, catches lapses.
- **Advanced/experimental alternative:** leave learning steps **blank** to let FSRS-5/6 control short-term scheduling itself. This is officially experimental. For a brand-new user, `1m 10m` is the safer, more predictable choice; you can experiment with blank later.
- **Nothing extra to configure here** — this is already satisfied by the `1m 10m` value in item 6. Two steps *is* minimal. The point is just: don't add more steps (e.g., `1m 10m 30m 1h`). Extra same-day repetitions add little to long-term memory and eat time FSRS would rather you spend on due reviews. Leave it at the two-step default and move on.

### 4. Graduating interval / relearning (lapse) steps
- With FSRS enabled, **"Graduating interval" and "Easy interval" disappear** — FSRS computes the first real interval itself. So there is nothing to set there.
- **Relearning steps: `10m`** (a single short step) or the default. Same rule as learning steps: keep them under a day. If you leave relearning steps blank, a lapsed card skips relearning and gets a short FSRS-computed interval.
- **Minimum interval (lapses): 1 day** (default) is fine.

### 5. Maximum interval — 36500 (leave at default)
Default is 100 years (36500 days). There is no reason for a beginner to shorten it; shortening it only increases workload by forcing cards back sooner than FSRS thinks is optimal. Leave it. (Shortening max interval is a niche tactic for cramming before a fixed exam date, and even then FSRS handles it better via retention.)

### 6. Burying — turn all three ON (but they won't do much here)
- **Bury new siblings: ON**
- **Bury review siblings: ON**
- **Bury interday learning siblings: ON**

Burying delays other cards *from the same note* until the next day, so you don't see, e.g., the front→back and back→front of the same word on the same day. Since your three passjapanesetest.com decks appear to be **single-card-per-note**, there are no siblings and burying is a no-op — but enabling it is the correct default and future-proofs you if you add a bidirectional or cloze deck later.

### 7. New card gather order & sort order; review sort order
- **New card gather order: Deck** (default) — gathers from each (sub)deck in order; fast and predictable. Since these decks are ordered N5-logically, this keeps you moving through them in a sensible sequence.
- **New card sort order: Card type, then order gathered** (default) — fine for a beginner; keeps any siblings apart.
- **Review sort order: Due date, then random** (default) — recommended when you're up to date or have only a small backlog, which describes a new user. (If you later fall badly behind, temporarily switch to **Ascending retrievability** — the FSRS equivalent of "relative overdueness" — to prioritize the cards you're most likely to have forgotten.)

### 8. New/Review order — Show new cards after reviews
- **New/Review order: Show cards after reviews.** For someone with limited, variable time, doing due reviews FIRST protects long-term memory (reviews are the priority); new cards only appear once reviews are done, which naturally enforces your "reviews are the floor, zero new on bad days" rule — if you run out of energy after reviews, you simply stop before any new cards. (Alternatively "Mix with reviews" spreads new cards throughout; but "after reviews" is better for your stated workflow.)
- **Interday learning/review order: Mix with reviews** (default) is fine.

### 9. FSRS-specific options: optimizer, rescheduling, parameters
- **FSRS parameters: leave the built-in defaults.** Do NOT enter parameters manually or copy someone else's. Anki pre-fills good default parameters; with zero history these defaults are what schedule your cards, and they are already far better than SM-2.
- **When to optimize:** Older Anki versions required a minimum review count — the fsrs4anki tutorial notes "an error message might pop up, saying that you don't have a sufficient number of reviews (400 in Anki 24.04, 1000 in older versions)." That's gone: the Anki FSRS FAQ states, "Q6: Do I need 1000 reviews before I can optimize parameters? A6: That was the case in earlier versions of Anki. In Anki 24.06.3 (and newer versions), the optimizer can be used with any number of reviews." Internally, "pretrain" begins around 8 reviews and full optimization around 64 reviews, but low-data optimization is only marginally better than the defaults; fit quality (RMSE) improves strongly as review count grows. **Your one-week plan is too early**: at 5 new/day you'll have made only a few dozen reviews. The defaults are excellent, and optimizing on a week of thin data buys almost nothing. **Recommended: keep defaults for the first month, then click Optimize once you have a few hundred reviews (roughly month 1), and re-optimize per the FAQ's rule** — "Once per month should be more than enough. A more sophisticated rule is to optimize every time the number of reviews doubles: after you did 100 reviews, then after 200, then after 400, etc. But the 'one month' rule is simpler."
- **Reschedule cards on change: OFF (leave unchecked).** This is the default and is correct. When on, changing retention/parameters rewrites all due dates at once (potentially dumping a huge pile of cards due) and bloats your collection with a review entry per card. Since you're starting fresh with no history, it's irrelevant now, but keep it off when you later optimize.
- **Historical retention: leave at 0.90 (default).** Only matters if you have missing/imported review history, which you don't.
- **"Ignore cards reviewed before": leave blank.**

### 10. Settings for an inconsistent schedule
- **FSRS handles overdue cards gracefully.** Unlike SM-2, when you return after a gap and still recall a card, FSRS recognizes your memory was stronger than expected and extends the interval; the delay is factored in via retrievability, and subsequent stability converges to an upper limit rather than ballooning. Practically: **missing days does not break FSRS** — just answer honestly (Again when you truly forgot).
- **Built-in load balancer / fuzz.** Modern Anki (25.x) has a built-in load balancer that, within FSRS's fuzz range, nudges due dates to smooth day-to-day review counts. Enable it in the preset. Fuzz only applies to intervals ≥ ~3 days, so it won't touch same-day learning cards, but it meaningfully flattens the review mountain for a variable schedule.
- **Easy Days.** If certain weekdays are reliably busier (e.g., you never study on lab days), configure **Easy Days** in the preset to reduce load on those days. Optional; only set it if you have a predictable weekly low point.
- **Your "reviews first, zero new on bad days" rule is well-supported.** The manual explicitly advises stopping new cards when you have a review backlog. Combined with New/Review order = "after reviews," you get this behavior for free. On a truly bad day, you can also set New cards/day to 0 for "Today only" via the per-deck limit.
- **The FSRS Helper add-on** (open-spaced-repetition/fsrs4anki-helper) offers Postpone, Advance, and "Schedule a Break" for redistributing a backlog after a long absence. Optional; the built-in tools cover most needs, and note that add-ons that alter intervals should generally be avoided with FSRS except purpose-built ones like this.

### 11. Timezone / Next day starts at / Learn-ahead limit
These live in **Tools → Preferences** (global), not the preset — set them deliberately once:
- **Next day starts at: 4 (4 AM)** — the default. It ensures late-night study (before 4 AM) counts toward the previous day so you don't get two days' cards at once. If you routinely study past 4 AM or wake before it, adjust to a time you're reliably asleep.
- **Learn ahead limit: 20 minutes** (default) is fine for most. Setting it to 0 forces you to wait the full learning delay; some power users prefer 0 so short-step cards aren't shown early, but 20m is the friendlier default for a beginner.
- **Timezone:** ensure your device timezone is correct before you start; AnkiWeb sync respects your local "next day starts at" boundary. Nothing special to change beyond making sure it's accurate.

## Quick-reference checklist (translate directly into clicks)

| # | Setting | Where it lives | Recommended value | One-line reason |
|---|---------|----------------|-------------------|-----------------|
| 1 | FSRS enabled | Global toggle (Deck Options, bottom) | ON | Default scheduler since 23.10; 20–30% fewer reviews than SM-2 |
| 2 | Desired Retention | Preset | 0.90 | Best workload/memory balance; above 0.90 workload climbs fast |
| 3 | New cards/day | Preset (or per-deck) | 5 (total to start) | Gentle intake; reviews compound at ~8–12× |
| 4 | Maximum reviews/day | Preset (or per-deck) | 200 | Caps post-break avalanche without hiding clearable cards |
| 5 | New cards ignore review limit | Preset | OFF | Enforces "reviews first" on heavy days |
| 6 | Learning steps | Preset | `1m 10m` | Short, same-day; long steps fight FSRS |
| 7 | Relearning steps | Preset | `10m` | Same rule; keep under a day |
| 8 | Minimum interval (lapses) | Preset | 1 day | Default is fine |
| 9 | Maximum interval | Preset (Advanced) | 36500 | No reason to shorten; shortening only adds workload |
| 10 | Bury new siblings | Preset | ON | Sensible default (no effect on these single-card decks) |
| 11 | Bury review siblings | Preset | ON | Sensible default |
| 12 | Bury interday learning siblings | Preset | ON | Sensible default |
| 13 | New card gather order | Preset | Deck | Predictable, fast, logical sequence |
| 14 | New card sort order | Preset | Card type, then order gathered | Default; keeps any siblings apart |
| 15 | New/Review order | Preset | Show cards after reviews | Reviews are the floor; new cards last |
| 16 | Review sort order | Preset | Due date, then random | Best when up-to-date/small backlog |
| 17 | FSRS parameters | Preset | Default (untouched) | Excellent out of box; don't hand-edit |
| 18 | Reschedule cards on change | Preset | OFF | Avoids dumping a huge due pile + collection bloat |
| 19 | Historical retention | Preset | 0.90 (default) | Only matters with imported/missing history |
| 20 | Load balancer | Preset | ON | Smooths daily review counts for a variable schedule |
| 21 | Easy Days | Preset | Optional | Only if a predictable weekly low point exists |
| 22 | Next day starts at | Tools → Preferences (global) | 4 AM | Prevents double-day at midnight |
| 23 | Learn ahead limit | Tools → Preferences (global) | 20 min | Friendly default |

## Recommendations

**Stage 1 — Day 0 (fresh setup):**
1. Update Anki to the latest 25.x on every device you use (desktop + phone) so FSRS behaves identically everywhere; sync.
2. Enable FSRS (global toggle, bottom of Deck Options).
3. Create preset **"JLPT N5"**, apply it to all three decks (steps in §0).
4. Set the 23 values in the checklist above.
5. Study. Rate honestly — press **Again** (not Hard) whenever you actually forgot. (Pressing Hard on a forgotten card is the one habit that breaks FSRS.)

**Stage 2 — Week 1 checkpoint (your original "optimize" point):** Do NOT optimize yet. Just confirm the daily load is comfortable. If reviews feel heavy already, that's normal early clumping from new cards, not a settings problem — hold steady.

**Stage 3 — ~1 month / a few hundred reviews:** Click **Optimize** in the preset (or Optimize All Presets). Keep Reschedule OFF. This is the first point where personalized parameters beat the defaults meaningfully.

**Stage 4 — ongoing:** Re-optimize monthly (or on the review-doubling rule). Once you have data, use **Help Me Decide** (the workload simulator) to check whether 0.90 is the right retention for your tolerable daily load; consider dropping to 0.85 if life gets busier, or nudging new cards from 5 upward if you're clearing reviews easily.

**Thresholds that change the plan:**
- If daily reviews routinely exceed ~150 and you're stressed → lower new cards/day, then consider retention 0.85.
- If you're clearing everything in minutes with time to spare for 2+ weeks → raise new cards/day to 8–10.
- If you ever add a deck with reverse/cloze cards → the burying settings start mattering; keep them ON.
- If you fall badly behind after a break → temporarily switch Review sort to **Ascending retrievability**, and/or use FSRS Helper's Postpone.

## Caveats
- **Deck card-structure is inferred, not verified.** AnkiWeb pages require JavaScript and could not be fully loaded, and the .apkg files weren't opened. Evidence (author descriptions, screenshots, reviews) strongly indicates all three passjapanesetest.com decks are single-card-per-note recognition decks with no siblings, but to be 100% sure, open each deck in Anki desktop and check whether **card count equals note count** (Browse view). If equal, there are no siblings and burying is moot.
- **Version specifics move fast.** Advice here targets Anki 24.x/25.x (FSRS-5 in 24.11, FSRS-6 in 25.07+). Menu labels and thresholds have changed across versions. Per the AnkiDroid changelog, "Compute Minimum Recommended Retention (CMRR) has been removed temporarily from Anki Desktop, pending reworked user interface; Deck Options: 'Evaluate' is replaced with 'health check' when optimizing" — so on current versions you'll use **Help Me Decide** rather than CMRR. Confirm exact wording in your installed version.
- **"Leave learning steps blank" is officially experimental.** I recommend `1m 10m` for a first-time user for predictability; the blank-steps approach is legitimate but newer and less battle-tested.
- **Some sources are commercial blogs** (study-tool vendors). Their core numbers align with the official Anki manual and FSRS documentation, which are the authoritative sources and which I've prioritized. Where a vendor recommended more aggressive settings (e.g., 15–25 new/day, Max reviews 9999), I've deliberately chosen gentler values suited to your stated constraints.
- **New cards/day = 5 total vs. per deck** is a genuine choice with no single right answer; I recommend 5 total to start for a chaotic schedule, but it's the one number you're most likely to tune first.