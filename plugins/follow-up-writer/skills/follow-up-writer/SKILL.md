---
name: follow-up-writer
description: Draft personalized meeting follow-up emails with action items, decisions, and next steps in your voice. Say "write a follow-up", "follow-up email for", "meeting follow-up", "send follow-up to", "draft a follow-up after", or "follow up on my meeting with".
user-invocable: true
---

# Follow-Up Writer

Takes meeting notes, transcripts, or calendar context and turns them into a polished follow-up email—action items called out, tone matched to your voice, ready to send.

## Workflow

### Step 1: Get the Meeting Input

Check for input in this order—use the first one that's available:

1. **Pasted notes** — if the user pasted text, use that directly
2. **Project transcript** — search `projects/{meeting-name}/` in the workspace for any meeting notes or transcript files
3. **Calendar + Gmail** — if neither above is available, pull the calendar event and related email thread using the Google Calendar and Gmail connectors, then ask the user to confirm which meeting this is for

If nothing is found, ask:
> "Paste your meeting notes here, or tell me the meeting name and I'll look for a transcript."

### Step 2: Load Voice Profile

Check for `training/voice/voice-template.md` in the workspace.

- **If found:** Read it. Apply the tone, vocabulary patterns, sentence structure, and any explicit rules throughout the entire email. Do not describe the voice—just write in it.
- **If not found:** Default to clean, direct, professional. After drafting, offer: "No voice template found. Want to set one up so future emails sound more like you?"

### Step 3: Read the Patterns

Read `references/email-patterns.md` and select the pattern that fits:
- Hard commitments made → Action-Item Follow-Up
- Key decision reached → Decision Confirmation
- Exploratory or planning call → Next Steps
- First meeting, sales, or relationship context → Thank You + Value Add
- Ambiguous → ask before drafting

### Step 4: Extract the Content

From the meeting input, pull:
- **Summary** — what was discussed in 2–3 sentences, no jargon
- **Action items** — who owes what, by when (if dates weren't stated, note "TBD")
- **Decisions made** — any choices locked in during the meeting
- **Next steps** — what happens after this, including any follow-up meetings

If action items or next steps are unclear from the notes, ask one targeted question before drafting:
> "I see [X] was discussed but I can't tell who's doing what next. Can you fill in the blanks?"

Don't ask more than once.

### Step 5: Draft the Email

Write the email. Keep it tight:
- Subject line: specific, not generic ("Follow-up: [meeting topic]" not "Following up")
- Body: under 200 words unless complexity demands more
- Action items as a bulleted list with owner + deadline
- One clear close—next meeting date, or the ball back in their court

Apply the voice template throughout. Don't announce that you're using it—just use it.

### Step 6: Save and Confirm

Save the draft to `output/follow-up-[recipient]-[YYYY-MM-DD].md` in the workspace.

If `.coworker/index.md` exists, append a one-line log entry:
```
- [YYYY-MM-DD] Follow-up drafted for [recipient] re: [meeting topic]
```

Present the draft to the user for review.

### Step 7: Send (Only With Explicit Approval)

After the user reviews, ask:
> "Want me to create this as a Gmail draft so you can send it from your inbox?"

Only proceed if the user says yes. Never send or create a Gmail draft without explicit approval.

If approved, use the Gmail connector to create a draft—do not send directly.

## Rules

- Never send or draft to Gmail without explicit user approval
- Always read the voice template if it exists—generic tone is the fallback, not the default
- One clarifying question maximum before drafting—don't interview the user
- Subject lines must be specific to this meeting, not templated
- Action items need owners—if unknown, flag them rather than leaving them blank
- Keep the draft under 200 words unless the meeting genuinely requires more
- Never include internal notes or confidential context not appropriate for external email
