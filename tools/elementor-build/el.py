"""Tiny helpers that emit Elementor (classic container + v3 widget) JSON."""
import itertools, json

_ids = itertools.count(0x1a2b3c0)
UP = 'https://personal-trainer-example.fi-c.seravo.com/wp-content/uploads/2026/10/'

LIME, LIME2, INK, SURF = '#DAF25E', '#E9FA94', '#0A1A1A', '#132626'
SOFT, MUTED, MUTED2, WHITE = '#D2DEDC', '#A6B8B6', '#8EA09E', '#FFFFFF'


def nid():
    return format(next(_ids), 'x')[-7:]


def px(v, unit='px'):
    return {'unit': unit, 'size': v, 'sizes': []}


def custom(expr):
    return {'unit': 'custom', 'size': expr, 'sizes': []}


def dims(t=0, r=None, b=None, l=None, unit='px'):
    r = t if r is None else r
    b = t if b is None else b
    l = r if l is None else l
    return {'unit': unit, 'top': str(t), 'right': str(r), 'bottom': str(b), 'left': str(l),
            'isLinked': t == r == b == l}


def gap(row, col=None):
    col = row if col is None else col
    return {'column': str(col), 'row': str(row), 'isLinked': row == col, 'unit': 'px', 'size': row}


def typo(family=None, size=None, weight=None, lh=None, ls=None, transform=None, style=None,
         size_t=None, size_m=None, prefix='typography'):
    s = {prefix + '_typography': 'custom'}
    if family: s[prefix + '_font_family'] = family
    if size is not None: s[prefix + '_font_size'] = size if isinstance(size, dict) else px(size)
    if size_t is not None: s[prefix + '_font_size_tablet'] = size_t if isinstance(size_t, dict) else px(size_t)
    if size_m is not None: s[prefix + '_font_size_mobile'] = size_m if isinstance(size_m, dict) else px(size_m)
    if weight: s[prefix + '_font_weight'] = str(weight)
    if lh is not None: s[prefix + '_line_height'] = lh if isinstance(lh, dict) else px(lh, 'em')
    if ls is not None: s[prefix + '_letter_spacing'] = ls if isinstance(ls, dict) else px(ls, 'em')
    if transform: s[prefix + '_text_transform'] = transform
    if style: s[prefix + '_font_style'] = style
    return s


def gtypo(gid, prefix='typography'):
    return {'__globals__': {prefix + '_typography': 'globals/typography?id=' + gid}}


def merge(*ds):
    out = {}
    for d in ds:
        for k, v in (d or {}).items():
            if k == '__globals__' and k in out:
                out[k] = {**out[k], **v}
            else:
                out[k] = v
    return out


def con(children, settings=None, cls=None, title=None, inner=True):
    s = {'content_width': 'full', 'flex_direction': 'column'}
    s.update(settings or {})
    if cls:
        s['css_classes'] = cls
    if title:
        s['_title'] = title
    return {'id': nid(), 'elType': 'container', 'isInner': inner, 'settings': s, 'elements': children}


def section(children, settings=None, cls=None, sid=None, title=None, boxed=True, pad=(120, 32, 140, 32)):
    t, r, b, l = pad
    s = {'content_width': 'boxed' if boxed else 'full', 'flex_direction': 'column',
         'padding': dims(t, r, b, l), 'padding_mobile': dims(round(t * .7), 20, round(b * .7), 20),
         'html_tag': 'section'}
    if sid:
        s['_element_id'] = sid
    s.update(settings or {})
    c = con(children, s, cls, title, inner=False)
    return c


def row(children, settings=None, cls=None, title=None):
    s = {'flex_direction': 'row', 'flex_wrap': 'wrap'}
    s.update(settings or {})
    return con(children, s, cls, title)


def grid(children, cols, gaps, cols_t=None, cols_m=1, settings=None, cls=None, title=None):
    s = {'container_type': 'grid', 'grid_columns_grid': px(cols, 'fr'), 'grid_rows_grid': px(1, 'fr'),
         'grid_columns_grid_tablet': px(cols_t or min(cols, 2), 'fr'), 'grid_columns_grid_mobile': px(cols_m, 'fr'),
         'grid_rows_grid_tablet': px(1, 'fr'), 'grid_rows_grid_mobile': px(1, 'fr'),
         'grid_gaps': {'column': str(gaps[1]), 'row': str(gaps[0]), 'isLinked': gaps[0] == gaps[1], 'unit': 'px'},
         'grid_auto_flow': 'row', 'grid_justify_items': 'stretch', 'grid_align_items': 'stretch'}
    s.update(settings or {})
    return con(children, s, cls, title)


def w(wtype, settings, cls=None, margin=None):
    s = dict(settings)
    if cls:
        s['_css_classes'] = cls
    if margin is not None:
        s['_margin'] = margin
    return {'id': nid(), 'elType': 'widget', 'widgetType': wtype, 'settings': s, 'elements': []}


def mt(top, top_m=None):
    """Top margin only (design spacing is expressed as margin-top)."""
    return dims(top, 0, 0, 0)


def heading(text, tag='h2', color=None, t=None, align=None, cls=None, margin=None, link=None, extra=None):
    s = {'title': text, 'header_size': tag}
    if color:
        if color.startswith('g:'):
            s['__globals__'] = {'title_color': 'globals/colors?id=' + color[2:]}
        else:
            s['title_color'] = color
    if align: s['align'] = align
    if link: s['link'] = {'url': link, 'is_external': '', 'nofollow': ''}
    s = merge(s, t, extra)
    return w('heading', s, cls, margin)


