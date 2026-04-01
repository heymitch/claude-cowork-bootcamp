---
name: subject-line-generator
description: Generate hook options for any platform — email subject lines, LinkedIn hooks, tweet openers, YouTube titles. Say "subject lines", "hook options", "better subject line", "LinkedIn hook", "YouTube title", "tweet opener", or "generate hooks".
user-invocable: true
---

# Hook Generator

Generates 5 hook options for any platform. Email subject lines, LinkedIn first lines, tweet openers, YouTube titles — each using a different proven pattern. You pick the winner.

## How to Run

- "Write subject lines for my newsletter"
- "Give me LinkedIn hook options"
- "YouTube title options"
- "Tweet opener ideas"
- "Generate hooks for this content"
- "I need a better subject line"

## What the Agent Does

### 1. Determine Platform and Load Rules

Identify the platform from context or request.

Load the matching platform guide:
- Newsletter → `references/platforms/newsletter.md` + `references/subject-line-patterns.md`
- LinkedIn → `references/platforms/linkedin.md` (hook = first line before "see more")
- Twitter → `references/platforms/twitter.md` (hook = first tweet in a thread)
- YouTube → `references/platforms/youtube-script.md` (hook = title + first 30 seconds)
- Substack note → Usually skip — notes ARE the hook

**Format constraints by platform:**
- Newsletter subject lines: under 60 characters, no spam triggers
- LinkedIn hooks: 1 punchy line, ends with a pattern-interrupt or bold claim
- Tweet openers: under 280 characters, standalone value even without the thread
- YouTube titles: 50-70 characters, front-load the most important word

### 2. Get the Input

Needs one of these:
- A full draft (best — more context = better hooks)
- A topic + angle (good — enough to work with)
- A topic only (okay — will ask for the angle)

If given nothing, ask: "What's the content about? Give me the topic and your take on it."

### 3. Load Hook Patterns

Read `references/subject-line-patterns.md` for the full pattern library.

### 4. Generate 5 Options

Write one hook using each of 5 different patterns (pick the most relevant to the content):

1. **The Number** — "7 things I learned about X"
2. **The Question** — "What if your Z was wrong?"
3. **The Curiosity Gap** — "I almost quit X. Here's what changed."
4. **The Direct Promise** — "How to X without Y"
5. **The Personal Story** — "I lost $X doing Y."
6. **The Contrarian** — "Stop doing X."
7. **The News Hook** — "[Event] + what it means for you"

For each option:

```
**[Number]. "[Hook]"**
Pattern: [Pattern name]
Why it works: [One sentence — what psychological trigger does this pull?]
```

Adapt the format to the platform: newsletter = subject line style, LinkedIn = first-line style, YouTube = title style, Twitter = opening tweet style.

### 5. Recommend the Top Pick

After listing all 5, add:

```
**My pick: #[X]**
[One sentence explaining why this one is the strongest for this specific content.]
```

### 6. Offer Complement

**Newsletter:** "Want preview text for the winner? It's the line that shows next to the subject in the inbox — basically a second subject line."

**LinkedIn:** "Want a second-line option? The line after the hook sets up whether people hit 'see more.'"

**YouTube:** "Want a thumbnail text option to pair with this title?"

**Twitter:** "Want a thread structure for this opener?"

## Rules

- All 5 options must use different patterns. No two hooks from the same framework.
- Match every hook to this specific content. No generic lines that work for any topic.
- The recommendation must have a real reason. "Curiosity gap works here because the story has a surprising twist" — not just "it's the strongest."
- If the content is weak, say so: "These would be stronger if the draft had a clearer angle. Want help with that first?"
- Platform character limits are hard constraints. Don't suggest anything that violates them.
