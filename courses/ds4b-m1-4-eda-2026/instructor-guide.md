# Instructor guide: session 03

**Session:** Wed 16 September 2026, 12:30-16:15 (Fib15-2.234)
**Audience:** MSc Business Data Science, straight after the pandas session
**Format:** [M1_03_exploring_distributions.ipynb](../../notebooks/M1_03_exploring_distributions.ipynb) and [M1_04_comparing_groups.ipynb](../../notebooks/M1_04_comparing_groups.ipynb)

## Teaching intent

Session 02 ended with a table nobody had looked at. This session looks at it, and then asks
what counts as a difference.

The arc is: distributions, then odd rows, then relationships, then group comparison, then the
thing the whole day is for, which is that on a table this size a significant result costs
nothing and an effect size is the finding. Students arrive believing p values are the point.
They should leave believing p values are the smallest claim in the sentence.

Continuity is deliberate, and it is a sentence rather than a pipeline. There are no joins in
this session: the raw file already carries every audio measurement on every row, so the setup
is two lines. Say out loud that this is last week's file and last week's row meaning, and that
nothing new has appeared, then move on. The merge machinery belongs to session 02 and has done
its job.

## Run of show

Deliberately less material than session 02. Two notebooks, 23 code cells between them, and no
joins anywhere. The file already carries every audio measurement on every row, so the session
opens with two lines rather than a pipeline. The time freed up is for talking.

| Time | Segment |
|---|---|
| 12:30-12:45 | Open. What one row is, and why there are two frames rather than one. |
| 12:45-14:00 | Part 1. Four ideas: what describe hides, rows that cannot be right, group sizes, correlation. |
| 14:00-14:10 | Break. |
| 14:10-15:05 | Part 2 through effect size. This is the core. |
| 15:05-15:15 | Break. |
| 15:15-16:10 | Sample size, ANOVA, chi-square, how to report a comparison. |
| 16:10-16:15 | Exit ticket. |

There is room in this plan. Use it on the histogram panel and on the two t-tests, which are
the two places students change their minds about something. If you finish early, do the
practice tasks together rather than adding material.

If you are behind, cut the chi-square section. Do not cut the sample-size demonstration.

## What came back from the 2025 notebook

Last year's version had better scaffolding than substance: a strong five-question EDA
checklist and a clean test-chooser table, wrapped around synthetic data and a p-value rule it
contradicted later in its own text. Three things were worth keeping and are now in these
notebooks.

The **five questions** open part 1 as a table, and the notebook then follows them in order.
Point at it and say it works on any table, not just this one. It is the most portable thing in
the session.

The **which-test table** opens part 2, before any test appears, so choosing between them stops
being mysterious before the interesting problem arrives.

The **multiple-testing warning** sits just before the reporting rule. It is more relevant now
than it was last year, which is the framing to use: running twenty tests used to take an
afternoon, and an agent will run fifty in one call and hand back the three that cleared 0.05.

What did not come back: the synthetic data generator, and the `if p < 0.05: print("REAL")`
pattern that appeared three times. If a student has seen last year's notebook, that second one
is worth naming out loud as the thing this session is arguing against.

## The moments

**The same row, caught twice.** Part 1 section 2 finds a four-second track from the minimum of
`duration_ms`, then finds a track with a tempo of exactly zero. It is the same record: "Hi,
How're You Doin'?" by DREAMS COME TRUE. Let the room notice it rather than announcing it. The
point is that nobody suspected that row. Two unrelated sanity checks found it.

**Valence has no middle.** The four-panel histogram in part 1 section 1 puts the mean on each
distribution as a vertical line. Valence is nearly flat across its range and tempo has a spike
at 120 with a second bump near 100, because produced music is written to conventional tempos.
In both, the mean is a real number and a poor summary. Ask what the mean of the tempo column
is describing before moving on.

**Two tests, one verdict.** Part 2 sections 2 and 3 are the centre of the session. edm against
rock: difference 0.068, p about 2e-91. pop against latin: difference 0.0095, p 0.0025. Both
significant. Run them back to back and let the room sit with it before introducing effect
size, which separates them cleanly at d = 0.41 against d = 0.04.

**The sample-size demo.** Section 5 reruns the pop-latin test on 30 rows a side, 200 times.
Median p is about 0.55 and it clears 5 percent in exactly 5 percent of runs, which is what
chance alone gives you. The difference in the data never changed. Only the row count
did. This is the cell that makes the lesson stick, so give it time.

**Eta squared.** Genre explains about 14 percent of the variation in energy, which means 86
percent of the variation is within genres. That single sentence is a better summary of the
dataset than any p value in the notebook, and it is the sort of thing a curation team can act
on.

## What to say about tests and language models

Same argument as session 02, one level up. Ask a model to test whether two genres differ and
you get a correct t-test, a correct p value, and a verdict. What you do not get is the
question of whether anybody should care, because that was not in the request and is not in the
output. The pop-latin comparison is the demonstration: everything about it is correct and the
conclusion is worthless.

If a student says they would just ask for the effect size too, that is the right answer, and
the point stands. You have to know the words. Prompting is expertise expressed somewhere else.

## Known traps to surface

- **Two frames, not one.** `songs` counts a track once per playlist; `tracks` counts it once.
  Most confusion in this session traces back to someone using the wrong one. Ask which
  question each answers rather than which is correct.
- **The 0.05 threshold is a convention.** Nothing in the data changes at 0.049. The pop-latin
  test lands at p = 0.02, comfortably inside a threshold nobody chose on principle.
- **Skew is not error.** In the practice task, `speechiness` has a long tail of tracks that are
  mostly talking. Those are real records. Students who have just learned about broken rows tend
  to want to delete anything unusual.
- **Correlation is not causation, and often not much else either.** Energy against loudness at
  0.68 is near tautological. Say which correlations are findings and which are definitions.

## Exit ticket

Two questions, three sentences each:

1. You ran a test, and p is less than 0.001. What do you still not know?
2. Name one column in this dataset whose mean is a bad summary, and say why.

Good answers to the first name the size of the difference, the number of rows, and whether it
matters practically. Good answers to the second name valence or tempo and describe the shape.
