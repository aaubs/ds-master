# Group assignment · From a table to a defensible answer

**Module 1 · Session 02 follow-up · Master's in Business Data Science**

| | |
|---|---|
| **Work in** | Your assigned group |
| **Hand in** | One `.ipynb` notebook + one video (link in the notebook's first cell) |
| **Deadline** | Friday 18 September 2026, 23:59 |
| **Expected effort** | About 40 hours of group work in total, including the recording |

## Why this assignment exists

In the session we practised a specific discipline: say what one row is, check the data before trusting it, protect a join, and report a number together with what it cannot support. This assignment asks you to do that once, on your own, on a question we have not answered for you.

The analysis itself is not large. Most of your 40 hours should go into the decisions and into being able to defend them — not into writing more code.

## The question

Some tracks sit on a single playlist. Others travel: the same track turns up on several. A curation team wants to know whether travelling tracks are recognisably different.

> **Part A — Do tracks that appear on more playlists differ from tracks that appear on only one?**
> Compare the two groups on at least two audio features and on `track_popularity`.
>
> **Part B — Does whatever you find in Part A hold inside every subgenre family?**
> Use the supplied `subgenre_families.csv` lookup to get the family label.
>
> **Part C — One question of your own.** Formulate a question the same tables can answer, and answer it to the same standard.

"Travelling" is not defined for you. Choosing the cut-off is part of the work, and so is showing what happens when you move it.

## The data

Both files are in `data/M1_2026/`, and load the same way as in the session notebooks.

- `spotify_songs.csv` — the same 2020 snapshot as Notebook 2.
- `subgenre_families.csv` — a subgenre → family grouping, **constructed for this assignment**. It is not an official Spotify taxonomy and carries no authority; it exists so that you have a lookup table to join. Treat it exactly as you would treat any lookup table handed to you by someone else: check its keys before you trust the join. It was not checked for you.

## What to produce

Work through these in order. Each numbered task should be visible as a section in your notebook.

**1 · State the grain (≈2 h).** Before any analysis, say in one sentence what one row of the raw file represents, and support it with output rather than assertion. Then decide what one row of *your* working table will represent, and say why that choice fits Part A. There is more than one defensible answer here; there is no defensible way to skip the question.

**2 · Audit before deciding (≈5 h).** Report what is missing in the fields your answer depends on, and decide what to do about each — including where the decision is "nothing". Do the same for release dates: say what precision the data actually carries and what you would be inventing if you parsed everything to a full date. A field you do not use needs no repair; say that rather than repairing it.

**3 · Measure reach (≈4 h).** Compute, for every track, the number of playlists it appears on. Two reasonable-looking ways to compute this disagree on this dataset. Find out whether yours is one of them, state which number you are reporting, and show the check that convinced you.

**4 · Join the family lookup (≈8 h).** Attach the family label to your working table. Predict the row count before you merge, use `validate=` and `indicator=`, and compare. If the merge does not behave as predicted, that is the task, not an obstacle to it: diagnose what is wrong with the keys, decide what to do, and record the decision and its cost. Report how many rows you could not label and what you did with them.

**5 · Answer Parts A and B (≈8 h).** Produce a summary table that carries counts next to every mean. Show how the answer changes when you move the "travelling" cut-off — at least three values. For Part B, be explicit about which families are too small to carry the comparison.

**6 · One chart and the interpretation (≈6 h).** One chart that supports your claim; reshape the data as needed to build it. Then write 250–400 words that state what you found, what the number rests on, and at least two things this data cannot tell the curation team. Include Part C here.

**7 · The video (≈5 h including rehearsal).**

- 8 minutes, maximum 10. Screen recording of your notebook with your voices over it.
- **Every group member speaks**, and each one presents a different decision your group made: what you chose, what you rejected, and why.
- Show at least one piece of your own code on screen while explaining what it does and why it is written that way.
- Do not narrate the notebook top to bottom. We have the notebook. Tell us about the decisions.

## Submission checklist

- [ ] One `.ipynb`, named `M1_assignment_<group>.ipynb`
- [ ] First cell: group number, member names, and the video link
- [ ] **Restart & Run All produces the notebook you are submitting**, from a fresh kernel, with no manual steps
- [ ] Data loaded by the supplied path/URL cell — do not attach copies of the CSVs
- [ ] Every section 1–6 present, in order
- [ ] A short decision log: for each of tasks 1, 2, 3 and 4, one line saying what you decided and what it cost you
- [ ] Video is reachable by someone who is not in your group

## How it is marked

| Weight | What we look at |
|---:|---|
| 20 | **Grain and audit.** Is the row meaning stated and supported? Are the missingness and date-precision decisions made deliberately, including the decisions to do nothing? |
| 25 | **The join.** Predicted row count, validation, diagnosis of what the keys do, a decision that is stated with its cost, and an honest count of what stayed unlabelled. |
| 20 | **The answer.** Counts reported next to means, cut-off sensitivity actually shown, small groups flagged rather than quietly averaged. |
| 10 | **Chart and reshape.** One chart that carries the claim, with a readable axis and the counts visible. |
| 15 | **Interpretation.** What the result rests on, what it cannot support, and language that does not slide into cause and effect. |
| 10 | **Reproducibility and craft.** Runs from a fresh kernel; steps small enough to follow; no dead code left behind. |

**The video is required.** A submission without a working video link is incomplete. We do not mark it separately, but we do use it: if the video and the notebook disagree about what you did, we mark the video.

Not marked: chart styling, notebook length, how many pandas methods you used, or whether your answer matches ours. A well-defended "the difference is too small to act on" scores better than an overclaimed effect.

## Tools and honesty

Use whatever tools help you, AI assistants included. Two conditions, and they are the whole policy:

1. Put a short note at the end of your notebook saying where you used AI assistance and for what.
2. Be able to explain every line you submit. That is what the video checks, and it is why each member presents a decision rather than reading a script.

Code you cannot explain is not your answer, whatever produced it.

## If you get stuck

The two session notebooks contain every technique this assignment needs. Notebook 2's join section is the closest model for task 4. Bring questions to the next session — but bring the output you already looked at, not only the error message.
