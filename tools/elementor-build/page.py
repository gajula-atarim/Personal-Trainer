from el import *


def anim(el, delay=0, kind='fadeInUp'):
    """Elementor Motion Effects entrance animation (restyled in getfit.css to the design's reveal)."""
    s = el['settings']
    key = 'animation' if el['elType'] == 'container' else '_animation'
    s[key] = kind
    if delay:
        s[key + '_delay'] = delay
    return el


def initials(txt, size=40, font=14):
    return heading(txt, 'div', INK, typo('Hanken Grotesk', font, 800, px(size, 'px')), 'center', 'gf-avatar',
                   extra={'_element_width': 'initial', '_element_custom_width': px(size)})


def author(ini, name, role, mt=16):
    return row([
        initials(ini),
        con([heading(name, 'div', WHITE, typo('Hanken Grotesk', 15, 700, 1.3)),
             heading(role, 'div', MUTED, typo('Hanken Grotesk', 13, 400, 1.4))],
            {'flex_gap': gap(0), 'width': px(0)}, cls='gf-grow'),
    ], {'flex_align_items': 'center', 'flex_gap': gap(12), 'flex_wrap': 'nowrap', 'margin': mt_dims(mt)}, cls='gf-author')


def mt_dims(v):
    return dims(v, 0, 0, 0)


def card_bg(att, fname, angle=0, a='rgba(10,26,26,0.97)', a_stop=0, b='rgba(10,26,26,0)', b_stop=75):
    return {'background_background': 'classic', 'background_image': {'url': UP + fname, 'id': att, 'size': '', 'source': 'library'},
            'background_position': 'center center', 'background_repeat': 'no-repeat', 'background_size': 'cover',
            'background_overlay_background': 'gradient', 'background_overlay_color': a, 'background_overlay_color_stop': px(a_stop, '%'),
            'background_overlay_color_b': b, 'background_overlay_color_b_stop': px(b_stop, '%'),
            'background_overlay_gradient_type': 'linear', 'background_overlay_gradient_angle': px(angle, 'deg'),
            'background_overlay_opacity': px(1)}


# ---------------------------------------------------------------- hero
HERO = [
    (7, 'getfit-hero-strength.jpg', 'Strength · Kamppi studio', 'Get strong.', 'Stay strong.',
     'Coached personal training in central Helsinki. A plan built for your body, technique checked every session, progress you can measure.'),
    (8, 'getfit-hero-weight-loss-scaled.jpg', 'Weight loss · Training + nutrition', 'Lose the weight.', 'For good.',
     'Training, nutrition and weekly check-ins in one plan you can keep — long after the first month.'),
    (9, 'getfit-hero-online-scaled.jpg', 'Online coaching · Anywhere', 'Your coach.', 'In your pocket.',
     'A programme in the app, video form reviews and a real coach checking in every week, wherever you train.'),
]
HERO_MIN = custom('clamp(640px, 96vh, 940px)')


def hero():
    slides = []
    for i, (att, f, eb, l1, l2, sub) in enumerate(HERO):
        bg = con([], merge(card_bg(att, f, 90, 'rgba(10,26,26,0.94)', 0, 'rgba(10,26,26,0.15)', 100),
                           {'min_height': px(100, '%')}), cls='gf-hero-bg', title='Slide image')
        content = con([
            eyebrow(eb),
            heading(l1 + '<br><span class="gf-lime">' + l2 + '</span>', 'h1' if i == 0 else 'h2', WHITE,
                    typo('Archivo', custom('clamp(52px, 7.4vw, 108px)'), 800, 0.98, -0.035), cls='gf-hero-title', margin=mt(22)),
            text('<p>' + sub + '</p>', SOFT, typo('Hanken Grotesk', 19, 400, 1.6, size_m=17), margin=mt(28),
                 extra={'_element_width': 'initial', '_element_custom_width': px(540), '_element_width_mobile': 'inherit'}),
            row([button('Book a free trial', '#book', 'primary', 'lg'),
                 button('How it works', '#method', 'ghost', 'lg')],
                {'flex_gap': gap(12), 'margin': mt_dims(36)}),
            icon_list([
                {'text': '<span class="gf-stars">★★★★★</span><strong>4.9</strong> from 380+ reviews', 'icon': ''},
                'Certified, insured coaches', 'No contract, cancel anytime'],
                SOFT, LIME, 14, inline=True, icon_size=11, cls='gf-trust', margin=mt(36),
                extra={'space_between': px(28)}),
        ], {'boxed_width': px(860), 'content_width': 'full', 'width': px(860), 'width_tablet': px(100, '%'),
            'flex_gap': gap(0)}, cls='gf-hero-copy', title='Slide text')
        wrap = con([content], {'content_width': 'boxed', 'boxed_width': px(1176), 'min_height': HERO_MIN,
                               'flex_justify_content': 'flex-end',
                               'padding': dims(150, 32, 135, 32), 'padding_mobile': dims(120, 20, 135, 20)},
                   cls='gf-hero-inner', title='Slide layout')
        slides.append(con([bg, wrap], {'min_height': HERO_MIN, 'flex_gap': gap(0)},
                          cls='gf-hero-slide' + (' is-active' if i == 0 else ''), title='Slide %d' % (i + 1)))
    tabs = []
    for i, t in enumerate(['Strength', 'Weight loss', 'Online coaching']):
        tabs.append(heading('0%d · %s' % (i + 1, t), 'div', MUTED2,
                            typo('Hanken Grotesk', 13, 700, 1.25, 0.12, 'uppercase'), cls='gf-hero-tab' + (' is-active' if i == 0 else '')))
    tabbar = grid(tabs, 3, (12, 24), 3, 3, {'padding': dims(0, 32, 40, 32), 'padding_mobile': dims(0, 20, 32, 20),
                                            'grid_gaps_mobile': {'column': '12', 'row': '12', 'isLinked': True, 'unit': 'px'}},
                  cls='gf-hero-tabs', title='Slide tabs')
    tabwrap = con([tabbar], {'content_width': 'boxed', 'boxed_width': px(1176)}, cls='gf-hero-tabwrap', title='Slide tabs')
    return con(slides + [tabwrap], {'content_width': 'full', 'min_height': HERO_MIN, 'flex_gap': gap(0),
                                    'overflow': 'hidden', 'background_background': 'classic', 'background_color': INK,
                                    'html_tag': 'section', '_element_id': 'top'},
               cls='gf-hero', title='Hero slider', inner=False)


