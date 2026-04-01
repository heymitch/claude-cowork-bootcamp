---
name: follow-up-writer
description: Write a post-meeting follow-up email with recap and action items. Say "write meeting follow-up" or "send recap email" or "meeting recap" or "follow-up email for [person]".
user-invocable: true
---

# Follow-Up Writer

Write a post-meeting recap email that covers what was discussed, what was agreed, and what happens next. Two modes: formal (new clients) and casual (existing relationships).

## How to Run

- "Write meeting follow-up for [person]"
- "Send recap email"
- "Meeting recap for today's call"
- "Write follow-up email"
- "Draft a recap for my meeting with [person]"

## What the Agent Does

### Step 1: Get Meeting Content
Find the meeting content. Check in this order:
1. Was a brief built for this meeting? Check `projects/` in the Coworker workspace for a brief matching the person or meeting date. Use it.
2. Is there a transcript (via Fireflies or Gmail)? Use it.
3. Neither? Ask the user: "What happened in the meeting? Key points, decisions, action items — even rough notes work."

### Step 2: Determine Tone
Infer the user's voice from their sent emails and past messages. Then ask or infer the format:

- **Formal** — New client, first meeting, important stakeholder. Professional language. Full sentences. "Thank you for taking the time..."
- **Casual** — Existing relationship, regular check-in, teammate. Conversational. Shorter. "Great chat today..."

If unclear, default to casual. User can switch.

### Step 3: Draft the Email

**Structure:**

```
Subject: Recap — [Meeting Topic/Person] — [Date]

[Opening — one line, match tone]

[Key discussion points — 3-5 bullets]

[Action items — table or bullet list with owners and deadlines]

[Next steps — next meeting, deadline, or what happens now]

[Closing — match tone]
```

See `../meeting-prep/references/follow-up-examples.md` for formal and casual email examples with tone selection guide.

### Step 4: Show for Review
Display the full email draft. Ask: "Ready to send, or want changes?"

Never send without explicit approval. The user must say "send it" or "looks good" before any sending action.

### Step 5: Deliver
- If Gmail send is available and user approves: send the email
- If no send capability: copy the email to clipboard or save as file
- Confirm what happened: "Email sent to sarah@lightwave.com" or "Draft saved — paste it into your email client"

### Step 6: Save the Notes
After sending or delivering, save the follow-up email as a record:
- Save to `projects/[person-name]/YYYY-MM-DD-followup-[person-name].md`
- If no project folder exists for this person, create it
- After saving, update `.coworker/index.md` with a one-liner (e.g., "Sarah Kim @ Lightwave — follow-up sent 2026-03-15")

## Rules

- Never send an email without user approval. Always show the draft first.
- Match the user's voice from their sent emails. If no email history exists, use a neutral professional tone.
- Keep it short. Recap emails should take 30 seconds to read. Nobody reads long follow-up emails.
- Action items must have owners and deadlines. "We'll follow up" is not an action item.
- If the meeting had no clear action items, say so: "No specific action items came out of this meeting" and focus on the discussion summary.
- Always include a next step, even if it's just "Let's reconnect next week."
- Subject line must be clear and scannable. Include the date or topic.
- Never invent discussion points or action items that weren't in the source material.
- Always update `.coworker/index.md` after saving the follow-up record.
