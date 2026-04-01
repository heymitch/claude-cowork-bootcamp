---
name: newsletter-outliner
description: Build a publish-ready newsletter outline with editorial intelligence. Assesses your topic, chooses the angle, picks the format, drafts a real hook, and builds a full section breakdown — the way a senior editor would before assigning a story. Say "outline my newsletter", "newsletter outline for [topic]", "outline this", "what should I write about [topic]".
user-invocable: true
---

# Newsletter Outliner

You type a topic. This skill produces a publish-ready newsletter outline with a real hook, full section breakdown, transition notes, and a CTA — all calibrated to your voice and audience.

Not a template. An editorial assessment followed by a structural decision.

## Workflow

### Step 1: Load Voice and Audience Context

Read silently before doing anything:

1. Check `.coworker/index.md` for voice samples in `training/voice/`
2. If `training/voice/voice-template.md` exists — load it. This is how the writer sounds.
3. Check for `CLAUDE.md` audience/voice sections — who reads this newsletter, what do they care about
4. If no voice data exists — proceed, but flag it: "I don't have your voice profile yet. This outline will be structurally solid but the hook and tone won't be calibrated to you. Run voice training to fix that."

### Step 2: Editorial Assessment

Before building anything, work through these four questions. This is what a good editor asks before assigning a story:

**Q1: Why now?** What happened this week, this month, in this industry that makes this topic timely? If the user gave context, extract the timeliness. If not, ask: "What made you think of this today?"

**Q2: What's the one-sentence argument?** Not the topic. The TAKE. Not "AI in content creation" but "Most people's AI workflow is backwards — they generate first and edit later, when they should be editing the prompt and generating last." If the user gave a take, use it. If they gave a bare topic, propose 2-3 angles and wait for them to choose.

**Q3: Who's this for?** The specific reader. Not "content creators" but "the writer who's been using ChatGPT for 6 months and still copy-pastes every output." If audience data exists in voice template or CLAUDE.md, use it. If not, ask.

**Q4: What does the reader DO at the end?** Reply, try something, change a behavior, click a link. The CTA should be clear before the outline is written.

Present the assessment:
```
EDITORIAL ASSESSMENT

Why now: [timeliness]
Argument: [one-sentence take]
Reader: [specific person]
After reading: [what they do]
```

Get approval on this before building the outline. If the take is weak, say so: "This reads more like a topic than an argument. What's your actual opinion on this?"

### Step 3: Choose the Format

Based on the editorial assessment, choose the best newsletter format:

| Format | When to Use |
|--------|------------|
| **Essay** | One strong opinion or story that builds to a conclusion |
| **Listicle** | Multiple quick insights on one theme (5 mistakes, 7 tools, etc.) |
| **Hybrid** | Original idea + supporting examples or links |
| **Case Study** | Deep analysis of one example that illustrates a principle |
| **How-To** | Step-by-step tactical guide (only when the topic is genuinely procedural) |

State the choice and why: "This is an essay — the argument lives in a single thread, not a list of disconnected points."

Let the user override if they want a different format.

### Step 4: Build the Outline

Generate the full outline:

```markdown
# [Newsletter Title]

## Hook
[Actual draft opening — 2-3 sentences. Starts in the middle of a thought.
Conversational. Matches writer's voice if template exists. NOT "In today's
rapidly evolving landscape." NOT a question. A statement that creates tension.]

## Section Breakdown

### [Section 1 Title]
- Argument this section carries: [one sentence]
- Key points: [2-3 bullets]
- Example or evidence: [specific]
→ Transition to Section 2: [how it connects]

### [Section 2 Title]
- Argument: [one sentence]
- Key points: [2-3 bullets]
- Example or evidence: [specific]
→ Transition to Section 3: [how it connects]

### [Section 3 Title]
- Argument: [one sentence]
- Key points: [2-3 bullets]
- Example or evidence: [specific]

## CTA
[Specific call to action calibrated to the audience — reply prompt,
action step, link, or question they carry into the next day]

## Meta
- Estimated word count: [X words]
- Estimated read time: [X minutes]
- Format: [essay/listicle/hybrid/case study/how-to]
```

### Step 5: Get Approval

Show the outline. Ask: "Does this structure work? Want me to change the angle, swap sections, or adjust the hook before we write?"

**Do not write the draft.** This skill produces the outline only. If the user wants to proceed to writing, suggest: "Ready to draft? Say 'write the draft from this outline.'" Hand off to content-creator's draft-writer or let them write it themselves.

## Rules

- **The hook is a REAL draft, not placeholder text.** Write an actual opening line that starts in the middle of a thought.
- **The editorial assessment is mandatory.** Don't skip it even if the user gives a detailed brief. The assessment catches weak angles before they become weak drafts.
- **Format choice is a judgment call, not a user decision.** Recommend the format, explain why, let them override. But don't ask "what format do you want?" — that's your job.
- **Every section carries an argument.** Not just "talk about X." What's the POINT of this section? What does the reader walk away knowing?
- **Transition notes between sections.** The outline should read as a logical flow, not a list of disconnected topics.
- **If the topic is thin, say so.** "This is a Substack Note, not a newsletter. Want me to draft it as a short post instead?"
- **Stop at the outline.** This skill does not write the full draft. It produces the blueprint and hands off.
