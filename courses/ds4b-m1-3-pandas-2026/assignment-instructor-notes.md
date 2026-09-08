# Assignment instructor notes — do not hand out

Companion to [assignment.md](assignment.md). Contains the planted flaws, the numbers a
correct submission lands on, and what to do with the answers you will actually receive.

## The design in one paragraph

The session taught four checks — state the grain, audit before deciding, validate a
merge, report counts beside means. A check only teaches if something fails it. So the
assignment ships a lookup table with three real key problems, asks a question whose
obvious computation is subtly wrong, and picks a comparison whose headline result
reverses when you move the threshold. A group that skips the discipline gets a
plausible, confidently wrong answer, and the video is where that becomes visible.

## Planted flaw 1 — the lookup table

`data/M1_2026/subgenre_families.csv` maps 24 subgenres to 6 families. Families cut
across `playlist_genre` deliberately (`dance pop` is a pop subgenre in the
`club_electronic` family; `latin hip hop` is a latin subgenre in `hiphop_lineage`), so
the family label cannot be reconstructed without the join.

**It has 24 rows and the data has 24 subgenres.** That coincidence is the trap: a group
that checks only `len(lookup) == df["subgenre"].nunique()` concludes the table is fine
and moves on. It contains three distinct problems:

| # | Problem | Where | Effect |
|---|---|---|---|
| 1 | `dance pop` appears twice, as `club_electronic` **and** `pop_craft` | duplicate key | `validate="many_to_one"` raises `MergeError`; without it the merge silently adds **1,298 rows** |
| 2 | `neo soul` is written `"Neo Soul "` — title case, trailing space | key that looks present but does not match | **1,637 rows** unmatched, fixable by cleaning the key |
| 3 | `tropical` is absent entirely | missing key | **1,288 rows** unmatched, not fixable — a decision is required |

Problems 2 and 3 both surface as `left_only` in the indicator, and telling them apart is
the analytical work. Problem 2 is the payoff for the header-cleaning step the session
notebook says is unnecessary on clean data.

**Expected numbers.** On a membership table of 32,833 rows (track–playlist–genre–subgenre):

- Unvalidated left merge: 34,131 rows, +1,298.
- `validate="many_to_one"` raises: *Merge keys are not unique in right dataset*.
- Unmatched before any fix: 2,925 rows — `neo soul` 1,637, `tropical` 1,288.
- After `.str.strip().str.lower()` on both keys and a decision on the duplicate: 32,833
  rows, `tropical` (1,288) still unmatched.

**The duplicate has no single right answer**, which is the point. Dropping `pop_craft`,
dropping `club_electronic`, or keeping both and reporting `dance pop` twice are all
defensible — what matters is that the choice and its cost are stated, not that they
match ours. What
is *not* defensible is `drop_duplicates()` with no comment, which silently keeps
whichever row sorted first.

## Planted flaw 2 — measuring reach

Question 1 asks for the number of playlists each track appears on. The two computations that
disagree:

```python
membership.groupby("track_id").size()                    # counts rows
membership.groupby("track_id")["playlist_id"].nunique()  # counts playlists
```

How far they differ depends on the grain the group chose. There are 32,251 distinct
track–playlist pairs; a second genre label adds 259 rows and a second subgenre label adds
a further 323.

| Membership grain | Rows | Tracks where `size` ≠ `nunique` | Mean reach, `size` vs `nunique` |
|---|---:|---:|---|
| track–playlist–genre–subgenre | 32,833 | 511 | 1.158 vs 1.137 |
| track–playlist–genre | 32,510 | 259 | 1.146 vs 1.137 |

Either way the gap is small enough that nobody notices without checking, and
`nunique` is the number that answers the question as asked. The session's own
pairs-versus-pairs-with-genre cell is the direct preparation.

A group that keeps `subgenre` in the grain has 32,833 membership rows; genre only gives
32,510. **These are not equally usable here.** The family lookup joins on `subgenre`, so a
group that follows Notebook 2's recipe exactly and drops `subgenre` in Question 1 cannot do
Question 2 without going back. That rework is legitimate — the grain has to support the
question you are going to ask, and the lookup is named in the setting before Question 1 —
but it is the most likely place for a group to lose an evening. If you hear it, the nudge
is "what does Question 2 join on?", not the answer.

