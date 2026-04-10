---
name: reference-builder
description: Generate all reference files a skill needs — templates, examples, and domain docs. Say "build references for skill" or "create skill references" or "write reference docs".
user-invocable: true
---

# Reference Builder

## Preflight

1. Read `config.md` for business context and voice.
   - If missing: "References need your business context to be specific. Run your business blueprint first."
2. Read `../skill-maker/references/example-skills.md` for reference file patterns.
3. Get the skill architecture — either from skill-architect output or the user's description.
4. Continue.

## What the Agent Does

### Step 1: Identify Required References

From the architecture plan, list every reference file needed:

**Standard skills may need:**
- `templates.md` — output format templates
- `examples.md` — sample inputs and expected outputs
- `domain.md` — domain rules, heuristics, frameworks

**Tutor skills may need:**
- `curriculum-map.md` — full module sequence with prerequisites
- `lessons/[module].md` — one per module, student-facing content
- `exercises/[exercise].md` — one per exercise, fillable worksheets

Show the list. Confirm with the user before building.

### Step 2: Build Each Reference File

For each file, follow these rules:

**Templates:** Include the full output structure with placeholders. Mark variable fields clearly. Add notes on when to use each template variation.

**Examples:** Show 2-3 complete input/output pairs. Annotate what makes each output good. Include edge cases if relevant.

**Domain docs:** Organize as actionable rules, not essays. Use tables and checklists. Include the "why" — not just the "what."

**Curriculum maps:** Table with Module ID, Name, Description, Deliverable, Prerequisite. Include phase groupings and recommended order.

**Lessons:** Student-facing tone. Conversational. Frameworks with clear steps. Real examples. Video URLs if provided. Written for reading in the editor, not chat.

**Exercises:** Blank fields with underscores or brackets. Instructions per field. One example of a good answer. "Done when" checklist at the bottom.

### Step 3: Review Each File

Show each reference file to the user as you complete it:
- File name and purpose
- Full content
- Ask: "Does this cover what you need? Anything to add or change?"

Make edits before moving to the next file.

### Step 4: Save All Files

On approval, save each file to the skill's `references/` directory.
Confirm the complete file tree when done.

## Rules
- Every reference file must be dense and actionable — no vague "tips" or "suggestions"
- Templates must be copy-paste ready with clear placeholders
- Examples must show complete input AND output — not just output
- Lesson files are for the student to read — conversational tone, never agent-notes
- Exercise files must have blank fields — never pre-fill answers
- Show each file for approval before saving — never batch-save without review
- If the user provides source material (PDFs, docs), extract from it — don't summarize it
- Personalize using config.md — templates should use the user's business name, voice, and context
