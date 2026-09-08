# Instructor guide: Python → NumPy → pandas

**Session:** 9 September 2026, 12:30–16:15 (Fib15-2.234)<br>
**Instructor:** Roman Jurowetzki<br>
**Audience:** MSc Business Data Science students with Python basics<br>
**Format:** [Notebook 1](../../notebooks/M1_01_control_flow_to_pandas.ipynb) and [Notebook 2](../../notebooks/M1_02_pandas_deep_dive.ipynb), with filenames preserved, plus the supplied sibling `data/` and `media/` structure.<br>
**Companion:** [Instructor solutions notebook](../../notebooks/M1_instructor_solutions_2026.ipynb) — every exercise with the model solution, the wrong answers to expect, expected numbers from the frozen snapshot, and three live diagnostic cells. This guide holds the timing and teaching intent; that notebook is the runnable half. Rebuild it with `build_instructor_notebook.py` after changing any student solution.

## Teaching intent

The session is a guided bridge from Python objects to array programming and then to tabular analysis. Keep the historical Udemy → Spotify sequence. It gives students a familiar cumulative narrative and preserves the existing data/media references; changing the dataset merely for novelty would spend scarce class time on context and file-path repair.

The conceptual spine is:

`list/dict → ndarray (dtype, shape, vectorized operations) → DataFrame (labels, selection, summaries) → combine/reshape → business interpretation`

Students should leave able to state the row grain, produce a reproducible summary, and explain the assumptions behind a join or reshape. Required scope includes key-based joins/combines and reshape; correlation is optional enrichment rather than a learning gate.

## Run of show (225 minutes)

| Time | Segment | Instructor emphasis |
|---|---|---|
| 12:30–12:40 | Launch (10 min) | State the data-analysis question, show the two-notebook path, open the setup cell, and run a version report before imports become scattered. |
| 12:40–14:00 | Notebook 1 (80 min) | Python refresher → genuine NumPy array work → pandas entry. Use predict–run–inspect–explain cycles and keep students coding. |
| 14:00–14:10 | Break (10 min) | — |
| 14:10–15:05 | Notebook 2, first half (55 min) | Spotify orientation, missingness and date precision, then the small join example and track/playlist tables. Include the embedded exercise attempts. |
| 15:05–15:15 | Break (10 min) | — |
| 15:15–16:10 | Notebook 2, second half (55 min) | Finish the join checkpoint, then grouped summaries, `melt`/`pivot_table`, and one chart with a sample-limited interpretation. |
| 16:10–16:15 | Exit ticket (5 min) | Collect a concise answer to the prompts below and have students note one safe pandas assignment pattern. |

Notebook 1 allocates 20 minutes to Python flow, 20 to NumPy, 25 to pandas inspection/selection, and 15 to groupby practice. Notebook 2 allocates 15 minutes to orientation, 15 to the audit, 30 to joins, 25 to grouping, and 25 to reshaping and interpretation. Exercise attempts are included in these times. The second break falls near the end of the join section; finish its checkpoint after the break.

Treat the robustness and date-precision checks as supplied support code: explain the decision and the output rather than every line. The main path now derives date precision from the text length and checks track consistency with `drop_duplicates`, so no regular expressions appear before the appendix; the stricter regex and grouped-`nunique` versions sit at the end of Notebook 2, labelled as later material, and each asserts that it agrees with the short version. If students need more practice, let pairs attempt two of the four Notebook 2 exercises in class and complete the others after class. Keep the joins, reshape demonstration, and final interpretation. The optional sampling extension is for after class.

## Scaffolding moves

- Begin every new operation with a question students can predict: “How many rows and columns?”, “Which rows survive this mask?”, “What is one row after this merge?”, or “What does wide-to-long create?”
- Keep a visible diagnostic cell near the top:

  ```python
  import sys
  import numpy as np
  import pandas as pd
  print(sys.version)
  print("numpy", np.__version__, "pandas", pd.__version__)
  ```

- After each structural operation, inspect `shape`, a few rows, and the key columns. Require students to say what changed before moving to a statistic.
- Use pair explanations for masks, merge keys, and grain. A useful prompt is: “If the key appears twice on the right, how many rows might this left merge produce?”
- For a stuck student, return to a three-line rescue path: `df.head()`, `df.columns`, `df.shape`. Then check spelling, brackets, and whether the cell defining the object has run.
- Keep the business interpretation beside the code. Ask what the number could support, what it cannot support, and what data-generating assumption is being made.

## Known data and interpretation traps to surface

These are short teaching interventions, not extra topics.

