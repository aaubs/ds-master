# Session 03: exploratory analysis and comparing groups

Module 1, session 03, for the 2026 Business Data Science cohort. Continues directly from
[session 02](../ds4b-m1-3-pandas-2026/README.md): the same Spotify snapshot, the same table,
rebuilt in one cell at the top of each notebook.

## What is here

- [moodle-session-03.html](moodle-session-03.html) is the fragment to paste into Moodle.
  [moodle-session-03-preview.html](moodle-session-03-preview.html) opens in a browser to check
  it, and the `-after-merge` copy has `main/` URLs for after the branch is merged.
- [instructor-guide.md](instructor-guide.md) is the run of show and the teaching moments.
- [student-reference.md](student-reference.md) is what each test answers and how to report a
  comparison. Linked from the Moodle page.

The notebooks live in `notebooks/`:

- `M1_03_exploring_distributions.ipynb`, part 1, about 80 minutes.
- `M1_04_comparing_groups.ipynb`, part 2, about 110 minutes.

Both are rebuilt by the generator in the session 02 folder's tooling and validated by
[validate_notebooks.py](../ds4b-m1-3-pandas-2026/validate_notebooks.py), which executes all six
module notebooks in a fresh kernel.

## The design in one paragraph

Session 02 taught the checks that keep a table honest. This session asks what the table looks
like, and then what counts as a difference. The second half turns on two comparisons that both
come back significant: edm against rock on energy, where the effect size is 0.41 and the
difference is real, and latin against pop, where the gap is seven thousandths of a bounded
index and the effect size is 0.04. No test can separate those two.

The track IDs in this file are real Spotify IDs, so both notebooks link to the songs and the
instructor guide lists five worth playing. The highest-energy track in the dataset is a
rainforest recording, which is funnier than any example anyone could invent and does most of
the work of explaining what an audio feature actually measures.

The guide also carries a break quiz on Spotify's 2025 global top ten, which exists to make one
point: eight of those artists appear in our 2020 file, and the two missing are the two a Danish
classroom never guesses.
