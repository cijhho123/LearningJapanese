# Setup

Written assuming you have not done this kind of thing before. It takes about
five minutes, plus ten for the guided setup afterwards.

## What you need

- **Python 3.9 or newer.** Check by opening a terminal and typing
  `python --version`. If that fails, install it from
  [python.org/downloads](https://www.python.org/downloads/) - on Windows, tick
  "Add Python to PATH" during installation.
- **Claude Code**, already installed and working.
- Nothing else. No `pip install`, no accounts, no services.

## Step 1 - run the setup script

Open a terminal in the repository folder and run:

```
python japanese-tutor/scripts/setup.py
```

You should see something like:

```
[ ok ] Python 3.11.9
[ ok ] Found Resources/ with 13 topics
[ ok ] Learner database ready
[ ok ] Memory folder ready
[ ok ] Added japanese-tutor/state/ to .gitignore
[ ok ] Catalogued 210 resources (210 new)
[ ok ] Anki not found - skipping
[ ok ] Plugin registered with Claude Code
```

It creates your database, catalogues what's in `Resources/`, makes sure your
personal data stays out of git, and registers the plugin.

**Anki is optional.** Whatever it says about Anki, including "not found", is
fine - the tutor has its own scheduler and needs nothing external.

If it says it could not register the plugin automatically, it prints the two
commands to run yourself. Either works.

## Step 2 - restart Claude Code

New plugins are picked up at startup. Close Claude Code and open it again in the
repository folder.

Type `/` and you should see the `japanese-tutor` commands listed. If you don't,
see Troubleshooting below.

## Step 3 - onboard

```
/japanese-tutor:onboard
```

This is the part that actually matters. The tutor walks you through:

- what you want to be able to do, and by when
- which teaching method suits you (it explains the tradeoffs)
- how much time you have, and how fast to introduce new material
- how you want to be taught - romaji or not, how bluntly to correct you
- **which resources to study from** - this repo has hundreds, and it will help
  you pick a small starting set
- a short level check, about fifteen questions

Questions come one at a time. You can stop partway and run it again later - it
picks up where you left off.

## Step 4 - study

```
/japanese-tutor:study
```

It tells you what's waiting and asks what you feel like. There is no routine to
keep up with and nothing to fall behind on.

---

## Troubleshooting

**The `/japanese-tutor:` commands don't appear.**
Restart Claude Code first - that fixes it most of the time. Still missing? Run:

```
claude plugin marketplace add .
claude plugin install japanese-tutor@learning-japanese
```

Or start Claude Code with the plugin loaded directly:

```
claude --plugin-dir ./japanese-tutor
```

**`python` is not recognised.**
Python isn't installed or isn't on your PATH. Reinstall from python.org with
"Add Python to PATH" ticked. On some systems the command is `py` instead.

**The tutor says it has nothing to teach from.**
No resources are switched on. Run `/japanese-tutor:resources` and pick a few, or
re-run `/japanese-tutor:onboard`.

**Checking everything is healthy:**

```
python japanese-tutor/scripts/setup.py --check
```

Reports what's set up and what isn't. Changes nothing.

**Starting completely over:**

```
python japanese-tutor/scripts/setup.py --reset
```

Deletes all progress, mistakes and remembered notes. It asks you to type
`delete` to confirm. There is no undo - the state is gitignored, so there's no
commit to recover from. Copy `japanese-tutor/state/` somewhere first if you're
unsure.

## Where your data lives

```
japanese-tutor/state/
  tutor.db        progress, items, mistakes, resource choices
  memory/         plain markdown notes about your goals and preferences
```

Both are excluded from git. Nothing is uploaded anywhere. To back up, copy the
folder. To move to a new machine, copy it across and run `setup.py` there.