# ---------------------------------------------------------------- studio
def studio():
    feats = [(28, 'getfit-icon-equipment.svg', 'Quality equipment', 'Racks, free weights and conditioning kit maintained to a high standard.'),
             (29, 'getfit-icon-spotless.svg', 'Spotless & private', 'Cleaned between every session, with a limited number of clients on the floor.'),
             (30, 'getfit-icon-showers.svg', 'Showers & lockers', 'Fresh towels, showers and secure lockers so you can train before work.'),
             (31, 'getfit-icon-nutrition.svg', 'Nutrition plan', 'Clear calorie and protein targets with meals you actually enjoy eating.')]
    items = []
    for i, (att, f, t, d) in enumerate(feats):
        items.append(anim(con([
            svg_icon(att, f, 60, 'gf-feature-icon'),
            heading(t, 'h3', WHITE, typo('Hanken Grotesk', 19, 600, 1.3, 0.04, 'uppercase'), 'center'),
            text('<p>' + d + '</p>', MUTED, gtypo('gfbody'), 'center', extra={'_element_width': 'initial', '_element_custom_width': px(250)}),
        ], {'flex_align_items': 'center', 'flex_gap': gap(18), 'padding': dims(0, 8)}, cls='gf-feature'), i * 120))
    return section([
        anim(con([eyebrow('Inside the studio', 'center'), h2('Transform your workout.', 'center'),
                  lead('A private studio in Kamppi with everything you need to train well — and nothing you don’t.', 'center', mt(20), 600)],
                 {'flex_align_items': 'center'}, cls='gf-head')),
        grid(items, 4, (40, 32), 2, 1, {'margin': mt_dims(64)}),
        anim(button('Discover more about us', '#about', 'primary', 'md', 'center', mt(48))),
    ], sid='studio', title='Inside the studio', pad=(120, 32, 140, 32))


# ---------------------------------------------------------------- about
def about():
    left = anim(con([
        eyebrow('About Get Fit'),
        h2('Built by Oliver Virtanen, for people done with starting over.'),
        lead('Oliver has coached in Helsinki for twelve years. He started Get Fit to give busy people what most gyms don’t: a real coach, a plan written for them and someone checking in every week.', margin=mt(24), maxw=520),
        lead('Today he leads a team of certified coaches in Kamppi and online — with the same no-shortcuts approach.', margin=mt(16), maxw=520),
        icon_list(['Certified Strength & Conditioning Specialist', 'Precision Nutrition Level 1', 'BSc Sports Science, University of Jyväskylä'],
                  SOFT, INK, 15, icon_size=11, cls='gf-checklist', margin=mt(32), extra={'icon_typography_font_weight': '600'}),
        button('Explore our plans →', '#pricing', 'primary', 'md', margin=mt(40)),
    ]))
    quote = con([
        text('<p>“I’d tried three gyms before Get Fit. Oliver’s team was the first to make it feel personal — and the first that stuck.”</p>',
             WHITE, typo('Hanken Grotesk', 17, 400, 1.6)),
        author('AL', 'Aino Laine', 'Client since 2024 · Helsinki'),
    ], {'padding': dims(22, 24), 'border_radius': dims(20)}, cls='gf-quote-card')
    right = anim(con([quote], merge(card_bg(10, 'getfit-about-oliver-scaled.jpg'),
                                    {'background_overlay_background': '', 'flex_justify_content': 'flex-end',
                                     'padding': dims(20), 'border_radius': dims(28), 'overflow': 'hidden'}),
                     cls='gf-ar-45 gf-about-media', title='Oliver photo'), 150)
    return section([grid([left, right], 2, (64, 64), 1, 1, {'grid_align_items': 'center'})],
                   sid='about', title='About', pad=(120, 32, 120, 32), cls='gf-glow gf-glow--lime-left')


