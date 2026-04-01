---
name: brief-builder
description: Build a structured meeting brief from raw context or your own notes. Say "build meeting brief for [person]" or "create brief for [person]" or "brief me on [person]".
user-invocable: true
---

# Brief Builder

Take raw context (from context-gatherer or pasted by the user) and assemble a clean, actionable meeting brief.

## How to Run

- "Build meeting brief for [person]"
- "Create brief for [person]"
- "Brief me on [person]"
- "Turn these notes into a meeting brief"

## What the Agent Does

### Step 1: Get the Raw Context
Check if context-gatherer already ran. If yes, use that output. If no, ask the user to either:
1. Run context-gatherer first ("Want me to pull context from your connected sources?")
2. Paste their own notes, emails, or context

### Step 2: Load the Template
Read `../meeting-prep/references/brief-template.md` for the standard brief format. Follow that structure exactly.

### Step 3: Assemble the Brief

Fill in each section from the raw context:

- **Header block** — Meeting details from calendar or user input (who, when, where, attendees)
- **Relationship summary** — Piece together from email history and meeting records. When did you first connect? What have you done together?
- **Last interaction** — Find the most recent touchpoint (email, call, meeting). Note the date, format, and what was discussed.
- **Open items** — Extract action items from past meetings and emails. For each, note who owns it, when it was agreed, and whether it appears to be done (check for follow-up emails).
- **Recent context** — Summarize what's happened since the last interaction. Group by source (email, Slack, docs).
- **Key documents** — List relevant shared documents with links and one-line descriptions.
- **Their recent activity** — If any public info was found (LinkedIn, company news), include it.
- **Talking points** — Generate 3-5 suggested topics based on open items and recent context. For each, explain why it matters and what to say.
- **Watch for** — Flag sensitive topics, unresolved tensions, or opportunities. Explain the background.
- **Sources used** — List which connectors contributed data and how many items each found.

### Step 4: Flag Urgency
If any open items are overdue or any context suggests time pressure, add a bold note at the top of the brief:
**Heads up: [description of urgent item]**

### Step 5: Show for Review
Display the completed brief. Ask: "Anything to add or change before I save this?"

### Step 6: Save
Save the brief as a markdown file in the Coworker workspace.

**Path logic:**
- If the person or company matches an active project in `.coworker/index.md`, save to `projects/[project-name]/[date]-brief-[person-name].md`
- If no matching project exists, save to `projects/[person-name]/[date]-brief-[person-name].md` (create the folder if needed)
- Name format: `YYYY-MM-DD-brief-[person-name].md` (e.g., `2026-03-15-brief-sarah-kim.md`)

After saving, update `.coworker/index.md`:
- Under Active Projects, find or add a one-liner for this person/company (e.g., "Sarah Kim @ Lightwave — meeting brief saved 2026-03-15")
- Keep it a summary count or one-liner, not a full file path list

## Handling New Contacts

If the person is someone you've never interacted with before (no email history, no meetings, no documents):
- Say so clearly: "This looks like a new contact — I don't have any interaction history."
- Focus on what is available: meeting details from calendar, any public info, what the user provides
- Ask: "What do you know about this person? Even a few sentences helps me build a better brief."

## Rules

- Follow the template format from references/brief-template.md exactly. Do not skip sections.
- If a section has no data, write "No data found" — never leave it blank, never invent content.
- Always show the brief before saving. Never auto-save without user review.
- Flag overdue items and urgent context at the top.
- Keep talking points specific and actionable. Not "discuss project status" but "Ask about the Q1 deliverable — it was due Feb 15 and no update yet."
- Source everything. Every claim in the brief should trace back to a specific email, message, or document.
- Never hallucinate relationship details, meeting history, or action items.
- Always update `.coworker/index.md` after saving.
