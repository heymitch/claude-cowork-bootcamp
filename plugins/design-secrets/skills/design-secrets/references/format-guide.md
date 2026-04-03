# Format Guide

Format-specific rules for every output type. Read the relevant section before generating. The design profile supplies the values — this file supplies the structure.

---

## SVG

**When to use:** Icons, logos, badges, illustrations, diagrams, social images, any graphic that doesn't need to be a scrollable document.

**Rules:**
- Always set explicit `viewBox` with width and height: `viewBox="0 0 800 600"`
- Set matching `width` and `height` on the `<svg>` element or use `width="100%" height="100%"` with a container
- Embed fonts via `@import` in a `<style>` block inside the SVG:
  ```svg
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Inter:wght@400;600&display=swap');
  </style>
  ```
- Use design profile hex codes as `fill` and `stroke` values — never CSS named colors, never HSL unless converted from the profile
- Keep all text as `<text>` elements with `font-family`, `font-size`, `font-weight` attributes — NOT as paths
- Group related elements with `<g>` and descriptive `id` attributes: `<g id="header">`, `<g id="content">`
- Background: first element should be a `<rect>` with the profile's background color filling the full viewBox
- For multi-line text, use `<tspan>` with `x` reset and `dy` for line height
- Test that all hex codes are valid 6-digit or 3-digit values before outputting

**Social image sizes:**
- Square (1:1): 1080x1080
- Landscape (16:9): 1920x1080
- Portrait (4:5): 1080x1350
- LinkedIn banner: 1584x396
- Twitter header: 1500x500

---

## HTML/CSS → PDF

**When to use:** Reports, guides, one-pagers, checklists, any document that gets printed or shared as PDF.

**Rules:**

**Page setup:**
```css
@page {
  size: A4;          /* or Letter: 8.5in 11in, or custom: 800px 1100px */
  margin: 40px;
}

body {
  print-color-adjust: exact;
  -webkit-print-color-adjust: exact;
}
```

**CSS variables at `:root`:**
```css
:root {
  --color-primary: #E8682A;
  --color-secondary: #1a1a1a;
  --color-background: #F0E8D4;
  --color-accent: #C0392B;
  --color-text: #1a1a1a;
  --font-display: 'Oswald', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'Space Mono', monospace;
}
```

**Google Fonts import** (top of `<style>`):
```css
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&family=Inter:wght@400;600&family=Space+Mono&display=swap');
```

**Puppeteer PDF generation:**
```bash
node -e "
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto('file://$(pwd)/output/[name].html', { waitUntil: 'networkidle0' });
  await page.pdf({
    path: 'output/[name].pdf',
    printBackground: true,
    format: 'A4',
    margin: { top: '0', right: '0', bottom: '0', left: '0' }
  });
  await browser.close();
  console.log('PDF written to output/[name].pdf');
})();
"
```

If Puppeteer isn't installed: `npm install puppeteer` (installs Chromium automatically).

**Multi-page documents:** Use `page-break-after: always` or `break-after: page` on section containers for clean page breaks.

---

## Landing Pages

**When to use:** Sales pages, opt-in pages, product pages, event pages. Anything that lives at a URL.

**Rules:**
- Single self-contained HTML file with embedded CSS (no external CSS files)
- Mobile-first responsive: base styles for mobile, media queries for desktop
- CSS variables at `:root` for all design profile values (same pattern as PDF)
- Google Fonts loaded via `<link>` in `<head>` (not `@import` — faster load)
- Page sections: hero, features/benefits, social proof, CTA. Use semantic HTML: `<header>`, `<section>`, `<footer>`
- All CTAs use `--color-accent` as background — consistent button color across the page
- No JavaScript required for rendering. JS only for optional interactions (scroll animations, modals)
- Comment the HTML: `<!-- HERO: swap headline and subhead -->`, `<!-- SOCIAL PROOF: add testimonials here -->` so the user knows where to edit
- Tailwind: if using Tailwind, pin v3 — `npm install -D tailwindcss@3`. v4 has completely different syntax.
- Deploy-ready: test that the file opens correctly in a browser with no server before handing off

---

## Presentations / Slides

**When to use:** Pitch decks, course modules, workshop slides, keynote-style presentations.

**Gamma API (preferred):**
If the Gamma connector is active (`mcp__claude_ai_Gamma__generate` is available):
1. Build slide content as structured markdown with slide breaks `---`
2. Map design profile colors to the Gamma theme parameters
3. Use `mcp__claude_ai_Gamma__generate` to create the presentation
4. Return the Gamma link to the user

**HTML slide fallback:**
If Gamma isn't connected, build a single HTML file with:
- Each slide as a `<section>` inside a `<div id="slides">`
- CSS: `section { width: 1280px; height: 720px; overflow: hidden; }` (16:9)
- Keyboard navigation: left/right arrows advance slides
- Design profile as CSS variables
- No external dependencies — fully self-contained

```javascript
// Minimal slide navigation
let current = 0;
const slides = document.querySelectorAll('#slides section');
const show = (n) => slides.forEach((s, i) => s.style.display = i === n ? 'flex' : 'none');
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight') { current = Math.min(current + 1, slides.length - 1); show(current); }
  if (e.key === 'ArrowLeft')  { current = Math.max(current - 1, 0); show(current); }
});
show(0);
```

---

## Email Templates

**When to use:** Email headers, value emails, onboarding sequences, newsletters.

**Rules:**
- Table-based layout (not flexbox/grid — email clients don't support them)
- Inline CSS only — no `<style>` blocks (Gmail strips them)
- Max width 600px, centered
- Background colors on `<td>` elements, not `<div>`
- Web-safe fonts as fallback: `font-family: 'Inter', Arial, sans-serif`
- Test in both light and dark mode (add `color-scheme: light dark` to `<meta>`)
- Design profile colors applied inline on every element — no variables (no CSS variable support in email)

---

## Output Checklist (run before delivering any asset)

- [ ] Design profile colors used (no improvised hex codes)
- [ ] Profile fonts loaded and applied
- [ ] Mood and style match the profile
- [ ] Nothing on the "Avoid" list is present
- [ ] File saved to `output/[descriptive-name].[ext]`
- [ ] Path shown to user
