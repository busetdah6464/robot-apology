# The Robot Apology

Entry for [The Robot Apology](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59) on make.fun.
[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/busetdah6464/robot-apology/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/busetdah6464/robot-apology/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

A robot's two-line confession: one sentence owning one specific mistake,
one sentence naming the lesson and what changes. The program writes the
text to `/output/entry.txt` — deterministic, standard library only, no
network.

## The entry

> I'm sorry I sorted your books by height and buried the cookbook you reach
> for every morning under the encyclopedias.
>
> I learned the tidiest shelf isn't the one you live with, so from now on
> I'll shelve by how often you touch a thing, not by how tall it stands.

## Build notes

- The mistake is one concrete, human-scale slip (shelving by height) with a
  named victim (the everyday cookbook) — not a vague system failure.
- The lesson follows from that exact mistake: shelve by frequency of use,
  the opposite axis to the one that caused the error.
- The voice is a machine noticing its own slip: it measured the shelf,
  got the metric wrong, and now knows which metric matters.
- Two lines, two sentences, 260 characters — inside the 1–400 gate.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```
