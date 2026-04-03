# Email Sequence Writer

Write complete email sequences: welcome, pre-launch, launch, abandoned cart, book-a-call. Framework-based, not fill-in-the-blank.

## Setup

1. Read `training/voice/voice-template.md` — REQUIRED before writing
2. Check `.coworker/index.md` for business context, offers, and audience
3. Read `references/sequence-templates.md`

## Determine Sequence Type

Ask the writer which sequence they need. If unclear, ask:

- "Are you setting up automation for new subscribers?" → Welcome Sequence
- "Do you have a product launching soon?" → Pre-Launch or Launch Sequence
- "Are you trying to recover people who didn't buy?" → Abandoned Cart
- "Are you selling high-ticket coaching or services?" → Book-a-Call

## What to Collect

Before writing any sequence, gather:

**For all sequences:**
- Newsletter / brand name
- Main offer (product, service, or course)
- Target reader — specific description, not "anyone interested in X"
- Desired outcome for the reader
- Biggest problem the reader faces

**For welcome sequences:**
- Publishing frequency and day
- 3 tangible things subscribers get from each email
- 2-3 "greatest hits" resources or pieces of content
- Origin story — what was happening before + what changed + where you are now
- Paid offer to soft-pitch in Email 4 (if any)

**For launch sequences:**
- Product name, price, core promise
- Launch window (open date, close date)
- Top 3 objections prospects have
- 1-2 customer results or testimonials

**For abandoned cart:**
- Product abandoned
- Timeline flexibility (when does cart actually close?)
- Most common objection that stops people from buying

## Writing Process

### Step 1: Present the Sequence Architecture

Before writing, show the skeleton:
- Number of emails
- Each email's goal in one sentence
- Timing/cadence

Get approval before writing full drafts.

### Step 2: Write Each Email

Use frameworks from `references/sequence-templates.md`. Do NOT copy templates verbatim—adapt to the writer's voice, niche, and specific details.

Every email must:
- Have a clear, single goal
- Serve the reader's interest (not just the writer's)
- Educate before it sells
- End with one clear action (reply, click, read, or buy)

### Step 3: Generate Subject Lines

For each email, generate 2 subject line options:
- Option A: curiosity/problem-framing
- Option B: outcome/benefit-framing

Both in sentence case, 5-15 words.

### Step 4: Timing Recommendations

Provide a deployment schedule with specific gaps between emails.

## Output Format

```
SEQUENCE: [Name]
TOTAL EMAILS: [N]
DEPLOYMENT: [schedule summary]

---
EMAIL 1: "[Goal Name]"
SUBJECT A: [option]
SUBJECT B: [option]
SEND: [when]

[Full email body]

---
EMAIL 2: "[Goal Name]"
...
```

## Save Output

Save to `output/sequences/[sequence-type]-[YYYY-MM-DD].md`
Note in `.coworker/index.md` what sequence was written and for which offer.