## Expected answer to Question 3

Reach distribution: 25,538 tracks on 1 playlist, 2,113 on 2, 481 on 3, 130 on 4, 51 on 5,
34 on 6, 7 on 7, 2 on 8.

| Cut-off | n travelling | energy (no / yes) | danceability (no / yes) | popularity (no / yes) |
|---|---:|---|---|---|
| ≥ 2 | 2,818 | 0.698 / 0.705 | 0.652 / 0.666 | 37.1 / **59.5** |
| ≥ 3 | 705 | 0.698 / 0.708 | 0.653 / 0.669 | 38.5 / **71.4** |
| ≥ 5 | 94 | 0.699 / **0.641** | 0.653 / 0.700 | 39.2 / **84.5** |

Three things to listen for:

1. **The audio features barely move.** 0.698 → 0.705 on energy is not a finding. Groups
   that report it as one have not asked whether the difference is worth acting on.
2. **Popularity moves enormously**, and it is the variable nobody was asked about. The
   good submissions notice, and then notice that the direction is unclear: curators add
   popular tracks, and being on many playlists makes tracks popular. This is the best
   available limitation and the strongest signal of a group that understood the session.
3. **The energy comparison reverses at ≥ 5** — travelling tracks become *less* energetic,
   on 94 tracks. A group that picked ≥ 5 and stopped will report the opposite headline
   from a group that picked ≥ 2. Both are "right"; what matters is that they showed the
   sensitivity, not which cut-off they chose.

### The second grain trap, inside Question 3

Grouping by family needs one family per track, and **1,614 tracks have more than one**,
because a track on playlists of different subgenres lands in different families. Grouping
naively double-counts them: 2,027 extra rows.

It is not evenly spread, and this is the part worth teaching:

| | share of tracks in more than one family |
|---|---:|
| Travelling tracks (reach ≥ 2) | **52.0%** |
| Non-travelling tracks | 0.6% |

A track that travels is far more likely to cross families — that is close to what
travelling means. So the naive per-family comparison inflates the travelling side of every
family, and it does so structurally rather than by accident. It is the Question 1 lesson at
a new level: *decide what one row is before you group*.

Very few groups will catch this unprompted. It is the best follow-up question you have for
a group whose Question 3 is otherwise clean, and a good thing to put on the screen in
class.

### The aggregate hides the biggest family

At a cut-off of 2, overall energy rises 0.698 → 0.705. In `club_electronic`, the largest
family, it **falls** 0.797 → 0.749 on 1,079 travelling tracks; every other family rises or
stays flat. A group that reports only the aggregate reports the opposite of what happens in
the family carrying the most rows.

`latin_rhythm` also loses `tropical` entirely to the unmatched keys, so its counts drop — a
group that handled Question 2 honestly will see that and should say so.

### Release year, and why the audit is no longer decorative

Question 1's date audit used to produce a column nothing downstream touched. Question 3
now asks whether the two groups differ in release year, so the audit has to be right.

Precision is not confounded — 94.1% of tracks carry a full day string in **both** groups —
so a year derived from the first four characters is safe to use, which is the audit's
honest conclusion rather than an assumption.

The comparison itself returns a **null, and that is the good answer**:

| | mean release year | median | tracks |
|---|---:|---:|---:|
| Not travelling | 2011.2 | 2016 | 25,538 |
| Travelling (≥ 2) | 2010.0 | 2016 | 2,818 |

The groups are the same age. So recency does **not** explain the +22 popularity gap, and a
group that checks this has *strengthened* its own result by ruling out the obvious
confound. That is the move worth praising in class: a check that comes back negative is
still a check.

A curious group that bins the years finds something better, and non-obvious:

| Era | tracks | mean popularity | share travelling |
|---|---:|---:|---:|
| pre-1990 | 2,166 | 42.9 | **16.0%** |
| 1990s | 2,153 | 37.5 | 9.3% |
| 2000s | 4,135 | 32.0 | 6.6% |
| 2010–14 | 4,977 | 31.9 | 8.0% |
| 2015–19 | 14,925 | 43.6 | 10.7% |

