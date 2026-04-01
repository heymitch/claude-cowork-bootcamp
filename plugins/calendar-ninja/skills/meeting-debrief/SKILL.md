---
name: meeting-debrief
description: Quick post-meeting capture — or batch-debrief your whole day. What was decided, action items, follow-up. Say "debrief my meeting", "I just finished my call with [person]", "debrief my day", "end of day debrief", "catch up on today's meetings".
user-invocable: true
---

# Meeting Debrief

Fast post-meeting capture. Three questions, two minutes, everything filed.

## Workflow

### Step 1: Identify the Meeting

Check which meeting just ended (or ask):

1. Pull today's calendar — find the most recent meeting that ended in the last 60 minutes
2. If found: "You just finished your call with [attendees] about [topic]. That the one?"
3. If multiple candidates or none obvious: "Which meeting are we debriefing?"

### Step 2: Three Questions

Ask these one at a time. Keep it fast.

**Q1: "What was decided?"**
Capture decisions, agreements, direction changes. If they say "nothing really" — that's fine, note "no decisions, informational only."

**Q2: "What are the action items? Who owes what?"**
For each item, capture: who, what, and when (if mentioned). If no clear deadline, note "no deadline set."

**Q3: "What's the follow-up? When do you talk to them again?"**
Next meeting, next email, next milestone. If "nothing planned" — flag it: "Want me to suggest a follow-up date?"

### Step 3: Build the Debrief

Compile into a structured note:

```markdown
# Meeting Debrief: [Person/Topic]
**Date:** YYYY-MM-DD
**Attendees:** [names]

## Decisions
- [decision 1]
- [decision 2]

## Action Items
- [ ] [Person]: [task] — due [date or "TBD"]
- [ ] [Person]: [task] — due [date or "TBD"]
- [ ] Me: [task] — due [date or "TBD"]

## Follow-Up
- Next meeting: [date or "not scheduled"]
- Follow-up email needed: [yes/no]

## Notes
[Any additional context the user shared]
```

Show it to the user: "Here's the debrief. Anything to add or change?"

### Step 4: File It

1. Check `.coworker/index.md` for an existing project matching this person/company
2. If project exists → save to `projects/[project-name]/debrief-YYYY-MM-DD.md`
3. If no project → save to `output/debriefs/debrief-[person]-YYYY-MM-DD.md`
4. Update `.coworker/index.md` — add or update the project one-liner with latest meeting date

### Step 5: Trigger Downstream Skills

After filing, offer:

- "Want me to **draft a follow-up email**?" → routes to follow-up-writer
- "Want me to **check this for content angles**?" → routes to meeting-to-content
- "Want me to **block focus time** to handle these action items?" → routes to deep-work-blocker

Don't run these automatically. Offer. Let the user pick.

### Step 6: Log

Append to `.coworker/logs/activity.md`:
```
### YYYY-MM-DD
- Debriefed: meeting with [person] — 2 decisions, 4 action items, follow-up scheduled
- Filed to: projects/[project-name]/
```

## Batch Mode

When triggered at end of day (manually or via scheduled task):

1. Pull today's calendar — list all meetings that happened
2. Check `projects/` and `output/debriefs/` for existing debriefs from today
3. Show the gap: "You had 5 meetings today. I have debriefs for 2. Want to quick-capture the other 3?"
4. Run through each un-debriefed meeting — same 3 questions, but faster:
   - Show the meeting name + attendees as context
   - Accept "skip" to move past meetings that don't need capture
   - Accept "nothing" for any question to keep it moving
5. File all debriefs, then offer batch downstream: "Want me to scan these for content angles?" or "Draft follow-ups for any with action items?"

Batch mode should take ~5 minutes for 3-4 meetings. Speed is everything — this runs at 5:30pm when they want to close their laptop, not write essays.

**Trigger phrases for batch:**
- "debrief my day"
- "catch up on today's meetings"
- "end of day debrief"
- "any meetings I missed debriefing?"

## Rules

- **Two minutes per meeting, five minutes for a full day.** Fast answers, file it. Not an interview.
- **Accept short answers.** "Nothing decided" and "I'll email them Friday" are complete answers. "Skip" is valid.
- **Never fabricate action items.** Only capture what the user actually says.
- **Offer downstream skills, don't auto-run them.** The debrief is the capture. Follow-up and content are separate decisions.
- **File to the right project.** If there's a matching project in the index, use it. New contacts can create new project folders.
