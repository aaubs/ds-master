# Student reference: session 03

What each test answers, how to report a comparison, and where to read more. Keep this open
while you work through the two notebooks.

## The one idea

A p value tells you whether a difference exists, given your sample size. It says nothing
about whether the difference is big enough to care about.

On a table with thirty thousand rows, almost every difference clears any threshold you pick,
so "significant" stops carrying information almost immediately. The number that carries the
finding is the effect size.

## Which test, and what it answers

| Situation | Test | What it answers | The size that goes with it |
|---|---|---|---|
| Two groups, one numeric column | `stats.ttest_ind(a, b, equal_var=False)` | Would a gap this large be surprising if the two groups really had the same mean? | Cohen's d |
| Three or more groups, one numeric column | `stats.f_oneway(*groups)` | Is any group different from the others? | eta squared |
| Two categorical columns | `stats.chi2_contingency(table)` | Are the two columns related, or independent? | Cramer's V |

`equal_var=False` gives you Welch's t-test, which does not assume the two groups have the
same spread. Use it by default. The version that assumes equal spread is a special case you
rarely have grounds for.

None of these tests tells you which direction, which pair, or how much. They tell you whether
a pattern is distinguishable from noise at your sample size. That is a smaller claim than it
sounds.

## Effect sizes, and the numbers to expect

Cohen's d is the difference between two means, divided by the pooled standard deviation.

```python
def cohens_d(a, b):
    pooled_sd = np.sqrt((a.std() ** 2 + b.std() ** 2) / 2)
    return (a.mean() - b.mean()) / pooled_sd
```

The conventional labels are 0.2 small, 0.5 medium, 0.8 large. They are conventions, not laws.
Their main use is showing you how far below them most real results sit.

Eta squared is the share of variation in the numeric column that sits between groups rather
than within them. In our data, genre explains about 14 percent of the variation in energy,
which means about 86 percent of it is variation between tracks inside the same genre.

Cramer's V rescales chi-square to run from 0 to 1. Anything around 0.1 is weak. A weak overall
V can still hide one category that is genuinely different, so look at the table of shares as
well as the single number.

## How to report a comparison

Three things, in this order:

1. the size of the difference, in the units you measured;
2. how many observations it rests on;
3. the p value, last, as the smallest of the three claims.

Good: "Mean energy is 0.80 for edm and 0.73 for rock, across 6,043 and 4,951 rows, a gap of
0.07 and d = 0.41 (p < 0.001)."

Not good: "The difference was significant (p < 0.001)."

The first sentence can be argued with. The second cannot, which is why it is worse.

## Things that will bite you

**Reporting a mean for a bimodal column.** Look at the histogram first. If the column has two
humps, the mean sits in the valley between them, where no row is.

**Plotting 28,000 points.** You get a block of ink. Sample with a fixed `random_state` and say
in the caption that you did.

**Using the wrong frame.** `songs` has a row per track-on-a-playlist, so popular songs are
counted several times. `tracks` has one row per song. Neither is correct in general; they
answer different questions.

**Comparing groups of very different sizes.** A difference between a group of 40 and a group of
40,000 tells you more about sample size than about the world. Print the counts.

**Treating a correlation as a finding.** Energy and loudness correlate at 0.68, and that is
close to a tautology. Energy and danceability correlate at -0.08, and that is the interesting
one, because the English words suggest otherwise.

**Chained cleaning without a note.** If you drop rows, print how many you dropped, before and
after.

## Reading

- pandas, [Exploratory data analysis tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) for the mechanics of describing and summarising.
- SciPy, [statistical functions reference](https://docs.scipy.org/doc/scipy/reference/stats.html). The docstrings for `ttest_ind`, `f_oneway` and `chi2_contingency` are short and say exactly what each one assumes.
- seaborn, [the tutorial](https://seaborn.pydata.org/tutorial.html). Every chart in session 03 is one seaborn call plus, occasionally, a matplotlib line on top.
- DataCamp practice for this session is listed in the [module practice guide](../ds4b-m1-3-pandas-2026/datacamp-practice.md).

If you want one longer read on why the significance half of this session is the way it is,
search for the American Statistical Association's 2016 statement on p values. It is three
pages, it is written for non-statisticians, and it says more carefully what we say in class.
