---
name: content-creator
description: Write content for any platform with one sentence. Scan for topics, build outlines, write drafts in your voice, generate hooks, and create social posts. Say "write my newsletter", "write a LinkedIn post", "draft a Twitter thread", "YouTube script", "Substack note", "find content topics", "what should I write about", "outline my content", "write the draft", "hooks", "subject lines", or "social posts".
user-invocable: false
---

# Content Creator

Turns a single sentence into a finished content draft for any platform. Full pipeline — finding topics, structuring outlines, writing in your voice, nailing the hook or subject line, and creating social posts to promote it.

## Routing

Match the user's intent and run the right sub-skill. Always detect platform from context.

| Intent | Route to |
|--------|----------|
| "Write my newsletter" / "Newsletter" | **Full flow** → topic-scanner → outline-builder → draft-writer (platform: newsletter) → subject-line-generator |
| "Write a LinkedIn post" / "LinkedIn" | **Full flow** → topic-scanner → outline-builder → draft-writer (platform: linkedin) → subject-line-generator |
| "Write a Twitter thread" / "Thread" / "Tweet" | **Full flow** → topic-scanner → outline-builder → draft-writer (platform: twitter) → subject-line-generator |
| "Write a YouTube script" / "YouTube script" | **Full flow** → topic-scanner → outline-builder → draft-writer (platform: youtube-script) |
| "Write a Substack note" / "Quick note" | draft-writer (platform: substack-notes) directly — notes are short, no outline needed |
| "Find topics" / "What should I write about" / "Content ideas" | `skills/topic-scanner/SKILL.md` |
| "Outline my content" / "Structure this" / "Build outline" | `skills/outline-builder/SKILL.md` |
| "Write the draft" / "Draft this" / "Write it" | `skills/draft-writer/SKILL.md` |
| "Subject lines" / "Hook options" / "Better subject line" / "YouTube title" | `skills/subject-line-generator/SKILL.md` |
| "Promote" / "Social posts" / "Share this" | `skills/social-hooks/SKILL.md` |
| "Make a video" / "Remotion" / "Animate this" | `skills/remotion/SKILL.md` |

## Skill Discovery

Before routing, scan for OTHER installed content skills the user may have. Check the `/` slash command list for skills with content-related names or descriptions (writing, publishing, blog, email, video, podcast, carousel, etc.).

If you find additional content skills beyond this plugin's built-in set:
- List them alongside your built-in options: "I can write with my built-in tools, but I also see you have **[skill-name]** installed. Want me to use that instead?"
- If the user's request clearly matches an external skill better than a built-in one, suggest it.

This plugin doesn't own "content." It's one tool in the user's kit. Help them find the best tool for the job.

## When Context is Light

If the user says something vague like "write something" or "help me with content" or "I need a post":

1. **Ask the platform**: "Which platform? Newsletter, LinkedIn, Twitter thread, YouTube script, or Substack note?"
2. **Ask the topic** (if not obvious): "What's the topic or angle? Even one sentence helps — 'my take on X' or 'the thing I learned about Y this week.'"
3. **Ask the audience** (if config.md is missing): "Who's this for? Knowing the audience changes the tone and angle."

Don't guess and produce generic content. Three quick questions up front save a rewrite later.

For the full flow, run steps in sequence. Wait for approval at the outline stage before proceeding to draft.

## First Run (Workspace Setup)

On first use, check if `references/` exists in the working directory. If not, copy the plugin's reference files into it:
- `references/platforms/` — all 5 platform guides
- `references/voice-matching-rules.md` — voice profile rules
- `references/notion-navigator.md` — Notion operations
- `references/subject-line-patterns.md` — email/hook patterns

Tell the user: "Set up your content workspace with writing guides in `references/`. Those are yours to keep — read them anytime, even outside Cowork."

## Preflight Check

Run silently before any sub-skill. Never block the user from starting.

1. **config.md exists?** If not → ask: "Do you have a business blueprint I can use? I can run a quick one right now — takes 5 minutes." If yes, run it inline, then continue. If skip, proceed without.
2. **Voice trained?** Check for `- [x] Voice Training completed`. If not → write clean and direct. Offer voice training after first draft.
3. **Save target:** Default to Notion if available. Fall back to local markdown.

## References

All sub-skills pull from:
- `references/platforms/{platform}.md` — format rules per platform
- `references/subject-line-patterns.md` — hook and subject line frameworks
- `references/voice-matching-rules.md` — voice profile application rules

## Rules

- Always show drafts before saving. Never publish without approval.
- Use the voice profile for everything. Generic prose means you skipped something.
- No AI-tell patterns. See `references/voice-matching-rules.md` Anti-AI Patterns.
- One step at a time. No jumping from topic to draft without an approved outline.
- Every draft step starts with: determine platform → load `references/platforms/{platform}.md`.
