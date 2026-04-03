---
name: design-generator
description: Generate branded visuals using your personal design profile. Every output matches your aesthetic — colors, fonts, spacing, mood. Triggers on "design a [thing]", "make this look branded", "generate a visual for", "create a graphic", "styled PDF", "branded image", "create a landing page", "make a slide".
user-invocable: true
---

# Design Generator

Generates branded visuals using the user's design profile. SVG for graphics, HTML/CSS for PDFs and landing pages, Gamma or HTML for slides. No output ships without reading the design profile first.

## Workflow

### Step 1 — Load Design Profile

Read `training/references/design-profile.md`. If missing, stop and say:

"I don't have your design profile yet. Run 'set up my design' first — takes 2 minutes. I'll extract your colors, fonts, and style so everything I make looks like you."

Do NOT proceed without the profile. Do NOT default to generic styling.

### Step 2 — Determine Output Format

Map the request to a format. When in doubt, prefer SVG for graphics and HTML/CSS for anything with text content.

| Request type | Format |
|---|---|
| Icon, logo, badge, illustration, diagram, banner | SVG |
| PDF report, guide, one-pager, checklist | HTML/CSS → Puppeteer → PDF |
| Landing page, sales page, opt-in page | HTML/CSS (deployable) |
| Presentation, slide deck | Gamma API (if connected) or HTML slides |
| Social image (1:1, 16:9, 4:5) | SVG → export or HTML/CSS |
| Email header, email template | HTML/CSS |

Read `references/format-guide.md` for format-specific rules before generating.

### Step 3 — Apply Design Profile

Pull these values from the profile and apply them consistently:

- **Colors**: Use exactly the hex codes from the profile. No improvising. Primary for dominant elements, accent for CTAs or highlights, background for page/card fill.
- **Typography**: Use their display font for headers, body font for text, mono for code/metadata. Load via Google Fonts `@import` in `<style>` tags or SVG.
- **Mood**: If the profile says "bold, structured, thick borders" — every element should reflect that. Thin lines = violation.
- **Avoid list**: Treat this as a hard constraint. If the profile says "avoid gradients" — no gradients. Period.
- **Signature patterns**: If the profile has motifs (stripes, tape accents, technical metadata, etc.) — use them. These are what makes it distinctly theirs.

Read `references/design-principles.md` for the philosophy behind these choices.

### Step 4 — Generate

Build the asset. For each format:

**SVG:**
- Set viewBox with explicit dimensions
- Embed fonts via `@import` in `<style>` block
- Use design profile colors as `fill`/`stroke` values
- Keep text as `<text>` elements (not paths) so it stays editable
- Structure: background → structural elements → text → details

**HTML/CSS → PDF:**
- Set page dimensions explicitly in CSS (`@page { size: A4; }` or custom)
- Set `print-color-adjust: exact` on body to preserve background colors when printing
- Load fonts from Google Fonts at the top of `<style>`
- Define design profile as CSS variables at `:root`
- Generate PDF: `node -e "const puppeteer = require('puppeteer'); (async()=>{ const b = await puppeteer.launch(); const p = await b.newPage(); await p.goto('file://[path]', {waitUntil:'networkidle0'}); await p.pdf({path:'[output].pdf', printBackground:true}); await b.close(); })()"`

**Landing page:**
- Full responsive HTML file with embedded CSS
- Define design profile as CSS variables or Tailwind config (pin Tailwind v3: `npm install tailwindcss@3`)
- Mobile-first, deploy-ready
- Comment the file so the user knows where to swap content

**Presentation:**
- Prefer Gamma API if user has it connected (check for `mcp__claude_ai_Gamma__generate`)
- Fallback: single HTML file with slide sections, JS for navigation
- Apply design profile as color variables

### Step 5 — Save and Show

1. Save to `output/[descriptive-name].[ext]`
2. Show the user the output file path
3. If HTML/SVG: display the code so they can preview it
4. If PDF: confirm the file was written to `output/`

Tell the user where to find it: "Saved to `output/[filename]`. Open it in your browser or viewer."

## Rules

- NEVER generate without reading the design profile first.
- NEVER use colors, fonts, or styles not in the profile.
- NEVER default to Bootstrap blue, system fonts, or generic gray cards.
- All output goes to `output/` — never the project root, never desktop.
- If the request is ambiguous ("make this look good"), ask: "What format? And what's the content?" before generating.
- Show the output before asking if the user wants revisions.
