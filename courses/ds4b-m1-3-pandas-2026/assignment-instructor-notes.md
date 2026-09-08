# Assignment notes for you, not for students

Companion to [assignment.md](assignment.md). The traps, the numbers a good submission
lands on, and what to do with what you'll actually get back.

## Why it's built like this

The session taught four checks: state the grain, audit before deciding, validate a merge,
put counts next to means. A check only teaches you anything if something fails it, and in
class nothing did. Every check passed, which is comfortable and slightly useless.

So this assignment breaks things on purpose. The lookup table has three real key problems.
The obvious way to count playlists is quietly wrong. The headline comparison flips sign
depending on where you draw the line. A group that skips the discipline gets a plausible,
confident, wrong answer, and the video is where that shows up.

## Trap 1: the lookup table

`data/M1_2026/subgenre_families.csv` maps 24 subgenres to 6 families. The families cross
`playlist_genre` on purpose (`dance pop` is a pop subgenre sitting in `club_electronic`,
`latin hip hop` is a latin subgenre in `hiphop_lineage`), so there's no way to reconstruct
the label without doing the join.

It has 24 rows. The data has 24 subgenres. That coincidence is deliberate: a group that
checks `len(lookup) == df["subgenre"].nunique()` decides the table is fine and moves on.
It isn't fine. There are three separate problems in it.

| # | Problem | Kind | Effect |
|---|---|---|---|
| 1 | `dance pop` appears twice, once as `club_electronic` and once as `pop_craft` | duplicate key | `validate="many_to_one"` raises `MergeError`. Without it, the merge quietly adds **1,298 rows** |
| 2 | `neo soul` is written `"Neo Soul "`, title case with a trailing space | looks present, doesn't match | **1,637 rows** unmatched, fixable by cleaning the key |
| 3 | `tropical` isn't in the file at all | missing key | **1,288 rows** unmatched, no fix available, only a decision |

Problems 2 and 3 both show up as `left_only` in the indicator. Telling them apart is the
work. Problem 2 is where the header-cleaning step pays off, the one Notebook 2 says you
don't need on clean data.

Numbers, on a membership table of 32,833 rows (track, playlist, genre, subgenre):

- Unvalidated left merge: 34,131 rows, so +1,298.
- `validate="many_to_one"` raises *Merge keys are not unique in right dataset*.
- Unmatched before any fix: 2,925 rows. `neo soul` 1,637, `tropical` 1,288.
- After `.str.strip().str.lower()` on both keys plus a decision about the duplicate:
  32,833 rows, with `tropical` (1,288) still unmatched.

The duplicate has no single right answer, deliberately. Drop `pop_craft`, drop
`club_electronic`, or keep both and let `dance pop` appear twice: all defensible. What
matters is that they say which they chose and what it cost, not that it matches ours. The
one bad answer is a bare `drop_duplicates()` with no comment, which silently keeps
whichever row happened to sort first.

## Trap 2: counting playlists

Question 1 asks how many playlists each track appears on. The two candidates:

```python
membership.groupby("track_id").size()                    # counts rows
membership.groupby("track_id")["playlist_id"].nunique()  # counts playlists
```

How badly they differ depends on the grain the group picked. There are 32,251 distinct
track-playlist pairs. A second genre label adds 259 rows, a second subgenre label another
323.

| Membership grain | Rows | Tracks where `size` ≠ `nunique` | Mean reach, `size` vs `nunique` |
|---|---:|---:|---|
| track, playlist, genre, subgenre | 32,833 | 511 | 1.158 vs 1.137 |
| track, playlist, genre | 32,510 | 259 | 1.146 vs 1.137 |

Either way the gap is small enough to go unnoticed, and `nunique` answers the question as
asked. The session's own pairs-versus-pairs-with-genre cell is the direct preparation for
spotting it.

One thing to watch: the two grains are not equally usable here. The lookup joins on
`subgenre`, so a group that follows Notebook 2's recipe exactly and drops `subgenre` in
Question 1 can't do Question 2 without going back. That rework is fair (the grain has to
support the question, and the lookup is named before Question 1 starts) but it's the
likeliest place to lose an evening. If you hear about it, the nudge is "what does Question
2 join on?" rather than the answer.