# ---------------------------------------------------------------- problems
def problems():
    data = [(32, 'getfit-icon-generic-plan.svg', 'A generic plan', 'Copied from an app or a friend, ignoring your body, your schedule and your goal.'),
            (33, 'getfit-icon-no-checkin.svg', 'Nobody checking in', 'Motivation drops in week three and there’s no one to notice, adjust or push.'),
            (34, 'getfit-icon-crash-diets.svg', 'Crash diets', 'They work for a month, then the weight comes back — and so does the frustration.')]
    cards = []
    for i, (att, f, t, d) in enumerate(data):
        cards.append(anim(row([
            svg_icon(att, f, 22, 'gf-icon-tile', {'_element_width': 'initial', '_element_custom_width': px(48)}),
            con([heading(t, 'h3', WHITE, typo('Hanken Grotesk', 19, 700, 1.3)),
                 text('<p>' + d + '</p>', MUTED, gtypo('gfbody'), margin=mt(6))], {'width': px(0)}, cls='gf-grow'),
        ], {'flex_gap': gap(20), 'flex_wrap': 'nowrap', 'flex_align_items': 'flex-start', 'padding': dims(26, 28), 'border_radius': dims(20)},
            cls='gf-glass gf-glass--hover'), i * 120))
    cards.append(anim(heading('Get Fit fixes all three. <a href="#method">Here’s how ↓</a>', 'div', WHITE,
                              typo('Archivo', 24, 800, 1.3, -0.02), cls='gf-fixes', margin=dims(14, 4, 0, 4)), 360))
    left = anim(con([eyebrow('01 · Sound familiar?'), h2('You’ve started before. Here’s why it didn’t stick.'),
                     lead('Most people don’t fail for lack of willpower. They fail because the plan was never built for them.', margin=mt(24), maxw=460)]))
    return section([grid([left, con(cards, {'flex_gap': gap(14)})], 2, (64, 64), 1, 1, {'grid_align_items': 'start'})],
                   title='Sound familiar', pad=(140, 32, 120, 32), cls='gf-glow gf-glow--teal-right')


# ---------------------------------------------------------------- method
def method():
    steps = [(11, 'getfit-method-1.jpg', 'Day 1', 'Free trial', 'Train with a coach, get a movement assessment and set a clear goal together.'),
             (12, 'getfit-method-2.jpg', 'Within 48 hours', 'Your plan', 'Training and nutrition built around your body, schedule and food you enjoy.'),
             (13, 'getfit-method-3.jpg', '2–3× a week', 'Coached sessions', 'In our Kamppi studio or online, with technique and load checked every time.'),
             (14, 'getfit-method-4.jpg', 'Every week', 'Check-in', 'We review your progress and update the plan so you never stall.')]
    items = []
    for i, (att, f, tag, t, d) in enumerate(steps):
        media = con([image(att, f, 'gf-step-img', 'medium_large'),
                     heading('0%d' % (i + 1), 'div', INK, typo('Hanken Grotesk', 15, 800, 1), 'center', 'gf-step-badge')],
                    {'width': px(232), 'min_height': px(232), 'flex_gap': gap(0)}, cls='gf-step-media')
        items.append(con([
            media,
            heading(tag, 'div', LIME, typo('Hanken Grotesk', 12, 700, 1.3, 0.12, 'uppercase'), 'center', 'gf-step-tag', mt(32)),
            heading(t, 'h3', WHITE, typo('Archivo', 26, 800, 1.2, -0.02), 'center', 'gf-step-title', mt(8)),
            text('<p>' + d + '</p>', SOFT, gtypo('gfbody'), 'center', 'gf-step-text', mt(10),
                 {'_element_width': 'initial', '_element_custom_width': px(260)}),
        ], {'flex_align_items': 'center'}, cls='gf-step' + (' is-active' if i == 0 else ''), title='Step %d' % (i + 1)))
    head = anim(row([
        con([eyebrow('02 · The Get Fit method'),
             h2('A coach, a plan and a check-in <span class="gf-lime">every week.</span>', maxw=620)], cls='gf-grow-auto'),
        text('<p>One coach walks with you from your free trial to results that last.</p>', MUTED, typo('Hanken Grotesk', 17, 400, 1.6),
             extra={'_element_width': 'initial', '_element_custom_width': px(420)}),
    ], {'flex_justify_content': 'space-between', 'flex_align_items': 'flex-end', 'flex_gap': gap(32)}))
    return section([head, grid(items, 4, (48, 24), 2, 1, {'margin': mt_dims(72)}, cls='gf-steps')],
                   sid='method', title='Method', pad=(40, 32, 140, 32))


