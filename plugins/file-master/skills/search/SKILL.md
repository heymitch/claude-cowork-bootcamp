---
name: searching-index
description: Searches the Coworker knowledge index for files by type, tags, content, or date. Returns matching entries with paths so other skills or the user can load them. Trigger phrases include "search for", "find", "what do you know about", "show me my", "any files about", "look up".
---

# Search

Query the Coworker index. Find files by type, tags, keywords, or date.

## Workflow

```
Progress:
- [ ] Parse the search query
- [ ] Read .coworker/index.md
- [ ] Match entries
- [ ] Present results
- [ ] Optionally load a result
```

## Step 1: Parse Query

Understand what the user wants:

| Query | Interpretation |
|-------|---------------|
| "find my voice samples" | type = voice-sample |
| "what do you know about Acme Corp" | tags contain "acme" OR content search |
| "show me everything from this week" | date filter: last 7 days |
| "any prompts for meeting prep" | type = prompt, tags contain "meeting" |
| "search for linkedin posts" | type = voice-sample, tags contain "linkedin" |

## Step 2: Read Index

Read `.coworker/index.md`. Parse each entry:
```
- `path` | type | tags | date
```

## Step 3: Match

Filter entries by the parsed query. Match against:
1. **Type** — exact match on the type field
2. **Tags** — any tag contains the search term
3. **Path** — filename contains the search term
4. **Date** — within the specified range

If the query is broad ("what do you know about X"), search across all fields.

If zero matches in the index, offer to search file contents directly: "Nothing in the index matches. Want me to scan the actual files for mentions of X?"

## Step 4: Present Results

Show a clean table:

| File | Type | Tags | Date |
|------|------|------|------|
| `training/voice/linkedin-ai-post.md` | voice-sample | linkedin, ai | 2026-03-15 |
| `training/references/acme-notes.md` | reference | acme, client | 2026-03-10 |

**X results found for "query"**

## Step 5: Load (optional)

If the user wants to see a result: "Show me that Acme notes file" — read and display it.

If another skill is searching (Content Creator looking for voice samples), return the paths silently so the skill can load them.

## Quick Queries

For common patterns, respond fast without a full table:

- "How many voice samples do I have?" → count type=voice-sample, respond: "You have 7 voice samples indexed."
- "When did I last ingest something?" → check dates, respond: "Last ingest was March 28 — 3 files."
- "What types of files do I have?" → list unique types with counts.
