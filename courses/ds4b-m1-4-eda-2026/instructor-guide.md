# Instructor guide: session 03

**Session:** Wed 16 September 2026, 12:30-16:15 (Fib15-2.234)
**Audience:** MSc Business Data Science, straight after the pandas session
**Format:** [M1_03_exploring_distributions.ipynb](../../notebooks/M1_03_exploring_distributions.ipynb) and [M1_04_comparing_groups.ipynb](../../notebooks/M1_04_comparing_groups.ipynb)

## Teaching intent

Session 02 ended with a table nobody had looked at. This session looks at it, under a brief
that has a wrong answer built into it.

**The brief, given in the first cell of part 1:** someone upstairs wants to know which musical
qualities make a track popular, so the label can commission more of them. Both notebooks answer
that question, and the answer is no. No audio measurement correlates with popularity above
0.14. All ten of them together account for 6 percent of the variation. Genre adds 4.

That is the spine. Everything else in the two notebooks is the work you have to do before you
are allowed to say it, and the reason to say it out loud is that "we looked and it is not
there" is a real deliverable that students are never taught to produce.

Three secondary lessons hang off it, and each has a cell:

- The strongest signal in the file, playlist placements at d = 1.62, runs the wrong way. Tracks
  get added to playlists because they are popular. It is the outcome wearing a hat.
- Nine percent of the popularity column is a spike at exactly zero, which may be "nobody
  listens" or may be "no figure available". Keeping or dropping it moves every genre mean by 3
  to 4.7 points.
- On 28,000 rows, significance is close to free. A 1.75-point gap on a 0-100 index clears
  p = 0.0008.

Students arrive believing p values are the point. They should leave believing p values are the
smallest claim in the sentence, and that the direction of the arrow is not in the output at all.

Continuity with session 02 is a sentence rather than a pipeline. There are no joins here: the
raw file already carries every audio measurement on every row, so the setup is two lines. Say
out loud that this is last week's file and last week's row meaning, then move on.

## Run of show

Two notebooks, 31 code cells between them, no joins anywhere. The time freed up is for talking.

| Time | Segment |
|---|---|
| 12:30-12:45 | Open. The brief. What one row is, and why there are two frames rather than one. |
| 12:45-14:00 | Part 1. The zero spike, what describe hides, impossible rows, group sizes, and the correlation table that answers the brief. |
| 14:00-14:10 | Break. |
| 14:10-15:05 | Part 2 to the end of track length. Placements, the reverse-causation trap, effect size. This is the core. |
| 15:05-15:15 | Break, and the ten-names quiz (it is a cell in part 2). |
| 15:15-16:10 | How much anything explains, the zeros chi-square, multiple testing, how to report a comparison, the memo. |
| 16:10-16:15 | Exit ticket. |

Use the slack on the two-panel scatter in part 1 and on the placements trap in part 2, which
are the two places students change their minds about something.

If you are behind, cut the chi-square section. Do not cut the placements trap or the
sample-size demonstration.

## What came back from the 2025 notebook

Last year's version had better scaffolding than substance: a strong five-question EDA checklist
and a clean test-chooser table, wrapped around synthetic data and a p-value rule it contradicted
later in its own text. Three things were worth keeping and are now in these notebooks.

The **five questions** open part 1 as a table, and the notebook follows them in order. Point at
it and say it works on any table. It is the most portable thing in the session.

The **which-test table** sits in part 2 before any test appears, so choosing between them stops
being mysterious before the interesting problem arrives.

The **multiple-testing warning** sits just before the reporting rule. Framing: running twenty
tests used to take an afternoon, and an agent will run fifty in one call and hand back the three
that cleared 0.05.

What did not come back: the synthetic data generator, and the `if p < 0.05: print("REAL")`
pattern that appeared three times. If a student has seen last year's notebook, name that second
one out loud as the thing this session argues against.

## The moments

**The zero spike.** Part 1, question 2. The popularity histogram has one bar nearly five times
its neighbour, sitting at zero, and almost nothing at 1, 2 or 3. Ask what would produce that
shape. Somebody will say "nobody listens to them"; ask them what a track with no figure at all
would look like in this column. There is no way to tell from the file, and that is the answer.
2,620 tracks, 9.2 percent.

**The same row, caught twice.** Part 1 finds a four-second track from the minimum of
`duration_ms`, then a track with a tempo of exactly zero. Same record: "Hi, How're You Doin'?"
by DREAMS COME TRUE, which is also the least danceable and the saddest thing in the file. Let
the room notice rather than announcing it. Nobody suspected that row; two unrelated sanity
checks found it.

**Four columns, four situations.** The histogram panel draws the mean on each distribution in
orange. Danceability is a single hump and its mean is fine. Energy is skewed so the mean sits
below the bulk. Valence is a broad plateau, so 0.51 describes nobody. Tempo has two clusters,
near 95 and near 125, and the mean lands on the taller one while the smaller disappears.