## What Question 3 should produce

Reach distribution: 25,538 tracks on one playlist, 2,113 on two, 481 on three, 130 on
four, 51 on five, 34 on six, 7 on seven, 2 on eight.

| Cut-off | n travelling | energy (no / yes) | danceability (no / yes) | popularity (no / yes) |
|---|---:|---|---|---|
| ≥ 2 | 2,818 | 0.698 / 0.705 | 0.652 / 0.666 | 37.1 / **59.5** |
| ≥ 3 | 705 | 0.698 / 0.708 | 0.653 / 0.669 | 38.5 / **71.4** |
| ≥ 5 | 94 | 0.699 / **0.641** | 0.653 / 0.700 | 39.2 / **84.5** |

Three things to listen for.

The audio features barely move. Going from 0.698 to 0.705 on energy is not a finding, and
a group reporting it as one hasn't asked whether it's big enough to act on.

Popularity moves enormously, and it's the variable nobody asked about. Good submissions
notice, then notice the direction is unclear: curators add popular tracks, and sitting on
many playlists makes tracks popular. This is the best limitation available in the data and
the clearest sign a group understood the session.

Energy reverses at ≥ 5. Travelling tracks become less energetic, on 94 tracks. A group
that picked ≥ 5 and stopped reports the opposite headline from a group that picked ≥ 2.
Both are "right". Showing the sensitivity is what counts, not the cut-off.

### The second grain trap, hidden in Question 3

Grouping by family needs one family per track, and 1,614 tracks have more than one,
because a track on playlists of different subgenres lands in different families. Group
naively and you double-count them: 2,027 extra rows.

The double count isn't evenly spread, and that's the interesting bit:

| | in more than one family |
|---|---:|
| Travelling tracks (reach ≥ 2) | **52.0%** |
| Non-travelling tracks | 0.6% |

A track that travels is far more likely to cross families, since crossing families is
close to what travelling means. So the naive per-family comparison inflates the travelling
side of every family, structurally, not by bad luck. It's the Question 1 lesson again one
level up: work out what one row is before you group.

Almost nobody will catch this on their own. It's your best follow-up question for a group
whose Question 3 is otherwise clean, and worth putting on the projector.

### The aggregate hides the biggest family

At a cut-off of 2, overall energy rises from 0.698 to 0.705. Inside `club_electronic`, the
largest family, it falls from 0.797 to 0.749 across 1,079 travelling tracks. Every other
family rises or stays flat. Report only the aggregate and you report the opposite of what
happens in the family with the most rows in it.

`latin_rhythm` also loses `tropical` to the unmatched keys, so its counts drop. A group
that handled Question 2 honestly will see that and should mention it.

### Release year, and why the audit isn't decorative any more

The date audit in Question 1 used to produce a column nothing downstream touched. Question
3 now asks whether the two groups differ in release year, so the audit has to be right.

Precision isn't confounded: 94.1% of tracks carry a full day string in both groups. A year
taken from the first four characters is safe, and that's a conclusion the audit earns
rather than an assumption it makes.

The comparison comes back null, and null is the good answer here:

| | mean release year | median | tracks |
|---|---:|---:|---:|
| Not travelling | 2011.2 | 2016 | 25,538 |
| Travelling (≥ 2) | 2010.0 | 2016 | 2,818 |

Same age, near enough. Recency doesn't explain the +22 popularity gap, so a group that
runs this check has strengthened its own result by ruling out the obvious confound. Praise
that in class. A check that comes back negative is still a check, and students rarely
believe this until someone says it.

A group that bins the years finds something better:

| Era | tracks | mean popularity | share travelling |
|---|---:|---:|---:|
| pre-1990 | 2,166 | 42.9 | **16.0%** |
| 1990s | 2,153 | 37.5 | 9.3% |
| 2000s | 4,135 | 32.0 | 6.6% |
| 2010-14 | 4,977 | 31.9 | 8.0% |
| 2015-19 | 14,925 | 43.6 | 10.7% |

