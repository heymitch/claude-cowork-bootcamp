# Skill Architecture Guide

Two patterns. Pick the right one before you build anything.

---

## Decision Guide

| Question | Answer | Pattern |
|----------|--------|---------|
| Does it DO a task? | Yes | Standard |
| Does it TEACH a curriculum? | Yes | Tutor |
| Does it do a task AND teach how? | Yes | Standard (with good reference docs) |

Simple test: If the user says "do this for me" — Standard. If the user says "teach me how" with multiple modules — Tutor.

---

## Standard Skill Pattern

For any task that follows a workflow: gather input, process, produce output.

### File Structure

```
skill-name/
├── SKILL.md              (under 100 lines)
└── references/
    ├── templates.md      (output format templates)
    ├── examples.md       (sample inputs and outputs)
    └── domain.md         (rules, heuristics, domain knowledge)
```

### What Goes Where

**SKILL.md contains:**
- Frontmatter: `name` and `description` (trigger phrases in description)
- How to run: 2-3 example prompts
- Workflow steps: what the agent does (action verbs, not descriptions)
- Rules: specific guardrails for this skill

**References contain:**
- Templates for output formatting
- Example inputs and expected outputs
- Domain knowledge that would bloat SKILL.md
- Anything over 10 lines that isn't core workflow logic

### When to Use

- Automating a recurring task (invoices, reports, emails)
- Processing input into output (transcript to action items, brief to draft)
- Multi-tool workflows (read Notion, generate content, post to social)
- Any "do this for me" request

### Example: Screenshot Scanner

A skill that scans screenshots, describes what's in them, and organizes findings.

**SKILL.md (65 lines):** Frontmatter, trigger phrases, 4-step workflow (scan, describe, suggest improvements, save organized report), rules about image handling.

**references/analysis-templates.md:** Templates for different screenshot types (UI, error messages, data dashboards).

**references/common-patterns.md:** Known UI patterns, common error types, what to flag.

The heavy lifting is in references. SKILL.md just orchestrates.

---

## Tutor Skill Pattern

For teaching multi-module course content where students progress through lessons.

### File Structure

```
skill-name/
├── SKILL.md                         (under 500 lines — CONDUCTOR only)
└── references/
    ├── curriculum-map.md            (module sequence + prerequisites)
    ├── lessons/
    │   ├── 01-first-topic.md        (student-facing lesson content)
    │   ├── 02-second-topic.md
    │   └── ...
    └── exercises/
        ├── exercise-one.md          (fillable worksheet)
        ├── exercise-two.md
        └── ...
```

### What Goes Where

**SKILL.md (the conductor) contains:**
- Environment check (config.md, file access)
- Two modes: Foundation (first-time setup) and Module-by-module
- Module routing logic: "Module 3" maps to which lesson and exercise files
- Teaching rules (behavioral guardrails)
- Progress tracking logic
- Commands summary

**SKILL.md does NOT contain:**
- Lesson content (that's in lessons/)
- Exercise templates (that's in exercises/)
- Module sequence details (that's in curriculum-map.md)
- Detailed framework explanations

**curriculum-map.md contains:**
- Table of all modules: ID, name, description, deliverable, prerequisite
- Phase groupings
- Recommended order

**Lesson files (lessons/*.md) contain:**
- Full teaching content formatted for the student to read
- Conversational tone — written as if the student is reading it, not the agent
- Frameworks, checklists, examples, video URLs
- Agent loads these into the student's workspace

**Exercise files (exercises/*.md) contain:**
- Fillable worksheets with blank fields
- Instructions for each field
- Examples of good answers
- "Done" criteria so the student knows when they've finished

### How the Three Pieces Work Together

```
Student says "Module 3"
         |
SKILL.md (conductor):
  1. Read curriculum-map.md → find Module 3
  2. Check prerequisites → verify prior modules complete
  3. Load lessons/03-topic.md → create file in workspace
  4. Load exercises/exercise-name.md → walk student through in chat
  5. Save completed exercise → update progress
```

### When to Use

- Teaching a multi-module course
- Guided onboarding with sequential steps
- Any "teach me" request with 3+ distinct topics that build on each other

---

## Side-by-Side Comparison

| Feature | Standard | Tutor |
|---------|----------|-------|
| **SKILL.md size** | Under 100 lines | Under 500 lines |
| **Primary action** | Does work for you | Teaches you to do work |
| **Trigger** | "Do X for me" | "Teach me X" / "Module 3" |
| **Reference files** | Templates, examples, domain docs | Curriculum map, lessons, exercises |
| **User interaction** | Minimal — approve output | Heavy — fill exercises, learn concepts |
| **Progress tracking** | Not needed | Required (which modules completed) |
| **Output** | Files, posts, emails, reports | Knowledge in the student's head + completed exercises |
| **Personalization** | Reads config.md for business context | Reads config.md for business context + tracks progress |
| **File routing** | SKILL.md handles everything | SKILL.md routes to lesson/exercise files |
| **Content location** | Can be inline if short | NEVER inline — always in lessons/ and exercises/ |

---

## Common Mistakes

1. **Building a Tutor when Standard would work.** If the user just needs the task done, don't teach them. Build a Standard skill.
2. **Putting lesson content in SKILL.md.** This bloats the conductor. One lesson and you're over 500 lines. Always use separate files.
3. **SKILL.md over 100 lines (Standard).** Split to references. If you can't, it might need sub-skills instead.
4. **No trigger phrases in frontmatter.** Without them, the skill won't auto-invoke. Always include 2-3 trigger phrases in the description.
5. **Generic references.** "Here are some tips" is useless. References should have concrete templates, real examples, and specific rules.
