---
name: skill-architect
description: Design the architecture for a new skill — determines type, structure, and feasibility. Say "build me a skill" or "create a skill" or "I need a skill that" or "turn this into a skill".
user-invocable: true
---

# Skill Architect

## Preflight

1. Read `config.md` for business context, tools, and voice.
   - If missing: "Run your business blueprint first — skills built without context are generic and useless."
2. Read `../skill-maker/references/cowork-capabilities.md` — know what's possible.
3. Continue silently.

## What the Agent Does

### Step 1: Interview (One Question at a Time)

Ask these five questions. Wait for each answer before asking the next.

1. **What task do you want to automate?** Describe it like you're explaining to a new hire.
2. **How often do you do this?** (Daily, weekly, per-project, on-demand)
3. **What's the input?** (A file, a meeting, a prompt, a voice memo, a Notion page, etc.)
4. **What's the output?** (A document, a post, an email, a presentation, a file in a folder)
5. **Who else needs to run this?** (Just you, your team, your clients)

### Step 2: Determine Skill Type

Read `../skill-maker/references/skill-architecture.md` for the decision guide.

- Does it DO a task? → Standard Skill
- Does it TEACH a curriculum? → Tutor Skill
- Does it do both? → Standard with good reference docs

Tell the user which type and why. Get their agreement before proceeding.

### Step 3: Check Feasibility

Using the interview answers and `cowork-capabilities.md`:
- List which tools/connectors the skill needs
- Check which ones the user has (from config.md)
- Flag anything that's impossible on the platform
- If a required tool is missing, explain what it does and offer alternatives

### Step 4: Design the Architecture

**For Standard Skills**, lay out:
- Skill folder name
- SKILL.md outline (workflow steps, rules)
- Reference files needed (templates, examples, domain docs)
- Which connectors it will use

**For Tutor Skills**, lay out:
- Skill folder name
- SKILL.md conductor outline (modes, routing, progress tracking)
- Curriculum map structure (modules, prerequisites)
- Lesson files needed (one per module)
- Exercise files needed (fillable worksheets)

### Step 5: Present the Blueprint

Show the full architecture plan:
- Folder tree with every file listed
- One-line description of what each file will contain
- Tools required vs. available
- Estimated build complexity (simple / moderate / complex)

Ask: "Does this architecture look right? I'll start building once you approve."

## Rules
- Never skip the interview — even if the user's first message is detailed, confirm the 5 answers
- Always check feasibility before designing — don't plan skills around impossible capabilities
- One architecture plan per skill — don't combine multiple skills into one
- If the user's request is too vague after the interview, ask ONE clarifying question
- Standard skills: plan for under 100 lines in SKILL.md
- Tutor skills: plan for under 500 lines in SKILL.md, all content in references/
- Always get approval before handing off to reference-builder