Ask what the mean of the tempo column is describing before moving on.

**The answer to the brief, in one line.** Part 1, question 5. The correlation table between ten
audio measurements and popularity, sorted by absolute size. The top of it is duration at -0.14.
This is the moment the session turns, and it is worth pausing on how cheap it was: one line, no
model, and the project is now a different project.

**What 0.68 and -0.10 look like.** The two-panel scatter immediately after. Left panel, energy
against loudness, is a real relationship and still a wide cloud. Right panel, popularity against
energy, has no shape at all. Students who have only met correlations as numbers systematically
overestimate what -0.10 looks like. Show this before they ever fit anything.

The line of dots along the bottom of the right panel is the zero spike turning up again in a
chart drawn for another reason. Point at it.

**The placements trap.** Part 2, question 1, and the best twenty minutes of the day. It is also
the debrief of their own assignment: question 3 asked whether travelling tracks look different
and was handed in on the 11th, five days before this session. Open by asking what they found,
then run the cell. Groups that picked different cut-offs will have different numbers, which is
the point. Mean
popularity by number of playlists: 37, 52, 67, 73, 85. A 34-point gap, d = 1.62, p = 10^-254.
The largest effect anyone will find in this file.

Then ask what the team should do about it. Somebody will say "get on more playlists". Ask how a
track gets onto a playlist. Editors add tracks that are already doing well, and being added
pushes them further, so the arrow runs both ways and this table cannot separate them. The
notebook's phrasing is that recommending it is telling them to make the thermometer read higher
by holding a match to it.

The general lesson, and it is worth writing on the board: **the biggest effect in a dataset is
very often the outcome in disguise.**

**Track length, the one usable finding.** 2:30-3:00 averages 42.6 against 31.2 for over five
minutes. Eleven points, d = 0.50, and the bars slope one way across the whole range. A quarter
of the placements effect, and the only one of the two anybody can act on. That asymmetry is the
normal shape of applied work.

**Significance is free.** rock against latin on popularity: 1.75 points on a 0-100 index,
d = 0.07, p = 0.0008. Then the sample-size demo reruns it on 30 rows a side, 200 times, and it
clears 0.05 in about 5 percent of runs. The difference never changed. Only the row count did.
Give this cell time.

**Six percent.** ANOVA gives genre eta squared 0.043; the regression preview gives all ten audio
columns R squared 0.058. Ninety-four percent of what makes a track popular is not in this file:
marketing, timing, an editor's decision, a soundtrack, a video. One honest sentence beats any
model fitted to these columns, and that sentence is the deliverable.

**The zeros, chi-square, and what it costs.** edm carries 13.3 percent zeros against pop's 6.1,
p = 10^-37, so the zeros are not spread evenly. Then the comparison table: dropping them lifts
every genre, edm most at +4.7. The ranking survives here. It did not have to, and you only know
because both were run. This is where the part 1 judgement call gets a number attached.

**The memo.** The last markdown cell in part 2 is one paragraph a student could actually send
upstairs. Read it aloud. Most of them have never seen what a negative result looks like when it
is written up confidently rather than apologetically.

## What to say about tests and language models

Same argument as session 02, one level up. Ask a model whether track length affects popularity
and you get a correct t-test, a correct p value and a verdict. What you do not get is whether
anybody should care, or which way the arrow points. The placements result is the demonstration:
everything about it is correct and acting on it would be nonsense.

If a student says they would just ask for the effect size too, that is the right answer, and the
point stands. You have to know the words. Prompting is expertise expressed somewhere else.

## The music, which is the point of using this data at all

The dataset carries real Spotify track IDs. Both notebooks have two helpers: `listen()` renders
a clickable link column, and `play()` embeds a Spotify player straight into the output, so a
track plays from the notebook without leaving it. The player needs a browser and is a 30-second
preview unless you are signed in; if it does not render, the links always work.

Three of these are already `play()` cells in the notebooks. The rest are yours to open.

**"Hotline Bling"** by Drake, which this file scores at popularity 0, is the best thirty seconds
of the day. Part 1 finds the zero spike, lists who is in it (Drake, Taylor Swift, four Eminem
records), and plays this. Ask the room whether it looks like a song nobody streams. Then the
next line: 1,746 of the 2,620 zeros are by artists who have scored tracks elsewhere in the same
file. The zeros are absence wearing the same clothes as a real value, and the room worked it out
by recognising a song rather than by being told.

**"Dance Monkey"** by Tones and I plays immediately after it, as the only track in the file
scoring 100. Nothing to say about it; the contrast does the work.

