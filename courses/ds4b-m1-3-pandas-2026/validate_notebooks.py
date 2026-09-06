"""Execute both notebooks in fresh kernels using this Python environment.

Usage: python validate_notebooks.py /absolute/path/to/output
Requires pandas, numpy, matplotlib, nbformat, nbclient and ipykernel.
Student notebooks remain unexecuted; review copies go to the output folder.
"""
from pathlib import Path
import sys
import json
import nbformat
import pandas as pd
import numpy as np
import matplotlib
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(sys.argv[1]).resolve()
OUT.mkdir(parents=True, exist_ok=True)
report = {'python':sys.version.split()[0], 'pandas':pd.__version__,
          'numpy':np.__version__, 'matplotlib':matplotlib.__version__, 'notebooks':[]}
for name in ['M1_01_control_flow_to_pandas.ipynb', 'M1_02_pandas_deep_dive.ipynb', 'M1_instructor_solutions_2026.ipynb']:
    nb = nbformat.read(ROOT/'notebooks'/name, as_version=4)
    nbformat.validate(nb)
    client = NotebookClient(nb, timeout=120, resources={'metadata': {'path':str(ROOT)}})
    client.create_kernel_manager()
    client.km.kernel_spec.argv = [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}']
    client.execute()
    nbformat.write(nb, OUT/name)
    errors=[]; warnings=[]
    for i,cell in enumerate(nb.cells):
        for output in cell.get('outputs',[]):
            if output.output_type=='error': errors.append({'cell':i,'error':output.ename})
            if output.output_type=='stream' and output.name=='stderr': warnings.append({'cell':i,'text':output.text})
    result={'name':name,'code_cells':sum(c.cell_type=='code' for c in nb.cells),
            'errors':errors,'stderr':warnings}
    report['notebooks'].append(result)
    print(json.dumps(result),flush=True)
(OUT/'report.json').write_text(json.dumps(report,indent=2)+'\n')
print('Saved execution evidence to',OUT)
