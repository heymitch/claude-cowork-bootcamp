---
name: business-blueprint
description: Build or update your business blueprint — the universal context file that makes every skill sound like you. Say "set up my business blueprint", "create my business config", "update my blueprint", "business blueprint", or "configure my business".
user-invocable: true
---

# Business Blueprint

Build a portable business context file from whatever you have — existing projects, handbooks, product lists, or just your answers. Every other skill in this plugin works without it — but with a blueprint, the outputs sound like you instead of a template. Proposals use your pricing. Emails match your voice. Decks reference your actual services. It's the difference between "pretty good first draft" and "almost ready to send."

## How to Run

- "Set up my business blueprint"
- "Create my business config"
- "Update my business blueprint"
- "Business blueprint"

## What This Produces

A single `business-blueprint.md` file containing:

- Business identity (name, one-liner, origin story)
- Services and offerings (what you sell, pricing ranges, delivery format)
- Target audience (who you serve, who you don't)
- Voice and tone (how you write, words you use, words you never use)
- Team and roles (who does what)
- Contact and logistics (email, scheduling link, timezone)
- Key differentiators (what makes you different from competitors)

## What the Agent Does

### Step 0: Check for existing blueprint

Check `training/references/business-blueprint.md` in the Coworker workspace. Also check `.coworker/index.md` for a pointer to the blueprint.

- **Found:** Ask "I found your existing blueprint. Want me to update it with new info, or start fresh?"
- **Not found:** Proceed to Step 1.

### Step 1: Gather existing context (before asking questions)

Before asking the user anything, silently check what's already available:

1. **Scan the workspace** — look for files that contain business context:
   - `.coworker/index.md` (active clients, context summaries)
   - Any file with "services", "pricing", "offerings", "products" in the name
   - Proposal files in `projects/` (they contain business descriptions and pricing)
   - Previous project folders (they show what you've actually delivered)

2. **Check connectors** — if Notion is connected, search for:
   - Pages with "about", "services", "pricing", "products", "team" in the title
   - Any business-related databases

3. **Web search** — if you know the business name from workspace files, do a quick web search to pull public positioning (website tagline, LinkedIn company description, etc.)

Collect everything you find. This pre-research means you ask fewer questions and smarter ones.

### Step 2: Smart interview (grouped questions)

Based on what you found (or didn't find) in Step 1, run through these question blocks. **Skip any block where you already have confident answers from Step 1.** When you do have partial info, pre-fill what you know and ask the user to confirm or correct.

**IMPORTANT:** Group related questions together. Never ask one tiny question at a time. Each round should cover a meaningful chunk of context.

---

**Block A: Identity & Positioning**

Ask together as one prompt:

> I need three things to start:
>
> 1. **Your business name** (or your name, if you are the business)
> 2. **The one sentence you'd use at a dinner party** to describe what you do — not your elevator pitch, just the real version
> 3. **How you got here** — one or two sentences about your origin. What were you doing before this? What made you start?

If you found a business name or description in Step 1, lead with: "I found [X] — is this right, or has it changed?"

---

**Block B: What You Sell**

Ask together:

> Now the offering:
>
> 1. **List your services or products** — what do people actually pay you for? Include the name, a one-line description, and a rough price range for each. (If you have a lot, just list the top 3-5.)
> 2. **How do you deliver?** — 1:1 calls, async, done-for-you, courses, software, physical products?
> 3. **What do you NOT do?** — what requests do you turn away? This is just as important as what you offer.

---

**Block C: Who You Serve**

Ask together:

> Who's this for:
>
> 1. **Describe your ideal client in one sentence** — not demographics, but the situation they're in when they find you. "A [role] who [situation] but hasn't [gap] yet."
> 2. **Who is NOT a fit?** — the type of person or company you'd refer elsewhere.
> 3. **Where do your best clients come from?** — referrals, content, ads, events, cold outreach?

---

**Block D: Voice & Tone**

Ask together:

> Last block — how you sound:
>
> 1. **Pick 3 words that describe your communication style.** (e.g., direct, warm, technical, casual, authoritative, playful)
> 2. **Words or phrases you NEVER want AI to use** when writing as you. (e.g., "leverage", "synergy", "I hope this email finds you well", "game-changer")
> 3. **If you have a writing sample** — a past email, proposal, LinkedIn post, or bio — paste it here. This is the single most useful thing for getting your voice right. Even one paragraph helps.

---

**Block E: Team & Contact (optional)**

Only ask if the business appears to have a team (from Step 1 context):

> Quick logistics:
>
> 1. **Who's on your team?** — names and roles for anyone a client might interact with.
> 2. **Best contact email** and scheduling link (if you have one).
> 3. **Your timezone** — so proposals and emails reference realistic timelines.

For solopreneurs, skip the team question and just ask for contact + timezone.

### Step 3: Build the blueprint

Compile everything into a clean, structured markdown file:

```markdown
# Business Blueprint

> [One-liner description]

## Identity
- **Business Name:** [name]
- **Founded:** [year or "N/A"]
- **Origin:** [1-2 sentence backstory]
- **Website:** [if known]

## Services & Offerings

### [Service/Product 1]
- **Description:** [what it is]
- **Price Range:** [range]
- **Delivery:** [how it's delivered]
- **Timeline:** [typical duration]

### [Service/Product 2]
...

### What We Don't Do
- [thing 1]
- [thing 2]

## Target Audience
- **Ideal Client:** [situation-based description]
- **Not a Fit:** [who to refer away]
- **Primary Channels:** [where clients come from]

## Voice & Tone
- **Style:** [3 descriptors]
- **Never Use:** [banned words/phrases]
- **Writing Sample:**
> [pasted sample or summary of their voice]

## Team
| Name | Role | Contact |
|------|------|---------|
| [name] | [role] | [email] |

## Contact & Logistics
- **Email:** [email]
- **Scheduling:** [link]
- **Timezone:** [tz]

## Key Differentiators
- [what makes them different — synthesized from everything above]
```

### Step 4: Review and save

Show the complete blueprint. Ask:
- "Does this look right? Anything missing or wrong?"
- Let them edit inline — "change the one-liner to..." or "add this service..."

On approval, save to `training/references/business-blueprint.md` in the Coworker workspace.

After saving, update `.coworker/index.md` with a one-liner noting the blueprint exists (e.g., "Business blueprint saved to training/references/business-blueprint.md").

### Step 5: Make it universal

After saving, offer the next step:

> Your blueprint is saved at `training/references/business-blueprint.md`. Every Project Kit skill will find it automatically from there.
>
> **Optional: Push to Notion** — I'll create a page in your Notion workspace so any Cowork session with the Notion connector can read it.
>
> **Pro tip:** You can also add this line to your Cowork global instructions (Customize → Instructions) so every skill finds it automatically:
> *"When helping with business tasks, check the business blueprint at training/references/business-blueprint.md."*

If they choose Notion:
- Create a page titled "Business Blueprint" in their Notion workspace
- Paste the full content
- Give them the link to reference in global instructions

## Updating an Existing Blueprint

When the user says "update my blueprint":

1. Read the existing `training/references/business-blueprint.md`
2. Ask: "What changed? New service, new pricing, rebranding, new team member — or something else?"
3. Make the specific update without rewriting the whole file
4. Show the diff — what changed and what stayed
5. Save the updated version
6. If it was also pushed to Notion, offer to update the Notion version too

## Rules

- **Save location is always `training/references/business-blueprint.md`** — never to a config.md, never to the workspace root.
- Never guess pricing. If they don't provide it, leave the field as "Ask [name] for current pricing" rather than inventing numbers.
- Never fabricate a backstory or origin. If they skip it, omit the section.
- The writing sample is the highest-value input. Push for it. Even one email or LinkedIn post transforms the voice section from generic descriptors to something actually useful.
- Keep the file under 500 lines. This is a reference doc, not a novel.
- Pre-fill everything you can from Step 1. The best interview is the one where the user just confirms what you already found.
- Always update `.coworker/index.md` after saving.
