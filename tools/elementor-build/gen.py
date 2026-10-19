"""Regenerate the Elementor JSON in /elementor from the Python page definitions.

    python3 tools/elementor-build/gen.py
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, '..', '..', 'elementor')

from el import dump  # noqa: E402
import page, hf  # noqa: E402
from fi import FI  # noqa: E402

TEXT_KEYS = ('title', 'editor', 'text', 'item_title', 'shortcode')
missing = set()


def tr(value):
    """Finnish for an English source string; untranslated copy is reported."""
    if value in FI:
        return FI[value]
    if any(c.isalpha() for c in value) and value not in KEEP:
        missing.add(value)
    return value


# Names, initials and logos that stay as they are.
KEEP = {'+45 kg', '−14 kg', '−9 kg', 'AL', 'MH', 'DO', 'JK', 'EN', 'HS', 'Aino Laine', 'Mikko Heikkinen', 'Daniel Okafor', 'Jussi Korhonen', 'Emma Nieminen',
        'Helmi Salo', 'Mikael Koski', 'Sofia Halonen', 'Elias Nyström', 'Laura Heikkilä', 'GET<span class="gf-lime">FIT</span>',
        '<p>Get Fit Studio<br>Urho Kekkosen katu 1, 00100 Helsinki</p>', 'hello@getfit.fi', '+358 40 123 4567'}


def translate(elements):
    for e in elements:
        s = e['settings']
        for k in TEXT_KEYS:
            if isinstance(s.get(k), str):
                s[k] = tr(s[k])
        for k in ('icon_list', 'items'):
            for item in s.get(k) or []:
                for kk in ('text', 'item_title'):
                    if isinstance(item.get(kk), str):
                        item[kk] = tr(item[kk])
        translate(e['elements'])
    return elements


files = {'home.json': dump(translate(page.page())), 'header.json': dump(translate(hf.header())),
         'footer.json': dump(translate(hf.footer())),
         'kit.json': json.dumps(hf.kit(), ensure_ascii=False)}
for name, data in files.items():
    with open(os.path.join(OUT, name), 'w') as fh:
        fh.write(data)
    print(name, len(data), 'bytes')
for m in sorted(missing):
    print('UNTRANSLATED:', m)
