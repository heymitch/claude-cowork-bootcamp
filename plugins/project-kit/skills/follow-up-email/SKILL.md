---
name: follow-up-email
description: Write a follow-up email referencing the proposal, deck, and meeting context. This skill runs as part of the Project Kit pipeline — for standalone follow-up emails, use the Meeting Prep plugin.
user-invocable: false
---

# Follow-Up Email (Pipeline Mode)

Write a follow-up email that references everything the Project Kit pipeline has built — the meeting, the strategy, the proposal, the deck. This is not a generic recap; it's a deliverable-aware email that ties everything together.

## When This Runs

This skill is called by the Project Kit router as step 5 of the full flow. It is NOT user-invocable. For standalone follow-up emails, the Meeting Prep plugin's `follow-up-writer` handles that.

## What the Agent Does

### Step 1: Gather Pipeline Context

Pull from everything built in this session and saved in `projects/[client-name]/`:

- **Transcript summary** — who was in the meeting, key discussion points, client quotes
- **Strategy brief** — the engagement design, what you're proposing to build
- **Proposal** — pricing tier selected, scope, timeline, payment terms
- **Presentation** — if a deck was built, reference it as an attachment

Read `training/references/business-blueprint.md` for voice and sign-off style.

### Step 2: Pick the Template

Based on the meeting type:

- **New Client Follow-Up** — First meeting with potential client. Professional, specific, proposal attached.
- **Post-Presentation** — After a pitch or demo. Reference what was shown, next step to sign.
- **Partner / Collaboration** — Exploratory partnership call. Lighter scope, mutual next steps.

If unsure, default to New Client Follow-Up.

### Step 3: Write the Email

**Structure:**

```
Subject: [Specific — not generic] — Under 60 characters

[Opening — reference something specific from the meeting. NOT "I hope this email finds you well."]

[1-2 sentences on what you discussed and what excited you about their business]

[Key deliverables attached or referenced:]
- Proposal: [brief summary of what's in it — tiers, timeline]
- Presentation: [if built — "deck attached with the approach and timeline"]
- Strategy: [if relevant — "the pipeline analysis we discussed"]

[Next step — ONE clear action]
- "Take a look at the proposal and let me know which tier fits."
- "I've blocked Tuesday at 2pm for a follow-up — calendar invite incoming."
- "Reply with any questions and I'll have answers same day."

[Sign-off — match voice from training/references/business-blueprint.md]
```

### Step 4: Quality Check

Before presenting, verify:
- Names spelled correctly
- No placeholder text left
- No AI-tell phrases ("I hope this email finds you well", "Per our conversation", "Just circling back", "In today's landscape")
- Tone matches the relationship stage
- One clear CTA — not three
- Under 200 words — shorter is almost always better
- All referenced attachments actually exist from the pipeline

### Step 5: Review

Show the email. Ask: "Ready to send, or adjust the tone?"

Never send without explicit approval. If Gmail tools are connected, offer to draft — but NEVER send without the user saying "send it" or "yes, send."

### Step 6: Save

After the user approves (whether sent or not), save the email draft:
- Save to `projects/[client-name]/YYYY-MM-DD-followup-email-[client-name].md`
- Update `.coworker/index.md` with a one-liner (e.g., "GreenLeaf Consulting — follow-up email drafted 2026-03-31")

## Rules

- **This skill only runs inside the pipeline.** It is not user-invocable. Standalone follow-up emails go through Meeting Prep.
- Keep under 200 words. Respect people's inboxes.
- One CTA per email. Not three options — one action.
- Always reference something specific from the meeting — a quote, a detail, a moment. Generic recaps get ignored.
- If deliverables were built (proposal, deck), mention them and reference as attachments.
- NEVER use: "I hope this email finds you well", "Per our conversation", "Just circling back", "As discussed"
- NEVER send without explicit approval.
- Reference `../project-kit/references/email-templates.md` for template structures.
- Run the deliverable checklist (`../project-kit/references/deliverable-checklist.md`) mentally before presenting.
- Always save to `projects/[client-name]/` and update `.coworker/index.md`.
