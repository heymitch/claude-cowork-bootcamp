---
name: project-kit
description: One meeting becomes a complete engagement — strategy, proposal, presentation, execution plan, and social content. Say "build a project kit", "turn this meeting into everything", "pull transcript", "get my meeting", "build a strategy", "write proposal", "build SOW", "make presentation", "build deck", "plan this project", "build the execution plan", "social posts from meeting".
user-invocable: false
---

# Project Kit — Router

One meeting. A complete engagement. This skill routes to the right sub-skill based on what you ask for.

## Routing

| You say | Runs |
|---------|------|
| "Build a project kit" / "turn this meeting into everything" | Full flow (see below) |
| "Pull transcript" / "get my meeting" / "find my last call" | `../transcript-extractor/SKILL.md` |
| "Build a strategy" / "map their pipeline" / "figure out what they need" | `../strategy/SKILL.md` |
| "Write proposal" / "build SOW" / "scope of work" | `../proposal-builder/SKILL.md` |
| "Make presentation" / "build deck" / "create slides" | `../deck-generator/SKILL.md` |
| "Plan this project" / "build the execution plan" / "set up the Rocks" | `../project-planner/SKILL.md` |
| "Social posts from meeting" / "post about this project" | `../social-content/SKILL.md` |
| "Set up my business blueprint" / "business blueprint" / "configure my business" | `../business-blueprint/SKILL.md` |

## Preflight (Run Silently)

1. **Workspace context** — Read `.coworker/index.md` to check for:
   - Active projects (use for client name matching and output path routing)
   - Existing business blueprint reference or path
   - Any prior project work for the current client
2. **Business Blueprint check:** Look for `training/references/business-blueprint.md` in the Coworker workspace. Also check `.coworker/index.md` for a pointer to the blueprint.
   - **Found:** Load it silently. Use it for voice, pricing, services, and contact info throughout the chain.
   - **Not found:** Proceed anyway. The chain works without it — outputs will just use generic placeholders for business name, pricing, and voice. After the chain completes, mention: "Tip: Run 'set up my business blueprint' and every future Project Kit will sound like you instead of a template."
3. **Scan connectors:** Fireflies, Gmail, Gamma, Notion. Note what's available. No connectors required — the user can always paste notes.
4. **Proceed.**

## Full Flow

When running the complete kit, execute in order. Each step feeds the next:

1. **transcript-extractor** — Get and structure the meeting content.
2. **strategy** — Map the client's pipeline, identify AI surface area, design the engagement.
3. **proposal-builder** — Build a custom proposal from the strategy brief (not a generic SOW).
4. **deck-generator** — Create the presentation from the proposal.
5. **follow-up-email** — Write a deliverable-aware email referencing the proposal and deck.
6. **project-planner** — Build the execution plan: Rocks, Kanban, scorecard, weekly pulse.
7. **social-content** — Extract one insight for social posts.

Show each output for review before moving to the next step.

## Rules

- Route based on intent. Don't run the full flow if they only asked for a strategy.
- Every sub-skill shows output for review before saving or sending.
- Never send anything without explicit approval.
- If a sub-skill needs input from a previous step that wasn't run, run that step first or ask for the input directly.
- **Strategy before proposal.** If someone asks for a proposal and the strategy hasn't been built, suggest running strategy first. Don't block them — but recommend it.
- **Follow-up email runs automatically in the full flow** but is NOT user-invocable. If someone asks for a standalone follow-up email, tell them: "Follow-up emails are in the Meeting Prep plugin. Say 'write the follow-up email' and it'll handle it."
- Always read `.coworker/index.md` in preflight — it tells you who the active clients are and where prior work lives.
