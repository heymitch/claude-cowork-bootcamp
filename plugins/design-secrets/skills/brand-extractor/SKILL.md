---
name: brand-extractor
description: Extract your visual identity and save it as a design profile Cowork uses for everything. Triggers on "set up my design aesthetic", "extract my brand", "analyze my brand", "upload my brand assets", "here's my logo", "here's my color palette", "here's my website".
user-invocable: true
---

# Brand Extractor

Extracts your visual identity from any source — logos, screenshots, website URLs, brand guidelines, or plain descriptions — and saves a `design-profile.md` that every other design skill reads before touching any output.

## Workflow

### Step 1 — Gather Source Material

Ask the user for reference material. Accept any combination:

- **Images** (logos, screenshots, designs they like, brand guidelines as images)
- **Website URL** (screenshot and analyze)
- **Color codes** (hex values they already use)
- **Plain description** ("warm, retro, cassette futurism", "minimal, dark, technical")
- **Vibes** (brands they admire, Pinterest boards, "like Apple but warmer")

Don't demand everything. One logo or one URL is enough to start. Ask: "What do you have? A logo, website, color codes, or just a description works."

### Step 2 — Extract Design Tokens

**From uploaded images:**
- Identify dominant colors → extract hex codes (primary, secondary, background, accent)
- Read typography: serif/sans/mono, weight preference (light/regular/bold/condensed), feeling (editorial, technical, friendly, authoritative)
- Read spacing patterns: tight/airy, dense/open
- Read mood: warm/cool, minimal/maximal, flat/textured, sharp/rounded

**From a website URL:**
Use browser to screenshot the site. Analyze: color palette from above-the-fold, heading font vs body font, overall density and whitespace, any signature patterns (stripes, borders, textures).

**From plain description:**
Map descriptive language to specific design tokens:
- "warm, retro, cassette futurism" → orange/cream/charcoal palette, bold condensed type, thick borders, tape-reel-style accents, technical metadata feel
- "minimal, dark, technical" → near-black background, white or phosphor-green text, monospace accents, no decoration
- "clean, professional, trustworthy" → navy/white/light grey, readable sans-serif, generous whitespace, no bold statement colors
- "bold, editorial, magazine" → high contrast, large display type, strong typographic hierarchy, black/white + one accent

If description is vague, ask one follow-up: "Warm or cool tones? Bold or understated type?"

### Step 3 — Build the Design Profile

Compile everything into this format and save to `training/references/design-profile.md`:

```markdown
# Design Profile

## Colors
- Primary: #[hex] ([description])
- Secondary: #[hex] ([description])
- Background: #[hex] ([description])
- Accent: #[hex] ([description])
- Text: #[hex] ([description])

## Typography
- Display: [Font name], [weight/style] — [use: headers, titles, hero text]
- Body: [Font name], [weight/style] — [use: paragraphs, captions]
- Mono: [Font name] — [use: code, metadata, small labels]

## Style
- Mood: [2-4 adjectives]
- Layout: [how elements are arranged — bold/structured/airy/dense]
- Signature patterns: [recurring motifs — stripes, textures, borders, accents]
- Avoid: [explicitly what to NOT do — gradients, glassmorphism, thin lines, etc.]

## Extracted From
- [Source: logo, URL, description — include date]
```

### Step 4 — Confirm with User

Show the design profile to the user before saving. Say: "Here's what I extracted. Does this feel right? Any hex codes to correct or moods to adjust?"

Apply any corrections, then save.

### Step 5 — Save and Update Index

1. Save profile to `training/references/design-profile.md` (create `training/references/` if it doesn't exist)
2. Update `.coworker/index.md` — add or update the Design Profile entry:

```markdown
## Design Profile
- **Status:** Active
- **Location:** `training/references/design-profile.md`
- **Last updated:** [date]
- **Mood:** [2-3 adjectives from profile]
- **Primary color:** [hex]
```

Tell the user: "Design profile saved. Every visual I create will match your aesthetic — no more generic output."

## Rules

- Never save a profile without user confirmation first.
- If extraction is ambiguous, ask one targeted clarifying question rather than guessing.
- Font names must be real, Google Fonts-available fonts when possible (for HTML/CSS use).
- Hex codes must be valid 6-digit values.
- Profile must include an "Avoid" section — knowing what NOT to do is as important as knowing what to do.