# ---------------------------------------------------------------- programmes
def programs():
    data = [(15, 'getfit-program-strength.jpg', '01 · Best for building strength', 'Strength Foundations',
             'Master the big lifts and get measurably stronger in 12 weeks, 2–3 studio sessions a week.'),
            (16, 'getfit-program-recomp.jpg', '02 · Best for fat loss', 'Body Recomposition',
             'Lose fat, keep your muscle. Training, nutrition targets and weekly weigh-ins in one plan.'),
            (17, 'getfit-program-online.jpg', '03 · Best for busy schedules', 'Online Coaching',
             'Train anywhere with a weekly-updated programme, form reviews within 24 hours and direct chat.')]
    cards = []
    for i, (att, f, best, name, desc) in enumerate(data):
        card = con([
            heading(best, 'div', LIME, typo('Hanken Grotesk', 12, 700, 1.3, 0.12, 'uppercase')),
            heading(name, 'h3', WHITE, typo('Archivo', 30, 800, 1.05, -0.02)),
            text('<p>' + desc + '</p>', SOFT, typo('Hanken Grotesk', 15, 400, 1.55)),
        ], merge(card_bg(att, f, 0, 'rgba(10,26,26,0.97)', 0, 'rgba(10,26,26,0)', 75),
                 {'flex_justify_content': 'flex-end', 'flex_gap': gap(10), 'padding': dims(30), 'border_radius': dims(24),
                  'border_border': 'solid', 'border_width': dims(1), 'border_color': 'rgba(255,255,255,0.08)', 'overflow': 'hidden'}),
            cls='gf-ar-45 gf-card-lift', title=name)
        cards.append(anim(con([card]), i * 120))
    head = anim(row([
        con([eyebrow('03 · Choose your path'), h2('One goal. The right programme for it.', maxw=720)], cls='gf-grow-auto'),
        button('Not sure? Ask in your free trial', '#book', 'ghost', 'mdo'),
    ], {'flex_justify_content': 'space-between', 'flex_align_items': 'flex-end', 'flex_gap': gap(24)}))
    return section([head, grid(cards, 3, (20, 20), 1, 1, {'margin': mt_dims(56)})], sid='programs', title='Programmes', pad=(40, 32, 140, 32))


# ---------------------------------------------------------------- results
def counter(num, suffix, label, last=False):
    s = {'starting_number': 0, 'ending_number': num, 'suffix': suffix, 'duration': 1600, 'thousand_separator': '',
         'title': label, 'title_tag': 'div', 'number_color': LIME, 'title_color': SOFT,
         **typo('Archivo', 56, 800, 1, -0.03, prefix='typography_number'),
         **typo('Hanken Grotesk', 15, 400, 1.5, prefix='typography_title')}
    return con([w('counter', s, 'gf-counter')], {'padding': dims(34, 30)}, cls='gf-stat' + (' gf-stat--last' if last else ''))


