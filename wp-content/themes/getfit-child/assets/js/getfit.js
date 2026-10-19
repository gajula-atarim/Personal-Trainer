/* Get Fit — interactions for the Elementor build (header state, hero slider,
   method steps, testimonial marquee, pricing toggle, booking flow).
   Every text it touches comes from Elementor widgets, so editors keep control. */
(function () {
	'use strict';

	var $ = function (s, c) { return (c || document).querySelector(s); };
	var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
	var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	/* Text the scripts write themselves (everything else is edited in Elementor). */
	var FI = /^fi/i.test(document.documentElement.lang || '');
	var T = FI ? {
		locale: 'fi-FI',
		quarterly: function (sym, total) { return total + ' ' + sym + ' laskutetaan 3 kk välein'; },
		price: function (sym, v) { return v + ' ' + sym; },
		at: ' klo ',
		confirm: 'Vahvista ilmainen kokeilu',
		full: 'varattu täyteen',
		interested: function (name) { return 'Kiinnostunut paketista: ' + name; },
		planSuffix: /\s*-?paketti\s*$/i
	} : {
		locale: 'en-GB',
		quarterly: function (sym, total) { return sym + total + ' billed every 3 months'; },
		price: function (sym, v) { return sym + v; },
		at: ' at ',
		confirm: 'Confirm my free trial',
		full: 'fully booked',
		interested: function (name) { return 'Interested in the ' + name + ' plan'; },
		planSuffix: /\s*package\s*$/i
	};
	var raf = window.requestAnimationFrame.bind(window);

	function inEditor() {
		return document.body.classList.contains('elementor-editor-active') ||
			!!(window.elementorFrontend && window.elementorFrontend.isEditMode && window.elementorFrontend.isEditMode());
	}

	function pressable(el, fn) {
		if (!el.hasAttribute('tabindex')) el.tabIndex = 0;
		if (!el.hasAttribute('role')) el.setAttribute('role', 'button');
		el.addEventListener('click', fn);
		el.addEventListener('keydown', function (e) {
			if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fn(e); }
		});
	}

	function headingText(el) {
		var t = el && ($('.elementor-heading-title', el) || el);
		return t ? t.textContent.trim() : '';
	}

	/* Header: transparent over the hero, solid after 40px, reading-progress line. */
	function header() {
		var h = $('.gf-header');
		if (!h) return;
		var bar = document.createElement('div');
		bar.className = 'gf-progress';
		h.appendChild(bar);
		var ticking = false;
		function update() {
			ticking = false;
			var y = window.scrollY;
			var max = document.documentElement.scrollHeight - window.innerHeight;
			h.classList.toggle('is-scrolled', y > 40);
			bar.style.width = (max > 0 ? y / max * 100 : 0) + '%';
		}
		window.addEventListener('scroll', function () { if (!ticking) { ticking = true; raf(update); } }, { passive: true });
		update();
	}

	/* Hero: crossfading slides with timed progress tabs (6.5 s per slide). */
	function hero() {
		var root = $('.gf-hero');
		if (!root) return;
		var slides = $$('.gf-hero-slide', root);
		var tabs = $$('.gf-hero-tab', root);
		if (slides.length < 2) return;
		var DUR = 6500, current = 0, start = performance.now();

		function go(n) {
			current = (n + slides.length) % slides.length;
			start = performance.now();
			slides.forEach(function (s, k) {
				s.classList.toggle('is-active', k === current);
				s.setAttribute('aria-hidden', k === current ? 'false' : 'true');
			});
			tabs.forEach(function (t, k) {
				t.classList.toggle('is-active', k === current);
				t.setAttribute('aria-pressed', k === current ? 'true' : 'false');
				t.style.setProperty('--p', k < current ? '100%' : (k === current && reduce ? '100%' : '0%'));
			});
		}
		tabs.forEach(function (t, k) { pressable(t, function () { go(k); }); });
		go(0);
		if (reduce) return;
		(function loop(now) {
			var el = now - start;
			if (tabs[current]) tabs[current].style.setProperty('--p', Math.min(100, el / DUR * 100) + '%');
			if (el > DUR) go(current + 1);
			raf(loop);
		})(performance.now());
	}

	/* Method: one step at a time, progress ring fills over 4.2 s. */
	function method() {
		var wrap = $('.gf-steps');
		if (!wrap) return;
		var steps = $$('.gf-step', wrap);
		if (!steps.length) return;
		var C = 703.7, DUR = 4200, current = 0, start = performance.now();
		var ring = '<svg class="gf-ring" viewBox="0 0 232 232" aria-hidden="true">' +
			'<circle cx="116" cy="116" r="112" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="4"></circle>' +
			'<circle class="gf-ring-bar" cx="116" cy="116" r="112" fill="none" stroke="#DAF25E" stroke-width="6" stroke-linecap="round" stroke-dasharray="703.7" stroke-dashoffset="703.7"></circle></svg>';
		steps.forEach(function (s, k) {
			var m = $('.gf-step-media', s);
			if (m && !$('.gf-ring', m)) m.insertAdjacentHTML('afterbegin', ring);
			pressable(s, function () { go(k); });
		});
		function bar(s) { return $('.gf-ring-bar', s); }
		function go(n) {
			current = n % steps.length;
			start = performance.now();
			steps.forEach(function (s, k) {
				s.classList.toggle('is-active', k === current);
				s.setAttribute('aria-pressed', k === current ? 'true' : 'false');
				var b = bar(s);
				if (b) b.setAttribute('stroke-dashoffset', k === current && reduce ? 0 : C);
			});
		}
		wrap.classList.add('is-ready');
		go(0);
		if (reduce) return;
		(function loop(now) {
			var el = now - start, b = bar(steps[current]);
			if (b) b.setAttribute('stroke-dashoffset', C * (1 - Math.min(1, el / DUR)));
			if (el > DUR) go(current + 1);
			raf(loop);
		})(performance.now());
	}

	/* Testimonials: endless marquee, pauses on hover. */
	function marquee() {
		$$('.gf-marquee').forEach(function (m) {
			var track = $('.gf-marquee-track', m);
			if (!track) return;
			$$(':scope > *', track).forEach(function (card) {
				var c = card.cloneNode(true);
				c.setAttribute('aria-hidden', 'true');
				c.removeAttribute('id');
				track.appendChild(c);
			});
			if (reduce) return;
			var x = 0, last = performance.now(), paused = false;
			m.addEventListener('mouseenter', function () { paused = true; });
			m.addEventListener('mouseleave', function () { paused = false; });
			(function loop(now) {
				var dt = Math.min(64, now - last);
				last = now;
				if (!paused) {
					x -= dt * 0.045;
					var half = track.scrollWidth / 2;
					if (-x >= half) x += half;
					track.style.transform = 'translateX(' + x + 'px)';
				}
				raf(loop);
			})(last);
		});
	}

	/* Pricing: Monthly / 3 months (10% off) toggle. Prices are read from the widgets. */
	function pricing() {
		var opts = $$('.gf-billing-opt');
		if (!opts.length) return;
		var cards = $$('.gf-plan').map(function (card) {
			var price = $('.gf-price .elementor-heading-title', card);
			var note = $('.gf-price-note .elementor-heading-title', card);
			var raw = price ? price.textContent : '';
			return {
				price: price, note: note,
				symbol: raw.replace(/[0-9.,\s]/g, '') || '€',
				monthly: parseFloat(raw.replace(/[^0-9.]/g, '')) || 0,
				noteText: note ? note.textContent : ''
			};
		});
		function set(quarterly) {
			opts.forEach(function (o) {
				var on = o.classList.contains(quarterly ? 'gf-billing-q' : 'gf-billing-m');
				o.classList.toggle('is-active', on);
				o.setAttribute('aria-pressed', on ? 'true' : 'false');
			});
			cards.forEach(function (c) {
				if (!c.price) return;
				var v = quarterly ? Math.round(c.monthly * 0.9) : c.monthly;
				c.price.textContent = T.price(c.symbol, v);
				if (c.note) c.note.textContent = quarterly ? T.quarterly(c.symbol, v * 3) : c.noteText;
			});
		}
		opts.forEach(function (o) { pressable(o, function () { set(o.classList.contains('gf-billing-q')); }); });
		set(false);
	}

	/* Booking: four-step trial booking (session → date & time → details → confirmed). */
	var booking = null;
	function bookingFlow() {
		var root = $('.gf-booking');
		if (!root) return;
		var panes = $$('.gf-pane', root);
		var stepRows = $$('.gf-bstep', root);
		var next = $('.gf-bnav-next', root), back = $('.gf-bnav-back', root), nav = $('.gf-bnav', root);
		var nextA = next && $('a', next), backA = back && $('a', back);
		var nextText = nextA && $('.elementor-button-text', nextA);
		var nextDefault = nextText ? nextText.textContent : 'Continue';
		var pane2 = $('.gf-pane--2', root);
		var pane2Step = pane2 && $('.gf-pane-step .elementor-heading-title', pane2);
		var pane2StepText = pane2Step ? pane2Step.textContent : '';
		var form = $('.gf-form', root);
		var daysEl = $('.gf-days', root), timesEl = $('.gf-times', root);
		var TIMES = ['07:00', '08:00', '09:30', '12:00', '16:00', '17:30', '19:00'];
		var services = $$('.gf-svc', root).map(function (el) {
			var meta = headingText($('.gf-svc-meta', el));
			return { el: el, id: (el.className.match(/gf-svc--([\w-]+)/) || [])[1], name: headingText($('.gf-svc-name', el)), where: meta.split('·').pop().trim() };
		});
		var days = [];
		var d = new Date();
		d.setHours(0, 0, 0, 0);
		d.setDate(d.getDate() + 1);
		while (days.length < 10) {
			if (d.getDay() !== 0) days.push(new Date(d));
			d.setDate(d.getDate() + 1);
		}
		var fmt = function (date, o) { return date.toLocaleDateString(T.locale, o).replace(/\.$/, ''); };
		var st = { step: 1, svc: null, day: null, time: null };

		if (daysEl) {
			daysEl.innerHTML = days.map(function (x, k) {
				return '<button type="button" class="gf-day" data-k="' + k + '" aria-pressed="false"><small>' + fmt(x, { weekday: 'short' }) +
					'</small><strong>' + x.getDate() + '</strong><span>' + fmt(x, { month: 'short' }) + '</span></button>';
			}).join('');
			daysEl.addEventListener('click', function (e) {
				var b = e.target.closest('.gf-day');
				if (!b) return;
				st.day = +b.getAttribute('data-k');
				st.time = null;
				render();
			});
		}
		if (timesEl) {
			timesEl.addEventListener('click', function (e) {
				var b = e.target.closest('.gf-time');
				if (!b || b.disabled) return;
				st.time = b.getAttribute('data-t');
				render();
			});
		}
		services.forEach(function (s) { pressable(s.el, function () { st.svc = s; render(); }); });
		if (form) {
			form.addEventListener('input', render);
			form.addEventListener('submit', function (e) { e.preventDefault(); goNext(); });
		}

		function valid() {
			if (st.step === 1) return !!st.svc;
			if (st.step === 2) return st.day !== null && !!st.time;
			if (st.step === 3) return form && form.elements.name.value.trim().length > 1 && /\S+@\S+\.\S+/.test(form.elements.email.value);
			return false;
		}
		function dateLabel() { return st.day === null ? '' : fmt(days[st.day], { weekday: 'long', day: 'numeric', month: 'long' }); }
		function fill(sel, val) { $$(sel, root).forEach(function (n) { n.textContent = val; }); }

		function render() {
			panes.forEach(function (p) { p.classList.toggle('is-active', p.classList.contains('gf-pane--' + st.step)); });
			stepRows.forEach(function (row, k) {
				var n = k + 1;
				row.classList.toggle('is-current', n === st.step);
				row.classList.toggle('is-done', n < st.step);
				var num = $('.gf-bstep-num .elementor-heading-title', row);
				if (num) num.textContent = n < st.step ? '✓' : String(n);
			});
			services.forEach(function (s) {
				s.el.classList.toggle('is-selected', st.svc === s);
				s.el.setAttribute('aria-pressed', st.svc === s ? 'true' : 'false');
			});
			if (pane2) pane2.classList.toggle('gf-has-date', st.day !== null);
			if (pane2Step) pane2Step.textContent = pane2StepText + (st.svc ? ' · ' + st.svc.name : '');
			$$('.gf-day', root).forEach(function (b) {
				var on = +b.getAttribute('data-k') === st.day;
				b.classList.toggle('is-selected', on);
				b.setAttribute('aria-pressed', on ? 'true' : 'false');
			});
			if (timesEl && st.day !== null) {
				timesEl.innerHTML = TIMES.map(function (t, j) {
					var off = (st.day * 3 + j) % 5 === 1;
					return '<button type="button" class="gf-time' + (st.time === t ? ' is-selected' : '') + '" data-t="' + t + '"' +
						(off ? ' disabled aria-label="' + t + ' ' + T.full + '"' : ' aria-pressed="' + (st.time === t) + '"') + '>' + t + '</button>';
				}).join('');
			}
			fill('.gf-summary-name', st.svc ? st.svc.name : '');
			fill('.gf-summary-when', st.day !== null && st.time ? dateLabel() + T.at + st.time + (st.svc ? ' · ' + st.svc.where : '') : '');
			if (st.step === 4 && form) {
				fill('.gf-first-name', form.elements.name.value.trim().split(' ')[0]);
				fill('.gf-done-service', st.svc ? st.svc.name : '');
				fill('.gf-done-date', dateLabel());
				fill('.gf-done-time', st.time || '');
				fill('.gf-done-email', form.elements.email.value.trim());
			}
			var ok = valid();
			if (next) next.classList.toggle('is-disabled', !ok);
			if (nextA) nextA.setAttribute('aria-disabled', ok ? 'false' : 'true');
			if (nextText) nextText.textContent = st.step === 3 ? T.confirm : nextDefault;
			if (back) back.classList.toggle('is-hidden', st.step === 1);
			if (nav) nav.style.display = st.step === 4 ? 'none' : '';
		}
		function goNext() {
			if (!valid()) return;
			st.step = Math.min(4, st.step + 1);
			render();
			if (st.step === 4) root.dispatchEvent(new CustomEvent('getfit:booked', { bubbles: true, detail: { service: st.svc && st.svc.id, day: days[st.day], time: st.time, name: form.elements.name.value, email: form.elements.email.value, note: form.elements.note.value } }));
		}
		if (nextA) nextA.addEventListener('click', function (e) { e.preventDefault(); goNext(); });
		if (backA) backA.addEventListener('click', function (e) { e.preventDefault(); st.step = Math.max(1, st.step - 1); render(); });
		$$('.gf-book-reset a', root).forEach(function (a) {
			a.addEventListener('click', function (e) {
				e.preventDefault();
				st = { step: 1, svc: null, day: null, time: null };
				if (form) form.reset();
				render();
			});
		});
		render();

		booking = {
			prefill: function (serviceId, note) {
				var s = services.filter(function (x) { return x.id === serviceId; })[0] || services[0];
				st = { step: 2, svc: s || null, day: null, time: null };
				if (form && note) form.elements.note.value = note;
				render();
			}
		};
	}

	/* "Choose plan" buttons pre-select the free trial and jump to the booking form. */
	function planButtons() {
		$$('.gf-plan-btn a').forEach(function (a) {
			a.addEventListener('click', function () {
				var card = a.closest('.gf-plan');
				var name = card ? headingText($('h3', card).closest('.elementor-widget')).replace(T.planSuffix, '') : '';
				if (booking) booking.prefill('trial', name ? T.interested(name) : '');
			});
		});
	}

	/* Mobile menu (UAE): close the dropdown after tapping a same-page link. */
	function mobileMenu() {
		document.addEventListener('click', function (e) {
			if (!e.target.closest('.gf-nav nav.hfe-dropdown a')) return;
			var toggle = $('.gf-nav .hfe-nav-menu__toggle');
			if (toggle && toggle.classList.contains('hfe-active-menu')) toggle.click();
		});
	}

	/* Finnish number format for the stats counters (4.9 -> 4,9). */
	function counters() {
		if (!FI) return;
		$$('.gf-counter .elementor-counter-number').forEach(function (n) {
			new MutationObserver(function () {
				if (n.textContent.indexOf('.') !== -1) n.textContent = n.textContent.replace('.', ',');
			}).observe(n, { childList: true, characterData: true, subtree: true });
		});
	}

	function init() {
		if (inEditor()) return;
		counters();
		header();
		mobileMenu();
		hero();
		method();
		marquee();
		pricing();
		bookingFlow();
		planButtons();
	}

	if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
	else init();
})();
