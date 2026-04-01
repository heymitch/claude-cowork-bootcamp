---
name: action-tracker
description: Track and manage action items from your meetings. Say "track action items" or "what's open from my meetings" or "meeting action items" or "show overdue items".
user-invocable: true
---

# Action Tracker

Find, track, and update action items from past meetings. Know what you owe, what they owe, and what fell through the cracks.

## How to Run

- "Track action items"
- "What's open from my meetings?"
- "Meeting action items for [person]"
- "Show overdue items"
- "What do I owe [person]?"

## What the Agent Does

### Step 1: Determine Scope
Ask or infer what the user wants:
- **All open items** — scan everything
- **For a specific person** — filter to one contact
- **For a specific project** — filter by project name
- **Overdue only** — only show items past their deadline

Also check `.coworker/index.md` — Active Projects are a shortcut to knowing which people and projects to scan for first.

### Step 2: Scan Sources
Search connected sources for action items:

**Meeting transcripts (via Gmail):**
- Use patterns from `../meeting-prep/references/transcript-search-patterns.md`
- Look for action item sections in transcript emails
- Extract: what was agreed, who owns it, when

**Email threads:**
- Search for phrases like "I'll send", "can you", "let's plan", "by Friday", "action items", "next steps", "follow up"
- Cross-reference with recent emails to check if items were completed

**Past briefs in workspace:**
- Check `projects/` in the Coworker workspace for existing meeting briefs. If any exist, read the Open Items tables from each.
- Prioritize briefs for people/companies matching the current scope.

**Fireflies (if connected):**
- Pull action items directly from transcript metadata

### Step 3: Build the Action Items Table

For each item found:

| Item | Owner | Agreed On | Source | Status |
|------|-------|-----------|--------|--------|
| [Description] | [You/Them/Name] | [Date] | [Which meeting/email] | Pending / Done / Overdue |

**Status logic:**
- **Pending** — No evidence of completion, not yet past deadline
- **Done** — Found a follow-up email, document, or message that completes it
- **Overdue** — Past the agreed deadline with no evidence of completion

### Step 4: Sort and Display
Sort by urgency:
1. Overdue items (oldest first)
2. Pending items (oldest first)
3. Done items (most recent first) — show these collapsed or at the bottom

### Step 5: Offer Next Steps
After showing the table, ask:
- "Want to mark any of these as done?"
- "Want me to draft a follow-up for the overdue items?"
- "Want me to save this list?"

## Updating Items

When the user marks an item as done:
- Update the status in the tracking list
- If a brief exists for that person in `projects/`, update the Open Items table there too
- Note the completion date

## Saving Action Items

If the user wants to save the list:
- Save to `projects/action-items/YYYY-MM-DD-action-items.md` (or scoped to a person: `projects/[person-name]/YYYY-MM-DD-action-items.md`)
- After saving, update `.coworker/index.md` with a summary (e.g., "Action items last reviewed: 2026-03-15 — 3 overdue, 5 pending")

## Rules

- Only extract action items that are clearly stated. Do not infer vague commitments.
- Always attribute items to a source (which meeting, which email, which date).
- Cross-reference before marking something as done. "Looks done" is not done — find the evidence.
- If no connected sources are available, ask the user to paste meeting notes or list their open items manually.
- Default time range is last 90 days. User can adjust.
- Never make up action items. If the data doesn't contain clear commitments, say "No clear action items found."
- Show the source date for every item so the user can verify.
