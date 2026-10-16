"""UAE header / footer templates and the Elementor kit (Site Settings)."""
from el import *


def logo(size, link='/'):
    return heading('GET<span class="gf-lime">FIT</span>', 'div', WHITE,
                   typo('Archivo', size, 900, 1, -0.04, style='italic'), cls='gf-logo', link=link)


def header():
    nav = w('navigation-menu', {
        'menu': 'primary-menu', 'layout': 'horizontal', 'navmenu_align': 'center', 'pointer': 'none',
        'dropdown': 'tablet', 'resp_align': 'left', 'full_width_dropdown': 'yes', 'toggle_align': 'right',
        'submenu_icon': 'arrow', 'menu_last_item': 'none',
        'padding_horizontal_menu_item': px(14), 'padding_vertical_menu_item': px(8), 'menu_space_between': px(0),
        **typo('Hanken Grotesk', 14, 600, 1.3, prefix='menu_typography'),
        'color_menu_item': SOFT, 'color_menu_item_hover': WHITE, 'color_menu_item_active': WHITE,
        'bg_color_menu_item': 'rgba(0,0,0,0)', 'bg_color_menu_item_hover': 'rgba(0,0,0,0)',
        'color_dropdown_item': SOFT, 'background_color_dropdown_item': INK,
        'color_dropdown_item_hover': WHITE, 'background_color_dropdown_item_hover': SURF,
        'toggle_color': WHITE, 'toggle_hover_color': LIME, 'toggle_size': px(24), 'toggle_border_width': px(0),
        'padding_horizontal_dropdown_item': px(24), 'padding_vertical_dropdown_item': px(14),
        **typo('Hanken Grotesk', 16, 600, 1.3, prefix='dropdown_typography'),
        '_flex_size': 'grow',
    }, 'gf-nav')
    bar = row([
        logo(26),
        nav,
        button('Book a free trial', '/#book', 'primary', 'sm', cls='gf-header-cta'),
    ], {'content_width': 'boxed', 'boxed_width': px(1176), 'flex_justify_content': 'space-between', 'flex_align_items': 'center',
        'flex_gap': gap(24), 'flex_wrap': 'nowrap', 'padding': dims(16, 32), 'padding_mobile': dims(14, 20)}, cls='gf-header-bar', title='Header bar')
    return [con([bar], {'content_width': 'full', 'flex_gap': gap(0)}, cls='gf-header', title='Site header', inner=False)]


def flinks(title, items):
    return con([
        heading(title, 'div', LIME, gtypo('gfeyebrow'), extra={'typography_font_size': px(12)}),
        icon_list([{'text': t, 'url': u, 'icon': ''} for t, u in items], SOFT, LIME, 15, gapv=12, cls='gf-flinks',
                  margin=mt(12), extra={'text_indent': px(0), 'icon_typography_line_height': px(1.6, 'em')}, hover=LIME),
    ], title=title)


