---
name: context-gatherer
description: Pull meeting context from all connected sources — Gmail, Slack, Docs, Fireflies, Calendar. Say "gather context for meeting with [person]" or "find everything about [person]" or "pull meeting context for [company]".
user-invocable: true
---

# Context Gatherer

Pull raw context about a person or company from every connected source. Run this before building a brief, or run it standalone when you need to know everything about someone fast.

## How to Run

- "Gather context for my meeting with [person]"
- "Pull meeting context for [person/company]"
- "Find everything about [person]"
- "What do we have on [company]?"

## What the Agent Does

### Step 1: Identify the Target
Get the person's name, email, and company. If the user only gives a name, ask for the company or email to narrow results.

Check `.coworker/index.md` — if the person or company matches an Active Project, note that context. It may contain relevant references or prior work.

### Step 2: Scan Available Connectors
Check which tools are available:
- Gmail tools
- Slack tools
- Google Drive/Docs tools
- Fireflies tools
- Calendar tools

If zero connectors are available, ask the user to paste or describe what they know. Build context from their input instead.

### Step 3: Pull from All Sources in Parallel

Speed matters. Pull from every available source at the same time — do not go one by one.

**Gmail (two passes):**
1. Email threads — search for emails to/from the person or company domain. Pull last 90 days.
2. Meeting recaps and summaries — use the patterns from `../meeting-prep/references/transcript-search-patterns.md`. Search for recap/summary emails mentioning the person or company. Most recording services (Fireflies, Fathom, Otter, Zoom, Read.ai) email recaps and summaries — not full transcripts. Search for "recap", "summary", and "meeting notes" before trying "transcript".

**Slack:**
- Search for the person's name and company name across channels you're in. Pull last 90 days of mentions and threads.

**Google Docs/Drive:**
- Search for documents shared with the person or containing their name/company. Pull document titles, last modified dates, and brief content summaries.

**Fireflies:**
- Search for meeting recaps with this person as a participant. Pull last 90 days.

**Calendar:**
- Search for past and upcoming meetings with this person. Pull meeting titles, dates, attendees, and descriptions.

### Step 4: Organize the Output

Structure the raw context by source:

```
## Context for [Person] @ [Company]
Gathered: [date and time]

### Gmail — Email Threads
[List of relevant email threads with dates and one-line summaries]

### Gmail — Meeting Recaps & Summaries
[List of recap/summary emails found, with dates and summaries]

### Slack
[Relevant mentions and thread summaries]

### Google Docs
[List of shared documents with titles and last modified]

### Fireflies
[Meeting summaries with dates]

### Calendar
[Past and upcoming meetings with dates and titles]

### Sources Not Available
[List which connectors were not connected]
```

### Step 5: Surface Highlights
After the structured dump, add a short "Highlights" section:
- Most recent interaction (date and type)
- Any open action items spotted
- Anything urgent or time-sensitive
- How much history exists (first interaction date if visible)

## Rules

- Pull from all available sources in parallel. Do not wait for one to finish before starting the next.
- If a source has no results, say "No results found" — do not skip the section.
- If a source is unavailable (not connected), note it in "Sources Not Available" — do not error or stop.
- Never make up context. If it's not in the data, it's not in the brief.
- Default to last 90 days. If the user asks for a different time range, use theirs.
- Keep raw context organized but complete. The brief-builder will distill it later.
- If zero connectors and zero user input, say so and stop. Don't generate an empty context dump.
