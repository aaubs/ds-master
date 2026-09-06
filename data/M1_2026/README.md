# Data for the 2026 pandas session

These are historical teaching data, not new measurements of the 2026 market.

## Spotify snapshot

`spotify_songs.csv` is an unchanged copy downloaded on 6 September 2026 from [TidyTuesday, 21 January 2020](https://github.com/rfordatascience/tidytuesday/tree/main/data/2020/2020-01-21). The [upstream data dictionary and attribution](https://github.com/rfordatascience/tidytuesday/blob/main/data/2020/2020-01-21/readme.md) credit Spotify data collected using `spotifyr`, with the example collection discussed by Kaylin Pavlik. [Direct upstream CSV](https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-01-21/spotify_songs.csv).

The class copy makes the notebook independent of upstream URL changes. No Spotify API account or live API calls are needed. Refer to upstream for dataset attribution and applicable terms; this copy makes no new licensing claim.

Measured on this file:

- 32,833 rows; 23 columns; 28,356 distinct track IDs.
- 32,251 distinct track–playlist pairs; 32,510 distinct track–playlist–genre associations.
- Five playlist IDs carry more than one genre label. The notebook preserves the recorded genre associations and names its analysis unit explicitly.
- Track name, artist, and album name each have five missing entries. Energy and danceability have none.
- Release-date precision: 30,947 day strings, 1,855 year strings, 31 month strings. Reduced precision is not the same thing as a malformed date.

The genre summary weights each retained track–playlist–genre association once. A track can contribute more than once and to more than one genre; these are not independent samples of all music. Energy and danceability are different 0–1 indices, not measurements of the same physical quantity. Album release dates, snapshot popularity scores, and playlist labels do not support conclusions about contemporary hit songs or the causal effect of genre.

## Udemy catalog

Notebook 1 retains the existing class file [`../udemy_courses_info.csv`](../udemy_courses_info.csv), taken from the class repository at the commit recorded in `manifest.json`. No source values were edited. The supplied file has 2,959 rows, 11 columns and unique `course_id` values. Its numeric metadata contains missing entries; `info()`/`describe()` expose these for discussion.

The class file is historical. The file itself does not establish a precise collection date or currency, so the lesson does not invent one. Listed price × enrollments is explicitly named `price_times_enrollments_proxy`; it is not observed revenue. Tiny examples inside the notebook are labeled synthetic and are separate from this file.

`manifest.json` records byte sizes and SHA-256 hashes for reproducibility.
