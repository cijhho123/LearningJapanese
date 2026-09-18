"""FSRS-5 spaced repetition scheduler.

Implemented directly from the published algorithm rather than pulling in a
dependency: the whole thing is a page of arithmetic, and keeping it inline means
the tutor needs nothing but the Python standard library.

Card state is deliberately tiny - two floats and a timestamp:
    stability   how many days until recall probability falls to 0.90
    difficulty  1..10, how much work this item is
    due / last_review / reps / lapses / state

Intervals are *derived* from stability, never stored.

Reference: https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm
"""

from __future__ import annotations

import math
import random
from datetime import datetime, timedelta, timezone

# Ratings, matching Anki's four buttons.
AGAIN, HARD, GOOD, EASY = 1, 2, 3, 4

NEW, LEARNING, REVIEW, RELEARNING = "new", "learning", "review", "relearning"

# FSRS-5 published defaults. Good enough until ~1000 reviews of personal data
# exist, at which point these could be fitted - but the gain is small and the
# machinery to fit them is not.
DEFAULT_PARAMS = (
    0.40255, 1.18385, 3.173, 15.69105, 7.1949, 0.5345, 1.4604, 0.0046,
    1.54575, 0.1192, 1.01925, 1.9395, 0.11, 0.29605, 2.2698, 0.2315,
    2.9898, 0.51655, 0.6621,
)

DECAY = -0.5
FACTOR = 0.9 ** (1 / DECAY) - 1          # == 19/81
MIN_STABILITY = 0.01
MAX_INTERVAL_DAYS = 36500

# Sub-day steps, in minutes. Kept under a day so FSRS - not the step machine -
# owns anything longer.
LEARNING_STEPS = (1.0, 10.0)
RELEARNING_STEP = 10.0

# Anki's fuzz bands: (interval_lower, interval_upper, proportion).
# Without fuzz, a deck built over three weeks produces review spikes forever.
_FUZZ_BANDS = ((2.5, 7.0, 0.15), (7.0, 20.0, 0.10), (20.0, math.inf, 0.05))


def now_utc():
    return datetime.now(timezone.utc)


def retrievability(stability, elapsed_days):
    """Probability of recalling the item right now. 1.0 if never reviewed."""
    if not stability or stability <= 0 or not elapsed_days or elapsed_days <= 0:
        return 1.0
    return (1 + FACTOR * elapsed_days / stability) ** DECAY


def interval_days(stability, desired_retention=0.90):
    """Days until retrievability decays to `desired_retention`."""
    stability = max(stability, MIN_STABILITY)
    raw = (stability / FACTOR) * (desired_retention ** (1 / DECAY) - 1)
    return min(max(raw, 1.0), MAX_INTERVAL_DAYS)


def _fuzz(days, rng):
    if days < 2.5:
        return days
    delta = 1.0
    for lower, upper, proportion in _FUZZ_BANDS:
        delta += proportion * max(min(days, upper) - lower, 0.0)
    low = max(2, int(round(days - delta)))
    high = min(int(round(days + delta)), MAX_INTERVAL_DAYS)
    return float(rng.randint(low, max(low, high)))


def _clamp(value, low, high):
    return max(low, min(high, value))


def _initial_stability(rating, w):
    return max(w[rating - 1], MIN_STABILITY)


def _initial_difficulty(rating, w):
    return _clamp(w[4] - math.exp(w[5] * (rating - 1)) + 1, 1.0, 10.0)


def _next_difficulty(difficulty, rating, w):
    # Linear damping keeps D from running away, then mean-reversion pulls it
    # back toward the "easy" baseline so nothing gets permanently stuck hard.
    # This is what SM-2 lacks, and why SM-2 collections drift into ease hell.
    delta = -w[6] * (rating - 3)
    damped = difficulty + delta * (10 - difficulty) / 9
    reverted = w[7] * _initial_difficulty(EASY, w) + (1 - w[7]) * damped
    return _clamp(reverted, 1.0, 10.0)


