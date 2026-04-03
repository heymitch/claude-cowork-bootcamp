# Ebook Style Presets

Adapted from the frontend-slides system. Each preset defines fonts, colors, and signature elements for a professional ebook. Abstract shapes only — no illustrations.

## Best For Ebooks

These presets work best for long-form documents:

### Paper & Ink (Recommended Default)
**Vibe:** Editorial, literary, thoughtful
**Fonts:** `Cormorant Garamond` (display) + `Source Serif 4` (body) — Google Fonts
**Colors:** Warm cream `#faf9f7`, charcoal `#1a1a1a`, crimson accent `#c41e3a`
**Signature:** Drop caps, pull quotes, elegant horizontal rules
**Best for:** Guides, playbooks, anything with dense text

### Vintage Editorial
**Vibe:** Witty, confident, editorial, personality-driven
**Fonts:** `Fraunces` (display) + `Work Sans` (body) — Google Fonts
**Colors:** Cream `#f5f3ee`, dark text `#1a1a1a`, warm accent `#e8d4c0`
**Signature:** Geometric accent shapes, bordered callout boxes, conversational tone
**Best for:** Opinionated guides, personal brand products

### Dark Botanical
**Vibe:** Elegant, sophisticated, premium
**Fonts:** `Cormorant` (display) + `IBM Plex Sans` (body) — Google Fonts
**Colors:** Deep dark `#0f0f0f`, warm text `#e8e4df`, gold accent `#c9b896`, pink `#e8b4b8`
**Signature:** Soft gradient circles, thin accent lines, italic signatures
**Best for:** High-end products, premium pricing

### Notebook Tabs
**Vibe:** Organized, tactile, approachable
**Fonts:** `Bodoni Moda` (display) + `DM Sans` (body) — Google Fonts
**Colors:** Cream page `#f8f6f1` on dark `#2d2d2d`, colorful section tabs (mint, lavender, pink, sky)
**Signature:** Paper container look, colored chapter tabs in margin, binder details
**Best for:** Workbooks, step-by-step guides, anything with exercises

### Swiss Modern
**Vibe:** Clean, precise, Bauhaus-inspired
**Fonts:** `Archivo` (display) + `Nunito` (body) — Google Fonts
**Colors:** White, black, red accent `#ff3300`
**Signature:** Visible grid structure, asymmetric layouts, geometric shapes
**Best for:** Technical guides, frameworks, systematic content

### Bold Signal
**Vibe:** Confident, bold, modern, high-impact
**Fonts:** `Archivo Black` (display) + `Space Grotesk` (body) — Google Fonts
**Colors:** Dark `#1a1a1a`, vibrant card `#FF5722`, white text
**Signature:** Bold colored chapter headers, large section numbers, navigation breadcrumbs
**Best for:** Action-oriented products, short punchy guides

## CSS Custom Properties Template

Every ebook uses this base variable system:

```css
:root {
    /* Fonts */
    --font-display: 'Display Font', serif;
    --font-body: 'Body Font', sans-serif;

    /* Colors */
    --bg-primary: #faf9f7;
    --bg-secondary: #f0ede8;
    --text-primary: #1a1a1a;
    --text-secondary: #555555;
    --accent: #c41e3a;
    --accent-light: rgba(196, 30, 58, 0.1);

    /* Typography — responsive for web, fixed for print */
    --title-size: clamp(2rem, 5vw, 3.5rem);
    --h2-size: clamp(1.5rem, 3vw, 2.25rem);
    --h3-size: clamp(1.1rem, 2vw, 1.5rem);
    --body-size: clamp(0.95rem, 1.3vw, 1.125rem);
    --small-size: clamp(0.8rem, 1vw, 0.875rem);

    /* Spacing */
    --page-padding: clamp(2rem, 6vw, 5rem);
    --section-gap: clamp(2rem, 4vw, 4rem);
    --content-gap: clamp(0.75rem, 1.5vw, 1.25rem);
}
```

## DO NOT USE

**Fonts:** Inter, Roboto, Arial, system fonts
**Colors:** `#6366f1` (generic indigo), purple gradients on white
**Patterns:** Everything centered, identical card grids, gratuitous glassmorphism
