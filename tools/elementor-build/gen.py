"""Regenerate the Elementor JSON in /elementor from the Python page definitions.

    python3 tools/elementor-build/gen.py
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, '..', '..', 'elementor')

from el import dump  # noqa: E402
import page, hf  # noqa: E402

files = {'home.json': dump(page.page()), 'header.json': dump(hf.header()), 'footer.json': dump(hf.footer()),
         'kit.json': json.dumps(hf.kit(), ensure_ascii=False)}
for name, data in files.items():
    with open(os.path.join(OUT, name), 'w') as fh:
        fh.write(data)
    print(name, len(data), 'bytes')
