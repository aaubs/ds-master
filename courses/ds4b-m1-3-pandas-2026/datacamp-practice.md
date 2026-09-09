# DataCamp practice for Module 1

The class has DataCamp access. This page says which courses are worth your time for sessions
02 and 03, in what order, and what they will and will not give you.

## What DataCamp is good for, and what it is not

DataCamp drills syntax. You type the right call into a box, it turns green, you move on. That
is genuinely useful, and it is the fastest way to stop fighting the library.

It is also the exact layer that a language model now does for you. Nobody is hiring you to
remember the argument order of `melt`. So do these courses to build fluency, not to build
judgement. The judgement parts of this module, deciding what one row means, predicting a row
count before a merge, telling a real difference from a significant one, do not appear in any
of them, because there is no way to auto-grade a decision.

Use DataCamp so the syntax stops being in your way. The sessions and the assignment are where
you learn the part that is actually scarce.

## If you only do two things

[Data Manipulation with pandas](https://www.datacamp.com/courses/data-manipulation-with-pandas),
then [Joining Data with pandas](https://www.datacamp.com/courses/joining-data-with-pandas).

Between them they cover almost everything in session 02, and the second one is the direct
drill for the part of the assignment that people find hardest.

## For session 02: pandas and NumPy

| Course | Covers | When |
|---|---|---|
| [Data Manipulation with pandas](https://www.datacamp.com/courses/data-manipulation-with-pandas) | Selecting, filtering, sorting, grouped summaries. The spine of notebook 1 and most of notebook 2. | Start here |
| [Joining Data with pandas](https://www.datacamp.com/courses/joining-data-with-pandas) | Merges, join types, and combining tables. Directly useful for the assignment. | Second |
| [Introduction to NumPy](https://www.datacamp.com/courses/introduction-to-numpy) | Arrays, shape and dtype, vectorised operations, boolean masks. The first half of notebook 1. | If arrays felt shaky |
| [Reshaping Data with pandas](https://www.datacamp.com/courses/reshaping-data-with-pandas) | Wide to long, `melt`, stacking, multi-index. The last section of notebook 2. | If `melt` felt like magic |
| [Cleaning Data in Python](https://www.datacamp.com/courses/cleaning-data-in-python) | Types, ranges, missing values, record linkage. | Optional, useful before the assignment |

## For session 03: exploring and comparing

| Course | Covers | When |
|---|---|---|
| [Exploratory Data Analysis in Python](https://www.datacamp.com/courses/exploratory-data-analysis-in-python) | Validating and summarising data, data quality problems, relationships between variables. Closest match to session 03 part 1. | Start here |
| [Introduction to Statistics in Python](https://www.datacamp.com/courses/introduction-to-statistics-in-python) | Summary statistics, distributions, correlation, the vocabulary the tests assume. | If the stats words are unfamiliar |
| [Hypothesis Testing in Python](https://www.datacamp.com/courses/hypothesis-testing-in-python) | t-tests, ANOVA, chi-square, and the assumptions behind them. Session 03 part 2, in much more detail. | After the session, not before |
| [Introduction to Data Visualization with Seaborn](https://www.datacamp.com/courses/introduction-to-data-visualization-with-seaborn) | The plotting library the session 03 notebooks use. One call per chart, sensible defaults. | Worth doing alongside |

Session 03 plots with seaborn, which sits on top of matplotlib and needs about one line per
chart. You will still meet raw matplotlib for the small adjustments seaborn does not cover,
such as drawing a vertical line at a mean.

## One warning about the hypothesis testing course

It will teach you to run a test and read a p value, and it will not spend much time on the
thing session 03 spends its second half on: that on a table with thirty thousand rows, almost
every difference is significant and almost none of them matter. Take the mechanics from
DataCamp. Take the interpretation from the session.

## Tracks, if you prefer a longer path

If you would rather follow a structured sequence than pick courses individually, the
[Data Manipulation in Python](https://www.datacamp.com/tracks/data-manipulation-with-python)
track bundles the pandas courses above, and
[Associate Data Scientist in Python](https://www.datacamp.com/tracks/associate-data-scientist-in-python)
covers the whole arc from manipulation through statistics. Neither is required for this
module.