def text(html, color=None, t=None, align=None, cls=None, margin=None, extra=None):
    s = {'editor': html}
    if color: s['text_color'] = color
    if align: s['align'] = align
    s = merge(s, t, extra)
    return w('text-editor', s, cls, margin)


def eyebrow(label, align=None, margin=None):
    return heading(label, 'div', LIME, gtypo('gfeyebrow'), align, 'gf-eyebrow', margin)


def h2(label, align=None, margin=None, cls=None, maxw=None):
    extra = {}
    if maxw:
        extra = {'_element_width': 'initial', '_element_custom_width': px(maxw)}
    return heading(label, 'h2', WHITE, gtypo('gfh2'), align, ('gf-h2 ' + (cls or '')).strip(), margin if margin is not None else mt(18), extra=extra)


def lead(html, align=None, margin=None, maxw=None, color=MUTED, gid='gflead'):
    extra = {}
    if maxw:
        extra = {'_element_width': 'initial', '_element_custom_width': px(maxw)}
    return text('<p>' + html + '</p>', color, gtypo(gid), align, 'gf-lead', margin, extra)


BTN_SIZES = {  # font, pad-y, pad-x  (taken from the design)
    'sm': (14, 12, 20), 'md': (15, 16, 28), 'lg': (16, 17, 30), 'xl': (16, 18, 32), 'mdo': (15, 14, 24), 'mdc': (15, 15, 26),
}


def button(label, url, kind='primary', size='md', align=None, margin=None, cls=None, icon=None, extra=None):
    f, py, pxx = BTN_SIZES[size]
    if kind == 'ghost':  # 1px border eats into the padding in the design
        py -= 1
    s = {'text': label, 'link': {'url': url, 'is_external': '', 'nofollow': ''},
         'text_padding': dims(py, pxx), 'border_radius': dims(999),
         **typo('Hanken Grotesk', f, 700, px(1.3, 'em'))}
    if kind == 'primary':
        s.update({'button_text_color': INK, 'background_background': 'classic', 'background_color': LIME,
                  'hover_color': INK, 'button_background_hover_background': 'classic', 'button_background_hover_color': LIME2})
    else:
        s.update({'button_text_color': WHITE, 'background_background': 'classic', 'background_color': 'rgba(0,0,0,0)',
                  'hover_color': WHITE, 'button_background_hover_background': 'classic', 'button_background_hover_color': 'rgba(0,0,0,0)',
                  'border_border': 'solid', 'border_width': dims(1), 'border_color': 'rgba(255,255,255,0.28)',
                  'button_hover_border_color': WHITE})
    if align: s['align'] = align
    if icon:
        s['selected_icon'] = {'value': icon, 'library': 'fa-solid'}
        s['icon_align'] = 'row-reverse'
        s['icon_indent'] = px(10)
    s = merge(s, extra)
    return w('button', s, ('gf-btn gf-btn--' + kind + ' ' + (cls or '')).strip(), margin)


def image(att_id, fname, cls=None, size='full', extra=None, alt=None):
    s = {'image': {'url': UP + fname, 'id': att_id, 'size': '', 'alt': alt or '', 'source': 'library'}, 'image_size': size}
    s = merge(s, extra)
    return w('image', s, cls)


def svg_icon(att_id, fname, size, cls=None, extra=None):
    s = {'selected_icon': {'value': {'url': UP + fname, 'id': att_id}, 'library': 'svg'},
         'size': px(size), 'primary_color': LIME, 'align': 'center'}
    s = merge(s, extra)
    return w('icon', s, cls)


def icon_list(items, color=SOFT, icon_color=LIME, size=15, inline=False, gapv=12, icon_size=12, cls=None, margin=None, extra=None, hover=None):
    lst = []
    for it in items:
        if isinstance(it, str):
            it = {'text': it}
        e = {'text': it['text'], '_id': nid()}
        if it.get('icon', 'fas fa-check'):
            e['selected_icon'] = {'value': it.get('icon', 'fas fa-check'), 'library': 'fa-solid'}
        else:
            e['selected_icon'] = {'value': '', 'library': ''}
        if it.get('url'):
            e['link'] = {'url': it['url'], 'is_external': 'on' if it['url'].startswith('http') else '', 'nofollow': ''}
        lst.append(e)
    s = {'icon_list': lst, 'space_between': px(gapv), 'icon_color': icon_color, 'icon_size': px(icon_size),
         'text_color': color, 'text_indent': px(10), **typo('Hanken Grotesk', size, None, None, prefix='icon_typography')}
    if hover: s['text_color_hover'] = hover
    if inline:
        s['view'] = 'inline'
    s = merge(s, extra)
    return w('icon-list', s, cls, margin)


def _sq(v):
    if isinstance(v, str):
        return v.replace('"', "'")
    if isinstance(v, list):
        return [_sq(x) for x in v]
    if isinstance(v, dict):
        return {k: _sq(x) for k, x in v.items()}
    return v


def dump(data):
    """JSON for _elementor_data. HTML attribute quotes become single quotes so the
    payload has no backslashes (update_post_meta() unslashes its input)."""
    out = json.dumps(_sq(data), ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in out, 'backslash would be stripped by update_post_meta'
    return out
