---
name: meeting-prep
description: Never walk into a meeting cold. Prep for meetings, gather context, build briefs, track action items, write follow-ups. Say "prep me for my meeting with [person]", "brief me on [person]", "gather context", "find everything about [person]", "action items", "what's open from my meetings", "write follow-up", or "meeting recap".
user-invocable: true
---

# Meeting Prep

Your meeting command center. Pulls context from Gmail, Slack, Docs, and Fireflies, builds a brief, tracks action items, and writes follow-up emails.

## How to Run

Tell me what you need and I'll route to the right sub-skill.

## Preflight (Run Silently Every Time)

1. **Workspace context** — Read `.coworker/index.md` to check for active projects, references, and any existing meeting briefs or notes. Note any clients or projects listed under Active Projects — these inform person/company matching.
2. **Connectors** — Scan available tools (Gmail, Slack, Drive, Fireflies, Calendar). Note what's connected. If zero: "No connectors found. I can still work with pasted notes, or I can walk you through connecting Gmail — it takes two clicks."
3. **Detect the user's timezone** — Before any calendar operation, pull the user's Google Calendar settings and extract the `timeZone` field from the calendar metadata. This is the authoritative source. Store it for the rest of the session and use it for **every** calendar read AND write. Never default to `America/New_York` or any hardcoded timezone. If the calendar response doesn't include a timezone, ask the user directly — don't guess.
4. **User identity** — As you gather context, infer the user's name, role, and company from their email signatures, calendar entries, and Slack profiles. No config file needed — the skill learns who you are from your data.

## Routing

| User says | Route to |
|-----------|----------|
| "Prep me for my meeting" / "Brief me on [person]" | context-gatherer then brief-builder (full flow) |
| "Gather context" / "Find everything about [person]" | context-gatherer |
| "Build a brief" / "Create brief for [person]" | brief-builder |
| "Action items" / "What's open from my meetings" | action-tracker |
| "Write follow-up" / "Meeting recap" / "Recap email" | follow-up-writer |

For the full flow ("prep me" / "brief me"), run context-gatherer first, then pass the output to brief-builder. Do not ask the user to run them separately.

## Sub-Skills

- `../context-gatherer/SKILL.md` — Pull raw context from all connected sources
- `../brief-builder/SKILL.md` — Assemble a structured meeting brief
- `../action-tracker/SKILL.md` — Find and track open action items
- `../follow-up-writer/SKILL.md` — Draft post-meeting recap emails

## References

- `references/brief-template.md` — Standard brief format and example
- `references/connector-guide.md` — How to set up each connector
- `references/transcript-search-patterns.md` — Gmail search patterns for finding meeting transcripts

## Rules

- Route based on intent. Don't ask "which sub-skill?" — figure it out from what they said.
- Always run preflight silently. Only speak up if zero connectors.
- For ambiguous requests, default to the full flow (context-gatherer then brief-builder).
- Never load reference files unless a sub-skill needs them. Keep context lean.
