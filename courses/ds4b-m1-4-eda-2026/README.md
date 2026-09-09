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
like, and then what counts as a difference. The second half is built around two comparisons
that both come back significant: edm against rock on energy, where the effect size is about
0.4 and the difference is real, and pop against latin, where the gap is one hundredth of a
bounded index and the effect size is 0.06. The p value cannot tell them apart. That is the
session.
