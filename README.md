# Get Fit — personal trainer website (WordPress + Elementor)

Build of the *Get Fit* design for https://personal-trainer-example.fi-c.seravo.com/.

* **Theme:** Hello Elementor + child theme `getfit-child` (`wp-content/themes/getfit-child`)
* **Page builder:** Elementor. Every section, heading, text, button, image, counter,
  icon list and the FAQ accordion is a normal Elementor widget inside containers,
  so all content and styling can be edited in the Elementor editor.
* **Header & footer:** Ultimate Addons for Elementor (UAE) templates
  (*Appearance → UAE → Header/Footer*), displayed on the entire site.
* **Global styles:** Elementor *Site Settings* hold the colours (Lime, Ink, Muted, Soft…)
  and typography presets (Eyebrow, Section title, Lead, Small body) that the widgets use.

## Design layer (child theme)

`assets/css/getfit.css` and `assets/js/getfit.js` add what Elementor has no control for:

| Feature | How it is built |
| --- | --- |
| Scroll reveals | Elementor *Motion Effects → Entrance animation* (Fade In Up / Zoom In) retuned to the design's 48 px, 0.9 s ease |
| Hero slider | 3 slide containers (`gf-hero-slide`) + tabs (`gf-hero-tab`); crossfade, slow zoom and timed progress bars |
| Method steps | 4 step containers (`gf-step`); active step scales up, progress ring drawn by JS |
| Testimonials | Cards in `gf-marquee-track`, duplicated by JS for an endless marquee that pauses on hover |
| Stats | Elementor Counter widgets (count-up) |
| Pricing toggle | Monthly / 3 months (−10 %) recalculated from the price widgets |
| Booking | 4-step free-trial flow (session → date & time → details → confirmed). It fires a `getfit:booked` event; connect it to a form/booking plugin or email to receive bookings. |
| Header | Transparent over the hero, solid + blur after scrolling, reading-progress line |
| Cursor | Dumbbell cursor on mouse devices |

## Rebuilding / re-importing

```bash
python3 tools/elementor-build/gen.py          # regenerate elementor/*.json
wp eval-file tools/import-to-wordpress.php     # push kit, header, footer, home page and assets
wp getfit export-assets                        # write getfit_css / getfit_js options to theme files
```
