---
name: ebook-designer
description: Turn your written product into a professionally designed, sellable ebook. Generates a styled HTML document with cover page, table of contents, styled chapters, and print-ready PDF export. Triggers — "design my ebook", "format my product", "make it look professional", "style my ebook"
user-invocable: true
---

# Ebook Designer

Turn raw written content into a designed, sellable HTML ebook. Zero dependencies — single file, opens in any browser, exports to PDF via File > Print.

## Process

### Step 1: Gather Inputs

Load:
- `.coworker/index.md` for active project context
- `projects/[product-name]/[product-name]-content.md` — written content from content-writer (the 10 sections)
- `projects/[product-name]/product-config.md` — for title and strategy brief (author, audience, transformation)
- `references/ebook-style-presets.md` for available styles

If the written content doesn't exist yet, stop: "You need written content first. Say **write my product** to create it."

### Step 2: Style Discovery

Show the user 3 style options as visual previews. Generate 3 small HTML files — each a styled cover page + one sample chapter page using their actual title and content.

Pick 3 presets that match the product's tone:
- **Opinionated/personal product** → Paper & Ink, Vintage Editorial, Dark Botanical
- **Step-by-step/workbook** → Notebook Tabs, Swiss Modern, Pastel Geometry
- **Bold/short/action-oriented** → Bold Signal, Creative Voltage, Electric Studio

For each preview, generate a single HTML file with:
- Cover page (title, subtitle, author)
- One sample chapter (first content section)
- The preset's fonts, colors, and signature elements

Save previews as `projects/[product-name]/preview-1.html`, `preview-2.html`, `preview-3.html`. Tell the user to open each in their browser.

Ask: "Open these 3 in your browser and pick your favorite. Or describe what you'd like changed."

### Step 3: Generate Full Ebook

Using the chosen style, generate a single HTML file with this structure:

**Cover Page**
- Product title (large, styled display font)
- Subtitle (if exists)
- Author name
- Styled background matching the preset
- Page break after

**Table of Contents**
- Linked chapter list (clicking jumps to section)
- Page numbers (CSS counters for print)
- Page break after

**Chapters (Sections 1-10)**
Each chapter gets:
- Chapter number + title (styled header)
- Content from content-writer
- **Callout boxes** for templates and checklists (bordered, accent-colored background)
- **Pull quotes** for key insights (large italic text, accent bar)
- **Action step boxes** for exercises (distinct styling from body text)
- Page break before each chapter

**CTA Page (Final)**
- Thank the reader
- Author contact / links
- "What to do next" section
- Page break before

### Step 4: CSS Requirements

The generated HTML must include:

**Web display:**
- CSS custom properties from the preset
- Responsive typography with `clamp()`
- Max-width content container (`max-width: 720px; margin: 0 auto`)
- Smooth scrolling between sections
- Fonts loaded via Google Fonts or Fontshare API link

**Print / PDF export:**
```css
@media print {
    @page {
        size: letter;
        margin: 1in 0.75in;
    }
    .cover-page { page-break-after: always; }
    .toc { page-break-after: always; }
    .chapter { page-break-before: always; }
    .cta-page { page-break-before: always; }
    .no-print { display: none; }
    body {
        font-size: 11pt;
        line-height: 1.6;
        color: #000;
    }
    a { color: inherit; text-decoration: none; }
}
```

**Callout box pattern:**
```css
.callout {
    background: var(--accent-light);
    border-left: 4px solid var(--accent);
    padding: 1.25rem 1.5rem;
    margin: 1.5rem 0;
    border-radius: 0 8px 8px 0;
}
.callout-title {
    font-family: var(--font-display);
    font-weight: 700;
    margin-bottom: 0.5rem;
}
```

**Pull quote pattern:**
```css
.pull-quote {
    font-family: var(--font-display);
    font-size: var(--h3-size);
    font-style: italic;
    border-left: 3px solid var(--accent);
    padding-left: 1.5rem;
    margin: 2rem 0;
    color: var(--text-secondary);
}
```

### Step 5: Review and Deliver

Save the ebook as `projects/[product-name]/[product-name].html` in the workspace.

Tell the user:
- "Open in your browser to preview"
- "File > Print > Save as PDF for the sellable version"
- "The web version has responsive styling. The PDF version has clean page breaks."

Ask if they want any changes — font swap, color tweak, layout adjustment.

## Handoff

After ebook is approved:
1. Update `projects/[product-name]/product-config.md` — check "Ebook designed", fill in Ebook style with chosen preset name.
2. Update `.coworker/index.md` — note "Ebook designed ([style])" next to the product.
3. Say: "Ebook done. Next up: **design my product** for cover art and visual assets, or skip to **build me a landing page** if you're ready to sell."

## Rules
- Zero dependencies. Single HTML file. No npm, no build tools, no frameworks.
- Fonts via Google Fonts or Fontshare API `<link>` tags only. No local font files.
- Never use Inter, Roboto, Arial, or system fonts as display fonts.
- Never use purple gradients on white backgrounds.
- Every ebook needs `@media print` styles. PDF export is non-negotiable.
- Callout boxes for every template and checklist in the content. These are the most valuable parts — make them visually distinct.
- Pull quotes for key insights. At least one per chapter.
- Content container max-width 720px. Long lines are unreadable.
- If content is very long (30,000+ words), warn the user that the HTML file will be large and PDF may take a moment to generate.
- Always write to `projects/[product-name]/` — never to workspace root.
