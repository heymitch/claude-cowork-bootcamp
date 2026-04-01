---
name: outline-builder
description: Build a structured content outline from a topic for any platform — newsletter, LinkedIn post, Twitter thread, YouTube script, or Substack note. Say "outline my content", "structure this", "build an outline", "outline my newsletter", "outline a LinkedIn post", or "outline a YouTube script".
user-invocable: true
---

# Outline Builder

Takes a topic and turns it into a structured outline you approve before writing begins.

## How to Run

- "Outline my [platform] about [topic]"
- "Structure this [content type]"
- "Build an outline for [topic]"
- "Outline my newsletter about [topic]"
- "Outline a LinkedIn post on [topic]"

## What the Agent Does

### 1. Determine Platform and Load Rules

Identify the platform from context or request.

Load the matching platform guide:
- Newsletter → `references/platforms/newsletter.md`
- LinkedIn → `references/platforms/linkedin.md`
- Twitter/thread → `references/platforms/twitter.md`
- Substack note → `references/platforms/substack-notes.md` (usually skip outline — too short)
- YouTube script → `references/platforms/youtube-script.md`

**Substack notes:** If the user asks to outline a Substack note, skip this skill and go directly to draft-writer. Notes are 1-3 sentences — an outline would be longer than the piece.

### 2. Confirm the Topic

If the user provides a topic, use it. If vague (just a word or phrase), ask one clarifying question:
- "What's your actual take on this? What's the argument you're making?"

Don't proceed until you have both a **topic** and an **angle** (the point they're making).

### 3. Recommend a Format

Read the platform guide. Based on the topic and angle, recommend a content format:

**Newsletter:**
- One strong opinion or story → Essay Style
- Multiple quick insights on one theme → Listicle
- Original idea + supporting links → Hybrid
- Sharing resources → Curated Links
- Answering reader questions → Q&A / Mailbag

**LinkedIn:**
- Personal story or lesson → Story arc (hook → tension → resolution → lesson)
- Opinion or take → Point-of-view post (bold claim → evidence → implication)
- Tactical advice → List post (numbered insights)

**Twitter thread:**
- Insight with evidence → Hook → Context → Insight → Proof → CTA
- Story → Hook → Setup → Turning point → Takeaway → CTA

**YouTube script:**
- Tutorial → Hook → Problem → Solution (steps) → Proof → CTA
- Story-driven → Hook → Setup → Conflict → Resolution → Lesson → CTA

Say: "I'd go with [format] because [one-sentence reason]. Sound good, or want a different format?" Let them override.

### 4. Build the Outline

Generate a structured outline following the chosen format from the platform guide.

The outline must include:
- **Hook:** 1-2 sentence draft of the opening (not placeholder — an actual draft hook)
- **Sections:** Each section with a title and 2-3 bullet points
- **Key points:** Specific arguments, examples, or stories per section
- **Transition notes:** How one section flows to the next
- **CTA:** What the reader/viewer should do at the end
- **Estimated length:** Word count (written platforms) or minutes (YouTube)

### 5. Get Approval

Show the outline and ask: "Does this structure work? Want me to change anything before I write the draft?"

Do not proceed to writing until they approve. On approval, hand off to the draft-writer skill.

## Rules

- Every outline needs a real draft hook, not "[Insert hook here]." Write an actual opening line.
- Never skip the approval step. Changing the outline now costs less than rewriting the draft.
- Keep outlines scannable. Bullets, not paragraphs. The user should read it in 30 seconds.
- Include estimated length so the user knows what they're getting.
- If the topic doesn't have enough meat for the chosen format, say so and suggest a shorter format.
- Platform rules from the guide are constraints, not suggestions. Follow them.
