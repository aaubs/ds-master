# Group assignment · From a table to a defensible answer

**Module 1 · Session 02 follow-up · Master's in Business Data Science**

| | |
|---|---|
| **Work in** | Your assigned group |
| **Hand in** | One `.ipynb` notebook + one video (link in the notebook's first cell) |
| **Deadline** | Friday 18 September 2026, 23:59 |

## Why this assignment exists

In the session we practised a specific discipline: say what one row is, check the data before trusting it, protect a join, and report a number together with what it cannot support.

There are three questions. None of them is long to code. What takes the time — and what is marked — is the decisions inside them and your ability to defend those decisions.

## The setting

Some tracks sit on a single playlist. Others travel: the same track turns up on several. A curation team wants to know whether travelling tracks are recognisably different.

You have two files, in `data/M1_2026/`, loading exactly as in the session notebooks:

- `spotify_songs.csv` — the same 2020 snapshot as Notebook 2.
- `subgenre_families.csv` — a subgenre → family grouping, **constructed for this assignment**. It is not an official Spotify taxonomy and carries no authority. Treat it as you would any lookup table handed to you by another team: check its keys before you trust the join. It was not checked for you.

---

## Question 1 · What is one row, and how far does each track travel?

State what one row of the raw file represents, and support it with output rather than assertion. Then build the working table your answer will rest on, and say what one of *its* rows is and why that fits the question.

For every track, compute how many playlists it appears on. **Two reasonable-looking ways to compute this disagree on this dataset.** Find out whether yours is one of them, report which number you are using, and show the check that settled it.

Before you go on, audit what is missing in the fields your answer actually depends on, and say what precision the release dates really carry. Decide what to do about each — including where the decision is to do nothing. A field you never use needs no repair; say so rather than repairing it.

## Question 2 · Attach the family label

Merge the family lookup onto your working table.

Predict the row count before you merge and write the prediction down. Merge with `validate=` and `indicator=`. Compare.

If the merge does not behave as you predicted, **that is the question, not an obstacle to it.** Diagnose what is wrong with the keys, decide what to do about each problem you find, and record what each decision costs you. Report how many rows end up with no family label and what you did with them.

## Question 3 · Do travelling tracks differ?

Compare travelling tracks with tracks that appear on one playlist, on at least two audio features and on `track_popularity`. Report counts next to every mean.

"Travelling" is not defined for you. Choosing the cut-off is part of the work — and so is showing what happens at three or more cut-offs. Then ask whether whatever you found holds inside every family, and be explicit about which families are too small to carry the comparison.

Finish with one chart that supports your claim, reshaping the data as needed, and 250–400 words: what you found, what it rests on, and at least two things this data cannot tell the curation team.

---

## The video

- 8 minutes, maximum 10. Screen recording of your notebook with your voices over it.
- **Every group member speaks**, and each one presents a different decision your group made: what you chose, what you rejected, and why.
- Show at least one piece of your own code on screen while explaining what it does and why it is written that way.
- Do not narrate the notebook top to bottom. We have the notebook. Tell us about the decisions.

## Submission checklist

- [ ] One `.ipynb`, named `M1_assignment_<group>.ipynb`
- [ ] First cell: group number, member names, and the video link
- [ ] **Restart & Run All produces the notebook you are submitting**, from a fresh kernel, with no manual steps
- [ ] Data loaded by the supplied path/URL cell — do not attach copies of the CSVs
- [ ] All three questions present, in order
- [ ] A short decision log: one line per question saying what you decided and what it cost you
- [ ] Video is reachable by someone who is not in your group

## How it is marked

| Weight | What we look at |
|---:|---|
| 25 | **Question 1.** Is the row meaning stated and supported? Was the reach computation checked rather than assumed? Are the audit decisions deliberate, including the decisions to do nothing? |
| 30 | **Question 2.** Predicted row count, validation, diagnosis of what the keys actually do, decisions stated with their cost, and an honest count of what stayed unlabelled. |
| 20 | **Question 3, the answer.** Counts reported next to means, cut-off sensitivity actually shown, small groups flagged rather than quietly averaged. |
| 15 | **Question 3, the interpretation.** One chart that carries the claim, what the result rests on, what it cannot support, and language that does not slide into cause and effect. |
| 10 | **Reproducibility and craft.** Runs from a fresh kernel; steps small enough to follow; no dead code left behind. |

**The video is required.** A submission without a working video link is incomplete. We do not mark it separately, but we do use it: if the video and the notebook disagree about what you did, we mark the video.

Not marked: chart styling, notebook length, how many pandas methods you used, or whether your answer matches ours. A well-defended "the difference is too small to act on" scores better than an overclaimed effect.

## Tools and honesty

Use whatever tools help you, AI assistants included. Two conditions, and they are the whole policy:

1. Put a short note at the end of your notebook saying where you used AI assistance and for what.
2. Be able to explain every line you submit. That is what the video checks, and it is why each member presents a decision rather than reading a script.

Code you cannot explain is not your answer, whatever produced it.

## If you get stuck

The two session notebooks contain every technique these questions need. Notebook 2's join section is the closest model for Question 2. Bring questions to the next session — but bring the output you already looked at, not only the error message.
