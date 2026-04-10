# Example Skills (Annotated)

Three fully-built examples showing what good looks like. Study the annotations.

---

## Example 1: Simple Standard Skill — Invoice Generator

A lean skill that produces professional invoices from minimal input.

### SKILL.md (78 lines)

```markdown
---
name: invoice-generator
description: Generate professional invoices from project details. Say "create an invoice for [client]" or "invoice [project] for [amount]" or "bill [client] for [hours] hours".
---

# Invoice Generator

Create clean, professional invoices personalized to your business. One sentence and it's done.

## How to Run
- "Create an invoice for Acme Corp"
- "Invoice the website project for $3,500"
- "Bill Sarah for 12 hours of consulting"

---

## Preflight

1. Read `config.md` — load business name, address, payment details, hourly rate.
   - If missing: "I need your business details to create invoices. Run your business blueprint first."
2. Continue silently.

## What the Agent Does

### Step 1: Gather Details
Ask for anything not already provided (one question at a time):
- Client name and email
- Project or service description
- Amount (or hours x rate from config.md)
- Due date (default: 30 days from today)

### Step 2: Load Template
Read `references/invoice-template.md` for the invoice format.

### Step 3: Generate Invoice
Fill in the template with:
- Your business details (from config.md)
- Client details (from Step 1)
- Line items, subtotal, tax if applicable, total
- Payment instructions (from config.md)
- Invoice number (auto-increment: check existing invoices in invoices/ folder)

### Step 4: Review and Save
- Show the complete invoice in chat
- Ask: "Look good? I'll save it to invoices/[number]-[client].md"
- On approval, save the file
- Offer: "Want me to email this to [client email]?"

## Rules
- Always show the invoice before saving — never auto-save
- If no hourly rate in config.md and user gives hours, ask for rate
- Invoice numbers auto-increment — check the invoices/ folder
- Default payment terms: Net 30 unless config.md specifies otherwise
- Include tax line only if config.md has a tax rate
- Never fabricate business details — everything comes from config.md or the user
```

**Why this works:**
- Frontmatter description has 3 trigger phrases — auto-invocation works for natural requests
- Preflight checks config.md — output is personalized, not generic
- Steps are action verbs: "Ask," "Read," "Fill," "Show" — the agent knows exactly what to do
- Rules are specific: "Never auto-save," "Default Net 30," "Include tax only if..." — not vague guidance
- Under 100 lines — the template lives in references, keeping SKILL.md lean

---

## Example 2: Complex Standard Skill — Content Repurposer

A multi-step skill that takes one piece of content and adapts it for multiple platforms.

### File Structure

```
content-repurposer/
├── SKILL.md                        (92 lines)
└── references/
    ├── platform-formats.md         (format rules per platform)
    └── repurposing-templates.md    (transformation templates)
```

### SKILL.md (92 lines)

```markdown
---
name: content-repurposer
description: Turn one piece of content into posts for every platform. Say "repurpose this for social" or "turn my blog post into LinkedIn and Twitter content" or "adapt this for all platforms".
---

# Content Repurposer

One input. Multiple platform-ready outputs. No more rewriting the same idea five times.

## How to Run
- "Repurpose this blog post for social media"
- "Turn my newsletter into LinkedIn and Twitter posts"
- "Take this transcript and make it content for all platforms"

---

## Preflight

1. Read `config.md` — load voice profile, platforms used, audience.
   - If missing: "I need your voice and platform preferences. Run your business blueprint first."
2. Continue silently.

## What the Agent Does

### Step 1: Identify the Source
- If user provides a file path, read it
- If user pastes content, capture it
- If user describes it, ask: "Can you paste the content or give me the file path?"
- Identify content type: blog post, newsletter, transcript, video script, or notes

### Step 2: Extract Core Message
- Pull out the main thesis (one sentence)
- Identify 3-5 key points or frameworks
- Note any stories, examples, or data points
- Flag quotable lines

### Step 3: Load Platform Rules
Read `references/platform-formats.md` for each target platform's constraints.

### Step 4: Generate Per Platform
Read `references/repurposing-templates.md` for transformation patterns.
For each platform the user wants (or all platforms in config.md):
- Apply platform-specific format rules
- Match the user's voice profile from config.md
- Transform — don't just truncate. Reshape the content for how people read on that platform.

### Step 5: Review
- Show all generated versions, grouped by platform
- Label each with platform name and character count
- Ask: "Want me to adjust any of these?"
- On approval, save to content/[date]-repurposed/

## Rules
- Never just shorten the original — reshape it for each platform's reading style
- LinkedIn: professional but personal, 800-1300 characters, hook in first line
- Twitter/X: punchy, under 280 characters per tweet, thread if needed
- Always match the user's voice from config.md — not generic marketing speak
- Show all versions before saving — never auto-publish
- If Ayrshare is connected, offer to post. If not, save as files.
```

