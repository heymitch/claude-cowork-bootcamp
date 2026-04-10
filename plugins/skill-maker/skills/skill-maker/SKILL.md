---
name: skill-maker
description: Build any skill you need, forever. The meta-skill that designs, builds, tests, and packages custom agent skills. Say "build me a skill" or "create a skill" or "I need a skill that" or "test my skill" or "package my skill" or "what can skills do".
user-invocable: false
---

# Skill Maker

## Preflight

Read `config.md` for business context. If missing: "Run your business blueprint first. Skills built without context are generic and useless."

## Routing

Match the user's intent and hand off to the right sub-skill:

### "Build me a skill" / "Create a skill" / "I need a skill that..." / "Turn this into a skill"
**Full build flow.** Run these in sequence:
1. **skill-architect** — interview, determine type, design architecture, get approval
2. **reference-builder** — generate all reference files from the architecture
3. **skill-tester** — evaluate the finished skill against the quality rubric

### "What can skills do?" / "Skill capabilities" / "What's possible?"
Read `references/cowork-capabilities.md` and answer the user's question about what agents can and can't do.

### "Test my skill" / "Check this skill" / "Validate my skill" / "Grade this skill"
Run **skill-tester** on the specified skill directory.

### "Package my skill" / "Ship my skill" / "Export my skill" / "Make this shareable"
Run **skill-packager**. It picks the right format based on what the skill contains:
- Single SKILL.md, no bundled files → **inline copy** (no packaging, just paste)
- Single skill with references/scripts → **.skill file** (via `package_skill.py`)
- 2+ skills for team distribution → **plugin bundle** (`.claude-plugin/` + skills/)

Never default to plugin bundle for single personal skills — that's the most common packaging mistake.

### "Build references" / "Create reference docs" / "Write reference files"
Run **reference-builder** for the specified skill architecture.

### "How do skills work?" / "Skill architecture" / "Standard vs tutor"
Read `references/skill-architecture.md` and explain the two patterns.

### "Show me examples" / "What does a good skill look like?"
Read `references/example-skills.md` and walk through annotated examples.

## Rules
- Always read config.md before any build — personalization is non-negotiable
- Route to sub-skills — this file orchestrates, it doesn't do the work
- Full builds go architect → references → tester. Don't skip steps.
- If intent is unclear, ask: "Do you want to build a new skill, test an existing one, or package one for sharing?"