- **Mixed date parsing:** mixed formats in a date column do not by themselves prove that dates are malformed. Show the parse result and missing count, make parsing assumptions explicit, and investigate the rows that fail rather than labeling the entire field bad.
- **Playlist grain and track deduplication:** the Spotify table can contain a track in multiple playlists. Establish whether the question is about playlist placements, track-level behavior, or unique tracks. Deduplicate only with a stated key and purpose; do not silently treat `track_id` as unique across the table.
- **Proxy language:** `price_times_enrollments_proxy` is a constructed practice proxy, not recorded sales. Investigate its assignment and label it as a proxy; avoid causal claims.
- **List masks versus pandas masks:** a Python list of booleans is positional; a pandas Boolean `Series` is label-aligned. Do not mix them casually. Check index alignment or use an explicit NumPy array/`reset_index()` when positional behavior is intended.
- **NumPy must be real:** Notebook 1 should include `np.array`, `shape`, dtype, vectorized arithmetic, and a mask. Importing NumPy only to support pandas examples does not establish the intended bridge.
- **Correlation is optional:** if included, treat it as a descriptive association and discuss missingness, selection, scale, and possible confounding. Do not let a rushed correlation segment displace merge, reshape, or the exit check.

## Version and Colab notes

As of 2026-09-06, pandas documentation is on the 3.0.5 line. pandas 3.0 makes Copy-on-Write the default and only mode, and infers a dedicated `str` dtype for text. Colab runtimes are managed independently and update their pre-installed libraries; Google’s 2026.07 past-runtime listing includes Python 3.12.13 and NumPy 2.0.2, so a student may have pandas 2.x even when the instructor has pandas 3.x.

Use patterns that behave across both lines:

- assign in one operation with `df.loc[mask, "column"] = value`;
- use `.copy()` when a subset should be independent;
- use `pd.isna`/`.isna()` for missingness and `pd.api.types.is_string_dtype` for a text-type check;
- use `astype("string")` when explicit nullable text semantics are needed, rather than `astype(str)`;
- use `.to_numpy()` when a NumPy array is required, rather than depending on `.values` for extension dtypes.

Avoid chained assignment, `dtype == "object"` as a text test, direct `None`/`np.nan` comparisons, and examples that depend on the exact display of a string dtype. Avoid package installation mid-class. If a controlled install is required, install before imports, verify once, restart the runtime, and run all cells.

Colab executes code in a virtual machine that may be reset or deleted after inactivity. Keep data loading in a rerunnable setup cell, save notebooks, and use a standard CPU runtime for this class.

## Group assignment

The follow-up assignment is [assignment.md](assignment.md), with a starter notebook at
[M1_assignment_2026_starter.ipynb](../../notebooks/M1_assignment_2026_starter.ipynb).
Groups answer whether tracks that appear on more playlists differ from tracks that appear
on one, using a supplied subgenre-family lookup, and submit a notebook plus an 8-minute
video in which every member presents one decision.

[assignment-instructor-notes.md](assignment-instructor-notes.md) — **not for students** —
documents the three key problems planted in the lookup table, the reach computation that
two reasonable methods disagree on, the expected numbers at each cut-off, and what to
expect in submissions. Read it before handing the assignment out; it also lists the four
things to confirm first, starting with the deadline.

## Exit ticket (5 minutes)

Ask students to answer these two prompts in two or three sentences:

1. What is the difference between a Python list, a NumPy `ndarray`, and a pandas `DataFrame`?
2. Name one limitation of the analysis: for example, what one row represents, what your join/deduplication assumes, why a mixed date format needs investigation, or why `price_times_enrollments_proxy` is not observed sales.

Use responses to identify follow-up needs around masks, grain, merge cardinality, and interpretation. Do not grade correlation as a required outcome.

## Source links and why they are here

All links were accessed on 2026-09-06.

| Source | Teaching use |
|---|---|
| [Python Tutorial](https://docs.python.org/3/tutorial/index.html) | Refresher for control flow, lists/dictionaries, and functions. |
| [NumPy absolute basics](https://numpy.org/doc/stable/user/absolute_beginners) | Beginner sequence for arrays, shape, indexing, and operations. |
| [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart) | Instructor reference for axes, masks, ufuncs, broadcasting, `empty`, and float-step `arange` pitfalls. |
| [pandas subset data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html) | Selection and Boolean filtering. |
| [pandas new columns](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html) | Element-wise derived columns without row loops. |
| [pandas summary statistics](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html) | Aggregation and split–apply–combine. |
| [pandas combine tables](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html) | Key-based `merge` and row-count reasoning. |
| [pandas reshape tables](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html) | `melt`, `pivot`, and long/wide grain. |
| [pandas Copy-on-Write guide](https://pandas.pydata.org/docs/user_guide/copy_on_write.html) | Why chained assignment fails and `.loc` is the stable pattern. |
| [pandas 3.0 string migration guide](https://pandas.pydata.org/docs/user_guide/migration-3-strings.html) | `str` default, missing-value sentinel, cross-version dtype checks, and `astype(str)` change. |
| [Google Colab FAQ](https://research.google.com/colaboratory/faq.html) | Virtual-machine state, saving, and runtime limits. |
| [Colab Runtime Version FAQ](https://research.google.com/colaboratory/runtime-version-faq.html) | Mutable pre-installed packages, version pinning, and the 2026.07 runtime listing. |
| [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) | Free optional NumPy/pandas reading; flag its historical API examples. |