**Why this works:**
- SKILL.md stays under 100 lines by offloading format rules and templates to references
- The references do the heavy lifting: platform-formats.md has character limits, tone rules, and structure for each platform. repurposing-templates.md has patterns for transforming long to short, formal to casual, written to visual concepts.
- Step 4 doesn't hardcode platform rules in SKILL.md — it reads them from a reference file, so adding a new platform means updating one file, not rewriting the skill
- Rules section has platform-specific constraints (LinkedIn character count, Twitter thread logic) as guardrails

### references/platform-formats.md (excerpt)

```markdown
# Platform Format Rules

## LinkedIn
- Length: 800-1300 characters for feed posts
- Hook: First line must stop the scroll. Question, bold claim, or surprising stat.
- Structure: Hook → Context → Framework/List → CTA
- Formatting: Line breaks after every 1-2 sentences. Use bold for key terms.
- Tone: Professional but conversational. First person. Stories work.

## Twitter/X
- Length: Under 280 characters per tweet
- Thread: If content needs more, use a thread (numbered 1/N format)
- Hook: Tweet 1 must stand alone — people may not read the thread
- Tone: Punchy. Direct. No fluff. Opinions and hot takes perform.
...
```

### references/repurposing-templates.md (excerpt)

```markdown
# Repurposing Templates

## Blog Post → LinkedIn
1. Extract the one counterintuitive insight from the post
2. Open with that insight as a hook ("Most people think X. They're wrong.")
3. Give 3 supporting points from the post (compressed)
4. Close with a question or CTA from the original

## Blog Post → Twitter Thread
1. Tweet 1: The boldest claim from the post (standalone value)
2. Tweets 2-5: One key point per tweet (no filler tweets)
3. Final tweet: CTA or link back to full post
...
```

---

## Example 3: Tutor Skill — Email Course Tutor

A tutor that teaches a 5-module email marketing course with guided exercises.

### File Structure

```
email-course-tutor/
├── SKILL.md                                    (conductor — 180 lines)
└── references/
    ├── curriculum-map.md                       (module sequence)
    ├── lessons/
    │   ├── 01-email-foundations.md              (student-facing)
    │   ├── 02-subject-lines.md
    │   ├── 03-welcome-sequences.md
    │   ├── 04-sales-emails.md
    │   └── 05-analytics-optimization.md
    └── exercises/
        ├── audience-profile.md                 (fillable worksheet)
        ├── subject-line-workshop.md
        ├── welcome-sequence-builder.md
        ├── sales-email-draft.md
        └── metrics-dashboard.md
```

### SKILL.md (conductor only — 180 lines)

```markdown
---
name: email-course-tutor
description: Learn email marketing from scratch — 5 modules from foundations to optimization. Say "teach me email marketing" or "email course module 3" or "start the email course".
---

# Email Course Tutor

Master email marketing in 5 modules. Each module has a lesson to read and an exercise to complete.

## Commands
- "Start the email course" — begin from Module 1
- "Module [number]" — jump to a specific module
- "What's next?" — see your progress and next module
- "My progress" — see which modules you've completed

---

## Preflight

1. Read `config.md` — load business context for personalized exercises.
   - If missing: "Your exercises will be generic without business context. Run your business blueprint first, or say 'skip' to continue without it."
2. Check for progress file: `email-course-progress.json`
   - If exists: load completed modules
   - If missing: create it with all modules marked incomplete
3. Continue.

## Mode: Foundation (First Time)

If no progress file exists:
1. Welcome the student: "5 modules. Each one has a lesson and a hands-on exercise. You'll build real email assets for your business as you go."
2. Show the module map (read curriculum-map.md, display as a numbered list)
3. Start Module 1

## Mode: Module-by-Module

### Routing Table
| Module | Lesson File | Exercise File |
|--------|-------------|---------------|
| 1 | lessons/01-email-foundations.md | exercises/audience-profile.md |
| 2 | lessons/02-subject-lines.md | exercises/subject-line-workshop.md |
| 3 | lessons/03-welcome-sequences.md | exercises/welcome-sequence-builder.md |
| 4 | lessons/04-sales-emails.md | exercises/sales-email-draft.md |
| 5 | lessons/05-analytics-optimization.md | exercises/metrics-dashboard.md |

### Module Flow
1. Check prerequisites (read curriculum-map.md)
2. Load the lesson file → create a copy in the student's workspace
3. Say: "I loaded Module [X]: [name]. Read through it in your editor, then tell me when you're ready for the exercise."
4. Wait for the student
5. Load the exercise file → walk through it in chat, one field at a time
6. Use config.md to personalize examples and suggestions
7. When exercise is complete, save it and update progress file
8. Offer: "Ready for Module [next]? Or take a break — your progress is saved."

## Teaching Rules
- Never dump lesson content into chat — always load it as a file
- Walk through exercises one field at a time — don't show the whole worksheet at once
- Use the student's business context (from config.md) in examples
- If a student is stuck, give ONE hint, not the answer
- Celebrate completed modules: "Module [X] done. [Remaining] to go."
- Never skip prerequisites — if Module 3 requires 1 and 2, check they're done

## Progress Tracking
File: `email-course-progress.json`
Structure:
  {
    "completed": [1, 2],
    "current": 3,
    "exercises_saved": ["audience-profile.md", "subject-line-workshop.md"]
  }
Update after each module completion.
```

