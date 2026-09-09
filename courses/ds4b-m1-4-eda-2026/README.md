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

Session 02 taught the checks that keep a table honest. This session hands students a brief with
a wrong answer built in: someone upstairs wants to know which musical qualities make a track
popular. Part 1 answers it in one line of `.corr()` — no audio measurement clears 0.14 — and
part 2 spends its time on what that does and does not license you to say. All ten audio columns
together account for 6 percent of the variation in popularity, genre for 4, and the strongest
signal in the file (playlist placements, d = 1.62) is the outcome in disguise. The deliverable
is a memo saying so, which most students have never been shown how to write.

The statistical machinery is unchanged: t-test, effect size, sample-size demonstration, ANOVA
with eta squared, chi-square with Cramer's V. It is attached to decisions rather than to trivia.

Two traps are planted in the data rather than in the prose. Nine percent of the popularity
column is a spike at exactly zero that may or may not be a measurement, and dropping it moves
every genre mean by 3 to 4.7 points. And the file's most extreme "songs" are field recordings
of rainfall and crickets, sitting on a latin playlist, inside any average anybody quotes.

The track IDs are real Spotify IDs, so both notebooks link to the songs and the instructor guide
lists five worth playing. Part 2 also carries a break quiz on Spotify's 2025 global top ten:
eight of those artists appear in our 2020 file, and the two missing are the two a Danish
classroom never guesses.
