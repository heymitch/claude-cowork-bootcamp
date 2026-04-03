---
name: social-content
description: Create social media posts from meeting insights or project details. Say "make social posts from meeting", "post about this project", "content from meeting", "LinkedIn post from this call", or "tweet about this project".
user-invocable: true
---

# Social Content from Meetings

Extract the valuable insight from a meeting and turn it into social content. Not "I had a great meeting" — the actual lesson, pattern, or idea worth sharing.

## How to Run

- "Make social posts from my meeting"
- "Post about this project"
- "LinkedIn post from this call"
- "Create content from this meeting"

## What the Agent Does

### Step 1: Gather inputs

Read `.coworker/index.md` first to identify the active client and check `projects/[client-name]/` for prior work.

Use what's available:
- Meeting transcript or structured summary (from transcript-extractor, saved in `projects/[client-name]/`)
- Proposal or project details (from proposal-builder, saved in `projects/[client-name]/`)
- User-provided notes or context

Read `training/references/business-blueprint.md` for voice profile, content style, and platform preferences.

### Step 2: Find the angle

Look for one of these in the meeting content:

1. **A problem worth talking about** — What was the client struggling with? Others probably have the same problem.
2. **An insight or pattern** — Did you notice something in the conversation that applies broadly?
3. **A lesson learned** — Did the meeting teach you something about your craft, your industry, or how you work?
4. **A contrarian take** — Did the conversation surface a common belief you disagree with?
5. **A framework or process** — Did you explain your approach in a way that could help others?

Pick the strongest angle. Ask if unsure: "I found a few angles — which one resonates?"

### Step 3: Write the posts

**LinkedIn post** (600-1200 characters):
- Hook: One line that stops the scroll. State the problem, the insight, or the contrarian take.
- Story: 3-5 short paragraphs. Set up the situation, share the insight, land the point.
- Takeaway: What the reader should do differently or think about.
- No hashtags in the body. 3 max at the bottom if you use them.

**X post** (under 280 characters):
- Punchy. One sharp observation or one-liner.
- If the idea needs more room, write a 3-4 tweet thread.

### Step 4: Review

Show both posts. Ask:
- "Which one do you want to post?"
- "Want me to adjust the angle or tone?"
- "Should I make this more personal or keep it general?"

### Step 5: Save

On approval:
- Save to `projects/[client-name]/YYYY-MM-DD-social-content-[client-name].md`
- Update `.coworker/index.md` with a one-liner (e.g., "GreenLeaf Consulting — social content created 2026-03-31")

## Rules

- NEVER write "I just had a great meeting with [client]." Nobody cares about your calendar.
- NEVER mention the client by name unless the user explicitly says to.
- NEVER reveal confidential project details, pricing, or business specifics.
- Extract the VALUE — the insight, the lesson, the pattern — and share that.
- Use the voice profile from `training/references/business-blueprint.md`. If none exists, write direct and conversational.
- No AI-tell phrases: "In today's landscape", "game-changer", "leverage", "streamline."
- Show for review before posting. Never post without approval.
- One post per platform. Quality over quantity.
- If the meeting didn't produce anything worth posting about, say so. Not every meeting is content.
- Always save to `projects/[client-name]/` and update `.coworker/index.md`.
