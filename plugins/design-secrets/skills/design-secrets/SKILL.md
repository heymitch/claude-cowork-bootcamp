---
name: design-secrets
description: Your personal design aesthetic baked into Cowork. Extract your visual identity from logos, websites, or descriptions, then apply it to every visual Cowork produces. Say "set up my design", "extract my brand", "design a graphic", "make this look branded", "generate a visual", "push to Figma", or "create in Figma".
user-invocable: false
---

# Design Secrets — Router

Routes design intent to the right sub-skill. The goal: every visual produced by Cowork looks like YOU, not like generic AI output.

## Routing Table

| Intent | Route to |
|--------|----------|
| "Set up my design" / "Extract my brand" / "Analyze my brand" / "Upload my brand assets" / "Here's my logo" / "Here's my website" | `skills/brand-extractor/SKILL.md` |
| "Design a [thing]" / "Make this look good" / "Make this look branded" / "Generate a visual" / "Create a graphic" / "Styled PDF" / "Branded image" / "Create a landing page" / "Make a slide" | `skills/design-generator/SKILL.md` |
| "Push to Figma" / "Create in Figma" / "Figma design system" / "Set up my Figma" / "Sync design to Figma" / "Build a component library" | `skills/figma-guide/SKILL.md` |

## Preflight

Before routing to design-generator, silently check whether `training/references/design-profile.md` exists.

- If it exists: proceed.
- If it doesn't: do NOT default to generic styling. Tell the user: "I don't have your design profile yet. Want to set it up now? Takes about 2 minutes — just share a logo, website, or describe your aesthetic." Then route to `skills/brand-extractor/SKILL.md`.

## Rules

- NEVER generate a visual without reading the design profile first.
- If no profile exists, ask before defaulting to anything generic.
- Keep all generated output in `output/`.
- Update `.coworker/index.md` after creating or updating the design profile.
