---
name: outline-builder
description: Build a product outline using the interactive 8-question framework. Triggers — "outline my product", "run the 8-question framework", "structure my product"
user-invocable: true
---

# Outline Builder

## Process

### Step 1: Load Context

Read:
- `.coworker/index.md` for active project context
- `../digital-product/references/ltl-frameworks.md` for the 8-question framework
- `projects/[product-name]/product-config.md` for any existing product info (idea, audience, strategy)

### Step 2: Run the Interview

Ask these questions ONE AT A TIME. Wait for the answer before asking the next one.

1. **Who is this for, specifically?** — not "everyone." A job title, situation, experience level.
2. **What problem of theirs are you solving?** — specific. "Marketing" is not a problem. "Can't get clients from LinkedIn" is.
3. **What benefit gets unlocked when this problem is solved?** — what does their life look like after?
4. **How expensive is this problem?** — what are they spending (time, money, stress) to deal with it now? How is your product a fraction of that cost?
5. **What myths keep people from solving this?** — what bad advice do they keep hearing?
6. **Your origin story moment?** — when did you first experience this problem, and how did you overcome it?
7. **Third-party proof?** — case studies, examples, or stories of others who solved this.
8. **What 3-7 action steps will you walk them through?** — these become the chapters of your product.

### Step 3: Compile the Outline

After all 8 answers, assemble:

```
# [Working Title]
## Target Reader — [Q1]
## The Problem — [Q2]
## The Transformation — [Q3]
## Value Proposition — [Q4]
## Myths to Bust — [Q5]
## Origin Story — [Q6]
## Proof — [Q7]
## Chapters
1. [Step from Q8]
2. [Step from Q8]
3. [Step from Q8]
...
```

### Step 4: Review and Approve

Show the compiled outline. Ask: "Does this look right? Anything to add, remove, or change?" Revise until approved.

### Step 5: Next Steps

After approval, recommend title-generator to name the product, then content-writer to expand it.

## Handoff

After outline is approved:
1. Save the outline to `projects/[product-name]/outline.md`.
2. Update `projects/[product-name]/product-config.md` — check "Outline complete", fill in Transformation from Q3.
3. Update `.coworker/index.md` — note "Outline complete" next to the product.
4. Say: "Outline locked. Next up: **name my product** to generate title options using the 1+1+1 framework."

## Rules
- Ask ONE question per message. Never batch questions.
- Wait for the answer before moving on.
- If an answer is vague, ask a follow-up. Push for specifics.
- Keep the compiled outline under 1 page. Skeleton, not full product.
- Save the outline after approval.
- Do not skip any of the 8 questions.
- Always write to `projects/[product-name]/` — never to workspace root.
