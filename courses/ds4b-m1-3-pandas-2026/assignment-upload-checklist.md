# Uploading the assignment: everything in one place

Not for students. Work down the list.

## 1. Decide these three things first

Nothing else can be finalised until these are settled, and all three appear in the text.

| Decision | Currently says | Where it appears |
|---|---|---|
| Deadline | Friday 11 September 2026, 23:59, two days after the session | `assignment.md`, `moodle-assignment.html`, Moodle activity settings |
| How videos reach you | not specified | Say it in the Moodle activity description |
| Group size | assumes 3 to 5 | the video asks everyone to present one decision |

The two-day window is tight for three questions. It is workable, because the code is small,
but see the effort section of [assignment-instructor-notes.md](assignment-instructor-notes.md)
for what to say at hand-out and what to cut first if you would rather shorten it.

On the video: the simplest option is a second file upload slot in the same Moodle assignment,
with a note that a shared link is fine if the file is too large. It has to be watchable by you
before the next session, so avoid anything that needs a request-access click.

## 2. Paste the Moodle page

`moodle-assignment.html` is the description for the assignment activity. Paste it into the
description field with the HTML editor turned on, not the visual one.

`moodle-session-02.html` is the updated session page. It now has a group assignment box with
the template link, and a DataCamp box. Repaste it over the existing session 02 page.

`../ds4b-m1-4-eda-2026/moodle-session-03.html` is the session 03 page, if you are putting that
up at the same time.

Open the matching `-preview.html` file in a browser first if you want to see them rendered.

## 3. Moodle activity settings

- Submission types: file upload. Two files, the notebook and the video, or one file plus a link.
- Group submission: on. One submission per group.
- Grade: none. The brief says it is not graded on the first line, so the activity should agree.
- Due date: as decided above. Consider leaving the cut-off open a few days after, since
  nothing is graded and a late notebook is still worth watching.

## 4. What students need, and where it lives

Everything is already published on the branch. No file uploads to Moodle are needed.

| Thing | Link |
|---|---|
| The brief | `courses/ds4b-m1-3-pandas-2026/assignment.md` on GitHub |
| The template notebook | `notebooks/M1_assignment_2026_starter.ipynb`, Colab link in the page |
| Spotify data | `data/M1_2026/spotify_songs.csv`, raw URL in the brief |
| Families lookup | `data/M1_2026/subgenre_families.csv`, raw URL in the brief |

All four URLs were checked and return 200 on the `codex/m1-pandas-2026` branch.

## 5. When you announce it

Three sentences worth saying out loud, because they change how the work gets done:

- It is not graded, and here is why: the discipline only becomes yours once you use it on a
  question nobody has answered for you first.
- The videos get watched, and two or three of them get discussed in the next session.
- Use whatever tools help, including AI, on two conditions: note what you used, and be able to
  explain any line. You are presenting it on video, so the second one enforces itself.

## 6. Before the next session

Read [assignment-instructor-notes.md](assignment-instructor-notes.md). It has the three key
problems planted in the lookup table, the numbers a good submission lands on, the two grain
traps, and what tends to come back. Do not hand that file out.

## 7. After the branch is merged

Every URL in the published material points at `codex/m1-pandas-2026`. The `-after-merge.html`
files have `main/` URLs ready, and the notebooks and the brief still need their raw data URLs
rewritten. Nothing is broken until the branch is deleted, so this is not urgent, but it is a
loose end.
