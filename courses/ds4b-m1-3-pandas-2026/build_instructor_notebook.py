"""Build the instructor notebook from the two student notebooks.

Solution code is copied verbatim out of the student solution cells, so the
instructor copy cannot drift from what students are given. Teaching notes,
diagnostics and expected numbers live here.

Usage: python build_instructor_notebook.py
Writes notebooks/M1_instructor_solutions_2026.ipynb
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
NB1 = "M1_01_control_flow_to_pandas.ipynb"
NB2 = "M1_02_pandas_deep_dive.ipynb"
STUDENT = {name: json.loads((ROOT / "notebooks" / name).read_text()) for name in (NB1, NB2)}

cells = []
_n = 0


def _cell(kind, source):
    global _n
    _n += 1
    cell = {"cell_type": kind, "id": f"m1-03-{_n:03d}", "metadata": {},
            "source": source.strip("\n").splitlines(keepends=True) + ["\n"]}
    if kind == "code":
        cell.update(execution_count=None, outputs=[])
    cells.append(cell)


def md(source):
    _cell("markdown", source)


def code(source):
    _cell("code", source)


def solution(book, anchor):
    """Copy a solution cell out of the student notebook, verbatim."""
    hits = [c for c in STUDENT[book]["cells"]
            if c["cell_type"] == "code" and anchor in "".join(c["source"])]
    if len(hits) != 1:
        raise SystemExit(f"{book}: anchor {anchor!r} matched {len(hits)} cells")
    _cell("code", "".join(hits[0]["source"]))


# ---------------------------------------------------------------------------

md(f'''
# Instructor solutions: session 02

**Master's in Business Data Science · Module 1 · 9 September 2026 · Roman Jurowetzki**

Every exercise from both student notebooks, with the model solution, what students
actually hand in, and what to say when they are stuck. The numbers quoted are from the
frozen class snapshot, so you can check a student's screen without re-running anything.

Solution code here is copied verbatim from the student notebooks — if you change a
solution there, rebuild this file with `courses/ds4b-m1-3-pandas-2026/build_instructor_notebook.py`
rather than editing it by hand.

**This file is for you, not for Moodle.** Timing, run of show, scaffolding moves and the
version/Colab notes live in [instructor-guide.md](../courses/ds4b-m1-3-pandas-2026/instructor-guide.md);
this notebook is the runnable half.

## How to run it

1. Run the helper cell below once.
2. Run the **Part 1 setup** cell, then anything in Part 1.
3. Run the **Part 2 setup** cell before anything in Part 2.

Both setup cells replay the matching student notebook end to end with its output
suppressed, so every object the solutions need is in scope and identical to what
students will have on screen.

⚠️ **Part 2's setup rebinds `df` to the Spotify data.** If you jump back to a Part 1
solution afterwards, re-run the Part 1 setup cell first.
''')

code('''
# Run once. Replays a student notebook quietly so its objects exist here too.
import json
from pathlib import Path
from urllib.request import urlopen

import matplotlib.pyplot as plt
from IPython.utils.capture import capture_output

RAW_NOTEBOOKS = "https://raw.githubusercontent.com/aaubs/ds-master/codex/m1-pandas-2026/notebooks"


def run_student_notebook(filename):
    """Execute every code cell of a student notebook in this kernel, silently."""
    candidates = [Path(filename),
                  Path("notebooks") / filename,
                  Path("..") / "notebooks" / filename,
                  Path("ds-master/notebooks") / filename]
    source = None
    for path in candidates:
        if path.exists():
            source = path.read_text()
            print(f"Replaying {path}")
            break
    if source is None:
        url = f"{RAW_NOTEBOOKS}/{filename}"
        source = urlopen(url).read().decode()
        print(f"Replaying {url}")

    with capture_output():
        for cell in json.loads(source)["cells"]:
            if cell["cell_type"] == "code":
                exec("".join(cell["source"]), globals())
    plt.close("all")
    print("Done. Every object from that notebook is now in scope.")
''')

# --- Part 1 ----------------------------------------------------------------

md("## Part 1 · From control flow to pandas")

code(f'run_student_notebook("{NB1}")\nprint("Catalog shape:", df.shape)')

md('''
### Practice 1 · Collect the free-course titles (loop + `if`)

> Write a loop that collects the titles of free courses into `free_titles`.

**Expected result:** `['Python Basics Lab', 'Security Lab']`, in that order. The
untouched proxy loop above it prints 3,550.

**What students actually hand in**

| What you will see | What went wrong | Say this |
|---|---|---|
| A list of dictionaries | They appended `course`, not `course["course_title"]` | "Print one element. Is that a title or a whole record?" |
| `[]` | `course["price"] == "0"` — comparing a number to text | "What type is `price`? Try `type(course['price'])`." |
| One title only | `free_titles = []` was written inside the loop | "Where does the empty list have to exist before the loop starts?" |
| `AttributeError: 'NoneType'` | They kept the starter's `= None` and called `.append` | "`None` is not a list yet." |

**Why this exercise exists:** this loop is the mental model for the boolean mask in
section 2 and the `.loc` filter in section 3. Keep it on the board — you will point back
at it twice.
''')

solution(NB1, "free_titles = []")

md('''
### Practice 2 · Combine two array conditions

> Use `&` to find Web Development courses that are popular.

**Expected result:** `[ True False  True False False]`

**The one error worth staging.** `&` binds *tighter* than `==` in Python, so leaving the
parentheses out does not produce a wrong answer — it raises. Run the next cell live: it
is faster than explaining precedence in the abstract.

Students who write `and` instead of `&` get a different error ("truth value of an array
is ambiguous"). Both errors say the same thing: `and` asks one yes/no question, `&` asks
the question once per element.
''')

solution(NB1, "web_and_popular = (subjects ==")

code('''
# Live demo: the two mistakes, and what each one says.
for label, attempt in [
    ("no parentheses", lambda: subjects == "Web Development" & enrollments >= 1000),
    ("and instead of &", lambda: (subjects == "Web Development") and (enrollments >= 1000)),
]:
    try:
        attempt()
        print(f"{label}: no error (unexpected)")
    except Exception as exc:
        print(f"{label}: {type(exc).__name__}: {exc}")
''')

md('''
### Practice 3 · A paid, popular mask on the real catalog

> Find courses that are paid and have at least 100,000 subscribers, then show three columns with `.loc`.

**Expected result: 2 rows.** Warn them — a two-row answer looks like a bug to a student
who expected a table. It is the correct answer for this historical file.

**What to watch for**

- `df["is_paid"] == True` — works, but the column is already `True`/`False`. Ask what
  the comparison adds. (The hint in the student notebook now says this.)
- `df[df["is_paid"]][["course_title", ...]]` — also works, and is the habit that produces
  `SettingWithCopyWarning` the moment they try to assign. Steer to `.loc[mask, columns]`
  now, while it costs nothing.
- `and` instead of `&` again. Second sighting; let a student explain it this time.
''')

solution(NB1, 'paid_and_popular = df["is_paid"]')

md('''
### Practice 4 · One constrained question

> Which subject has the highest average subscribers among `Beginner Level` courses?

**Expected result:** Web Development, ≈7,864 mean subscribers, ahead of Business Finance
(≈2,331), Musical Instruments (≈1,627) and Graphic Design (≈1,310).

**What to watch for**

- **No filter.** They group the whole catalog and get the section-4 numbers instead. Ask
  what `Beginner Level` rows the answer is based on.
- **`.sum()` instead of `.mean()`.** The question says average. This is the whole point of
  section 4's warning, so make them say why the totals mislead — the demo cell below
  shows the ranking actually changing.
- **`level` spelled from memory.** `"Beginner"` returns an empty frame. `df["level"].unique()`
  is the rescue: the four values are `Intermediate Level`, `All Levels`, `Beginner Level`,
  `Expert Level`.
- **Reporting `.max()`** — that is the number, not the subject. `.index[0]` after sorting,
  or `.idxmax()`, gives the label.
''')

solution(NB1, 'beginner = df.loc[df["level"] == "Beginner Level"]')

code('''
# Live demo for the totals-versus-averages point: the ranking moves.
by_subject = df.groupby("subject")["num_subscribers"]
comparison = pd.DataFrame({
    "courses": df.groupby("subject").size(),
    "total_subscribers": by_subject.sum(),
    "average_subscribers": by_subject.mean().round(0),
})
print("Ranked by total:")
display(comparison.sort_values("total_subscribers", ascending=False))
print("Ranked by average:")
display(comparison.sort_values("average_subscribers", ascending=False))
''')

md('''
Business Finance is second on totals and third on averages, because it carries 968
courses to Graphic Design's 447. That is the sentence to get out of a student's mouth
before the break: *a bigger total can just mean a bigger catalog.*

### Optional extension · Price bands with `pd.cut`

Only if the room is ahead of schedule. `pd.cut` is the same `price_tier` ladder from
section 1.2 written as one call, which is a satisfying callback.

Two things students trip on: bin edges are **closed on the right**, so free courses need
a lower edge below zero (`-1`) to fall inside the first band; and the edges must
increase, so `bins=[0, 0, 100, inf]` raises. If someone asks about conditions that are
not ranges — say, price *and* subject — that is `np.select`, and it is fine to name it
without teaching it today.
''')

solution(NB1, 'df["price_tier"] = pd.cut(')

# --- Part 2 ----------------------------------------------------------------

md('''
## Part 2 · Pandas deep dive

Run the setup cell below before any Part 2 solution. It takes a few seconds — it replays
the whole student notebook, including its charts, with output suppressed.
''')

code(f'''run_student_notebook("{NB2}")
print("Membership rows:", len(membership))
print("Track rows:", len(tracks))
print("Joined rows:", len(joined))''')

md('''
### Exercise 1 · What is actually missing? (4 min)

**Expected result:** `title` and `artist` have **5 missing each**; `energy` and
`danceability` have **none**.

**The decision, not the count, is the exercise.** The follow-up question — *would you
drop every row with a missing field?* — is the one that matters. No: the rows with an
unknown artist still carry observed audio features, and the comparison is about energy by
genre. Dropping them would discard usable measurements to tidy a column nobody is
analysing.

**What to watch for**

- The `.dropna()` reflex, applied to the whole frame before looking at anything.
- `df.isna().sum().sum()` — one grand total, which answers nothing.
- Treating `"Unknown artist"` as a finding. It is a display label; it recovers no identity.
  If a student groups by `artist_display` later, that is where this bites.
''')

solution(NB2, "# Solution 1:")

md('''
### Exercise 2 · Check a join (6 min)

**Expected result:** 32,510 rows before and 32,510 after, every row `both`.

**Make them write the prediction down before running it.** The prediction is the exercise;
the merge is just the check. A student who cannot predict the row count does not yet know
what their table's rows are.

**What to watch for**

- **Merging the other way round** (`tracks.merge(membership, ...)`). It runs, and it
  silently changes what a row means — now one row per membership *of a track*, with the
  track table on the left. Ask: "what is one row now?"
- **`how="inner"`.** Also runs, also 32,510 rows here, and would silently drop
  unmatched memberships on any less tidy snapshot. The left join states the intent.
- **Dropping `validate=`** because it "didn't do anything". It did: it asserted the
  assumption. Answer the "what if the right side had two rows for one track" question
  concretely — one membership becomes two output rows, and every count and mean built on
  it is inflated. The duplicate-rows meme in the student notebook is there for this moment.
''')

solution(NB2, "# Solution 2:")

md('''
### Exercise 3 · Conditional grouping (8 min)

**Expected result at `energy >= 0.8`:** edm 3,433 · rock 2,232 · pop 1,774 · latin 1,586 ·
rap 1,146 · r&b 717.

**At `0.7`:** edm 4,659 · **pop 3,115 · rock 3,032** · latin 2,935 · rap 2,394 · r&b 1,591.

**The threshold change reorders the table.** Rock is behind pop at 0.7 and ahead of it at
0.8; across the demo cell below it climbs from 5th place at 0.6 to 2nd at 0.8, while edm
never moves and r&b never moves. This is the best thirty seconds in the notebook — run it
live. A "working definition" is not a neutral choice, and the ranking it produces is a
property of the cutoff as much as of the music.

**What to watch for**

- **Filtering after grouping** rather than before, or filtering `df` instead of `joined`.
- **Reading counts as popularity.** edm leads partly because edm has more associations
  overall. Push them to the share: `count / association_count` from `summary`.
- **Causal language** — "edm makes people energetic". These are playlist placements
  labelled by playlist genre, in one 2020 snapshot.
''')

solution(NB2, "# Solution 3, step 1")
solution(NB2, "# Solution 3, step 2")

code('''
# Live demo: the ranking is a property of the threshold.
ranks = {}
for threshold in (0.6, 0.7, 0.8, 0.9):
    counts = joined.loc[joined["energy"] >= threshold].groupby("genre").size()
    ranks[f">= {threshold}"] = counts.rank(ascending=False).astype(int)
display(pd.DataFrame(ranks).sort_values(">= 0.8"))
''')

md('''
### Exercise 4 · Reshape and interpret (7 min)

**Expected result:** one row of `genre_feature_long` is **one genre–measure mean** — for
example, the mean danceability of pop associations.

By mean danceability: rap 0.718 · latin 0.714 · r&b 0.670 · edm 0.655 · pop 0.639 ·
rock 0.520. By mean energy: edm 0.801 · rock 0.733 · latin 0.711 · pop 0.701 · rap 0.651 ·
r&b 0.591. **Rock is second on energy and last on danceability** — a useful reminder that
the two indices are different constructs, not two ways of saying "lively".

**What to watch for**

- **Melting the count columns too**, producing rows where `measure` is
  `association_count`. Technically long, semantically nonsense: means and counts are not
  the same kind of quantity.
- **"Long format lost information."** Nothing was lost; the same numbers are addressed by
  `(genre, measure)` instead of by column name. `pivot_table` goes back.
- **Comparing across measures.** A 0.1 difference in energy is not a 0.1 difference in
  danceability. Both are bounded 0–1, which is why they share an axis — that is a display
  convenience, not a claim of equivalence.
- **A caption with no limitation.** The exercise asks for one result *and* one snapshot
  limitation. Accept nothing without both.
''')

solution(NB2, "# Solution 4, step 1")
solution(NB2, "# Solution 4, step 2")
solution(NB2, "# Solution 4, step 3")

md('''
### Optional extension · Sampling and correlation (after class)

Not a learning gate, and not worth displacing the merge or reshape segment. If a student
asks in class, the worked version is below.

The correlations are small and their **signs differ by genre** — about -0.15 in edm, rock
and rap, +0.12 to +0.16 in latin and r&b, and -0.03 in pop. That is the teaching point:
there is no single "energy–danceability relationship" here to report.

A 2,000-row sample leaves roughly 330 rows per genre and moves the estimates by up to
~0.11 — edm's weak negative association all but disappears — even though the signs happen
to survive. Magnitudes from a few hundred rows are not something to quote.
''')

code('''
# Worked version of the optional starter.
sample = joined.sample(n=min(2_000, len(joined)), random_state=2026)

full_corr = joined.groupby("genre")["energy"].corr(joined["danceability"])
sample_corr = sample.groupby("genre")["energy"].corr(sample["danceability"])

comparison = pd.DataFrame({
    "full_snapshot": full_corr,
    "sample_2000": sample_corr,
    "rows_in_sample": sample.groupby("genre").size(),
})
display(comparison.round(3))
''')

md('''
## Appendix cells in the student notebook

The student notebook ends with two appendix cells: the regular-expression version of the
date-precision check, and the grouped-`nunique` version of the track-consistency check.
Both finish by asserting they reach the same conclusion as the short versions in the main
path.

They are labelled *for later, not for today*. If a student runs ahead and asks, the honest
framing is: the short version is exact **because the class snapshot is frozen and clean**;
the appendix version is what you write when you do not control the file. Do not teach
regular expressions today.

## Exit-ticket answers you are listening for

**1. List vs `ndarray` vs `DataFrame`.** A list holds any objects and needs a loop to
compute; an `ndarray` holds one dtype in a shape and computes on every element at once;
a `DataFrame` adds labelled columns of possibly different dtypes plus an index, so rows
and columns can be selected by name. Accept anything that names *loop → vectorised →
labelled*; a student who only says "a DataFrame is a table" has not got it yet.

**2. One limitation.** Any of: a row is a track–playlist–genre association, so a popular
song counts more than once; the left join assumes `track_id` is unique in the track table
and validation is what enforces it; `2018` is a real release date at year precision, and
parsing it to 1 January invents a day; `price_times_enrollments_proxy` is a constructed
proxy, not observed revenue; the Spotify data is a 2020 snapshot and says nothing about
today.

Weak answer to push on: "the data might be biased." Ask *which* row, *which* assumption.
''')

# ---------------------------------------------------------------------------

notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3"},
        "colab": {"name": "M1_instructor_solutions_2026.ipynb"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}
out = ROOT / "notebooks" / "M1_instructor_solutions_2026.ipynb"
out.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n")
print(f"Wrote {out} ({len(cells)} cells, "
      f"{sum(c['cell_type'] == 'code' for c in cells)} code)")