def results():
    stats = grid([counter(340, '+', 'clients coached in Helsinki and online'),
                  counter(4.9, '★', 'average rating from 380+ reviews'),
                  counter(87, '%', 'still training with us after 6 months'),
                  counter(9, ' kg', 'average fat loss in 16 weeks', True)], 4, (0, 0), 2, 1,
                 {'margin': mt_dims(56), 'border_radius': dims(24), 'overflow': 'hidden'}, cls='gf-glass gf-stats')
    data = [(18, 'getfit-result-mikko.jpg', '−14 kg', 'in 20 weeks', 'Mikko, 41', 'Body Recomposition'),
            (19, 'getfit-result-jussi.jpg', '+45 kg', 'on his deadlift in 6 months', 'Jussi, 34', 'Strength Foundations'),
            (20, 'getfit-result-daniel.jpg', '−9 kg', 'in 16 weeks, fully online', 'Daniel, 29', 'Online Coaching')]
    cards = []
    for i, (att, f, metric, when, name, prog) in enumerate(data):
        cards.append(anim(con([
            heading(metric, 'div', LIME, typo('Archivo', 52, 800, 1, -0.03)),
            heading(when, 'div', SOFT, typo('Hanken Grotesk', 14, 400, 1.4), margin=mt(6)),
            text('<p><strong>' + name + '</strong> · <span class="gf-soft">' + prog + '</span></p>', WHITE,
                 typo('Hanken Grotesk', 15, 400, 1.5), margin=mt(14)),
        ], merge(card_bg(att, f, 0, 'rgba(10,26,26,0.97)', 0, 'rgba(10,26,26,0)', 75),
                 {'flex_justify_content': 'flex-end', 'padding': dims(30), 'border_radius': dims(24), 'overflow': 'hidden'}),
            cls='gf-ar-45', title=name), i * 120))
    quotes = [('I know exactly what to do every session and why. Six months in and I’m stronger than I’ve ever been.', 'Aino Laine', 'AL', 'Strength Foundations'),
              ('Fourteen kilos down without feeling like I’m on a diet. The weekly check-ins kept me honest.', 'Mikko Heikkinen', 'MH', 'Body Recomposition'),
              ('I travel constantly for work and still haven’t missed a week. The app and form reviews are brilliant.', 'Daniel Okafor', 'DO', 'Online Coaching'),
              ('My back pain is gone and I squat more than ever. Calm, precise coaching that actually cares.', 'Jussi Korhonen', 'JK', 'Studio plan'),
              ('The free trial sold me. I left with a real plan and a coach who remembered my name the next week.', 'Emma Nieminen', 'EN', 'Intensive plan'),
              ('First gym I’ve stuck with for more than two months. It feels personal, never intimidating.', 'Helmi Salo', 'HS', 'Studio plan')]
    qcards = []
    for q, name, ini, role in quotes:
        qcards.append(con([
            heading('★★★★★', 'div', LIME, typo('Hanken Grotesk', 16, 400, 1, px(3, 'px'))),
            text('<p>“' + q + '”</p>', WHITE, typo('Hanken Grotesk', 17, 400, 1.6)),
            author(ini, name, role + ' · Verified client', 0),
        ], {'width': px(400), 'width_mobile': px(320), 'padding': dims(30), 'border_radius': dims(24), 'flex_gap': gap(18)},
            cls='gf-glass gf-glass--hover gf-quote', title=name))
    marquee = con([con(qcards, {'flex_direction': 'row', 'flex_wrap': 'nowrap', 'flex_gap': gap(20)}, cls='gf-marquee-track', title='Quotes')],
                  {'margin': mt_dims(56), 'padding': dims(4, 0), 'overflow': 'hidden'}, cls='gf-marquee', title='Testimonials marquee')
    inner = con([
        anim(con([eyebrow('04 · The proof', 'center'), h2('Real people. Busy lives. Results that last.', 'center')],
                 {'flex_align_items': 'center'}, cls='gf-head')),
        anim(stats),
        grid(cards, 3, (20, 20), 1, 1, {'margin': mt_dims(20)}),
    ], {'content_width': 'boxed', 'boxed_width': px(1176), 'padding': dims(0, 32), 'padding_mobile': dims(0, 20)}, title='Results')
    return con([inner, marquee], {'content_width': 'full', 'html_tag': 'section', '_element_id': 'results',
                                  'padding': dims(40, 0, 140, 0), 'padding_mobile': dims(28, 0, 98, 0)},
               cls='gf-glow gf-glow--lime-left', title='Results', inner=False)


# ---------------------------------------------------------------- coaches
def coaches():
    data = [(21, 'getfit-coach-mikael.jpg', 'Mikael Koski', 'Strength & conditioning', 'CSCS · 9 years coaching'),
            (22, 'getfit-coach-sofia.jpg', 'Sofia Halonen', 'Weight loss & nutrition', 'Precision Nutrition L2 · 7 years'),
            (23, 'getfit-coach-elias.jpg', 'Elias Nyström', 'Online coaching', 'BSc Sports Science · 6 years'),
            (24, 'getfit-coach-laura.jpg', 'Laura Heikkilä', 'Mobility & rehab', 'Physiotherapist · 8 years')]
    items = []
    for i, (att, f, name, role, cred) in enumerate(data):
        items.append(anim(con([
            image(att, f, 'gf-coach-img', 'medium_large', alt=name),
            heading(name, 'h3', WHITE, typo('Hanken Grotesk', 19, 700, 1.3), 'center', margin=mt(22)),
            heading(role, 'div', LIME, typo('Hanken Grotesk', 14, 600, 1.4), 'center', margin=mt(4)),
            heading(cred, 'div', MUTED, typo('Hanken Grotesk', 13, 400, 1.4), 'center', margin=mt(8)),
        ], {'flex_align_items': 'center'}, title=name), i * 100))
    return section([
        anim(con([eyebrow('05 · Your coaches', 'center'), h2('Experts who care whether you show up.', 'center'),
                  lead('Every Get Fit coach is certified, insured and has at least five years of hands-on coaching.', 'center', mt(20), 560)],
                 {'flex_align_items': 'center'}, cls='gf-head')),
        grid(items, 4, (32, 32), 2, 1, {'margin': mt_dims(64)}),
    ], sid='coaches', title='Coaches', pad=(40, 32, 140, 32), cls='gf-glow gf-glow--teal-right')