**Why this works:**
- SKILL.md is pure orchestration — it never contains a single paragraph of lesson content
- The routing table maps every module to its files. No ambiguity about what loads when.
- curriculum-map.md holds the sequence and prerequisites. SKILL.md just reads it.
- Lesson files are student-facing: written for the student to read directly in their editor
- Exercise files are fillable: blank fields with instructions, not pre-filled answers
- Progress tracking prevents re-doing completed work and enables "what's next?"

### curriculum-map.md (excerpt)

```markdown
# Email Course — Curriculum Map

| Module | Name | Description | Deliverable | Prerequisite |
|--------|------|-------------|-------------|--------------|
| 1 | Email Foundations | List building, platform setup, deliverability basics | Audience profile document | None |
| 2 | Subject Lines | Psychology of opens, formulas, A/B testing | 20 tested subject lines | Module 1 |
| 3 | Welcome Sequences | First impressions, 5-email welcome series structure | Complete welcome sequence draft | Module 2 |
| 4 | Sales Emails | Urgency, proof, objection handling in email | 3 sales emails ready to send | Module 3 |
| 5 | Analytics & Optimization | Open rates, click rates, what to improve | Personal metrics dashboard | Module 4 |

## Recommended Order
Sequential. Each module builds on the previous. Do not skip.
```

### lessons/01-email-foundations.md (excerpt)

```markdown
# Module 1: Email Foundations

Welcome to the course. Before you write a single email, you need three things in place: a list, a platform, and an understanding of what makes email actually land in inboxes.

## Why Email Still Wins

Every social platform can change its algorithm tomorrow. Your email list? That's yours. No middleman. No algorithm. You press send, it arrives.

The numbers back this up. Email marketing returns $36 for every $1 spent on average. No other channel comes close...

## Building Your List From Zero

Here's the honest truth: buying a list is a waste of money. Those people didn't ask to hear from you, and they'll mark you as spam faster than you can say "unsubscribe."

Instead, you build it the right way...
```

Notice the tone: conversational, direct, written for the student. Not "This module covers..." but "Here's the honest truth..."

### exercises/audience-profile.md (excerpt)

```markdown
# Exercise: Audience Profile Builder

Build a detailed profile of your ideal email subscriber. This profile drives every email you'll write in this course.

## Instructions
Fill in each field. If you're unsure, write your best guess — you can refine later.

---

**Business name:** _______________
**What you sell:** _______________
**Your ideal subscriber's job title:** _______________
**Their biggest frustration right now:** _______________
**What they've already tried that didn't work:** _______________
**The transformation they want:** _______________
**Why they'd open YOUR email (not a competitor's):** _______________

## Example (good answer)
> **Their biggest frustration:** "I post content every day but nobody buys. I have followers but zero revenue from them."

## Done When
- [ ] Every field is filled (no blanks)
- [ ] "Why they'd open YOUR email" is specific to your business, not generic
- [ ] You could describe this person to a friend in 30 seconds
```

Notice: blank fields with underscores, clear instructions, an example of a good answer, and a "done" checklist. The student fills this in, not the agent.