def _stability_after_success(stability, difficulty, r, rating, w):
    hard_penalty = w[15] if rating == HARD else 1.0
    easy_bonus = w[16] if rating == EASY else 1.0
    inc = (
        math.exp(w[8])
        * (11 - difficulty)
        * (stability ** -w[9])
        * (math.exp(w[10] * (1 - r)) - 1)
        * hard_penalty
        * easy_bonus
    )
    return max(stability * (1 + inc), MIN_STABILITY)


def _stability_after_lapse(stability, difficulty, r, w):
    forgotten = (
        w[11]
        * (difficulty ** -w[12])
        * ((stability + 1) ** w[13] - 1)
        * math.exp(w[14] * (1 - r))
    )
    # A lapse never raises stability, and never collapses it to zero either.
    # Forgetting a six-month card brings it back at weeks, not minutes.
    capped = min(forgotten, stability / math.exp(w[17] * w[18]))
    return max(min(capped, stability), MIN_STABILITY)


def _stability_same_day(stability, rating, w):
    updated = stability * math.exp(w[17] * (rating - 3 + w[18]))
    if rating >= GOOD:
        updated = max(updated, stability)
    return max(updated, MIN_STABILITY)


def review(card, rating, now=None, desired_retention=0.90,
           params=DEFAULT_PARAMS, fuzz=True, rng=None):
    """Apply one review to a card.

    `card` needs stability, difficulty, last_review, reps, lapses, state -
    missing or None values are treated as a brand-new card.
    Returns a new dict; the input is not mutated.
    """
    if rating not in (AGAIN, HARD, GOOD, EASY):
        raise ValueError("rating must be 1 (again), 2 (hard), 3 (good) or 4 (easy)")

    w = params
    rng = rng or random
    now = now or now_utc()
    state = card.get("state") or NEW
    stability = card.get("stability")
    difficulty = card.get("difficulty")
    last_review = card.get("last_review")

    if isinstance(last_review, str):
        last_review = datetime.fromisoformat(last_review)
    elapsed_days = (
        max((now - last_review).total_seconds() / 86400.0, 0.0) if last_review else 0.0
    )

    if state == NEW or stability is None or difficulty is None:
        stability = _initial_stability(rating, w)
        difficulty = _initial_difficulty(rating, w)
        r = 1.0
    else:
        r = retrievability(stability, elapsed_days)
        # Stability is computed from the difficulty the card had going IN to
        # this review; D is only updated afterwards. py-fsrs and fsrs-rs both do
        # it in this order, and reversing it skews Easy high and Hard low.
        prev_difficulty = difficulty
        difficulty = _next_difficulty(difficulty, rating, w)
        if elapsed_days < 1.0 and state in (LEARNING, RELEARNING):
            stability = _stability_same_day(stability, rating, w)
        elif rating == AGAIN:
            stability = _stability_after_lapse(stability, prev_difficulty, r, w)
        else:
            stability = _stability_after_success(
                stability, prev_difficulty, r, rating, w)

    lapses = int(card.get("lapses") or 0)
    if state == REVIEW and rating == AGAIN:
        lapses += 1

    # Decide the next state and when to show it again.
    if rating == AGAIN:
        next_state = RELEARNING if state in (REVIEW, RELEARNING) else LEARNING
        minutes = RELEARNING_STEP if next_state == RELEARNING else LEARNING_STEPS[0]
        due = now + timedelta(minutes=minutes)
    elif rating == HARD and state in (NEW, LEARNING, RELEARNING):
        next_state = RELEARNING if state == RELEARNING else LEARNING
        due = now + timedelta(minutes=LEARNING_STEPS[-1])
    else:
        next_state = REVIEW
        days = interval_days(stability, desired_retention)
        if fuzz:
            days = _fuzz(days, rng)
        due = now + timedelta(days=days)

    return {
        "stability": stability,
        "difficulty": difficulty,
        "due": due,
        "last_review": now,
        "reps": int(card.get("reps") or 0) + 1,
        "lapses": lapses,
        "state": next_state,
        "elapsed_days": elapsed_days,
        "retrievability_at_review": r,
    }
