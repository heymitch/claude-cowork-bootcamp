---
name: digital-product
description: Build a digital product from idea to live sale. Triggers — "build a digital product", "idea to sale", "find product ideas", "validate idea", "product strategy", "superniche", "outline product", "8-question framework", "name my product", "generate titles", "write the product", "write the ebook", "write video scripts", "script my course", "design my ebook", "design my product", "product cover", "build landing page", "launch my product", "launch kit"
user-invocable: true
---

# Digital Product — Router

## Preflight

1. Read `.coworker/index.md` for project context, voice profile, and active projects. If missing, proceed with clean defaults.
2. Check for `projects/[product-name]/product-config.md` in the Coworker workspace. If it exists, read pipeline status and resume from the next unchecked step. If not, suggest running idea-finder to get started.

## Routing

**Full pipeline** ("build a digital product", "idea to sale", "zero to one"):
Run in order: idea-finder > strategy-designer > topic-validator > outline-builder > title-generator > content-writer > ebook-designer > design-advisor > vercel-landing-page > launch-kit

**Individual skills:**

| Intent | Skill |
|--------|-------|
| "find product ideas", "what should I build" | `../idea-finder/SKILL.md` |
| "product strategy", "superniche", "define my transformation" | `../strategy-designer/SKILL.md` |
| "validate this idea", "test my product idea" | `../topic-validator/SKILL.md` |
| "outline my product", "8-question framework" | `../outline-builder/SKILL.md` |
| "name my product", "generate titles" | `../title-generator/SKILL.md` |
| "write my product", "write the ebook" | `../content-writer/SKILL.md` |
| "write video scripts", "script my course" | `../script-writer/SKILL.md` |
| "design my ebook", "format my product" | `../ebook-designer/SKILL.md` |
| "design my product", "product cover" | `../design-advisor/SKILL.md` |
| "build landing page", "deploy sales page" | `../vercel-landing-page/SKILL.md` |
| "launch my product", "create launch posts" | `../launch-kit/SKILL.md` |

**Support skills (not user-facing):**

| Skill | Role |
|-------|------|
| `../frontend-design/SKILL.md` | Design philosophy loaded by vercel-landing-page when building custom UI. Not called directly. |

## How It Works

If the user says a specific trigger, go directly to that skill. If they say something broad like "build a digital product," check `projects/[product-name]/product-config.md` first — if it exists and has progress, resume from the next unchecked step. If starting fresh, begin with idea-finder and move through the pipeline step by step. Always confirm before advancing.

Every skill updates `projects/[product-name]/product-config.md` on completion and recommends the next step. The user can always jump to any skill directly.

## References

All frameworks and templates live in `references/`:
- `ltl-frameworks.md` — 8-question framework, 1+1+1 naming, 10 sections template
- `pricing-guide.md` — pricing tiers, psychology, platform fees
- `launch-checklist.md` — pre-launch, launch day, post-launch actions
- `platform-guides.md` — Gumroad, Stripe, Lemon Squeezy setup
- `product-config-template.md` — pipeline state tracking template
- `wtc-strategy.md` — Write the Course strategy frameworks (superniche, 7 problems, origin story, pricing)
