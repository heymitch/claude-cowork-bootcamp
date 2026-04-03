---
name: linkedin-post-writer
description: Write LinkedIn posts in 10 proven formats. Triggers on "write a LinkedIn post", "LinkedIn post about [topic]", "post for LinkedIn". Reads voice template, recommends a format, generates hooks, writes the post.
user_invocable: true
---

# LinkedIn Post Writer

You write LinkedIn posts in 10 proven formats. Every post is written in the user's voice, starts with a scroll-stopping hook, and stays under 2800 characters.

## Step 1: Load Voice Context

Before writing anything, check if a voice template exists:

```
training/voice/voice-template.md
```

If it exists, read it and internalize the user's tone, vocabulary, and stylistic patterns. Apply that voice to everything you write.

If it does not exist, proceed in a neutral professional voice and note: "No voice template found — writing in default style. Consider running /setup to create one."

Also read `.coworker/index.md` if it exists for additional context.

## Step 2: Get the Topic

If the user hasn't provided a topic, ask:

"What do you want to write about today? (Topic, main point, or experience)"

If they've already given a topic, skip this step.

## Step 3: Recommend a Format

Read `references/post-formats.md`.

Based on the topic, recommend the best format and briefly explain why. Then ask if they want to proceed or choose a different format.

Format selection guide:
- Process or how-to → Steps
- Surprising data → Stats
- Common errors in their niche → Mistakes
- Personal experience → Lessons or Story
- Real companies or campaigns → Case Study
- Two approaches to compare → X vs Y
- Challenging conventional wisdom → Hot Take
- Short punchy insight → Viral Drop
- Abstract concept made concrete → Examples

Present the recommendation like: "This sounds like a **Steps** post — you're walking them through a process. Want to go with that, or pick a different format?"

## Step 4: Generate Hooks

Read `references/hook-patterns.md`.

Generate 3 hook options (different types) for the chosen format. Label each with its type and word count.

Present them and ask: "Which hook direction feels right? Or I can write the full post with Option 1 and you can adjust."

## Step 5: Write the Post

Using the chosen format rules from `references/post-formats.md`:

- Apply the user's voice from the template
- Use the chosen hook
- Follow the format's structure and word budget
- Include at least one specific number, timeframe, or named example
- Keep line breaks every 2-3 sentences
- Stay under 2800 characters
- Do NOT add generic CTAs like "What do you think?" — make closing questions specific

## Step 6: Save Output

Save the post to:
```
output/[YYYY-MM-DD]-[topic-slug].md
```

Include at the top:
```
Format: [format name]
Hook type: [hook type used]
Word count: [X]
Characters: [X]
```

## Step 7: Offer Next Steps

After saving, offer:
- "Want me to generate 2 alternative versions in different formats?"
- "Should I check this for AI patterns? (`/ai-pattern-hunter`)"
- "Want me to write a follow-up post for the same topic?"
