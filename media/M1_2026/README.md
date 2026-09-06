# Teaching visuals · M1 2026

Four explanatory PNGs were drawn with Matplotlib and visually checked. Run `python render_diagrams.py` with Matplotlib installed to rebuild them. They use the session palette and can be displayed directly from raw GitHub URLs in Colab markdown. Every notebook image has accompanying prose so the concept is accessible if the image cannot load.

| Asset | Purpose |
|---|---|
| `loop_to_mask.png` | Connect a record-by-record decision to NumPy positions and pandas labels. |
| `split_apply_combine.png` | Show the change from one course per row to one subject per row. |
| `join_cardinality.png` | Show exactly why repeated lookup keys multiply rows and how merge validation detects it. |
| `reshape.png` | Connect long/wide layouts and explain why aggregation cannot be reversed. |
| `duplicate_rows_meme.png` | Optional dry-humour pause after joins; it supplements the precise diagram. |

## Comic provenance

Created on 6 September 2026 with the built-in GPT image-generation tool (not a CLI/API fallback). Original generation copied into this repository as a PNG; no further image editing. Reviewed for legible and accurate text. Exact generation prompt follows.

> Use case: illustration-story. Asset type: one restrained educational comic for a masters business data science pandas notebook. Create a clean landscape two-panel editorial cartoon on warm white with crisp ink lines and a limited palette of navy #211a52, muted teal, warm amber. Same calm analyst at a desk in both panels. Left panel: a small orderly stack of paper rows, analyst composed. Right panel: desk buried in comically multiplied stacks of identical paper rows, analyst quietly raising one eyebrow. Sophisticated understated dry humour, not cute, no pandas bears, no robots, no logos, no internet meme characters. Exact text: left panel heading "Before the merge"; right panel heading "After the merge"; single bottom caption "The business did not grow. The keys were not unique." Text should be sharp, large, correctly spelled, with generous negative space. Concept refers specifically to a join where duplicate keys multiply rows. Do not include code or additional text.
