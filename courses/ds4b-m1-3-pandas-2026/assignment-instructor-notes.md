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
defensible — the mark is for stating the choice and its cost, not for matching us. What
is *not* defensible is `drop_duplicates()` with no comment, which silently keeps
whichever row sorted first.

## Planted flaw 2 — measuring reach

Task 3 asks for the number of playlists each track appears on. The two computations that
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
32,510. Both are defensible if stated. Neither is defensible if the row count is never
mentioned.

## Expected answer to Parts A and B

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
   from a group that picked ≥ 2. Both are "right"; the mark is for showing the sensitivity
   rather than for the cut-off chosen.

Part B: several families are small once you split by travelling, and `latin_rhythm` loses
`tropical` entirely to the unmatched keys — a group that handled task 4 honestly will see
its family counts drop and should say so.

## What you will actually receive

- **A confident 0.7-versus-0.65 headline** with no counts and no sensitivity. Weight-20
  section, mark it there.
- **`drop_duplicates()` on the lookup with no comment.** Ask in the video which of the two
  `dance pop` rows survived and why.
- **`.dropna()` early**, dropping the unmatched rows before anyone counts them. The count
  of what you discarded is the deliverable, not the tidy frame.
- **`size()` for reach**, undetected. Not fatal — the difference is small — but the check
  was the task. Look for whether they checked, not for which number they got.
- **Causal drift**: "travelling makes tracks more popular". Push back in feedback.
- **A notebook that does not restart-and-run**, usually because the lookup fix was applied
  in a cell that was later edited. This is why the checklist item exists.

## Marking mechanics

The rubric is in the student brief; the weights are 20/25/20/10/15/10. Two notes:

- **Mark the video when it disagrees with the notebook.** Stated in the brief. It is the
  only practical check on generated code, and it is why every member presents a decision
  rather than a section.
- **Do not reward matching our numbers.** A group that chose a different grain, said so,
  and carried it consistently should out-score one that reproduced our table by accident.

## Effort budget

The brief's per-task hours total about 33, leaving room for integration and rehearsal
inside 40. If groups report spending far more, the usual cause is task 4 — they treat the
broken merge as an obstacle rather than as the assignment. Say so in class on the day
after hand-out if you hear it twice.

## Before handing out

- [ ] Confirm the deadline: the brief says **Friday 18 September 2026, 23:59**
- [ ] Confirm the hand-in channel and how they submit the video link
- [ ] Confirm group size — the video asks every member to present one decision, which
      works for 3–5 and needs adjusting outside that range
- [ ] Decide whether the starter notebook is handed out or only linked