**"Closer"** by The Chainsmokers sits on ten playlists, more than anything else in the file, and
opens the placements section in part 2.

Five more worth having ready, in the order they come up:

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

**"Low Rider"** by War is valence 0.99, the happiest thing in the dataset, and here the model
is obviously right. Worth playing straight after the rainforest so the room sees that the
measures are not simply broken.
`https://open.spotify.com/track/7kigmgx2tJJsZHKaa2QC0w`

**"bad guy"** by Billie Eilish appears under five different genres: edm, latin, pop, r&b and
rock. 265 tracks sit in three or more. If anyone still thinks genre is a property of a song
rather than of a playlist, this settles it.
`https://open.spotify.com/track/2Fxmhks0bxGSBdJ92vM42m`

## The break quiz

**[Aim for Ten](https://claude.ai/code/artifact/315cf590-a544-4f90-9f1e-91aeb72d6d20)**: open it on the projector at the 15:05 break. It is also in the repo
as [break-quiz.html](break-quiz.html). The arrow keys move between rounds, a number key turns
that rank's card (0 turns #10), and A turns them all. The explanation and the songs appear once
all ten cards in a round are turned. Songs open in Spotify in a new tab, so have Spotify signed
in on the teaching machine.

Every round is a top ten. Each group writes down one entry per round and scores its rank: #10
is worth 10 points, #1 is worth 1, and anything off the list scores 0. The obvious answer is
usually #1 and worth one point. Turn the cards from #1 upwards, so the jackpot comes last.

**Round 1, Spotify's most-streamed artists of 2025.** Bad Bunny is #1. The jackpot is Fuerza
Regida (#10) and Arijit Singh (#9), the two nobody in a Danish classroom names. The notebook's
next cell shows both have zero rows in our file. (Re-check the ranking before class.)

**Round 2, the richest musicians** (Forbes: 2026 for #1–6, 2025 estimates for #7–10). Jay-Z
$2.8bn, Taylor Swift $2.0bn, Bruce Springsteen $1.2bn, then Rihanna, Beyoncé and Dr. Dre, tied
at $1.0bn and ranked by who got there first (give 5 points for any of the three if you prefer).
Then Madonna $850m, Selena Gomez $700m, Celine Dion $570m, Barbra Streisand $510m. Bloomberg puts
Gomez at $1.3bn, so expect an argument. Play "My Heart Will Go On".

**Round 3, most weeks on the Billboard Hot 100** (Christmas songs excluded). "Lose Control" by
Teddy Swims holds the record at 112 weeks, having passed "Heat Waves" (91) in May 2025. #10 is
Billie Eilish's "WILDFLOWER" at 72. "Levitating" and "A Bar Song" are tied on 77, ranked by who
got there first. Play "WILDFLOWER".

Rounds 2 and 3 are as of September 2026. Forbes revises its figures every spring.

Sources: [Forbes celebrity billionaires 2026](https://www.forbes.com/sites/idonnkanga/2026/03/10/the-worlds-celebrity-billionaires-2026/),
[music artists by net worth](https://en.wikipedia.org/wiki/List_of_music_artists_by_net_worth),
[Hot 100 milestones](https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_chart_achievements_and_milestones).

## Known traps to surface

- **Two frames, not one.** `songs` counts a track once per playlist; `tracks` counts it once.
  Most confusion in this session traces back to someone using the wrong one. Ask which
  question each answers rather than which is correct.
- **The 0.05 threshold is a convention.** Nothing in the data changes at 0.049. The
  rock-latin test lands at p = 0.0008 on a gap of 1.75 points, comfortably inside a threshold
  nobody chose on principle.
- **A correlation of zero is a result.** The hardest thing for students here is believing that
  "no audio feature predicts popularity" is an answer rather than a failure. Say early that a
  well-supported no is worth more than a badly-supported yes, and that the memo at the end of
  part 2 is what one looks like written down.
- **Skew is not error.** In the practice task, `speechiness` has a long tail of tracks that are
  mostly talking. Those are real records. Students who have just learned about broken rows tend
  to want to delete anything unusual.
- **Correlation is not causation, and often not much else either.** Energy against loudness at
  0.68 is near tautological. Say which correlations are findings and which are definitions.
- **Direction is never in the output.** `ttest_ind` does not know which variable came first.
  The placements result is significant, enormous, and backwards, and nothing in scipy will tell
  you so.

## Exit ticket

Two questions, three sentences each:

1. You ran a test, and p is less than 0.001. What do you still not know?
2. The strongest predictor of popularity in this file is playlist placements. Why can the team
   not use it?

Good answers to the first name the size of the difference, the number of rows, whether it
matters practically, and which way the arrow points. Good answers to the second say that tracks
get added to playlists because they are already popular, so the relationship runs backwards
from the one the recommendation would assume.
