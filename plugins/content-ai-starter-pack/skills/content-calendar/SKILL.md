---
name: content-calendar
description: Build content plans and posting schedules using the Content Bucket-Pillar Matrix and Audience Archetypes system. Triggers on "content calendar", "plan my week", "what should I post", "content strategy", "content ideas".
user_invocable: true
---

# Content Calendar

You build content plans using the frameworks in `references/content-strategy.md`. Output a usable calendar with specific topics, formats, and hooks — not vague suggestions.

## Step 1: Load Context

Check `.coworker/index.md` for any existing context about the user's niche, audience, or goals.

## Step 2: Gather Inputs

Ask the user:

1. "What's your niche or topic area?" (Be specific — who do you serve and with what expertise?)
2. "Have you defined your content pillars? If yes, what are they? If not, I'll help you define them."
3. "How far out do you want to plan — 1 week, 2 weeks, 30 days?"
4. "How often are you posting? (Daily, 3x/week, weekdays only?)"

If they say they're just getting started, use the 10-Day Quick Start framework from `references/content-strategy.md`.

## Step 3: Define Pillars (if needed)

If they haven't defined pillars:

Prompt: "What are the 3-5 things your audience absolutely must understand or do to succeed in [their niche]?"

Help them test each pillar: Is it broad enough to write about for months? Focused enough that their audience immediately sees relevance? Aligned with their expertise?

## Step 4: Build the Content Matrix

Read `references/content-strategy.md` → Content Matrix section.

For each pillar, generate one idea per bucket (Futurism, Your Story, Actionable Advice).

Present as a table:

| Pillar | Futurism | Your Story | Actionable Advice |
|--------|----------|-----------|-------------------|
| [pillar] | [topic idea] | [topic idea] | [topic idea] |

## Step 5: Generate the Calendar

Map topics from the matrix onto the calendar.

**Calendar format per post:**

```
Day [X] — [Date]
Topic: [Specific topic]
Format: [Steps / Stats / Lessons / Story / Hot Take / etc.]
Hook: [One hook option — 9 words or fewer]
Bucket: [Futurism / Your Story / Actionable Advice]
Pillar: [Which pillar this serves]
```

**Rotation rules:**
- Don't use the same format two days in a row
- Vary buckets throughout the week (don't do all Actionable Advice)
- Mix easy and harder posts (Hot Takes take more thought than Steps posts)
- If posting 5 days/week: 2 Actionable Advice, 2 Your Story, 1 Futurism

## Step 6: Apply Magical Multipliers (if requested)

If the user wants more ideas from the same topics, run any topic through the 10 Magical Multipliers from `references/content-strategy.md`.

Present as: "Here are 10 angles on [topic]:" + the list.

## Step 7: Save Output

Save the calendar to:
```
output/content-calendar.md
```

Format:
```markdown
# Content Calendar — [Date Range]

Generated: [YYYY-MM-DD]
Pillars: [list]
Cadence: [X posts/week]

---

[Calendar entries]
```

Also update `.coworker/index.md` with a note that the calendar was generated and the date range it covers.

## Step 8: Offer Next Steps

After saving:
- "Want me to write the first post from this calendar?"
- "Should I expand any of these topics into a full ideas list using the Magical Multipliers?"
- "Want to run this plan against your audience archetypes to prioritize?"

## Rules

- Every calendar entry must have a specific topic, not a vague category
- Hook suggestions must be actual hooks (9 words or fewer), not descriptions of what a hook should do
- Don't generate more than 30 days without asking if the user wants to proceed
- If user is at Day Zero (no clients, no case studies), use the 10-Day Quick Start framework explicitly
