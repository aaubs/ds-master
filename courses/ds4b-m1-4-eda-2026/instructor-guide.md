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

Continuity is deliberate and worth pointing at explicitly. Both notebooks rebuild last week's
table in one cell, marked as a recap with nothing new in it. Say out loud that this is the
same 32,510 associations, so nobody thinks a new dataset has appeared.

## Run of show

| Time | Segment |
|---|---|
| 12:30-12:40 | Open. Show that the recap cell reproduces last week's numbers exactly. |
| 12:40-14:00 | Part 1: distributions, odd rows, base rates, relationships. |
| 14:00-14:10 | Break. |
| 14:10-15:05 | Part 2 through effect size, which is the core. |
| 15:05-15:15 | Break. |
| 15:15-16:10 | Sample-size demo, ANOVA, chi-square, how to report it. |
| 16:10-16:15 | Exit ticket. |

If you are behind, cut the chi-square section and the second practice task. Do not cut the
sample-size demonstration in part 2 section 5, which is the load-bearing cell of the day.

## The moments

**The same row, caught twice.** Part 1 section 3 finds a four-second track from the minimum of
`duration_ms`, then finds a track with a tempo of exactly zero. It is the same record: "Hi,
How're You Doin'?" by DREAMS COME TRUE. Let the room notice it rather than announcing it. The
point is that nobody suspected that row. Two unrelated sanity checks found it.

**Valence has no middle.** The four-panel histogram in part 1 section 2 puts the mean on each
distribution as a vertical line. Valence is nearly flat across its range and tempo has a spike
at 120 with a second bump near 100, because produced music is written to conventional tempos.
In both, the mean is a real number and a poor summary. Ask what the mean of the tempo column
is describing before moving on.

**Two tests, one verdict.** Part 2 sections 2 and 3 are the centre of the session. edm against
rock: difference 0.068, p about 2e-91. pop against latin: difference 0.0095, p 0.0025. Both
significant. Run them back to back and let the room sit with it before introducing effect
size, which separates them cleanly at d = 0.40 against d = 0.06.

**The sample-size demo.** Section 5 reruns the pop-latin test on 30 rows a side, 200 times.
Median p is about 0.45 and it clears 5 percent in roughly 6 percent of runs, which is what you
would expect from chance alone. The difference in the data never changed. Only the row count
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

- **Association grain versus track grain.** The mean of `energy` differs slightly between
  `joined` and `tracks` because popular tracks are counted many times in the first. Part 1
  section 1 shows both. Make somebody say which one answers which question.
- **The 0.05 threshold is a convention.** Nothing in the data changes at 0.049. If you have
  time, say where the number came from and that the ASA has spent a decade asking people to
  stop treating it as a verdict.
- **Multiple comparisons.** Part 2 runs fifteen pairwise tests in one cell. Nobody corrects for
  it, and on this data it does not matter because the effect sizes carry the conclusions. Worth
  one sentence so nobody is surprised when it comes up in a later course.
- **Correlation is not causation, and also not much else.** Energy against loudness at 0.68 is
  near tautological. Say which correlations are findings and which are definitions.

## Exit ticket

Two questions, three sentences each:

1. You ran a test, and p is less than 0.001. What do you still not know?
2. Name one column in this dataset whose mean is a bad summary, and say why.

Good answers to the first name the size of the difference, the number of rows, and whether it
matters practically. Good answers to the second name valence or tempo and describe the shape.
