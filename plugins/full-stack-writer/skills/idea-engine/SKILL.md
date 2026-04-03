# Idea Engine

Generate newsletter and content ideas that never run out. Uses the 3-step Endless Idea System from the CNC framework.

## Setup

1. Check for voice template at `training/voice/voice-template.md` — load if present
2. Check `.coworker/index.md` for niche, content pillars, and audience context
3. Read `references/idea-frameworks.md` before proceeding

## What to Collect First

Ask the writer (or pull from workspace context):

- **Main topic / niche** — what is your newsletter about?
- **Content pillars** — do you have 3-5 recurring themes? (Help define if not)
- **Target reader** — who specifically? (role, experience level, situation)
- **Starting point** — do you have a topic seed, or are we generating from scratch?
- **Analytics data** — any posts that performed well recently? (optional but powerful)

If context is already in `.coworker/index.md`, skip questions that are already answered.

## Idea Generation Process

### Phase 1: Run the 10 Magical Ways

Take the writer's topic (or their strongest content pillar) and generate all 10 frames:

Tips / Stats / Steps / Lessons / Benefits / Reasons / Mistakes / Examples / Questions / Personal Stories

Output: 10 specific, usable newsletter titles — not vague descriptions. Each title should be a real subject line draft.

### Phase 2: Audience Archetype Expansion

Pick the 3-4 strongest ideas from Phase 1. For each, generate 3 audience-specific variations by swapping the reader archetype.

Keep archetypes relevant to the writer's actual niche. Don't force demographics that don't fit.

### Phase 3: Sub-Topic Branching (if writer wants more)

Take the top 5 ideas and generate 2-3 adjacent sub-topic variations for each. These should feel like natural extensions — topics the same reader also cares about.

## Output Format

Present ideas in batches, not walls of text:

```
PILLAR: [Content Pillar Name]

CORE TOPIC: [Topic]

10 WAYS:
1. Tips — [Specific title]
2. Stats — [Specific title]
3. Steps — [Specific title]
...

TOP 3 EXPANDED:
[Title A]
  - For [Audience 1]: [Variation]
  - For [Audience 2]: [Variation]
  - For [Audience 3]: [Variation]
```

After the batch, ask: "Want me to expand any of these into a full newsletter outline, or keep generating ideas?"

## Pinpoint Check

Before finalizing the top picks, run the Pinpoint Writing filter (in references) on the writer's top 2-3 choices. Flag any that are still too broad.

## Save Output

If the writer approves a list, save to `output/idea-bank.md` with today's date and pillar tag. Update `.coworker/index.md` if new pillars were defined.
