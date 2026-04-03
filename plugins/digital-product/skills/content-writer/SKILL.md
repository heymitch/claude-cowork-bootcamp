---
name: content-writer
description: Write the full digital product from a completed outline using the 10 Proven Sections template. Triggers — "write my product", "expand the outline", "write the ebook"
user-invocable: true
---

# Content Writer

## Process

### Step 1: Gather Inputs

Load before writing:
- `.coworker/index.md` for active project context
- `projects/[product-name]/outline.md` — the completed outline from outline-builder
- `projects/[product-name]/product-config.md` — for title and strategy brief
- `../digital-product/references/ltl-frameworks.md` for the 10 Sections template
- `training/voice/voice-template.md` — if it exists, use the voice profile for writing
- `training/references/business-blueprint.md` — if it exists, load business context

### Step 2: Confirm Scope

Ask the user what size:
- **Mini guide** (5,000-10,000 words) — 3 steps max, quick read
- **Standard guide** (15,000-30,000 words) — 5-7 steps, the main product type
- **Premium** (30,000+ words) — 7+ steps, deep examples, templates throughout

### Step 3: Write the 10 Sections

**Section 1 — Dear WHO:** Profiles of who this is for, their struggles, 3 myths busted, the unlikely answer, benefits, future vision, call to adventure.

**Section 2 — Origin Story:** When you were stuck, bad advice you got, the low point, the turning point, your success, "I did it, you can too."

**Sections 3-7 — Steps (from Q8):** Each step gets: No Shortcuts (why they cannot skip it), Step Detail (the action), Motivational Reminder, Caution Signs (3-5 mistakes), Examples (3+), Template (fill-in-the-blank).

**Section 8 — Before/After:** Transformation recap, 3+ case studies, continuous improvement steps.

**Section 9 — FAQ:** 10+ questions with 1-3 paragraph answers. Cover objections and edge cases.

**Section 10 — CTAs:** Thank the reader, link resources, give contact info, pitch 1:1 work.

### Step 4: Match the Voice

Use `training/voice/voice-template.md` if it exists. If not, write in a clear, direct, conversational tone. No jargon. No filler.

### Step 5: Review and Save

Show the draft for feedback. Revise as needed. Save the final version to `projects/[product-name]/[product-name]-content.md`.

## Handoff

After content is approved:
1. Save content to `projects/[product-name]/[product-name]-content.md`.
2. Update `projects/[product-name]/product-config.md` — check "Content written", fill in Scope with chosen size.
3. Update `.coworker/index.md` — note "Content written ([scope])" next to the product.
4. Say: "Content done. Next up: **design my ebook** to turn this into a professionally styled, sellable document. Or skip to **design my product** for cover art."

## Rules
- Follow the 10 Sections structure. Do not skip sections.
- Plain language. Every sentence teaches, motivates, or gives an action.
- Include templates and checklists inside each step — these are the most valuable parts.
- Do not invent case studies or statistics. Use examples from the outline or mark as placeholders.
- Confirm scope before writing. Do not assume.
- Save work incrementally on long products.
- Always write to `projects/[product-name]/` — never to workspace root.