# ---------------------------------------------------------------- pricing
def pricing():
    plans = [('Online', 'Remote coaching, any gym', 129, False, ['Personal programme in the app', 'Weekly check-in & adjustments', 'Video form reviews', 'Chat with your coach']),
             ('Studio', '4 coached sessions a month', 299, True, ['4 × 60 min studio sessions', 'Everything in Online', 'Personal nutrition plan', 'Monthly progress review']),
             ('Intensive', '8 coached sessions a month', 529, False, ['8 × 60 min studio sessions', 'Everything in Studio', 'Body composition scans', 'Priority booking'])]
    cards = []
    for i, (name, tag, price, feat, feats) in enumerate(plans):
        top = [heading(name + ' package', 'h3', WHITE, typo('Hanken Grotesk', 18, 700, 1.3))]
        if feat:
            top.append(heading('Popular', 'div', LIME, typo('Hanken Grotesk', 11, 600, 1.3, 0.04), cls='gf-popular'))
        cards.append(anim(con([
            row(top, {'flex_justify_content': 'space-between', 'flex_align_items': 'center', 'flex_gap': gap(12), 'flex_wrap': 'nowrap'}),
            heading(tag, 'div', MUTED2, typo('Hanken Grotesk', 14, 400, 1.4), margin=mt(6)),
            row([heading('€' + str(price), 'div', WHITE, typo('Archivo', 52, 800, 1, -0.03), cls='gf-price'),
                 heading('/ month', 'div', SOFT, typo('Hanken Grotesk', 17, 400, 1.3))],
                {'flex_align_items': 'baseline', 'flex_gap': gap(8), 'margin': mt_dims(28), 'flex_wrap': 'nowrap'}, cls='gf-price-row'),
            heading('Billed monthly · cancel anytime', 'div', MUTED2, typo('Hanken Grotesk', 13, 400, 1.4), cls='gf-price-note', margin=mt(8)),
            icon_list(feats, '#9FB0AE', LIME if feat else MUTED2, 15, gapv=14, icon_size=11, cls='gf-plan-feats',
                      margin=dims(28, 0, 36, 0), extra={'icon_typography_line_height': px(1.4, 'em')}),
            button('Choose plan', '#book', 'primary', 'md', 'justify', cls='gf-plan-btn' + (' gf-plan-btn--featured' if feat else ''),
                   icon='fas fa-arrow-right',
                   extra={'text_padding': dims(15, 20), 'border_radius': dims(10), **typo('Hanken Grotesk', 15, 600, px(1.3, 'em')),
                          'icon_indent': px(14), 'background_color': LIME if feat else '#173434', 'button_text_color': INK if feat else WHITE,
                          'button_background_hover_color': LIME if feat else '#173434', 'hover_color': INK if feat else WHITE,
                          '_element_width': 'initial', '_element_custom_width': px(86, '%'), '_flex_align_self': 'center',
                          'link': {'url': '#book', 'is_external': '', 'nofollow': ''}}),
        ], {'padding': dims(36, 30, 30, 30), 'border_radius': dims(22)},
            cls='gf-plan' + (' gf-plan--featured' if feat else ''), title=name + ' plan'), i * 120))
    billing = anim(row([heading('Monthly', 'div', INK, typo('Hanken Grotesk', 14, 700, 1.3), cls='gf-billing-opt gf-billing-m is-active'),
                        heading('3 months · save 10%', 'div', MUTED, typo('Hanken Grotesk', 14, 700, 1.3), cls='gf-billing-opt gf-billing-q')],
                       {'flex_gap': gap(4), 'padding': dims(4), 'border_radius': dims(999), 'flex_wrap': 'nowrap'},
                       cls='gf-glass gf-billing', title='Billing toggle'))
    return section([
        anim(con([eyebrow('06 · Pricing', 'center'), h2('Simple plans. Zero risk to start.', 'center'),
                  heading('<span class="gf-offer-tag">OFFER</span>50% off your first month — until 30 November', 'div', WHITE,
                          typo('Hanken Grotesk', 14, 600, 1.4), 'center', 'gf-offer', mt(24))],
                 {'flex_align_items': 'center'}, cls='gf-head')),
        con([billing], {'flex_align_items': 'center', 'margin': mt_dims(32)}),
        grid(cards, 3, (20, 20), 1, 1, {'margin': mt_dims(40), 'grid_align_items': 'stretch'}, cls='gf-plans'),
        anim(icon_list(['First session free', 'No lock-in contract', 'Pause up to 4 weeks a year', 'Secure payment'], SOFT, LIME, 15,
                       inline=True, icon_size=12, cls='gf-trust gf-trust--center', margin=mt(36),
                       extra={'space_between': px(36), 'icon_align': 'center'})),
    ], sid='pricing', title='Pricing', pad=(40, 32, 140, 32))


