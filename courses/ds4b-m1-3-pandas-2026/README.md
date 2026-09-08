# Session 02 · Pandas and NumPy · 2026

**Wednesday 9 September · 12:30–16:15 · Fib15-2.234 · Roman Jurowetzki**

This update preserves the class repository's `notebooks/`, `data/`, `media/`, and `courses/` structure and the two original notebook filenames. The course-catalog and Spotify examples remain useful; the revision improves the learning sequence and interpretation rather than replacing data for novelty.

## Group assignment

[assignment.md](assignment.md) is the student brief; [assignment-instructor-notes.md](assignment-instructor-notes.md)
is the marking companion and is not for hand-out. The starter notebook is
[M1_assignment_2026_starter.ipynb](../../notebooks/M1_assignment_2026_starter.ipynb) and the
supplied lookup table is `data/M1_2026/subgenre_families.csv`, which is constructed for the
assignment rather than downloaded.

## Open the updated notebooks

- [Part 1 in Colab](https://colab.research.google.com/github/aaubs/ds-master/blob/codex/m1-pandas-2026/notebooks/M1_01_control_flow_to_pandas.ipynb) — 80 minutes: Python records, actual NumPy array work, pandas labels/masks, assignment, and grouped summaries.
- [Part 2 in Colab](https://colab.research.google.com/github/aaubs/ds-master/blob/codex/m1-pandas-2026/notebooks/M1_02_pandas_deep_dive.ipynb) — 110 minutes: missingness and dates, track/playlist associations, checked joins, grouping, reshape, and interpretation.

The links use the review branch `codex/m1-pandas-2026`, including hosted data and images, so they work before a merge into `main`. Keep that branch available while these links are in use. Your original `main` Colab links show the old notebooks until the pull request is merged.

## Moodle: what to paste

1. Open [`moodle-session-02.html`](moodle-session-02.html) as text and copy its complete contents into the HTML/source view of the Moodle session description or Page resource.
2. Save and check the student view. Moodle's theme or HTML sanitization may alter layout; the content uses inline styles and ordinary links, with no scripts or external font requirement.
3. Use [`moodle-preview.html`](moodle-preview.html) for a standalone visual preview. It is a complete HTML page; the paste-ready file above is only the required fragment.

The description already includes the two notebook links, preparation advice, objectives, reading, and historical-data caveat. No separate image uploads to Moodle are required. Student downloads link to raw notebook files.

After merging into `main`, [`moodle-session-02-after-merge.html`](moodle-session-02-after-merge.html) restores your original Colab URLs and links the student guide from `main`. Before deleting the review branch, also change the notebooks' raw data/image URLs from `codex/m1-pandas-2026` to `main` and verify them.

## Included material

- [Student reference](student-reference.md): a short preparation route, selected official tutorials, optional free handbook chapters, and a runnable small reference example.
- [Instructor guide](instructor-guide.md): full 225-minute schedule including breaks, teaching decisions, pacing fallback, and exit ticket.
- [Data provenance](../../data/M1_2026/README.md) and checksums: an unchanged Spotify snapshot in the class repository and documentation of the existing Udemy file.
- [Four teaching diagrams and one optional comic](../../media/M1_2026/README.md): hosted PNGs, reproducible diagram source, and the GPT image-generation prompt.
- [Validation report](validation.md): tested versions, execution checks, and remaining environment-specific limits.

## Main improvements

The Python-to-pandas transition now includes explicit NumPy arrays and list/array behavior. Both notebooks use prediction and modification tasks with separate solution keys. The Spotify analysis preserves playlist context, audits partial dates honestly, validates join cardinality, and reports counts alongside genre means. It avoids claims about current music charts, actual course revenue, artist collaborations inferred from names, or causal effects of genre.

Advanced sampling is an optional after-class extension. Support code is labeled for explanation rather than memorization.
