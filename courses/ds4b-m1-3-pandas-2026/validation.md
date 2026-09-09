# Validation · 9 September 2026

All six module notebooks passed nbformat validation and executed top to bottom in separate fresh Python kernels in each environment below. Session 02 contributes 33 code cells in Part 1 and 48 in Part 2, including the supplied solution cells; exercise placeholders remain intentionally unfilled. Session 03 adds 18 and 19 code cells. The instructor notebook adds 19, which replay both session 02 notebooks and then re-run every solution, and the assignment template adds 15. Delivered files have no saved outputs or execution counts.

The session 03 notebooks need `scipy` in addition to pandas, NumPy and Matplotlib. It is pre-installed in Colab and was installed into both validation environments.

| Environment | Python | pandas | NumPy | Result |
|---|---|---|---|---|
| Current package environment | 3.12.9 | 3.0.5 | 2.5.3 | All six notebooks passed; no cell errors or stderr |
| Compatibility environment | 3.12.9 | 2.2.3 | 2.0.2 | All six notebooks passed; no cell errors; one first-use Matplotlib font-cache notice |

Every notebook reads its data straight from the repository's raw URLs, which is what students run, so the executions used the same bytes they will. They did not replace the datasets or modify notebook cells for execution. The optional sampling starter remains commented in the student notebook, as delivered; the instructor notebook carries the worked version.

## Content and output checks

- Tiny Python/NumPy examples, expected masks, and exercise answers were checked against the code and historical Udemy data.
- Udemy: 2,959 unique course IDs; 315 missing metadata entries. The paid, ≥100,000-enrollment filter yields two rows.
- Spotify: 28,356 distinct track IDs and 32,510 retained track–playlist–genre associations. Track attributes are consistent under the supplied check. The validated left join preserves 32,510 rows with all keys matched.
- Audio-feature means have explicit observation counts. Energy and danceability are described as distinct bounded indices, not interchangeable units.
- Four deterministic diagrams and the generated comic were visually inspected. Rendered notebook output and a standalone browser preview of the Moodle fragment were checked.
- The source preserves the class repository layout; local documentation links and Git whitespace checks were checked.

## Reproduce the execution

Install `pandas`, `numpy`, `matplotlib`, `nbformat`, `nbclient`, and `ipykernel` in the environment to be tested. Run:

```sh
python courses/ds4b-m1-3-pandas-2026/validate_notebooks.py /absolute/path/to/review-output
```

The script creates executed review copies and a JSON report in the chosen output folder. It leaves student notebooks untouched. Data checksums are in [`../../data/M1_2026/manifest.json`](../../data/M1_2026/manifest.json).

## Practical limits

These are local Jupyter-kernel checks, not an execution inside a live Google Colab runtime. The notebooks use standard CPU libraries, print versions, and avoid installation cells; Colab's managed package versions can still change. Moodle HTML was checked in a browser preview, not in the institution's authenticated Moodle theme. Confirm the saved student view when pasting it into Moodle.
