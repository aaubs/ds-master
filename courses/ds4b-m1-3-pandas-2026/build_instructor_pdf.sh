#!/bin/bash
# Build a printable PDF of the instructor solutions notebook, with outputs.
#
# Run from the repository root (the directory containing ds-master/):
#   bash ds-master/courses/ds4b-m1-3-pandas-2026/build_instructor_pdf.sh [notebook-name]
#
# Defaults to the instructor solutions. Pass another name to print any validated notebook,
# for example M1_04_comparing_groups.
#
# Needs: a validated copy in validation/pandas3 (run validate_notebooks.py first),
# nbconvert, and Google Chrome for the HTML-to-PDF step.
set -euo pipefail

NAME="${1:-M1_instructor_solutions_2026}"
NB="validation/pandas3/${NAME}.ipynb"
OUT="ds-master/courses/ds4b-m1-3-pandas-2026/${NAME}.pdf"
WORK="$(mktemp -d)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

[ -f "$NB" ] || { echo "No executed notebook at $NB. Run validate_notebooks.py first."; exit 1; }

.venv/bin/python -m nbconvert --to html --output-dir "$WORK" \
  --output solutions.html "$NB" >/dev/null 2>&1

# Print styling: portrait, readable on a tablet, no cell split across a page.
python3 - "$WORK/solutions.html" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[1])
css = """<style>
@page { size: A4 portrait; margin: 13mm 12mm; }
html, body { background: #fff !important; }
body { font-size: 11.5pt; }
.jp-Notebook { padding: 0 !important; }
.jp-Cell { page-break-inside: avoid; break-inside: avoid; margin: 0 0 6px !important; padding: 2px 0 !important; }
.jp-InputArea-editor, .jp-OutputArea-output { page-break-inside: avoid; break-inside: avoid; }
.jp-InputPrompt, .jp-OutputPrompt { display: none !important; }
.jp-InputArea-editor { border-left: 3px solid #211a52 !important; background: #f7f7f9 !important; }
.jp-RenderedHTMLCommon pre, .CodeMirror-line, .highlight pre {
  white-space: pre-wrap !important; word-break: break-word; font-size: 10pt !important; }
.jp-RenderedHTMLCommon table { font-size: 9.5pt !important; }
.jp-RenderedHTMLCommon h1 { page-break-before: always; break-before: page; }
.jp-RenderedHTMLCommon h1:first-of-type { page-break-before: avoid; break-before: avoid; }
.jp-RenderedHTMLCommon h2, .jp-RenderedHTMLCommon h3 { page-break-after: avoid; break-after: avoid; }
.jp-RenderedHTMLCommon blockquote { border-left: 4px solid #d97941; background: #fdf6f1;
  padding: 6px 12px; margin: 8px 0; }
img { max-width: 100% !important; height: auto !important; }
</style>"""
html = p.read_text()
p.write_text(html.replace("</head>", css + "\n</head>", 1))
PY

"$CHROME" --headless --disable-gpu --no-pdf-header-footer --virtual-time-budget=20000 \
  --print-to-pdf="$PWD/$OUT" "file://$WORK/solutions.html" >/dev/null 2>&1

rm -rf "$WORK"
echo "wrote $OUT ($(du -h "$OUT" | cut -f1))"
