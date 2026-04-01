---
name: morning-brief
description: Daily briefing — pulls calendar, triages email, preps meetings, finds deep work windows. Schedule at 7am or say "morning brief", "daily briefing", "what's my day look like", "brief me".
user-invocable: true
---

# Morning Brief

Concise, actionable morning briefing. Under 400 words. Under 2 minutes to read. No fluff.

## Workflow

### Step 1: Load Context

Read `.coworker/index.md` silently. Check:
- Active projects with deadlines this week
- Any pending action items from recent debriefs

### Step 2: Pull Today's Calendar

Read Google Calendar for today. For each event:
- Meeting title and time
- Who's attending (names and roles if available)
- Location or video link
- Any notes attached to the event

### Step 3: Scan Recent Emails

Search Gmail for emails received in the last 18 hours. Focus on:
- Emails from people I'm meeting with today
- Anything flagged as urgent or marked important
- Replies to threads I started
- Ignore newsletters, marketing, and automated notifications

### Step 4: Check Slack (if connected)

Scan for overnight activity:
- Direct messages
- Mentions in channels
- Threads I'm part of that got new replies

Skip if Slack isn't connected — the brief still works with just Calendar + Gmail.

### Step 5: Check for Conflicts and Gaps

- Flag overlapping meetings
- Note back-to-back blocks with no buffer
- Identify gaps of 45+ minutes (deep work windows)
- Cross-reference gaps with active project deadlines to suggest what to work on

### Step 6: Generate the Brief

```
# Morning Brief — [Today's Date]

## Your Day at a Glance
[Timeline: time | meeting | key person]

## Priority Alerts
[Urgent items — conflicts, hot emails, project deadlines, Slack mentions needing response]

## Meeting Quick-Prep
[For each meeting: 1-2 lines of context from recent emails/Slack/project notes]

## Deep Work Windows
[Open blocks with suggested focus areas from active projects]

## Follow Up Today
[The 1-3 most important emails or threads needing your attention]
```

### Step 7: Save and Log

Save the brief to `output/morning-brief-YYYY-MM-DD.md` in the workspace.

Update `.coworker/logs/activity.md`:
```
### YYYY-MM-DD
- Morning brief generated — X meetings, X priority alerts, X deep work windows
```

## Connectors

- **Google Calendar** (required) — reads today's schedule
- **Gmail** (required) — scans recent emails for context
- **Slack** (optional) — overnight activity and mentions

## Rules

- **Under 400 words.** If it's longer, cut the least urgent items.
- **Under 2 minutes to read.** This runs before coffee. Respect the reader's time.
- **No speculation.** Only include information from actual calendar events, real emails, real Slack messages. Never invent context.
- **Meeting Quick-Prep is the highest-value section.** For each meeting, find the most recent email or Slack thread with that person and surface it. Walking into a meeting knowing the last conversation is the whole point.
- **Deep Work Windows suggest what to work on.** Don't just say "free from 2-4pm." Say "free from 2-4pm — Acme proposal due Thursday."