Popularity is U-shaped, not increasing, and **old catalogue tracks travel most**. The
intuitive story — newer means more popular means more playlists — is simply wrong here.
Worth putting on screen if a group finds it.

## What you will actually receive

- **A confident 0.7-versus-0.65 headline** with no counts and no sensitivity. The most
  common submission you will get, and the one most worth showing the class.
- **`drop_duplicates()` on the lookup with no comment.** Ask in the video which of the two
  `dance pop` rows survived and why.
- **`.dropna()` early**, dropping the unmatched rows before anyone counts them. The count
  of what you discarded is the deliverable, not the tidy frame.
- **`size()` for reach**, undetected. Not fatal — the difference is small — but the check
  was the task. Look for whether they checked, not for which number they got.
- **Causal drift**: "travelling makes tracks more popular". Push back in feedback.
- **A notebook that does not restart-and-run**, usually because the lookup fix was applied
  in a cell that was later edited. This is why the checklist item exists.

## Verified by cold-solving it

The three questions were worked through in order against the real files, without pre-known
answers, on 8 September 2026. Everything above is what that produced. Three things came out
of it that were not visible when the assignment was designed: the grain constraint in
Question 2, the multi-family double count, and the `club_electronic` reversal.

Two mechanics worth knowing before you help anyone:

- `validate="many_to_one"` names the offending key in its error text — pandas prints
  `Duplicates in right: dance pop`. Flaw 1 is therefore handed to the group; the work is
  deciding what to do about it, not finding it.
- `set(lookup["subgenre"]) - set(df["subgenre"])` prints `['Neo Soul ']`, trailing space
  visible inside the quotes. That is the intended discovery route for flaw 2, and the one
  hint worth giving a stuck group.

### One deliberate change after the cold solve

The brief used to tell groups outright that two ways of counting reach *disagree on this
dataset*, which turned a discovery into an instruction. It now says only that there is
more than one way to count and asks for the check. **Expect fewer groups to catch it** —
possibly none. That is the intended trade: the ones who check have actually learned
something, and for everyone else it becomes the sharpest five minutes of the debrief. Have
the `01R0Xdwje645C6xFCnMRvm` example ready — same track, same playlist, twice, under
`classic rock` and `hard rock`.

Question 3 also asks groups to say what a better grouping than the supplied families would
have been. The taxonomy is invented, they can tell, and inviting the criticism is better
than hoping nobody notices.

## Feedback, not marks

The assignment is not graded, and the brief says so on the first line. What replaces the
rubric is the "what we will be looking at" list in the brief and the videos themselves.

- **The videos are the session material.** Watch them before the next session and pick two
  or three to talk about — ideally one group that found the duplicate key by prediction
  and one that found it by the row count looking wrong afterwards. Both are wins; they are
  different wins.
- **Feedback lands on the decision, not the number.** A group that chose a different grain,
  said so, and carried it consistently did better work than one that reproduced our table
  by accident. Say that out loud, because ungraded work makes students look for the
  "right" answer to compare against.
- **The video is where generated code becomes visible.** No marks to withhold, so the
  lever is the conversation: ask the group to explain a line on screen. That is also the
  honest framing to give them — the exam is where explaining your own code counts.
- **Chase missing videos rather than notebooks.** A notebook with no video is the failure
  mode that costs the next session its material.

## Effort

The window is about 40 hours of group work including the recording, but **the brief does
not state an hours figure and should not**: quoting one invites groups to pad to it, and
none of the three questions is long to code. The time goes into the decisions.

If groups report spending far more than the window, the usual cause is Question 2 — they
treat the broken merge as an obstacle to the assignment rather than as the assignment. Say
so in class if you hear it twice.

Question 3 previously carried a fourth part, a self-chosen question. It was cut to keep
the problem set at three: it added scope without exercising anything the other two do not
already cover.

## Before handing out

- [ ] Confirm the deadline: the brief says **Friday 18 September 2026, 23:59**
- [ ] Confirm the hand-in channel and how they submit the video link
- [ ] Confirm group size — the video asks every member to present one decision, which
      works for 3–5 and needs adjusting outside that range
- [ ] Decide whether the starter notebook is handed out or only linked
- [ ] Decide where the videos go, and tell groups — you need to be able to watch them all
      before the next session
