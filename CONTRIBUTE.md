# Contributing

Suggestions, corrections and new material are all welcome. This file explains what belongs here and
how to add it so the repo stays consistent.

The repo has three layers - the topic **guides**, the archived **resources** they index, and the
**tutor** plugin - and each one is contributed to differently.

---

## Suggesting a resource

The lowest-effort contribution, and a genuinely useful one. Add it to
[NEW_RESOURCES.md](NEW_RESOURCES.md) or open an issue. Say which topic it belongs to and why it is
worth having - "another grammar guide" is not a reason; "the only guide that covers X properly" is.

You do not have to archive it yourself.

## Adding a resource

1. **Put it in the right topic folder** under `Resources/<Topic>/`, in a sub-folder named after the
   resource. Site mirrors, books, decks and datasets all live alongside each other.
2. **Prefer the source over the rendering.** If a guide is published from a git repository, take the
   repository - it is smaller, diffable, and updatable. Mirror the built site as well only when it
   carries something the source does not, such as images referenced by path but not committed.
3. **Record it in that folder's `sources.md`**, one row per resource:
   `Resource | Source URL | Retrieved | License / status | Format | Why it is worth having`.
   The last column is prose, not a label - it should explain what this adds that the folder did not
   already have.
4. **Index it in that folder's `readme.md`**, so it appears in the guide rather than only existing
   on disk. A resource nobody can find from the guide may as well not be here.

If you are unsure how something can be archived, add it to
[NEW_RESOURCES.md](NEW_RESOURCES.md) with what you know and leave the rest for the maintainers.

## Writing or correcting a guide

The guides follow one house style, and it is the whole point of them:

- **Lay the options out fairly first, then recommend one and say why.** A guide that presents only
  the author's preference is a worse guide, even when the preference is right.
- **Give the honest case against your own recommendation.** Every approach here has real costs; a
  guide that hides them is not saving the reader anything.
- **Be concrete.** Hours, counts, checkpoints and "done when" conditions beat encouragement.
- **No unsourced numbers.** If you cite a study or a statistic, link it. If it is a rule of thumb,
  say that it is one.

Corrections are especially welcome on the Japanese itself. An example sentence that is wrong, or a
rule stated more confidently than it deserves, is the most damaging kind of error here - it gets
taught, confidently, and takes weeks to unlearn.

## Contributing to the tutor

[`japanese-tutor/`](japanese-tutor/README.md) is a Claude Code plugin. A few constraints keep it
installable by anyone:

- **Python standard library only.** No `pip install` for anything in the core path. Optional extras
  are fine if the feature degrades silently when they are absent.
- **Nothing personal gets committed.** `japanese-tutor/state/` is gitignored and stays that way.
- **Keep the skills short.** Instructions live in `references/`; a `SKILL.md` that grows past a few
  hundred lines should be pushing detail out into a reference file instead.

Before opening a PR, run `python japanese-tutor/scripts/setup.py --check` and confirm the plugin
still validates with `claude plugin validate .`.

## Branching and pull requests

`main` holds the released state. **`Staging` is the integration branch, and it is what pull requests
target** - nothing lands on `main` directly.

1. **Branch from `Staging`**, not from `main`, and name the branch for what it does:
   `add/grammar-dojg-deck`, `fix/kana-chart-typo`, `guide/listening-rewrite`.
2. **Keep a branch to one thing.** One resource, one guide, one correction. A branch that adds a
   deck and rewrites a guide is two reviews wearing one hat.
3. **Open the PR against `Staging`.** Say what you added and which `sources.md` and `readme.md` you
   updated. For a guide change, say which claim changed and what it is based on.
4. **`Staging` merges into `main` at release time**, together with the version bump and the
   changelog entry.

### Commit granularity for large additions

This matters more here than in a normal repository. Git uploads a whole push as one pack, and a pack
of several gigabytes will fail against GitHub - by timeout or a dropped connection - after
transferring the lot. If you are adding a large mirror or a set of books:

- **Split it across commits of a few hundred megabytes each**, by sub-folder, and push after each
  one. Interrupted work then resumes instead of restarting.
- **Never commit a file over 100 MB.** GitHub rejects it outright and the push fails. Split the
  archive, or leave it out and record it in [NEW_RESOURCES.md](NEW_RESOURCES.md) instead.
- **Push over SSH rather than HTTPS.** Large pushes over HTTPS fail far more readily.

## Versioning and the changelog

Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html), read for an archive
rather than a library: **MAJOR** when the layout breaks existing paths or links, **MINOR** when
material or a guide is added, **PATCH** for corrections that leave the structure alone.

Add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as part of your PR - describe
what a reader gains or loses, not which files moved. Renames and relocations belong there too; a
path that silently changes breaks other people's links and bookmarks. The version in
[README.md](README.md) and the `[Unreleased]` heading are updated when `Staging` merges to `main`,
so leave both alone in your PR.

## A note on size

The repository is large and getting larger. Before adding hundreds of megabytes, check it is not
already covered - `sources.md` in each folder lists everything - and say in your entry why the
material justifies its size. Full site mirrors are worth it when a site might disappear; a second
mirror of the same content is not.