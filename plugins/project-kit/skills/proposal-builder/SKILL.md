---
name: proposal-builder
description: Build a custom proposal or SOW informed by the strategy brief. Say "build a proposal", "write the SOW", "create proposal from meeting", "write up the scope of work", or "proposal for [client]".
user-invocable: true
---

# Proposal Builder

Take the strategy brief and meeting context and turn it into a custom proposal — not a generic scope of work, but a pitch designed around the client's actual delivery pipeline.

## How to Run

- "Build a proposal from my meeting with [person]"
- "Write the SOW"
- "Create a proposal from this transcript"
- "Write up the scope of work for [project]"

## What the Agent Does

### Step 1: Gather inputs

Read `.coworker/index.md` first to identify the active client and check for prior work in `projects/`.

Check for context from this session, in priority order:

**Strategy brief available?** (from strategy skill, saved in `projects/[client-name]/`)
- This is the gold. Pull: pipeline map, AI surface area, recommended engagement phases, quick wins, core build, ongoing value, out-of-scope items, key risks.
- The proposal becomes a direct translation of the strategy.

**Transcript available but no strategy?**
- Check `projects/[client-name]/` for a saved transcript summary.
- Use the transcript. The proposal will be good but less targeted.
- Suggest: "Want me to run the strategy skill first? It'll make this proposal much sharper."

**Neither available?**
- Ask: "Do you have meeting notes or a transcript? Paste them here, or say 'pull my transcript' and I'll find it."

**Always check for:**
- `training/references/business-blueprint.md` — business name, contact info, services, pricing, voice profile. If not found, the proposal still works — just uses generic placeholders for business details and asks the user for pricing directly.
- Any uploaded client documents (website, pitch deck, org chart) that add context

### Step 2: Choose format

Based on the project size:
- **Under $3,000 or simple scope** — Use the one-pager format from `../project-kit/references/proposal-template.md`
- **$3,000+ or multi-phase** — Use the full proposal format from `../project-kit/references/proposal-template.md`

If unsure, ask: "Is this a quick project or a bigger engagement? I'll format the proposal to match."

### Step 3: Build the proposal

**If strategy brief exists** — the proposal follows the strategy structure:

1. **Cover**: Project name, client name, date, your info (from `training/references/business-blueprint.md`)
2. **Executive Summary**: Lead with the client's own words about their problem. Reference the pipeline bottleneck the strategy identified. State the transformation: "from [current state] to [future state]."
3. **The Opportunity**: Summarize the AI surface area analysis. Show you understand what AI can and can't do for their business. This builds credibility.
4. **Scope of Work — Phase 1: Quick Wins** (Week 1-2): Map directly from the strategy's quick wins. Specific deliverables with descriptions.
5. **Scope of Work — Phase 2: Core Build** (Week 2-6): Map from the strategy's core build. Break into deliverables with descriptions, timelines, and what the client gets at each milestone.
6. **Scope of Work — Phase 3: Ongoing Value** (Month 2+): Map from the strategy's ongoing section. Position as optional retention.
7. **Timeline**: Visual phase breakdown. Be realistic. Add buffer. Flag client dependencies.
8. **Pricing**: Three tiers built around the phases:
   - **Starter**: Quick wins only (Phase 1)
   - **Growth**: Quick wins + core build (Phase 1-2)
   - **Scale**: Everything including ongoing optimization (Phase 1-3)
9. **Payment Terms**: Default to 50/50 for projects under $10K. 30/30/40 milestone payments for larger.
10. **Included / Not Included**: Pull "not included" directly from the strategy's out-of-scope section.
11. **Next Steps**: One clear action for the client.
12. **Key Risks & Assumptions**: Pull from the strategy brief. Shows maturity and builds trust.

**If no strategy brief** — use the standard template:

1. **Cover**: Project name, client name, date, your info
2. **Executive Summary**: Use client's words from transcript
3. **Scope of Work**: Break into deliverables with descriptions and timelines
4. **Timeline**: Map to phases
5. **Pricing**: Three tiers if `training/references/business-blueprint.md` has pricing data. If not, ask for a ballpark.
6. **Payment Terms**: Default 50/50
7. **Included / Not Included**: Draw clear lines
8. **Next Steps**: One clear action
9. **Terms**: Brief working agreement language

### Step 4: Review

Show the complete proposal. Ask:
- "Does the scope match what you discussed?"
- "Is the pricing right?"
- "Anything to add or cut?"

### Step 5: Save

On approval:
- Save to `projects/[client-name]/YYYY-MM-DD-proposal-[client-name].md`
- Create the folder if it doesn't exist
- If the user wants PDF format, output clean markdown with a note: "Copy this into your PDF tool or say 'make this a PDF' if you have a converter set up."
- Update `.coworker/index.md` with a one-liner (e.g., "GreenLeaf Consulting — proposal saved 2026-03-31")
- This proposal feeds into deck-generator (for presentation) and project-planner (for execution)

## Rules

- **Strategy-first proposals are always better.** If the strategy skill hasn't run, suggest it. But don't block — the user may have good reasons to skip.
- Never guess pricing. If `training/references/business-blueprint.md` has no pricing and the user doesn't provide it, ask.
- Always use three-tier pricing unless the user explicitly wants flat rate.
- Use the client's language from the transcript in the executive summary and scope descriptions.
- Keep proposals under 2 pages for one-pager format, under 5 pages for full format.
- **The "Not Included" section is mandatory.** It prevents scope creep and shows the client you thought about boundaries.
- **If the strategy identified risks, the proposal must address them.** Don't bury bad news — surface it and show you have a plan.
- Show for review before saving. Never save or send without approval.
- Reference `../project-kit/references/proposal-template.md` for structure.
- Run the deliverable checklist (`../project-kit/references/deliverable-checklist.md`) mentally before presenting.
- Always save to `projects/[client-name]/` — never to workspace root.
- Always update `.coworker/index.md` after saving.
