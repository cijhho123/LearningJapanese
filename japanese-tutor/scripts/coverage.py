"""Measure how much of a Japanese text the learner already knows.

Answers the two questions that make sentence mining work:
  * what percentage of this text do I know?
  * which sentences contain exactly one unknown thing (i+1)?

Segmentation uses SudachiPy if it happens to be installed, and otherwise falls
back to longest-match against the learner's own known-word set. The fallback is
crude on unknown spans but exact on known ones, which is the half that actually
matters here - we only need to identify what is *not* known.

Usage:
    python coverage.py --file path/to/text.txt
    python coverage.py --text "<japanese text>"
    echo "<text>" | python coverage.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb  # noqa: E402

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):  # pragma: no cover
        pass

# Character-class ranges, written as escapes to keep this file ASCII.
HIRA_LO, HIRA_HI = 0x3040, 0x309F
KATA_LO, KATA_HI = 0x30A0, 0x30FF
KANJI_LO, KANJI_HI = 0x4E00, 0x9FFF
EXT_A_LO, EXT_A_HI = 0x3400, 0x4DBF        # CJK Extension A
HALFWIDTH_LO, HALFWIDTH_HI = 0xFF66, 0xFF9F    # half-width katakana
MAX_KANJI_RUN = 4          # longer true compounds are rare; see _tokenize_fallback
ITERATION_MARK = 0x3005                       # the "same again" mark
SENTENCE_ENDERS = (0x3002, 0xFF01, 0xFF1F)    # ideographic full stop, fullwidth ! ?

HIRAGANA = "%s-%s" % (chr(HIRA_LO), chr(HIRA_HI))
KATAKANA = "%s-%s" % (chr(KATA_LO), chr(KATA_HI))
KANJI = "%s-%s%s" % (chr(KANJI_LO), chr(KANJI_HI), chr(ITERATION_MARK))
SENTENCE_END = "".join(chr(c) for c in SENTENCE_ENDERS)

HALFWIDTH = "%s-%s" % (chr(HALFWIDTH_LO), chr(HALFWIDTH_HI))
EXT_A = "%s-%s" % (chr(EXT_A_LO), chr(EXT_A_HI))

_RUN = re.compile("[%s%s%s%s%s]+" % (HIRAGANA, KATAKANA, KANJI, EXT_A, HALFWIDTH))
_SENTENCE = re.compile("[^%s\n]+[%s]?" % (SENTENCE_END, SENTENCE_END))

# Particles and inflection tails are grammar, not vocabulary, so they are not
# reported as unknown words. Kept in a data file rather than inline so the list
# is editable and the source stays ASCII.
_NOISE_FILE = Path(__file__).resolve().parent / "data" / "grammar-noise.txt"


def _load_grammar_noise():
    try:
        lines = _NOISE_FILE.read_text(encoding="utf-8").splitlines()
    except OSError:
        return set()
    return {ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")}


GRAMMAR_NOISE = _load_grammar_noise()

# Splitting and trimming use the narrower particle list only. Using the full
# noise list here eats verb and adjective stems, because inflection tails are
# not word boundaries.
_PARTICLE_FILE = Path(__file__).resolve().parent / "data" / "particles.txt"


def _load_particles():
    try:
        lines = _PARTICLE_FILE.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    words = {ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")}
    return sorted(words, key=len, reverse=True)


PARTICLES = _load_particles()
_NOISE_BY_LENGTH = sorted(GRAMMAR_NOISE, key=len, reverse=True)


def _try_sudachi():
    try:
        from sudachipy import dictionary, tokenizer  # type: ignore
        return dictionary.Dictionary().create(), tokenizer.Tokenizer.SplitMode.C
    except Exception:       # not installed, or no dictionary - both are fine
        return None, None


def _tokenize_sudachi(text, tok, mode):
    out = []
    for m in tok.tokenize(text, mode):
        surface = m.surface()
        if _RUN.fullmatch(surface):
            out.append((surface, m.dictionary_form()))
    return out


def _trim_noise(chunk):
    """Strip particles and inflection tails off an unknown chunk.

    Without a morphological analyser we cannot segment properly, so a chunk can
    come out as particle + word + inflection. Shaving the known grammar off both
    ends gets close enough to a dictionary form to be a useful mining candidate.
    """
    changed = True
    while changed and chunk:
        changed = False
        for word in PARTICLES:
            if len(chunk) > len(word) and chunk.startswith(word):
                chunk, changed = chunk[len(word):], True
                break
    return chunk


def _tokenize_fallback(text, known):
    """Longest-match known words; whatever is left over is a candidate."""
    by_length = sorted((w for w in known if w), key=len, reverse=True)
    tokens = []
    for run in _RUN.findall(text):
        i = 0
        while i < len(run):
            hit = next((w for w in by_length if run.startswith(w, i)), None)
            if hit:
                tokens.append((hit, hit))
                i += len(hit)
                continue
            # Grammar sitting between words - emit it as its own token so it
            # does not get glued onto the next unknown chunk. Longest first, so
            # copulas like desu are not sliced apart by the de particle inside
            # them.
            grammar = next((w for w in _NOISE_BY_LENGTH if run.startswith(w, i)), None)
            if grammar:
                tokens.append((grammar, grammar))
                i += len(grammar)
                continue
            # Unknown span: the kanji cluster plus its okurigana tail, which
            # approximates a word boundary well enough to mine from.
            j = i
            # Cap the run: an unbroken string of kanji with no known-word hit
            # would otherwise become one enormous "word" and make the coverage
            # percentage meaningless.
            while (j < len(run) and run[j] in _kanji_set
                   and (j - i) < MAX_KANJI_RUN):
                j += 1
            if j == i:
                j = i + 1
                while (j < len(run) and run[j] not in _kanji_set
                       and not any(run.startswith(w, j) for w in PARTICLES)):
                    j += 1
            else:
                while (j < len(run) and run[j] in _kana_set and (j - i) < 8
                       and not any(run.startswith(w, j) for w in PARTICLES)):
                    j += 1
            chunk = run[i:j]
            trimmed = _trim_noise(chunk)
            # Re-check: trimming may have revealed a word we do know.
            tokens.append((chunk, trimmed if trimmed else chunk))
            i = j
    return tokens


_kanji_set = ({chr(c) for c in range(KANJI_LO, KANJI_HI + 1)}
              | {chr(c) for c in range(EXT_A_LO, EXT_A_HI + 1)}
              | {chr(ITERATION_MARK)})
_kana_set = ({chr(c) for c in range(HIRA_LO, KATA_HI + 1)}
             | {chr(c) for c in range(HALFWIDTH_LO, HALFWIDTH_HI + 1)})


def analyse(text, known=None):
    known = known if known is not None else kb.known_words()
    tok, mode = _try_sudachi()
    engine = "sudachipy" if tok else "known-word longest match"

    sentences = []
    all_tokens = 0
    known_tokens = 0
    unknown_counts = {}

    for raw in _SENTENCE.findall(text):
        sentence = raw.strip()
        if not sentence or not _RUN.search(sentence):
            continue
        tokens = (_tokenize_sudachi(sentence, tok, mode) if tok
                  else _tokenize_fallback(sentence, known))
        unknown = []
        for surface, lemma in tokens:
            all_tokens += 1
            if lemma in known or surface in known:
                known_tokens += 1
            elif surface in GRAMMAR_NOISE or lemma in GRAMMAR_NOISE:
                known_tokens += 1        # grammar, not vocabulary
            else:
                unknown.append(lemma)
                unknown_counts[lemma] = unknown_counts.get(lemma, 0) + 1
        sentences.append({
            "sentence": sentence,
            "tokens": len(tokens),
            "unknown": unknown,
            "unknown_count": len(unknown),
        })

    if not all_tokens:
        return {
            "engine": engine,
            "known_words_in_profile": len(known),
            "sentences": 0, "tokens": 0,
            "coverage": None, "coverage_pct": None,
            "verdict": "no Japanese text found",
            "unknown_types": 0, "top_unknown": [],
            "i_plus_1": [], "i_plus_2": [], "all_sentences": [],
        }
    coverage = known_tokens / all_tokens
    one_t = [s for s in sentences if s["unknown_count"] == 1]
    two_t = [s for s in sentences if s["unknown_count"] == 2]

    return {
        "engine": engine,
        "known_words_in_profile": len(known),
        "sentences": len(sentences),
        "tokens": all_tokens,
        "coverage": round(coverage, 4),
        "coverage_pct": round(coverage * 100, 1),
        "verdict": _verdict(coverage),
        "unknown_types": len(unknown_counts),
        "top_unknown": sorted(unknown_counts.items(), key=lambda kv: -kv[1])[:30],
        "i_plus_1": one_t[:25],
        "i_plus_2": two_t[:15],
        "all_sentences": sentences,
    }


def _verdict(coverage):
    # There is no sharp comprehension threshold - these are conventions, not
    # cliffs - but they are useful conventions for choosing material.
    if coverage >= 0.98:
        return "comfortable - you can read this unassisted"
    if coverage >= 0.95:
        return "workable - the usual target for extensive reading"
    if coverage >= 0.90:
        return "hard - usable for intensive study, tiring for volume"
    if coverage >= 0.80:
        return "too hard for reading; fine as a source of mining targets"
    return "far too hard - decoding, not reading"


def main(argv=None):
    p = argparse.ArgumentParser(prog="coverage.py")
    p.add_argument("--file")
    p.add_argument("--text")
    p.add_argument("--full", action="store_true",
                   help="include every sentence, not just the summary")
    a = p.parse_args(argv)

    if a.text:
        text = a.text
    elif a.file:
        path = Path(a.file)
        if not path.exists():
            print(json.dumps({"error": "no such file: %s" % a.file}))
            return 1
        text = path.read_text(encoding="utf-8", errors="replace")
    else:
        text = sys.stdin.read()

    if not text.strip():
        print(json.dumps({"error": "no text given"}))
        return 1

    result = analyse(text)
    if not a.full:
        result.pop("all_sentences", None)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
