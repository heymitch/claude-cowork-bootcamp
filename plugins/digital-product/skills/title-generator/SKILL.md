---
name: title-generator
description: Generate product titles using the 1+1+1 naming framework. Triggers — "name my product", "generate titles", "title my ebook"
user-invocable: true
---

# Title Generator

## Process

### Step 1: Gather Input

Load:
- `.coworker/index.md` for active project context
- `projects/[product-name]/product-config.md` for product info and completed outline
- `../digital-product/references/ltl-frameworks.md` for the 1+1+1 naming framework

You need three things: the product topic, the target audience, and the problem or transformation.

### Step 2: Apply the 1+1+1 Framework

From `../digital-product/references/ltl-frameworks.md`:
- **1 Product** — what is the topic?
- **1 Audience** — who specifically is this for?
- **1 Problem/Transformation** — what changes for them?

Format: Main Title (product + audience) + Subtitle (problem/transformation)

### Step 3: Generate 5 Titles

Each follows the 1+1+1 structure. Label each with its style:

1. **Direct** — clear, obvious what the product is
2. **Aspirational** — focuses on the dream outcome
3. **Contrarian** — challenges a common belief
4. **Numbered** — specific quantity of steps, strategies, or templates
5. **Story-based** — frames it as a journey or narrative

### Step 4: Recommend Top Pick

Choose the best one. Explain why: clarity, scroll-stopping power, market positioning.

### Step 5: Iterate

Ask: "Go with this one, tweak it, or see 5 more?" Refine until the user picks a winner.

## Handoff

After the user picks a title:
1. Update `projects/[product-name]/product-config.md` — check "Title chosen", update Working title with final pick.
2. Update `.coworker/index.md` — update the product one-liner with the final title.
3. Ask: "What format is this product? Say **write my product** for a written guide/ebook, or **write video scripts** for a video course."

## Rules
- Always generate exactly 5 titles.
- Every title follows 1+1+1: product + audience + problem.
- Every title has a main title AND a subtitle.
- Label each with its style.
- Always recommend one with reasoning.
- Be specific. "The Ultimate Guide" is lazy. "The LinkedIn Playbook for B2B Founders" is specific.
- Main titles under 10 words. Subtitles can be longer.
