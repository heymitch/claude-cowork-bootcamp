---
name: figma-guide
description: Connect Cowork to Figma, push your design profile as variables and tokens, and build a full design system from your brand. Triggers on "push to Figma", "create in Figma", "Figma design system", "set up my Figma", "sync design to Figma", "build a component library", "create color palette in Figma".
user-invocable: true
---

# Figma Guide

This is a knowledge skill. It teaches you how to connect Figma to Cowork and use your design profile to build a real Figma design system. The actual Figma MCP tools live in the Figma connector — this skill tells you how to use them effectively.

## First: Connect Figma

Before anything else, you need the Figma connector active in Cowork.

**How to connect:**
1. In Cowork, open Settings → Connectors
2. Find "Figma" and click Connect
3. Paste your Figma personal access token (get it at figma.com → Account Settings → Access Tokens)
4. Cowork will confirm the connection

Once connected, the Figma tools are available as slash commands. You'll see them when you type `/figma`.

**Check if it's connected now:**
If Figma MCP tools are active in this session, I can run Figma operations directly. If not, I'll walk you through connecting first.

## Using Figma Tools in Cowork

Once connected, these are the core operations:

### Read a design
```
"Read the frame called [name] from my Figma file"
"What's in my design file [file ID]?"
"Show me the components in [file name]"
```
Cowork reads the Figma file and returns the structure — frames, layers, colors, text, component names.

### Push your design profile to Figma as variables

This is the power move — your design-profile.md becomes a Figma variable collection that every file can reference.

To do this, say: "Push my design profile to Figma as variables"

What happens:
1. Cowork reads `training/references/design-profile.md`
2. Creates a Figma variable collection called "Brand Tokens"
3. Adds color variables: `brand/primary`, `brand/secondary`, `brand/background`, `brand/accent`, `brand/text`
4. Adds typography variables: `type/display`, `type/body`, `type/mono`
5. Your Figma files can now reference these tokens — update once, updates everywhere

### Build a component library

Say: "Build a component library matching my brand" or use the skill `/figma:figma-generate-library`

The figma-generate-library skill takes your design profile and builds:
- Color swatches and palette documentation
- Text style definitions (H1, H2, H3, body, caption, mono)
- Base components: Button (primary, secondary, ghost), Card, Badge, Tag, Divider
- Layout frames: mobile, tablet, desktop grids

### Implement a Figma design in code

Say: "Read frame [name] and implement it in code" or use `/figma:figma-implement-design`

Cowork reads the frame, extracts layout, colors, and typography, and generates HTML/CSS or React code — styled with your design profile variables.

### Create design system rules

Use `/figma:figma-create-design-system-rules` to generate a document describing your design system's rules, usage patterns, and "do/don't" examples based on your profile.

## Practical Examples

### "Create a color palette in Figma from my design profile"
1. Load `training/references/design-profile.md`
2. Create a new Figma frame called "Color Palette"
3. Add color swatches for each profile color with hex labels
4. Organize into a grid: primary, secondary, background, accent, text + variants

### "Build a component library matching my brand"
Runs `/figma:figma-generate-library` with your design profile as the input. Creates buttons, cards, typography styles, and icon placeholders all using your exact colors and fonts.

### "Read a Figma frame and implement it in code"
Runs `/figma:figma-implement-design`. Give it a frame name or node ID, it reads the layout and produces HTML/CSS that matches the design — with your brand variables wired in.

## Figma Token File Format

If you want to export your design profile as a Figma-compatible tokens JSON file:

```json
{
  "brand": {
    "primary": { "value": "#E8682A", "type": "color" },
    "secondary": { "value": "#1a1a1a", "type": "color" },
    "background": { "value": "#F0E8D4", "type": "color" },
    "accent": { "value": "#C0392B", "type": "color" },
    "text": { "value": "#1a1a1a", "type": "color" }
  },
  "typography": {
    "display": { "value": "Oswald", "type": "fontFamily" },
    "body": { "value": "Inter", "type": "fontFamily" },
    "mono": { "value": "Space Mono", "type": "fontFamily" }
  }
}
```

This file can be imported via the Tokens Studio plugin in Figma.

## Rules

- Always check for Figma connector before attempting Figma operations.
- If not connected, walk the user through connecting before anything else.
- Read the design profile before pushing anything to Figma — Figma should match the profile, not the other way around.
- Use the figma-generate-library and figma-implement-design skills for production work — don't reinvent them.
