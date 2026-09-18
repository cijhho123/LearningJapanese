-- Japanese Tutor knowledge base.
-- Every table is created IF NOT EXISTS so init is idempotent.

PRAGMA foreign_keys = ON;

-- Internal bookkeeping (schema_version, created timestamp).
CREATE TABLE IF NOT EXISTS meta (
    key     TEXT PRIMARY KEY,
    value   TEXT
);

-- Settings the learner chose: active method, budgets, format preferences.
CREATE TABLE IF NOT EXISTS profile (
    key     TEXT PRIMARY KEY,
    value   TEXT NOT NULL,
    updated TEXT NOT NULL
);

-- A study session. Opened by a skill, closed when it wraps up.
CREATE TABLE IF NOT EXISTS sessions (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    started TEXT NOT NULL,
    ended   TEXT,
    method  TEXT,
    summary TEXT
);

-- Anything learnable. One row per distinct thing.
CREATE TABLE IF NOT EXISTS items (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    kind        TEXT NOT NULL,      -- vocab | kanji | grammar | phrase | counter
    key         TEXT NOT NULL,      -- the word / character / grammar-point id
    reading     TEXT,
    meaning     TEXT,
    extra       TEXT,               -- JSON blob: pos, jlpt, components, examples, mnemonic...
    source      TEXT,               -- where it came from (resource path, "mined:<title>", "anki")
    first_seen  TEXT NOT NULL,
    UNIQUE (kind, key)
);

-- FSRS state, one row per item PER DIRECTION.
-- Separate directions are what let us see a recognition/production gap.
CREATE TABLE IF NOT EXISTS cards (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id     INTEGER NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    direction   TEXT NOT NULL,      -- recognition | recall | reading | listening | production
    stability   REAL,
    difficulty  REAL,
    due         TEXT,
    last_review TEXT,
    reps        INTEGER NOT NULL DEFAULT 0,
    lapses      INTEGER NOT NULL DEFAULT 0,
    state       TEXT NOT NULL DEFAULT 'new',   -- new | learning | review | relearning
    suspended   INTEGER NOT NULL DEFAULT 0,
    UNIQUE (item_id, direction)
);

-- Append-only log of every answer. Never summarised away: this is the
-- evidence base for scheduling, weak-point detection and level estimation.
CREATE TABLE IF NOT EXISTS reviews (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id         INTEGER NOT NULL REFERENCES cards(id) ON DELETE CASCADE,
    ts              TEXT NOT NULL,
    rating          INTEGER NOT NULL,   -- 1 again | 2 hard | 3 good | 4 easy
    correct         INTEGER NOT NULL,
    given           TEXT,
    expected        TEXT,
    latency_ms      INTEGER,
    elapsed_days    REAL,
    stability_after REAL,
    session_id      INTEGER REFERENCES sessions(id) ON DELETE SET NULL
);

-- Classified mistakes. error_type comes from references/error-taxonomy.md.
CREATE TABLE IF NOT EXISTS errors (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    ts             TEXT NOT NULL,
    error_type     TEXT NOT NULL,
    item_id        INTEGER REFERENCES items(id) ON DELETE SET NULL,
    learner_output TEXT,
    correction     TEXT,
    context        TEXT,
    session_id     INTEGER REFERENCES sessions(id) ON DELETE SET NULL
);

-- Explicit pairs the learner confuses. Populated from wrong answers that
-- name another known item, plus structural signals (shared components etc).
CREATE TABLE IF NOT EXISTS confusions (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    a_id     INTEGER NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    b_id     INTEGER NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    reason   TEXT,               -- visual | reading | transitivity | semantic | observed
    hits     INTEGER NOT NULL DEFAULT 1,
    last_hit TEXT,
    UNIQUE (a_id, b_id)
);

-- The curated resource catalogue. The tutor only teaches from status='active'.
CREATE TABLE IF NOT EXISTS resources (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    path     TEXT NOT NULL UNIQUE,   -- repo-relative path, or an https:// URL
    title    TEXT NOT NULL,
    topic    TEXT,                   -- Grammar | Kanji | Vocabulary | ...
    kind     TEXT,                   -- guide | deck | book | site | video | audio | list | folder
    status   TEXT NOT NULL DEFAULT 'unseen',  -- active | ignored | unseen
    priority INTEGER NOT NULL DEFAULT 0,
    position TEXT,                   -- "Lesson 12", "kanji #143", free text
    notes    TEXT,
    added    TEXT NOT NULL,
    updated  TEXT
);

-- Optional study plans. Absent by default; the tutor is free-flowing unless asked.
CREATE TABLE IF NOT EXISTS plans (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    created      TEXT NOT NULL,
    goal         TEXT NOT NULL,
    horizon      TEXT,
    steps        TEXT NOT NULL,      -- JSON array of {title, detail, done}
    current_step INTEGER NOT NULL DEFAULT 0,
    active       INTEGER NOT NULL DEFAULT 1,
    notes        TEXT
);

CREATE INDEX IF NOT EXISTS idx_items_kind      ON items (kind);
CREATE INDEX IF NOT EXISTS idx_cards_due       ON cards (due) WHERE suspended = 0;
CREATE INDEX IF NOT EXISTS idx_cards_item      ON cards (item_id);
CREATE INDEX IF NOT EXISTS idx_reviews_card    ON reviews (card_id);
CREATE INDEX IF NOT EXISTS idx_reviews_ts      ON reviews (ts);
CREATE INDEX IF NOT EXISTS idx_errors_type     ON errors (error_type);
CREATE INDEX IF NOT EXISTS idx_errors_ts       ON errors (ts);
CREATE INDEX IF NOT EXISTS idx_resources_state ON resources (status);