def footer():
    top = row([
        con([heading('Ready when you are.', 'h2', WHITE, typo('Archivo', custom('clamp(32px, 4vw, 52px)'), 800, 1.02, -0.03)),
             text('<p>Your first session is free. No contract, no pressure.</p>', MUTED, typo('Hanken Grotesk', 16, 400, 1.6), margin=mt(12))],
            title='CTA text'),
        row([button('Book a free trial →', '/#book', 'primary', 'md'),
             button('Call +358 40 123 4567', 'tel:+358401234567', 'ghost', 'mdc')], {'flex_gap': gap(12)}),
    ], {'flex_justify_content': 'space-between', 'flex_align_items': 'flex-end', 'flex_gap': gap(32), 'padding': dims(0, 0, 48, 0),
        'border_border': 'solid', 'border_width': dims(0, 0, 1, 0), 'border_color': 'rgba(255,255,255,0.1)'}, title='Footer CTA')
    social = w('social-icons', {
        'social_icon_list': [
            {'_id': nid(), 'social_icon': {'value': 'fab fa-instagram', 'library': 'fa-brands'}, 'link': {'url': '#top', 'is_external': '', 'nofollow': ''}},
            {'_id': nid(), 'social_icon': {'value': 'fab fa-facebook-f', 'library': 'fa-brands'}, 'link': {'url': '#top', 'is_external': '', 'nofollow': ''}},
            {'_id': nid(), 'social_icon': {'value': 'fab fa-youtube', 'library': 'fa-brands'}, 'link': {'url': '#top', 'is_external': '', 'nofollow': ''}},
            {'_id': nid(), 'social_icon': {'value': 'fab fa-tiktok', 'library': 'fa-brands'}, 'link': {'url': '#top', 'is_external': '', 'nofollow': ''}},
        ],
        'shape': 'circle', 'align': 'left', 'icon_color': 'custom', 'icon_primary_color': 'rgba(0,0,0,0)', 'icon_secondary_color': WHITE,
        'icon_size': px(16), 'icon_padding': px(13, 'px'), 'icon_spacing': px(10),
        'image_border_border': 'solid', 'image_border_width': dims(1), 'image_border_color': 'rgba(255,255,255,0.16)',
        'hover_primary_color': LIME, 'hover_secondary_color': INK, 'hover_border_color': LIME,
    }, 'gf-social', mt(24))
    cols = grid([
        con([logo(32, '/'),
             text('<p>Personal training in central Helsinki and online. Strength, weight loss and coaching that fits your life.</p>',
                  MUTED, typo('Hanken Grotesk', 15, 400, 1.7), margin=mt(16)),
             social], {'width': px(320), 'width_tablet': px(100, '%')}, title='Brand'),
        flinks('Explore', [('About', '/#about'), ('How it works', '/#method'), ('Programmes', '/#programs'), ('Pricing', '/#pricing'), ('FAQ', '/#faq')]),
        con([
            heading('Visit', 'div', LIME, gtypo('gfeyebrow'), extra={'typography_font_size': px(12)}),
            text('<p>Urho Kekkosen katu 1<br>00100 Helsinki, Finland</p>', SOFT, typo('Hanken Grotesk', 15, 400, 1.6), margin=mt(12)),
            icon_list([{'text': 'Get directions ↗', 'url': 'https://maps.google.com/?q=Urho+Kekkosen+katu+1+Helsinki', 'icon': ''}], SOFT, LIME, 15,
                      cls='gf-flinks', margin=mt(12), extra={'text_indent': px(0)}, hover=LIME),
            text('<p>Mon–Fri 06:30 – 20:00<br>Sat 08:00 – 14:00</p>', SOFT, typo('Hanken Grotesk', 15, 400, 1.6), margin=mt(20)),
        ], title='Visit'),
        flinks('Contact', [('hello@getfit.fi', 'mailto:hello@getfit.fi'), ('+358 40 123 4567', 'tel:+358401234567'), ('Coach with us', 'mailto:coaches@getfit.fi')]),
    ], 4, (48, 48), 2, 1, {'padding': dims(48, 0)}, title='Footer columns')
    bottom = row([
        w('copyright', {'shortcode': '© [hfe_current_year] Get Fit Personal Training. All rights reserved.', 'align': 'left',
                        'text_color': MUTED, **typo('Hanken Grotesk', 13, 400, 1.5, prefix='caption_typography')}, 'gf-copyright'),
        row([
            heading('Privacy', 'div', MUTED, typo('Hanken Grotesk', 13, 400, 1.5), link='/privacy-policy/', cls='gf-flink'),
            heading('Terms', 'div', MUTED, typo('Hanken Grotesk', 13, 400, 1.5), link='#top', cls='gf-flink'),
            heading('Back to top <span class="gf-totop">↑</span>', 'div', WHITE, typo('Hanken Grotesk', 13, 600, 1.5), link='#top', cls='gf-backtotop'),
        ], {'flex_gap': gap(24), 'flex_align_items': 'center'}),
    ], {'flex_justify_content': 'space-between', 'flex_align_items': 'center', 'flex_gap': gap(16), 'padding': dims(22, 0),
        'border_border': 'solid', 'border_width': dims(1, 0, 0, 0), 'border_color': 'rgba(255,255,255,0.1)'}, title='Footer bottom')
    card = con([top, cols, bottom], {'padding': dims(56, 48, 0, 48), 'padding_mobile': dims(40, 24, 0, 24), 'border_radius': dims(32),
                                     'overflow': 'hidden'}, cls='gf-glass gf-footer-card', title='Footer card')
    return [con([card], {'content_width': 'boxed', 'boxed_width': px(1176), 'padding': dims(0, 32, 32, 32),
                         'padding_mobile': dims(0, 16, 16, 16), '_element_id': 'contact'}, cls='gf-footer', title='Site footer', inner=False)]


def tg(_id, title, family, size, weight, lh=None, ls=None, transform=None, size_t=None, size_m=None):
    d = {'_id': _id, 'title': title, **typo(family, size, weight, lh, ls, transform, size_t=size_t, size_m=size_m)}
    return d


def kit():
    return {
        'system_colors': [
            {'_id': 'primary', 'title': 'Lime', 'color': LIME},
            {'_id': 'secondary', 'title': 'Ink', 'color': INK},
            {'_id': 'text', 'title': 'Muted text', 'color': MUTED},
            {'_id': 'accent', 'title': 'Soft text', 'color': SOFT},
        ],
        'custom_colors': [
            {'_id': 'gfwhite', 'title': 'White', 'color': WHITE},
            {'_id': 'gflime2', 'title': 'Lime hover', 'color': LIME2},
            {'_id': 'gfsurf', 'title': 'Surface', 'color': SURF},
            {'_id': 'gfmuted2', 'title': 'Muted 2', 'color': MUTED2},
        ],
        'system_typography': [
            tg('primary', 'Display (Archivo)', 'Archivo', 60, 800, 1.02, -0.03),
            tg('secondary', 'UI (Hanken Grotesk)', 'Hanken Grotesk', 16, 600),
            tg('text', 'Body', 'Hanken Grotesk', 16, 400, 1.6),
            tg('accent', 'Button', 'Hanken Grotesk', 15, 700, 1.3),
        ],
        'custom_typography': [
            tg('gfeyebrow', 'Eyebrow', 'Hanken Grotesk', 13, 700, 1.3, 0.14, 'uppercase'),
            tg('gfh2', 'Section title (H2)', 'Archivo', custom('clamp(36px, 4.6vw, 60px)'), 800, 1.02, -0.03),
            tg('gflead', 'Lead paragraph', 'Hanken Grotesk', 18, 400, 1.65, size_m=17),
            tg('gfbody', 'Small body', 'Hanken Grotesk', 15, 400, 1.6),
        ],
        'body_background_background': 'classic', 'body_background_color': INK,
        'body_color': WHITE, **typo('Hanken Grotesk', 16, 400, 1.6, prefix='body_typography'),
        'link_normal_color': LIME, 'link_hover_color': LIME2,
        'h2_color': WHITE, 'h3_color': WHITE,
        'container_width': px(1176), 'container_padding': dims(0), 'space_between_widgets': gap(0),
        'site_name': 'Get Fit', 'site_description': 'Personal training in Helsinki and online',
        'viewport_md': 768, 'viewport_lg': 1025,
    }
