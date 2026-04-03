# Editorial Calendar

Build a 90-day content calendar: 12 newsletter topics + supporting social content for each week. Grounded in content pillars and audience archetypes.

## Setup

1. Check `.coworker/index.md` for niche, pillars, audience, and publishing history
2. Read `references/calendar-framework.md`
3. Voice template not required — this is planning, not writing

## What to Collect

Before generating, gather (pull from workspace or ask):

- **Niche and newsletter topic** — what is this writer covering?
- **Content pillars** — 3-5 recurring themes (help define if they don't have them)
- **Primary reader** — specific description
- **Publishing frequency** — how often do they plan to publish? (default: 1x/week)
- **Newsletter type** — Original Thinking, Curation, or Hybrid?
- **Anything off-limits** — topics they don't want to cover or have already covered recently

If pillars don't exist, run a quick pillar-building exercise first:
- "Name 3-5 topics inside [their niche] that you could write about forever and never run out of ideas."
- Confirm each pillar has genuine depth for 12+ issues.

## Calendar Generation Process

### Step 1: Core Expansion

For each pillar, apply the 10 Magical Ways from the framework. Generate candidate headlines — not abstract descriptions, actual newsletter title drafts.

### Step 2: Sequence into 12 Weeks

Arrange 12 newsletter topics across 12 weeks:
- Balance across pillars (don't do 6 consecutive weeks on the same theme)
- Open with a high-confidence topic (something the writer knows cold and readers will immediately value)
- Mix formats: some tips-based, some steps-based, some story/personal, some data-driven
- Space out "personal story" entries — effective, but lose impact if overused

### Step 3: Supporting Social Content

For each of the 12 weeks, generate 7-8 social post concepts tied to the newsletter topic:
- Vary: question, stat, tip, story, list, quote, carousel, thread concept
- Each should thematically link to the newsletter but stand alone without it
- Match the archetype of that week's newsletter

### Step 4: Frequency Recommendation

Based on their niche and newsletter type, recommend the right cadence and explain why. Use the "information speed" framework from the reference doc.

## Output Format

```
90-DAY CONTENT CALENDAR: [Newsletter Name]
Primary Reader: [description]
Publishing Cadence: [recommended]

---

WEEK 1
Newsletter: "[Headline]"
Pillar: [Content Pillar]
Format: [Original Thinking / Curation / Hybrid]
Audience Archetype: [specific]
Sub-topic: [specific]
Description: [2-3 sentences]

Supporting Content (7-8 posts):
1. [Format: text] — [concept]
2. [Format: carousel] — [concept]
3. [Format: question] — [concept]
4. [Format: stat] — [concept]
5. [Format: story] — [concept]
6. [Format: tip] — [concept]
7. [Format: thread] — [concept]

---

WEEK 2
...
```

After the full 12-week calendar, include:
- Batching recommendation (Option A or B based on their situation)
- 4-week review prompt (what to check, what to adjust)
- Top 3 "write first" picks from the list — based on confidence and audience warmth

## Save Output

Save to `output/editorial-calendar.md`
Update `.coworker/index.md` with the calendar date range and confirmed pillars.
