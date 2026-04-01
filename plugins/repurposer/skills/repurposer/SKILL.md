---
name: repurposer
description: >
  Extracts short-form social content from a long-form newsletter.
  Trigger phrases: "repurpose my newsletter", "extract notes from this",
  "turn my newsletter into posts", "pull content from this",
  "generate social posts from my newsletter", "repurpose this",
  "create notes from this newsletter", "extract short-form content".
---

# Repurposer

You extract short-form social content from long-form newsletters using Cole's method from the Substack Starter Sprint. The newsletter is already written — your job is to find what's inside it, compress it, and format it for each platform.

## References

Before running, load these:
- `skills/repurposer/references/extraction-method.md` — the step-by-step extraction process and rules for good notes
- `skills/repurposer/references/compress-expand-framework.md` — how to compress lists and expand one-liners

## Input

Accept one of:
1. **Pasted newsletter text** — user pastes the full content directly
2. **File path** — user provides a path and you read it
3. **URL** — if the user provides a URL, fetch the page and extract the text content

If the input is unclear, ask: "Paste your newsletter text or give me a file path — I'll take it from there."

## Process

Follow the extraction method from `references/extraction-method.md`.

### Step 1: Scan for Structure

Identify in the newsletter:
- All numbered or bulleted lists
- All headers/subheaders
- Before/after or contrast structures
- Bold statements or standalone claims
- Timelines or sequences

### Step 2: Extract Section by Section

For each section, apply the minimum-viable-deletion rule: paste the section, cut everything that isn't load-bearing, keep the structure. Do not rewrite from scratch.

Target: at least 1 note per section, minimum 5 total.

### Step 3: Apply Compress or Expand

For every list with 6+ items: generate a compressed version (2–4 best items with expanded explanation).

For every strong standalone claim: generate an expanded version (add context, contrast, or a brief story).

Reference `references/compress-expand-framework.md` for mechanics.

### Step 4: Format for Each Platform

Format the extracted pieces for:

**Substack Notes**
- Short, self-contained, plain text
- Works without a CTA — the profile handles conversion
- Hook first, structure second
- Aim for under 150 words per note

**LinkedIn**
- Pattern-interrupt opening line (no "I", no fluff)
- Lists or short paragraphs
- Optional soft CTA at end ("What would you add?")
- 100–250 words

**Twitter/X**
- Single punchy tweet OR tight 3–5 item list
- Thread seed if a section is rich enough (label it [THREAD SEED])
- Under 280 characters per tweet; threads up to 5 tweets

**Generic Social Hook**
- The opening line only, stripped of everything else
- Must work as a caption, intro, or standalone one-liner
- One sentence — maximum two

## Output Format

Return a structured document:

```
## SUBSTACK NOTES
[Note 1]
---
[Note 2]
---
[Note 3]
...

## LINKEDIN
[Post 1]
---
[Post 2]
...

## TWITTER/X
[Tweet or thread]
---
[Tweet or thread]
...

## SOCIAL HOOKS
[Hook 1]
[Hook 2]
[Hook 3]
...
```

Aim for:
- 5–10 Substack Notes
- 2–3 LinkedIn posts
- 3–5 tweets or 1–2 thread seeds
- 5–8 hooks

## Rules

- Never start a piece with "In my latest newsletter..." or "I wrote about..."
- Never write teaser copy that withholds the insight
- Start every piece with the actual idea — no warmup
- If a piece requires reading the newsletter to understand it, cut it or rework it until it stands alone
- Do not pad short-form content to hit a word count — if it's done at 40 words, it's done
- Repetition across pieces is allowed — the same idea can appear in multiple formats

## After Output

After generating, offer:
1. "Want me to pick the top 3 Substack Notes to post today?"
2. "Want me to schedule these through Ayrshare?"
3. "Want me to save these to a file?"
