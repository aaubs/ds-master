# Group assignment · From a table to a defensible answer

**Module 1 · Session 02 follow-up · Master's in Business Data Science**

| | |
|---|---|
| **Work in** | Your assigned group |
| **Hand in** | One `.ipynb` notebook + one video (link in the notebook's first cell) |
| **Deadline** | Friday 18 September 2026, 23:59 |
| **Graded** | No |

## Why this assignment exists

In the session we practised a specific discipline: say what one row is, check the data before trusting it, protect a join, and report a number together with what it cannot support.

**This is not graded.** It exists because the discipline only becomes yours once you have used it on a question nobody has answered for you first. There are three questions; none of them is long to code. What takes the time is the decisions inside them.

Your videos are what we discuss in the next session, so make them the ones you would want to watch.

## The setting

Some tracks sit on a single playlist. Others travel: the same track turns up on several. A curation team wants to know whether travelling tracks are recognisably different.

You have two files. The starter notebook loads them for you; these are the direct links if you want to read them into your own notebook, or open them in a browser first.

- **`spotify_songs.csv`** — the same 2020 snapshot as Notebook 2.<br>
  `https://raw.githubusercontent.com/aaubs/ds-master/codex/m1-pandas-2026/data/M1_2026/spotify_songs.csv`
- **`subgenre_families.csv`** — a subgenre → family grouping, **constructed for this assignment**. It is not an official Spotify taxonomy and carries no authority. Treat it as you would any lookup table handed to you by another team: check its keys before you trust the join. It was not checked for you.<br>
  `https://raw.githubusercontent.com/aaubs/ds-master/codex/m1-pandas-2026/data/M1_2026/subgenre_families.csv`

Both are read straight from the URL by `pd.read_csv`, so nothing needs downloading:

```python
songs_raw = pd.read_csv("https://raw.githubusercontent.com/aaubs/ds-master/codex/m1-pandas-2026/data/M1_2026/spotify_songs.csv")
families_raw = pd.read_csv("https://raw.githubusercontent.com/aaubs/ds-master/codex/m1-pandas-2026/data/M1_2026/subgenre_families.csv")
```

Do not attach copies of the CSVs to your submission — load them from the URL or from `data/M1_2026/` so the notebook runs on someone else's machine.

---

## Question 1 · What is one row, and how far does each track travel?

State what one row of the raw file represents, and support it with output rather than assertion. Then build the working table your answer will rest on, and say what one of *its* rows is and why that fits the question.

For every track, compute how many playlists it appears on. There is more than one way to count this, and they do not all count the same thing. Report which one you used, and show the check that convinced you it counts what you think it counts.

Before you go on, audit the fields your answer depends on: what is missing, and what precision the release dates actually carry. Derive a release year you can defend — Question 3 needs it — and be explicit about what you would be inventing if you parsed every date to a full day. Where the right decision is to leave something alone, say so; a field you never use needs no repair.

## Question 2 · Attach the family label

Merge the family lookup onto your working table.

Predict the row count before you merge and write the prediction down. Merge with `validate=` and `indicator=`. Compare.

If the merge does not behave as you predicted, **that is the question, not an obstacle to it.** Diagnose what is wrong with the keys, decide what to do about each problem you find, and record what each decision costs you. Report how many rows end up with no family label and what you did with them.

## Question 3 · Do travelling tracks differ?

Compare travelling tracks with tracks that appear on one playlist, on at least two audio features and on `track_popularity`. Report counts next to every mean.

"Travelling" is not defined for you. Choosing the cut-off is part of the work — and so is showing what happens at three or more cut-offs. Then ask whether whatever you found holds inside every family, and be explicit about which families are too small to carry the comparison. The families are a grouping someone made up; say what a better grouping would have been if you can think of one.

Before you write it up, check whether your two groups differ in **release year**, and say what that does to your reading of the popularity result. `track_popularity` is one number, measured once, in 2020.

Finish with one chart that supports your claim, reshaping the data as needed, and 250–400 words: what you found, what it rests on, and at least two things this data cannot tell the curation team.

---

## The video

Once the notebook is done, record your group presenting it. A screen recording of the notebook with your voices over it is enough — no slides, no editing, no production.

- 8 minutes, maximum 10.
- **Everyone in the group speaks.** The simplest split is one decision each: what you chose, what you rejected, and why.
- Have your own code on screen while you talk about it.
- Do not read the notebook out top to bottom. We have the notebook. Tell us what you decided and where you were unsure.

A rough single take with a real disagreement in it is worth more than a polished one that skips the interesting part.

## Submission checklist

- [ ] One `.ipynb`, named `M1_assignment_<group>.ipynb`
- [ ] First cell: group number, member names, and the video link
- [ ] **Restart & Run All produces the notebook you are submitting**, from a fresh kernel, with no manual steps
- [ ] Data loaded from `data/M1_2026/` or the URLs above — do not attach copies of the CSVs
- [ ] All three questions present, in order
- [ ] A short decision log: one line per question saying what you decided and what it cost you
- [ ] Video is reachable by someone who is not in your group

## What we will be looking at

No marks, but we do read these, and this is what we will pick up on in feedback and in class:

- Whether the row meaning is **stated and supported by output**, not asserted.
- Whether the reach computation was **checked** rather than assumed.
- Whether the audit decisions are deliberate — including the decisions to leave something alone — and whether the release year rests on what the dates actually record.
- On the merge: a **prediction written down first**, validation, a diagnosis of what the keys actually do, and each decision stated with its cost.
- **Counts next to means**, sensitivity actually shown, small groups flagged rather than quietly averaged.
- Language that does not slide into cause and effect.
- Whether **Restart & Run All** works.

We are not looking at chart styling, notebook length, how many pandas methods you used, or whether your answer matches ours. A well-defended "the difference is too small to act on" is a better answer than an overclaimed effect.

## Tools and honesty

Use whatever tools help you, AI assistants included. Two conditions, and they are the whole policy:

1. Put a short note at the end of your notebook saying where you used AI assistance and for what.
2. Be able to explain every line you submit. You are about to present it on video, which is the practical version of that condition.

Code you cannot explain is not your answer, whatever produced it — and it is the code that will fail you in the exam, where nothing is generated for you.

## If you get stuck

The two session notebooks contain every technique these questions need. Notebook 2's join section is the closest model for Question 2. Bring questions to the next session — but bring the output you already looked at, not only the error message.