Popularity is U-shaped rather than rising, and old catalogue tracks travel most. The
intuitive story (newer, so more popular, so more playlists) is just wrong here. Put it on
the projector if someone finds it.

## What you'll actually get back

A confident "0.70 versus 0.65" headline with no counts and no sensitivity. This will be
the most common submission, and it's the most useful one to walk through in class.

`drop_duplicates()` on the lookup, uncommented. In the video, ask which of the two `dance
pop` rows survived and why.

An early `.dropna()`, throwing away the unmatched rows before anyone counts them. The
count of what got discarded was the deliverable. The tidy frame wasn't.

`size()` for reach, undetected. Not fatal, the difference is small, but checking was the
task. Look for whether they checked, not for which number came out.

Causal drift: "travelling makes tracks more popular." Push back.

A notebook that won't restart and run, usually because the lookup fix lives in a cell that
got edited afterwards. Hence the checklist item.

## This was cold-solved before you got it

The three questions were worked through in order against the real files on 8 September
2026, without knowing the answers in advance. Everything above came out of that. Three
things only showed up then and weren't visible when the assignment was designed: the grain
constraint in Question 2, the multi-family double count, and the `club_electronic`
reversal.

Two mechanics worth knowing before you help anyone:

`validate="many_to_one"` names the offending key in its error text. Pandas prints
`Duplicates in right: dance pop`, so trap 1 is handed to the group. The work is deciding
what to do about it, not finding it.

`set(lookup["subgenre"]) - set(df["subgenre"])` prints `['Neo Soul ']` with the trailing
space visible inside the quotes. That's the intended route to trap 2 and the one hint
worth giving a group that's stuck.

### One thing was made harder on purpose

The brief used to say outright that two ways of counting reach disagree on this dataset,
which turns a discovery into an instruction. Now it only says there's more than one way to
count and asks for the check. Expect fewer groups to catch it, possibly none. That's the
trade: whoever checks has actually learned something, and for everyone else it's the
sharpest five minutes of the debrief. Have this example ready:
`01R0Xdwje645C6xFCnMRvm`, same track, same playlist, listed twice, once under
`classic rock` and once under `hard rock`.

Question 3 also asks what a better grouping than our invented families would be. Students
can tell it's invented, so asking for the criticism beats hoping nobody brings it up.

## Feedback instead of marks

It isn't graded, and the brief says so in the first table. What replaces a rubric is the
"what we'll notice" list in the brief, plus the videos.

Watch the videos before the next session and pick two or three to discuss. Ideally one
group that predicted the duplicate key and one that found it afterwards because the row
count looked wrong. Both are wins, just different ones.

Aim feedback at the decision, not the number. A group that chose a different grain, said
so, and stayed consistent did better work than one that reproduced our table by accident.
Say this out loud, because ungraded work sends students hunting for a right answer to
compare themselves against.

The video is where generated code becomes visible. There are no marks to withhold, so the
lever is just conversation: ask someone to explain a line on screen. That's also the
honest framing to give them, since the exam is where explaining your own code starts
counting.

Chase missing videos harder than missing notebooks. A notebook with no video is the
failure mode that costs the next session its material.

## Effort

The window is roughly 40 hours of group work including the recording. The brief doesn't
say so and shouldn't: quote an hours figure and groups pad to it. None of the three
questions is much code.

If groups report spending far more than that, it's usually Question 2, because they're
treating the broken merge as something blocking the assignment rather than as the
assignment. Say so in class if you hear it twice.

Question 3 used to carry a fourth part, a question of the group's own choosing. Cut, to
keep it at three. It added scope without exercising anything the other two don't.

## Before you hand it out

- [ ] Confirm the deadline. The brief says Friday 18 September 2026, 23:59
- [ ] Confirm the hand-in channel, and how the videos get to you
- [ ] Confirm group size. The video asks everyone to present one decision, which works for
      3 to 5 and needs rethinking outside that
- [ ] Decide whether the starter notebook goes out or just gets linked
