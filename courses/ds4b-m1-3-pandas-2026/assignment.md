# Group assignment: travelling tracks

**Module 1 · after session 02**

| | |
|---|---|
| **Work in** | Your group |
| **Hand in** | A notebook and a video |
| **Deadline** | Friday 11 September 2026, 23:59 |
| **Graded** | No |

## What this is

Last session we kept asking the same four things: what is one row, what's missing, is this join about to do something stupid, and what can this number honestly support. Asking them about a notebook that's already been debugged for you is easy. Asking them about a question nobody has answered yet is the actual skill.

So, three questions. None of them is much code. The time goes into deciding things and being able to say why.

We watch the videos before the next session and talk about them there, so make one you'd be willing to sit through.

## The setting

Some tracks live on one playlist. Others get around: same track, five different playlists. A curation team wants to know whether the ones that get around are recognisably different.

Two files. Both read straight from the URL, so there's nothing to download.

**`spotify_songs.csv`** · the 2020 snapshot from Notebook 2
`https://raw.githubusercontent.com/aaubs/ds-master/codex/m1-pandas-2026/data/M1_2026/spotify_songs.csv`

**`subgenre_families.csv`** · sorts the 24 subgenres into six broader families, so you can ask whether a pattern holds inside each one
`https://raw.githubusercontent.com/aaubs/ds-master/codex/m1-pandas-2026/data/M1_2026/subgenre_families.csv`

We made that second one up for this assignment. It isn't a Spotify taxonomy, it carries no authority, and nobody checked it before handing it to you. Treat it like any lookup table that turns up from another team.

```python
songs_raw = pd.read_csv("https://raw.githubusercontent.com/aaubs/ds-master/codex/m1-pandas-2026/data/M1_2026/spotify_songs.csv")
families_raw = pd.read_csv("https://raw.githubusercontent.com/aaubs/ds-master/codex/m1-pandas-2026/data/M1_2026/subgenre_families.csv")
```

## Question 1 · What is one row, and how far does each track get?

Say what one row of the raw file is, and show the output that convinced you rather than just the sentence. Then build the table your answer will sit on, and say what one of *its* rows is.

Now count how many playlists each track appears on. There's more than one way to count that, and they don't all count the same thing. Tell us which one you used and show the check that convinced you it counts playlists and not something else.

One more thing before you move on. Look at what's missing in the columns you're actually going to use, and at what the release dates really record. Pull out a release year you're willing to defend, because Question 3 wants one. If a column is a mess and you never touch it, leave it alone and say so. Cleaning things you don't need is just a way of looking busy.

## Question 2 · Bolt on the family label

Merge the lookup onto your table.

Write down the row count you expect before you run it. Then merge with `validate=` and `indicator=`, and find out whether you were right.

If the merge doesn't do what you predicted: congratulations, you've found the real question. Work out what's wrong with the keys, decide what to do about each thing you find, and write down what each decision costs you. Say how many rows end up with no family label and what happened to them.

## Question 3 · Do the tracks that get around look different?

A travelling track is one that appears on more than a certain number of playlists. **We haven't fixed that number for you.** Two playlists? Three? Five? Choosing where the line goes is part of the job, and there is no number we are quietly waiting for you to guess.

Compare travelling tracks against tracks that appear on one playlist only, on at least two audio features and on `track_popularity`. Counts next to every mean, every time.

Show what happens when you move the line. Three cut-offs, minimum. Then check whether the pattern survives inside each family, and say which families are too thin to carry the comparison. The families are a grouping we invented, so if you can think of a better one, tell us what it would be.

Before you write up: check whether your two groups differ in release year, and say what that does to the popularity result. `track_popularity` is a single number, measured once, in 2020.

Finish with one chart that carries your claim, reshaping as needed, and 250 to 400 words. What you found, what it's resting on, and two things this data can't tell the curation team.

## The video

Once the notebook is done, record your group talking through it. A screen recording with your voices over it is plenty. No slides, no editing, no intro music.

- Eight minutes. Ten at the absolute outside.
- Everyone talks. Easiest split is one decision each: what you picked, what you didn't, and why.
- Have your own code on screen while you talk about it.
- Don't read the notebook out loud. We have the notebook. Tell us what you decided and where you weren't sure.

One take with a real argument in it beats a polished one where everybody agrees.

## Handing in

- [ ] The notebook, named `M1_assignment_<group>.ipynb`, with group number and names in the first cell
- [ ] The video, alongside it
- [ ] **Restart & Run All** produces the notebook you're handing in, from a clean kernel, no manual steps
- [ ] Data read from the URLs above, no CSV copies attached
- [ ] Three questions, in order
- [ ] A decision log: one line per question, what you decided and what it cost

## What we'll notice

No marks, but we do read these, and this is what we'll pick up on in class:

- Whether the row meaning is shown or just asserted.
- Whether you checked how you counted playlists or trusted the first thing that ran.
- Whether the audit decisions were decided, including the ones where you decided to do nothing.
- A row count predicted before the merge, not explained after it.
- Counts beside means. Sensitivity actually shown. Thin groups flagged instead of quietly averaged.
- Language that stays on the right side of cause and effect.
- Whether Restart & Run All works.

We're not looking at chart styling, notebook length, how many pandas methods you got in, or whether your answer matches ours. "The difference is too small to act on" is a good answer if you can defend it, and a better one than a confident effect that isn't there.

## Tools

Use whatever helps, AI included. Two conditions:

1. A note at the end saying which tools you used and what for.
2. You can explain any line you hand in. You're about to present it on video, so this one mostly enforces itself.

The exam won't have a chat window in it.

## Stuck?

Everything these questions need is in the two session notebooks, and Notebook 2's join section is the closest thing to Question 2. Bring questions to the next session. Bring the output you already looked at too, not just the error message.
