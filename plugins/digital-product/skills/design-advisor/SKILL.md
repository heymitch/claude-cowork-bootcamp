---
name: design-advisor
description: Get design direction for your product cover and visuals by budget level. Triggers — "design my product", "product cover", "Fiverr outreach for design"
user-invocable: true
---

# Design Advisor

## Process

### Step 1: Load Context

Read:
- `.coworker/index.md` for active product context
- `projects/[product-name]/product-config.md` for title, subtitle, audience, and mood

### Step 2: Ask About Budget

Ask: "What's your design budget?" and present the three tiers:
- **Free** — DIY with Canva or Keynote
- **$20-200** — Fiverr freelancer
- **$500+** — Professional designer

### Step 3: Recommend by Tier

**Free — DIY Cover**
- Use Canva (canva.com) or Keynote
- Style: minimalist. 1-2 colors, bold sans-serif font, clean background
- Dimensions: 1600x2560px for ebook cover, 1280x720px for product thumbnail
- Template search: "ebook cover" in Canva for starting points
- Keep it simple. A clean cover with clear text beats a cluttered design every time.

**$20-200 — Fiverr Freelancer**
Generate a ready-to-send outreach message:

> Hey there, I'm looking for someone to design an eBook cover for me. I have a few ideas in mind, and looking for this to be a quick, one-off project. If I gave you a bit of direction, would you be able to create something for me in a few hours of work?

Tell the user to search Fiverr for "ebook cover design" and filter by budget and rating.

**$500+ — Professional Designer**
- Search "I Need A Book Cover" or publishing designer communities
- Provide a design brief with: title, subtitle, target audience, mood/tone, 2-3 examples of covers you like
- Expect 2-3 rounds of revisions

### Step 4: Create a Design Brief

Regardless of budget, generate a design brief:
- Product title and subtitle
- Target audience (who picks this up)
- Mood: professional, playful, bold, minimal
- Color preferences (or "designer's choice")
- 2-3 reference covers the user likes (ask them)
- Required text on the cover

### Step 5: Gamma Mockup (Optional)

Run `ToolSearch("gamma generate")` to check if Gamma is connected.
- **If found:** Generate a cover mockup and product preview using Gamma.
- **If not found:** Skip silently. Describe the visual direction clearly enough that the user or a designer can execute it. Do not tell the user to connect Gamma — the design brief is sufficient.

### Step 6: Next Step

After design direction is set, recommend launch-kit to prepare launch content and go live.

## Handoff

After design direction is set:
1. Save design brief to `projects/[product-name]/design-brief.md`.
2. Update `projects/[product-name]/product-config.md` — check "Cover/visuals done".
3. Update `.coworker/index.md` — note "Design brief created" next to the product.
4. If no landing page yet: "Cover direction locked. Next up: **build me a landing page** to deploy a live sales page."
5. If landing page exists: "Cover direction locked. Next up: **launch my product** to prepare pricing, posts, and go live."

## Rules
- Always ask about budget before recommending.
- Generate the Fiverr outreach message for the $20-200 tier without being asked.
- Include specific dimensions for every recommendation.
- Do not over-design. A simple, clean cover sells better than a busy one.
- Always create a design brief regardless of which tier they choose.
- If no budget preference, default to the free DIY recommendation.
- Always write to `projects/[product-name]/` — never to workspace root.
