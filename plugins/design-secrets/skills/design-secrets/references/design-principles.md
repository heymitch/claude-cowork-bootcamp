# Design Principles

These principles govern every visual produced by the design-secrets plugin. The goal is brand consistency, not artistic expression. Every output should feel like it came from the same person.

---

## 1. Brand First, Always

Before any aesthetic decision, check the design profile. Colors, fonts, spacing, mood — all of it is already decided. The job is to apply those decisions faithfully, not to make new ones.

If you're tempted to choose a color because it "looks nice" — stop. Use the profile's color. If you're tempted to use a different font because it "feels right" — stop. Use the profile's font.

Generic output is what happens when the designer ignores the brief. The profile is the brief.

---

## 2. Typography Hierarchy is Non-Negotiable

Three roles, three fonts. Never mix outside this system:

- **Display font** — headers, titles, hero text. Bold and authoritative. Sets the register.
- **Body font** — paragraphs, captions, supporting text. Readable at any size.
- **Mono font** — code, metadata, small labels, technical details. Signals precision.

If the brand is bold, every header is bold. Don't go condensed-bold for H1 and light-regular for H2 — the contrast breaks the system. Keep weight consistent within each role.

---

## 3. Weight Consistency

If the brand is thick and bold, everything in it is thick and bold. Thin lines, light text, and airy spacing feel like a different brand living in the same file.

If the brand is minimal and airy, everything breathes. Dense layouts feel like an intrusion.

Pick a register. Stay in it.

---

## 4. SVG is the Default for Graphics

SVG is resolution-independent, editable, and ships without pixel artifacts. Use it for:
- Icons and logos
- Illustrations and diagrams
- Social images and banners
- Any graphic that doesn't need to be a document

Keep text as `<text>` elements, not paths. Paths look the same but break editability.

---

## 5. HTML/CSS for Documents

When the output has structured content — paragraphs, sections, headers, tables — use HTML/CSS. It gives precise control over dimensions, renders consistently, and converts to PDF cleanly via Puppeteer.

Avoid canvas-based or image-only PDFs. They're hard to update and impossible to copy text from.

---

## 6. Physical Product Aesthetic Over Web Default

Web defaults are flat cards, rounded corners, Bootstrap blue, and system fonts. That's what you get when a developer picks UI components without brand intent.

The target aesthetic is physical product — designed things that feel like they exist in the real world. Think:
- Thick borders instead of hairline rules
- Bold condensed type instead of thin sans-serif
- Warm backgrounds instead of pure white
- Structured zones instead of floating cards
- Technical details and metadata as design elements

Not every brand has this aesthetic — some are minimal and digital. But "physical product feel" is the antidote to generic web output. When in doubt, go more physical, not more web.

---

## 7. The Avoid List is a Hard Stop

Every design profile has an "Avoid" section. These are not suggestions. They are:
- Things the user has already decided look wrong for their brand
- Patterns that break the visual identity
- Aesthetic violations that undo the whole profile

If the profile says "avoid gradients" — no gradients. Not even subtle ones. Not "just this once." No gradients.

---

## 8. No Profile, No Output

If no design profile exists, do not default to generic. Ask the user to set up their brand first. Generic output is worse than no output — it trains the user to expect mediocrity.

The right response when the profile is missing: "I need your design profile before I can make something that looks like you. Want to set it up now?"

---

## 9. Save Everything to `output/`

No generated files in the project root, no files on the desktop, no files in temp directories. Everything lives in `output/` so the user can find it and version it.

---

## 10. Show, Don't Describe

After generating, show the output (inline SVG, HTML preview, file path). Don't summarize what you built — show it. Let the output speak.
