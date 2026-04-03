# Social Repurposer

Take any newsletter (or long-form piece) and extract a full week of cross-platform social content. Uses the Extract → Compress → Expand method.

## Setup

1. Read `training/voice/voice-template.md` — REQUIRED before writing anything
2. Check `.coworker/index.md` for platform preferences and active campaigns
3. Read `references/platform-rules.md`

## What to Collect

Ask the writer (or pull from workspace):
- **The source content** — paste the newsletter, or give a file path
- **Platforms to target** — X/Twitter, LinkedIn, Substack Notes, or all three?
- **Priority** — does any specific section feel most shareable?

## Repurposing Process

### Step 1: Extract Standalone Ideas

Read the full piece. Identify every idea that can stand alone without the surrounding context. Mark them. A good newsletter typically contains:
- 10-20+ standalone tweet-sized ideas
- 3-5 LinkedIn post-worthy angles
- 1-2 thread structures
- 3-5 Substack Notes

### Step 2: Generate by Platform

**For X/Twitter — generate 10 posts:**
- 4 using Style 1 (2-liner / contrast)
- 3 using Style 2 (compressed paragraph)
- 3 using Style 3 (bulleted contrast list)

Each post ≤280 characters. Check the count. Preserve the voice exactly—do not sanitize, genericize, or make it sound like AI wrote it.

**For LinkedIn — generate 3 posts:**
- 1 using the Contrarian Take format
- 1 using the Story + Lesson format
- 1 using the Numbered List format

Each post 1,300-1,800 characters. Single-sentence line breaks. No hashtags in body.

**For Substack Notes — generate 3 notes:**
1-3 sentences each. Standalone. Not a teaser—a complete micro-thought that stands without the newsletter.

**Optional: Thread structure**
If a clear sequential argument exists in the source, output a 5-12 tweet thread. Hook tweet first. No "1/10" numbering. End with CTA.

### Step 3: Voice Check

Before finalizing, compare against the voice template. Flag any posts that:
- Sound generic or AI-polished
- Lost the specific details from the original
- Changed the writer's actual opinion or framing

Rewrite flagged posts before presenting.

## Output Format

Present grouped by platform. For each post, include the character/word count.

```
--- X / TWITTER ---

[1] (Style: 2-liner | 142 chars)
[post text]

[2] (Style: Compressed paragraph | 278 chars)
[post text]

...

--- LINKEDIN ---

[1] (Format: Contrarian Take | 1,420 chars)
[post text]

...

--- SUBSTACK NOTES ---

[1] (87 chars)
[note text]

...
```

## Save Output

Save to `output/repurposed/[YYYY-MM-DD]-[source-slug]-social.md`
Note in `.coworker/index.md` that repurposing was completed for this issue.
