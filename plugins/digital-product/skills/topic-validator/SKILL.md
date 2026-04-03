---
name: topic-validator
description: Validate a product idea with 3 test social posts before building anything. Triggers — "validate this idea", "test my product idea", "validate before building"
user-invocable: true
---

# Topic Validator

## Process

### Step 1: Get the Idea

Take a product idea from idea-finder output or direct user input. Check `.coworker/index.md` for any active product context. Confirm the topic before generating posts.

### Step 2: Load Voice (If Available)

Check `training/voice/voice-template.md` — if it exists, use the voice profile when writing the posts.

### Step 3: Generate 3 Test Posts

Each post tests a different angle:

**Post 1 — "Here's What I Learned"**
Share one specific insight from the topic. Teach something useful. Do not mention a product. Tests whether the topic gets engagement.

**Post 2 — "Would You Want This?"**
Describe the potential product. What it covers, who it is for, what they would learn. Ask for feedback. Tests whether explicit demand exists.

**Post 3 — "The Contrarian Take"**
Challenge a common belief about the topic. Bust a myth. Take a strong position. Tests whether the topic sparks conversation.

### Step 4: Format for Platforms

Write each post in two versions:
- **LinkedIn** — 800-1200 characters, short paragraphs, hook in the first line
- **X/Twitter** — under 280 characters or a 2-3 tweet thread

### Step 5: Explain the Signals

Tell the user what to watch for after posting:

- Post 2 gets comments asking "where can I buy this?" = strong demand, build it
- Post 1 gets engagement but Post 2 is flat = people like the topic but don't see it as a product yet, refine the angle
- Post 3 sparks debate = energy here, use the contrarian angle in positioning
- All 3 are flat = try a different topic or angle

### Step 6: Save and Recommend Next Step

Save posts to `projects/[product-name]/validation-posts.md` in the Coworker workspace. Recommend coming back after one week of posting to run outline-builder with the validated topic.

## Handoff

After posts are saved:
1. Update `projects/[product-name]/product-config.md` — check "Demand validated".
2. Update `.coworker/index.md` — note "Validation posts created [date]" next to the product.
3. Say: "Posts saved. Publish them over the next week and watch for signals. When you're ready, say **outline my product** to structure the content."

## Rules
- Always generate exactly 3 posts with exactly 3 angles.
- Posts must be publish-ready, not drafts.
- Never use the word "validate" or "test" in the posts themselves.
- Use voice from `training/voice/voice-template.md` if available.
- LinkedIn under 1200 characters. X under 280 characters per tweet.
- Always write to `projects/[product-name]/` — never to workspace root.
