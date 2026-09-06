# Python, NumPy and pandas: student reference

**Session:** 9 September 2026, 12:30–16:15<br>
**Course:** MSc Business Data Science<br>
**Instructor:** Roman Jurowetzki

This page is a small map for [Notebook 1](../../notebooks/M1_01_control_flow_to_pandas.ipynb) and [Notebook 2](../../notebooks/M1_02_pandas_deep_dive.ipynb). Keep their existing filenames and use the supplied sibling `data/` and `media/` folders. The notebooks are the main learning material; the links below are selected reading, not chapters to complete before class.

## What you should be able to do

By the end of the session, you should be able to:

- move from ordinary Python lists/dictionaries to a NumPy array and then to a labeled pandas `DataFrame`;
- inspect data with `shape`, `head()`, `info()`, and `describe()`;
- select rows and columns, create element-wise columns, and summarize by a group;
- combine tables with a key-based `merge`;
- reshape long/wide data with `melt` or `pivot_table`, while stating what one row represents.

## Choose a 15–20 minute reading path

Choose the route that matches your confidence. Open one or two examples and try a small variation in a notebook; do not read every linked page in full.

1. **Python → NumPy route:** [Python Tutorial](https://docs.python.org/3/tutorial/index.html), skimming control flow and lists/dictionaries, then [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners), focusing on `ndarray`, `shape`, indexing, and element-wise operations.
2. **pandas route:** [Select a subset of a DataFrame](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html), focusing on columns, Boolean row filters, and `.loc`.

Use the remaining pages as lookup during or after class:

- [Create new columns](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html) for element-wise calculations.
- [Calculate summary statistics](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html) for reductions and grouping.
- [Combine data from multiple tables](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html) for key-based `merge`.
- [Reshape table layout](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html) for `melt` and `pivot`.

### Optional references

- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) is a compact pandas overview for after class.
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) is free online. The relevant chapters are [NumPy](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html) and [pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.00-introduction-to-pandas.html). It uses a historical API in places, so use the current pandas documentation when code differs.

## Small patterns worth remembering

This tiny dataset is synthetic: one row per promotional campaign, with courses allowed to recur. The catalog has one row per course. The long table has one row per campaign–measure pair; the measures keep their different meanings and units.

```python
import numpy as np
import pandas as pd

arr = np.array([10, 20, 30])
arr.shape                 # dimensions, not a function call
arr * 2                   # element-wise calculation

courses = pd.DataFrame({
    "campaign_id": [1, 2, 3, 4],
    "course_id": [101, 102, 101, 103],
    "price": [50, 75, 50, 100],
    "enrollments": [10, 4, 7, 2],
})
catalog = pd.DataFrame({
    "course_id": [101, 102, 103],
    "subject": ["Python", "Data", "SQL"],
})
courses["price_times_enrollments_proxy"] = courses["price"] * courses["enrollments"]
courses["investigate"] = False
courses.loc[courses["enrollments"] >= 7, "investigate"] = True
joined = courses.merge(catalog, how="left", on="course_id", validate="many_to_one")
assert len(joined) == len(courses)
long = joined.melt(
    id_vars=["campaign_id", "course_id", "subject"],
    value_vars=["price", "enrollments"],
    var_name="measure", value_name="value",
)
```

`.loc[...] = ...` makes the target of an assignment explicit. Add `.copy()` when a filtered table is meant to become an independent working table. Use `pd.isna(...)` or `.isna()` for missing values; do not check whether a value is exactly `None` or exactly `np.nan`.

## Data questions to ask before calculating

Before a `merge`, aggregation, or reshape, write down the grain: “one row per ___.” Check the key columns and row counts before and after the operation. A track can occur in several playlists, so a row in the Spotify data is not automatically a unique track. Likewise, `price_times_enrollments_proxy` is a practice proxy, not observed sales.

The Colab notebook state is not a permanent computer. Run cells in order, keep the data-loading cell rerunnable, and save your notebook. If a package version changes, restart the runtime and run all cells from the top.
