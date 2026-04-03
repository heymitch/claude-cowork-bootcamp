---
name: strategy-designer
description: Design your product strategy before building — define your superniche, transformation, 7 problems, and origin story using proven frameworks. Triggers — "design my product strategy", "who is this for", "define my transformation", "superniche my product", "product strategy"
user-invocable: true
---

# Strategy Designer

Shape the positioning, audience, and transformation of your product before writing a single word. Uses the Write the Course frameworks.

## Process

### Step 1: Load Context

Read:
- `.coworker/index.md` for project context and any active product info
- `../digital-product/references/wtc-strategy.md` for all frameworks
- `projects/[product-name]/product-config.md` for any existing product info (idea, audience)
- `training/references/business-blueprint.md` if it exists — for business context and voice

If the user already ran idea-finder, pull their chosen topic as a starting point.

### Step 2: Superniche Interview

Ask ONE question at a time. Wait for each answer before moving on.

**Q1 — Who specifically is this for?**
Not "entrepreneurs" or "beginners." A job title, a situation, an experience level. Push for specifics. "Freelance writers who want to break into ghostwriting" is good. "People who want to write" is not.

**Q2 — What's the transformation?**
What does their life look like AFTER they use your product? Be concrete — income, time saved, confidence, capability, status. "Go from charging $0.10/word to $1/word as a ghostwriter" is specific.

**Q3 — What are the 7 problems standing between them and that transformation?**
List them. Mix all three types:
- Understanding problems (myths, confusion, wrong mental models)
- Actionable problems (know what to do but can't execute)
- Emotional problems (fear, imposter syndrome, lack of confidence)

If the user gives fewer than 5, push for more. If they give vague ones, push for specifics.

**Q4 — What's your origin story?**
When were YOU stuck on this exact problem? What bad advice did you follow? What was the low point? What changed? One paragraph, not an essay.

**Q5 — What's your unique method?**
Do you have a name for your approach? A framework, a system, a process? If yes, use it. If not, help them name it. "[Number] + [Noun]" patterns work well (e.g., "The 30-Day Ship Method", "The 5-Layer Ghostwriting System").

### Step 3: Compile Strategy Brief

After all 5 answers, assemble:

```
## Strategy Brief

- **Superniche:** [audience] + [specific angle/method]
- **Transformation:** [before state] → [after state]
- **Main Offer:** [1 sentence — the big promise]
- **7 Problems:**
  1. [Understanding] ...
  2. [Actionable] ...
  3. [Emotional] ...
  4-7. ...
- **Origin hook:** [1-2 sentences]
- **Method name:** [name, or "TBD"]
```

### Step 4: Review and Approve

Show the brief. Ask: "Does this feel right? Anything missing or off?" Revise until approved.

### Step 5: Stress Test (Optional)

If the user hasn't validated demand yet, flag it: "Before building, consider running **validate this idea** to test demand with 3 social posts. It takes a week but saves you from building something nobody wants."

## Handoff

After strategy brief is approved:
1. Update `projects/[product-name]/product-config.md` — check "Strategy defined", fill in Superniche, 7 Problems, Origin hook, Transformation, Method name.
2. Update `.coworker/index.md` — update the product one-liner with superniche and transformation.
3. If demand not yet validated: "Strategy locked. Next up: **validate this idea** to test demand before building."
4. If demand already validated: "Strategy locked. Next up: **outline my product** to structure the content using the 8-question framework."

## Rules
- Ask ONE question per message. Never batch.
- Push for specifics. Vague = redo. "Too niche" = perfect.
- Keep the Strategy Brief under half a page. It's a compass, not a map.
- Do not skip the 7 Problems — they become the product's chapters.
- Reference wtc-strategy.md frameworks when coaching, but don't dump the whole doc on the user.
- If the user has no origin story, help them find one. Everyone has a "when I was stuck" moment.
