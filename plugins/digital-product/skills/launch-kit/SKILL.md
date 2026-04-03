---
name: launch-kit
description: Generate a complete launch kit — pricing, sales page copy, launch posts, platform setup, and promotion templates. Triggers — "launch my product", "create launch posts", "generate launch kit"
user-invocable: true
---

# Launch Kit

## Process

### Step 1: Gather Inputs

Load:
- `.coworker/index.md` for active project context
- `projects/[product-name]/product-config.md` — the completed product (title, outline, content, pipeline status)
- `training/voice/voice-template.md` — if it exists, use the voice profile for launch content
- `training/references/business-blueprint.md` — if it exists, load business context for platform and pricing decisions
- `../digital-product/references/pricing-guide.md`
- `../digital-product/references/launch-checklist.md`
- `../digital-product/references/platform-guides.md`

### Step 2: Pricing Recommendation

Using the pricing decision tree from pricing-guide.md, recommend a price. Show the reasoning:
- Product length and depth
- User's audience size (ask if unknown)
- Problem severity
- Recommended price with rationale

### Step 3: Product Description

Write the sales page copy:
- **Teaser paragraph** — industry context + problem + why it matters now
- **"In This Product, You Will Learn"** — 5-7 bullet points of specific outcomes
- **About the Author** — 2-3 sentences positioning the user as credible
- **Social proof section** — placeholder for testimonials (or real ones if available)

### Step 4: Platform Recommendation

Based on the user's situation, recommend one platform from platform-guides.md:
- First product, wants speed = Gumroad
- Existing business, wants low fees = Stripe
- International audience = Lemon Squeezy

Give them the quick-start steps for that platform.

### Step 5: Launch Posts

Generate 3 launch day posts using the voice from `training/voice/voice-template.md` if available:
- **LinkedIn** — announcement with hook, what the product is, who it helps, CTA in comments
- **X/Twitter** — 2-tweet thread (announcement + link)
- **Newsletter/Email** — subject line + 3-paragraph teaser with buy link

### Step 6: Evergreen CTA Templates

Generate 3 reusable promotion templates:
1. **Insight + CTA** — share a key takeaway from the product, link in bio/comments
2. **Story + CTA** — tell a short story related to the topic, mention the product naturally
3. **Results + CTA** — share a buyer result or testimonial, link to product

### Step 7: Launch Checklist

Present the key items from launch-checklist.md as a personalized checklist based on what the user has completed so far.

### Step 8: Review

Show the full launch kit for approval. Revise as needed. Save everything to `projects/[product-name]/launch-kit.md`.

## Handoff

After launch kit is approved:
1. Save to `projects/[product-name]/launch-kit.md`.
2. Update `projects/[product-name]/product-config.md` — check "Launched", fill in Price and Platform.
3. Update `.coworker/index.md` — note "Launch kit complete — [price], [platform]" next to the product.
4. Say: "You're ready to ship. Set up [platform], upload the product, and post on Tuesday-Thursday morning. Come back anytime to generate more promotion content."

## Rules
- Always recommend a specific price with reasoning. Do not say "price it however you want."
- Launch posts must be platform-native. LinkedIn posts are not tweets.
- Include the launch checklist — do not skip it.
- If the user has no audience size info, ask before recommending a price.
- Save all launch assets in one organized location under `projects/[product-name]/`.
- Use voice from `training/voice/voice-template.md` if available.
- Always write to `projects/[product-name]/` — never to workspace root.