# ---------------------------------------------------------------- booking
def booking():
    steps = []
    for i, l in enumerate(['Choose a session', 'Pick date & time', 'Your details', 'Confirmed']):
        steps.append(row([
            heading(str(i + 1), 'div', MUTED2, typo('Hanken Grotesk', 13, 800, px(34, 'px')), 'center', 'gf-bstep-num',
                    extra={'_element_width': 'initial', '_element_custom_width': px(34)}),
            heading(l, 'div', WHITE, typo('Hanken Grotesk', 15, 700, 1.3), cls='gf-bstep-label'),
        ], {'flex_align_items': 'center', 'flex_gap': gap(14), 'padding': dims(12, 0), 'flex_wrap': 'nowrap'},
            cls='gf-bstep' + (' is-current' if i == 0 else ''), title='Step %d' % (i + 1)))
    left = con(steps + [
        text('<p>Get Fit Studio<br>Urho Kekkosen katu 1, 00100 Helsinki</p>', MUTED, typo('Hanken Grotesk', 14, 400, 1.7), cls='gf-baddr'),
    ], {'padding': dims(20), 'flex_gap': gap(4), 'width': px(340), 'width_tablet': px(100, '%')}, cls='gf-bsteps', title='Steps')

    def pane_head(step, title):
        return [heading(step, 'div', LIME, typo('Hanken Grotesk', 12, 700, 1.3, 0.12, 'uppercase'), cls='gf-pane-step'),
                heading(title, 'h3', WHITE, typo('Archivo', 28, 800, 1.2, -0.02), margin=mt(8))]

    svcs = []
    for sid_, name, dur, where, price in [('trial', 'Free trial session', '45 min', 'Studio or video', 'Free'),
                                          ('pt', '1:1 Strength Session', '60 min', 'Studio', '€85'),
                                          ('online', 'Online Coaching Kick-off', '45 min', 'Video call', '€60')]:
        svcs.append(row([
            con([heading(name, 'div', None, typo('Hanken Grotesk', 16, 700, 1.3), cls='gf-svc-name'),
                 heading(dur + ' · ' + where, 'div', None, typo('Hanken Grotesk', 14, 400, 1.4), cls='gf-svc-meta')],
                {'flex_gap': gap(4), 'width': px(0)}, cls='gf-grow'),
            heading(price, 'div', None, typo('Archivo', 22, 800, 1.2), cls='gf-svc-price'),
        ], {'flex_justify_content': 'space-between', 'flex_align_items': 'center', 'flex_gap': gap(16), 'flex_wrap': 'nowrap',
            'padding': dims(20, 22), 'border_radius': dims(16)},
            cls='gf-svc gf-svc--' + sid_, title=name))
    pane1 = con(pane_head('Step 1 of 3', 'Choose a session') + [con(svcs, {'flex_gap': gap(12), 'margin': mt_dims(28)})],
                cls='gf-pane gf-pane--1', title='Step 1 – session')
    pane2 = con(pane_head('Step 2 of 3', 'Pick a date & time') + [
        w('html', {'html': '<div class="gf-days" aria-label="Choose a day"></div><div class="gf-times-label">Available times</div><div class="gf-times" aria-label="Choose a time"></div><div class="gf-times-empty">Select a day to see open slots.</div>'})],
        cls='gf-pane gf-pane--2', title='Step 2 – date & time')
    pane3 = con(pane_head('Step 3 of 3', 'Your details') + [
        w('html', {'html': '<div class="gf-summary"><div class="gf-summary-name"></div><div class="gf-summary-when"></div></div>'
                           '<form class="gf-form" novalidate>'
                           '<label>Full name<input name="name" autocomplete="name" placeholder="Aino Laine"></label>'
                           '<label>Email<input name="email" type="email" autocomplete="email" placeholder="you@example.com"></label>'
                           '<label>What would you like to achieve? <span>Optional</span><textarea name="note" rows="3" placeholder="e.g. Lose 8 kg before summer"></textarea></label>'
                           '</form>'})],
        cls='gf-pane gf-pane--3', title='Step 3 – details')
    pane4 = con([
        heading('✓', 'div', INK, typo('Hanken Grotesk', 28, 800, px(64, 'px')), 'center', 'gf-done-check',
                extra={'_element_width': 'initial', '_element_custom_width': px(64)}),
        heading('You’re in, <span class="gf-first-name">friend</span>.', 'h3', WHITE, typo('Archivo', 40, 800, 1.05, -0.03, size_m=32)),
        text('<p><span class="gf-done-service">Your session</span> on <span class="gf-done-date"></span> at <span class="gf-done-time"></span>. Your coach will confirm by email at <span class="gf-done-email"></span> within the hour.</p>',
             SOFT, typo('Hanken Grotesk', 17, 400, 1.6)),
        button('Book another session', '#book', 'ghost', 'sm', margin=mt(12), cls='gf-book-reset'),
    ], {'flex_justify_content': 'center', 'flex_align_items': 'flex-start', 'flex_gap': gap(16)},
        cls='gf-pane gf-pane--4 gf-pane--done', title='Step 4 – confirmed')
    nav = row([
        button('← Back', '#book', 'ghost', 'md', cls='gf-bnav-back', extra={'border_border': 'none', 'text_padding': dims(12, 0)}),
        button('Continue', '#book', 'primary', 'md', cls='gf-bnav-next', extra={'text_padding': dims(16, 30)}),
    ], {'flex_justify_content': 'space-between', 'flex_align_items': 'center', 'flex_gap': gap(12), 'flex_wrap': 'nowrap',
        'padding': dims(32, 0, 0, 0)}, cls='gf-bnav', title='Back / Continue')
    panel = con([pane1, pane2, pane3, pane4, nav],
                {'padding': dims(36), 'padding_mobile': dims(24), 'border_radius': dims(20), 'min_height': px(480), 'width': px(0), 'width_tablet': px(100, '%')},
                cls='gf-bpanel gf-grow', title='Booking panel')
    box = anim(row([left, panel], {'flex_gap': gap(16), 'padding': dims(16), 'border_radius': dims(28), 'flex_wrap': 'nowrap',
                                   'flex_direction_tablet': 'column', 'flex_align_items': 'stretch', 'margin': mt_dims(48)},
                   cls='gf-glass gf-booking', title='Booking widget'))
    return section([
        anim(con([eyebrow('07 · Your first step', 'center'), h2('Book your free trial in 60 seconds.', 'center')],
                 {'flex_align_items': 'center'}, cls='gf-head')),
        box,
    ], sid='book', title='Book a free trial', pad=(40, 32, 140, 32))


