# 🎓 Semester at the study office

**Assignment, Business Data Science, session 10 · deadline Monday 5 October 2026, 23:59**

About one first-year student in five leaves the university during the first semester. The study office can hold
about **40 conversations** at the end of week 6. Can a model help it decide who to talk to, and what mistakes will
it make: students worried for nothing (**false positives**) and students missed (**false negatives**)?

[![Open the starter notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aaubs/ds-master/blob/main/assignments/study-office/starter.ipynb)

## What you do

1. **Work through `starter.ipynb`** (the button above; *File → Save a copy in Drive* first). It gives you the steps,
   you write the code: the problem → leakage → a split by time → a model → the confusion matrix → a cut-off from
   costs → only 40 conversations → fairness → store the model → this week's list.
2. **Build a Streamlit app** for the study office and deploy it from GitHub on
   [share.streamlit.io](https://share.streamlit.io).
3. **Record a video** (8–10 minutes) of a Teams call in which your group explains the system.

**Your template for every step is the hotel case from session 10:** the
[hotel notebook](https://colab.research.google.com/github/aaubs/ds-master/blob/main/notebooks/M1_10_hotels_ensembles.ipynb)
and the [hotel app](https://github.com/aaubs/tonights-front-desk). `GUIDE.md` explains the ideas on one page.
AI assistants are welcome for the code, but you must be able to explain every step.

## Files

| File | What it is |
|---|---|
| `starter.ipynb` | the starter notebook: the steps, your code |
| `GUIDE.md` | confusion matrix, precision and recall, a cut-off from costs, capacity, fairness, storing the model |
| `data/history_week6.csv` | students from 2023–2025 still enrolled at week 6, what the office knew then, and `left` |
| `data/new_week6.csv` | this year's students at week 6: the list the office has to act on |

The notebook reads the data straight from GitHub, so nothing needs uploading. The students are synthetic, but every
profile is resampled from a real student (UCI *Predict students' dropout and academic success*, Realinho et al.
2022, CC BY 4.0), and the risk of leaving follows a model fitted on the real outcomes.
