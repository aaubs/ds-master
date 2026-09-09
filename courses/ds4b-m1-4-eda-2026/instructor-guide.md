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

**Four columns, four situations.** The histogram panel in part 1 question 3 draws the mean on
each distribution in orange. Danceability is a single hump and its mean is fine. Energy is
skewed so the mean sits below the bulk. Valence covers the whole range with a broad plateau, so
0.51 describes nobody in particular. Tempo has two clusters, near 95 and near 125, because
produced music sticks to conventional tempos, and the mean lands on the taller one while the
smaller disappears.

Ask what the mean of the tempo column is describing before moving on. It is the fastest way to
make the point that one number per column is a choice, not a summary.

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

## The music, which is the point of using this data at all

The dataset carries real Spotify track IDs, so `https://open.spotify.com/track/<id>` opens the
song. Both notebooks have a `listen()` helper that renders the links as a clickable column.
Have Spotify open on the projector.

Five worth playing, in the order they come up:

**"Rain Forest and Tropical Beach Sound"**, by Nature Sounds Nature Music, is the highest-energy
track in the file at 1.00.
`https://open.spotify.com/track/5CwOUooch74h0XarhDfAQK`

**"Relaxing Crickets And Waterfall"** is the lowest.
`https://open.spotify.com/track/5iAB4tlYseBES4MKqgY4KG`

Play four seconds of the rainforest, then ask the room what "energy" measures. Somebody will
have written "edm is the most energetic genre" in session 02 and meant something about
excitement. It is loudness, density and noisiness, and a downpour scores maximum on all three.

**"Hi, How're You Doin'?"** is four seconds long with a tempo of zero, and it holds three
records at once: shortest, least danceable, saddest.
`https://open.spotify.com/track/51w6nRCU68klqNfYaaVP2j`

**"Low Rider"** by War is valence 1.00, the happiest thing in the dataset, and here the model
is obviously right. Worth playing straight after the rainforest so the room sees that the
measures are not simply broken.
`https://open.spotify.com/track/7kigmgx2tJJsZHKaa2QC0w`

**"bad guy"** by Billie Eilish appears under five different genres: edm, latin, pop, r&b and
rock. 265 tracks sit in three or more. If anyone still thinks genre is a property of a song
rather than of a playlist, this settles it.
`https://open.spotify.com/track/2Fxmhks0bxGSBdJ92vM42m`

## The break quiz

Run this at 15:05, as the second break rather than before it. Groups of three or four, five
minutes, and it does real work.

**The question.** Write down Spotify's ten most-streamed artists worldwide in 2025, in any
order. A point per correct name.

**The answer**, from Spotify Wrapped 2025: 1 Bad Bunny, 2 Taylor Swift, 3 The Weeknd, 4 Drake,
5 Billie Eilish, 6 Kendrick Lamar, 7 Bruno Mars, 8 Ariana Grande, 9 Arijit Singh, 10 Fuerza
Regida.

Reveal one through eight first. Most groups will have five or six of them. Then reveal nine and
ten and wait.

**Arijit Singh** is a Hindi playback singer and the first Indian artist in the global top ten.
**Fuerza Regida** is a regional Mexican band from San Bernardino. A Danish classroom writes ten
Anglo-American pop acts and gets both of these wrong, every time.

**The bridge back**, and the reason this is not just a game. Our dataset has six genres: edm,
latin, pop, r&b, rock. Nothing in it could have told you about Arijit Singh, because nothing in
it is from that world. When we wrote "genre" all afternoon, we meant six categories somebody at
Spotify drew for one market in 2020.

That is the honest limitation on every number in both notebooks, and the room will believe it
now in a way they would not have at 12:40.

Then check the dataset in front of them, which lands harder than anything you can say:

    a = songs["artist"].astype("string").str.lower()
    for name in ["Bad Bunny", "Taylor Swift", "Arijit Singh", "Fuerza Regida"]:
        print(name, int(a.str.contains(name.lower(), na=False).sum()), "rows")

Eight of the 2025 global top ten have songs in our 2020 file. Bad Bunny has 61 rows, Drake 104,
The Weeknd 76, Ariana Grande 55. Arijit Singh has zero. Fuerza Regida has zero.

The two the room could not name are the two the dataset does not contain. Your students'
intuition about who the world listens to and this dataset's coverage have the same blind spot,
and it is the same blind spot, because both were built from the same slice of the market.

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