# ---------------------------------------------------------------- faq
FAQ = [('I’m a complete beginner. Is this for me?', 'Yes. Most of our clients start with little or no gym experience. Your free trial includes a movement assessment, and the plan starts exactly where you are.'),
       ('What happens in the free trial?', '45 minutes with a coach: a short chat about your goal, a movement assessment and a real workout. You leave with a recommended plan — no obligation to join.'),
       ('How does online coaching work?', 'Your programme lives in the app and is updated weekly. Film key lifts for form feedback within 24 hours, chat with your coach any time, and join a monthly video review.'),
       ('Is there a contract?', 'No. Plans are billed monthly and you can cancel any time. Sessions can be moved free of charge up to 24 hours before.'),
       ('Can I pause my plan?', 'Yes, up to four weeks a year for holidays or illness, at no cost.')]


def faq():
    items, kids = [], []
    for i, (q, a) in enumerate(FAQ):
        items.append({'item_title': q, '_id': nid(), 'element_css_id': ''})
        kids.append(con([text('<p>' + a + '</p>', MUTED, typo('Hanken Grotesk', 15, 400, 1.7))],
                        {'padding': dims(0, 70, 24, 26), 'padding_mobile': dims(0, 26, 22, 22)}, title='Answer %d' % (i + 1)))
    acc = w('nested-accordion', {
        'items': items, 'default_state': 'expanded', 'max_items_expended': 'one', 'title_tag': 'div',
        'accordion_item_title_icon': {'value': 'fas fa-plus', 'library': 'fa-solid'},
        'accordion_item_title_icon_active': {'value': 'fas fa-minus', 'library': 'fa-solid'},
        'accordion_item_title_position_horizontal': 'stretch', 'accordion_item_title_icon_position': 'end',
        'accordion_item_title_space_between': px(12),
        'accordion_padding': dims(22, 26), 'accordion_padding_mobile': dims(20, 22),
        'title_typography_typography': 'custom', 'title_typography_font_family': 'Hanken Grotesk', 'title_typography_font_size': px(17),
        'title_typography_font_weight': '700', 'title_typography_line_height': px(1.4, 'em'),
        'normal_title_color': WHITE, 'hover_title_color': WHITE, 'active_title_color': WHITE,
        'icon_size': px(14), 'icon_color': WHITE, 'icon_active_color': INK, 'icon_spacing': px(24),
    }, 'gf-faq')
    acc['elements'] = kids
    left = anim(con([eyebrow('08 · Questions'), h2('Still deciding? Good questions.'),
                     lead('Anything else, email <a href="mailto:hello@getfit.fi">hello@getfit.fi</a>. We reply within one working day.', margin=mt(20), maxw=420)]))
    return section([grid([left, anim(acc)], 2, (56, 56), 1, 1, {'grid_align_items': 'start'})],
                   sid='faq', title='FAQ', pad=(40, 32, 140, 32))


# ---------------------------------------------------------------- final CTA
def cta():
    box = anim(con([
        eyebrow('09 · Your move'),
        heading('Stop wishing.<br><span class="gf-lime">Start training.</span>', 'h2', WHITE,
                typo('Archivo', custom('clamp(44px, 6vw, 80px)'), 800, 0.98, -0.035), margin=mt(20)),
        text('<p>Your first session is free. If it’s not for you, you walk away with a plan anyway.</p>', SOFT,
             typo('Hanken Grotesk', 18, 400, 1.6), margin=mt(24), extra={'_element_width': 'initial', '_element_custom_width': px(480), '_element_width_mobile': 'inherit'}),
        button('Book a free trial →', '#book', 'primary', 'xl', margin=mt(32)),
        heading('Only 6 trial slots left this week', 'div', SOFT, typo('Hanken Grotesk', 14, 400, 1.4), margin=mt(18)),
    ], merge(card_bg(25, 'getfit-cta-scaled.jpg', 90, 'rgba(10,26,26,0.95)', 0, 'rgba(10,26,26,0.2)', 100),
             {'min_height': px(520), 'flex_justify_content': 'center', 'padding': dims(72, 56), 'padding_mobile': dims(48, 24),
              'border_radius': dims(32), 'overflow': 'hidden'}), cls='gf-cta', title='Final call to action'), 0, 'zoomIn')
    return section([box], title='Final CTA', pad=(0, 32, 100, 32))


def page():
    return [hero(), studio(), about(), problems(), method(), programs(), results(), coaches(), pricing(), booking(), faq(), cta()]
