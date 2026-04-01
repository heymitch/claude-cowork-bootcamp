---
name: deep-work-blocker
description: Scan your calendar for open gaps and block deep work time. Knows what you're working on from your projects. Say "block deep work time", "protect my calendar", "find me focus time", "when can I do deep work", "block off time for [project]".
user-invocable: true
---

# Deep Work Blocker

Scan today's (or this week's) calendar for gaps between meetings. Propose deep work blocks. Actually create calendar events to protect that time.

## Workflow

### Step 1: Read Context

1. Read `.coworker/index.md` — check Active Projects for deadlines and priorities
2. Pull today's calendar via Google Calendar connector
3. Identify all gaps of 45+ minutes between meetings (shorter gaps aren't worth protecting)

### Step 2: Match Gaps to Work

For each gap, propose what to work on:

- If a project has a deadline this week → suggest that project for the longest gap
- If content is due (check `output/` for pending drafts) → suggest content review/editing
- If no specific priority → label as "Open Focus Time"

Present the plan:

```
I found 3 gaps in your calendar today:

1. 8:00-9:30 AM (90 min) → Suggested: Acme proposal (due Thursday)
2. 11:00-12:00 PM (60 min) → Suggested: Newsletter draft review
3. 3:30-5:00 PM (90 min) → Suggested: Open Focus Time

Want me to block these? I'll create calendar events so nobody books over them.
```

### Step 3: Get Approval

User can:
- "Yes, block all" → create all events
- "Block 1 and 3, skip 2" → selective
- "Change 3 to [project name]" → adjust before blocking
- "Just show me the gaps, don't block" → info only

### Step 4: Create Calendar Events

For each approved block, create a Google Calendar event:
- **Title:** "🔒 Deep Work: [project or label]"
- **Description:** "Protected focus time. Created by Calendar Ninja."
- **Show as:** Busy (so others can't book over it)
- **No notifications** — this is YOUR time, not a meeting to attend

### Step 5: Update Index

Append to `.coworker/logs/activity.md`:
```
### YYYY-MM-DD
- Blocked 3 deep work sessions (total: 4 hours)
- Focus areas: Acme proposal, newsletter review, open focus
```

### Step 6: Weekly Mode

If user says "block my week" or "protect my week":
- Pull the full week's calendar
- Find all gaps across 5 days
- Propose a weekly deep work plan
- Same approval flow, but batch by day

## Rules

- **Minimum gap: 45 minutes.** Anything shorter isn't worth blocking.
- **Never move or delete existing meetings.** Only fill gaps.
- **Always ask before creating events.** Propose first, block second.
- **Morning blocks are gold.** If there's a pre-meeting gap in the morning, prioritize it for the highest-value project.
- **Respect lunch.** Don't auto-block 12-1pm unless the user explicitly asks. Suggest it but flag: "This is your lunch hour — want to block it anyway?"
- **Show the math.** "You have 6 hours of meetings and 3 hours of gaps today. Here's how to use the gaps."
