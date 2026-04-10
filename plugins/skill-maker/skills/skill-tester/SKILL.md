---
name: skill-tester
description: Evaluate any skill against the High Protein quality rubric. Say "test my skill" or "validate this skill" or "check my skill" or "grade this skill".
user-invocable: true
---

# Skill Tester

## Preflight
1. Read `../skill-maker/references/quality-rubric.md` for the evaluation framework.
2. Get the skill path. If not provided, ask: "Which skill? Give me the folder path."
3. Read the skill's SKILL.md and all reference files.
4. Determine type: Standard (no lessons/) or Tutor (has lessons/ and exercises/).

## What the Agent Does

### Step 1: The 5-Second Test
Read the frontmatter description. In 5 seconds, can you tell what this skill does and when you'd use it? Report PASS or FAIL with one sentence.

### Step 2: High Protein Checklist
**Standard Skills (10 items):**
1. Saves real hours? (not a party trick)
2. Does work, not describes work? (produces output)
3. One-sentence trigger? (no multi-step setup)
4. Uses config.md? (personalized output)
5. SKILL.md under 100 lines? (count them)
6. Trigger phrases in frontmatter?
7. Specific rules? (not "be helpful" — real guardrails)
8. Shows before saving? (user approves output)
9. Handles missing tools? (graceful degradation)
10. Weekly use test? (solves a real recurring problem)

**Tutor Skills add 5 more:**
11. SKILL.md is conductor only? (no lesson content)
12. curriculum-map.md complete? (every module mapped)
13. Lessons student-facing? (conversational, not agent-notes)
14. Exercises fillable? (blank fields, not pre-filled)
15. End-to-end flow works? (module request to completion)

Score each PASS or FAIL with specific notes.

### Step 3: Simulated Execution
Walk through as a user: trigger it, follow the workflow, check config.md usage, check missing-tool handling, check output-before-save. For tutors: request a module, check exercise fields, check progress tracking.

### Step 4: Generate Report
```
SKILL TEST REPORT
Skill: [name] | Type: Standard/Tutor | Path: [path]
5-SECOND TEST: PASS/FAIL — [one sentence]
CHECKLIST: [X/10] or [X/15]
[each item: PASS/FAIL + note]
SIMULATED RUN: Trigger used, result, issues found
GRADE: [A/B/C/D/F]
TOP 3 FIXES: [numbered list]
```

### Step 5: Offer to Fix
- Grade A: "Ready to ship."
- Grade B: "Close. Want me to fix [specific issues]?"
- Grade C-D: "Biggest issue is [X]. Want me to fix it?"
- Grade F: "Needs a rebuild. Start fresh with skill-architect?"

## Rules
- Be honest — a bad grade now prevents a bad user experience later
- Count SKILL.md lines exactly, don't estimate
- Read every file in the skill directory, don't skip references
- No frontmatter = automatic D at best
- Never give an A to a skill that skips config.md
- Show the full report before offering fixes
