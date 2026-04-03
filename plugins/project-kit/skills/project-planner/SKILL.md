---
name: project-planner
description: Turn a strategy into an execution plan with quarterly Rocks, a Kanban board, scorecard, and weekly pulse structure. Say "build the project plan", "create the execution plan", "plan this out", "what are the milestones", "break this into tasks", or "set up the Rocks for this project".
user-invocable: true
---

# Project Planner

Take the strategy brief and build a structured execution plan. Everything the AI can't do in real time gets planned, tracked, and made visible. Uses EOS Rocks for the big picture and Kanban for the daily work.

## How to Run

- "Build the project plan"
- "Create the execution plan for this"
- "Plan this out — what are the milestones?"
- "Break this into tasks"
- "Set up the Rocks for this project"

## What the Agent Does

### Step 1: Gather Inputs

Read `.coworker/index.md` first to identify the active client and check `projects/[client-name]/` for prior work (strategy brief, proposal).

Check for context from this session:

**Strategy brief available?** (from strategy skill, saved in `projects/[client-name]/`)
- Pull: engagement phases, deliverables, timeline, out-of-scope items, AI surface area

**Proposal available?** (from proposal-builder, saved in `projects/[client-name]/`)
- Pull: scope, pricing tiers, payment milestones, timeline

**Neither available?**
- Ask: "Tell me about the project. What are we building, for whom, and what does done look like?"
- Get enough to define the outcome and rough timeline

### Step 2: Define the Rocks

Rocks are quarterly priorities. Binary — done or not done. Format: **"From X to Y by [date]"**

Generate 3-5 Rocks based on the engagement:

**Rules for good Rocks:**
- Specific enough to be binary (not "improve the quoting process" but "AI quoting system handles 80% of standard quotes without Frank by June 30")
- Owned by one person (tag who owns each Rock — client or consultant)
- Achievable in 90 days (if bigger, break into phases with separate Rocks)
- Tied to a measurable outcome

**Example Rocks:**
- "From 0 to live AI quoting system handling Class 3-5 poles by April 15" (Consultant)
- "From 4-hour quote turnaround to 15-minute turnaround for standard specs by May 1" (Client validates)
- "From Frank-dependent to 2 team members trained on AI-assisted quoting by June 1" (Client)

Present Rocks and ask: "Do these capture what matters? Any missing or wrong?"

### Step 3: Build the Scorecard

5-8 weekly measurables that track whether the project is healthy. Mix of lead measures (actions you control) and lag measures (outcomes you track).

| Measure | Type | Target | Owner |
|---------|------|--------|-------|
| ... | Lead | ... | ... |
| ... | Lag | ... | ... |

**Lead measures** = predictive inputs you can act on:
- Hours spent on build this week
- Training sessions delivered
- Integrations configured
- Documents reviewed

**Lag measures** = outcomes that confirm it's working:
- Quote accuracy rate (AI vs Frank)
- Time-to-first-draft reduction
- Client satisfaction score
- System adoption rate

Ask: "What numbers would tell you this project is on track every week?"

### Step 4: Build the Kanban Board

Break the engagement into concrete tasks organized by phase:

```markdown
## Backlog
- [ ] [Rock 1] Research current quoting logic with Frank (3 sessions)
- [ ] [Rock 1] Document pricing rules for Class 1-5 poles
- [ ] [Rock 1] Build quoting prompt with Frank's decision tree
- [ ] [Rock 2] Map current order tracking spreadsheet
- [ ] [Rock 2] Design AI query layer for order status
...

## This Week
(Empty — user fills during weekly pulse)

## In Progress (WIP: 3)
(Empty — max 3 items at a time)

## Waiting On
(Items blocked by client, vendor, or external dependency)

## Done
(Completed items — move here when finished)
```

**Task format:**
- Tag by Rock: `[Rock 1]`, `[Rock 2]`, etc.
- Include owner if split work: `(Mitch)`, `(Client)`, `(Frank)`
- Add dependencies in parentheses: `(needs: pricing doc from Frank)`
- Estimate size: `S` (< 2 hrs), `M` (half day), `L` (full day), `XL` (multi-day)

**WIP limit = 3.** This is non-negotiable. Finishing beats starting. If someone wants to start a 4th task, they must finish or park one of the three.

### Step 5: Create the Issues List

Seed it with known risks from the strategy brief:

```markdown
## Issues List
(Review and IDS weekly: Identify → Discuss → Solve)

1. Frank retires before knowledge transfer is complete — what's the contingency?
2. Shop floor team resistance to new system — how do we get buy-in?
3. Steel pricing volatility affects quoting accuracy — how often do we update rates?
4. Client's existing spreadsheets may have inconsistent data — need audit
```

### Step 6: Design the Weekly Pulse

Create a 30-minute weekly review template:

```markdown
## Weekly Pulse — [Project Name]
**Date:** ___
**Duration:** 30 minutes

### 1. Scorecard Review (5 min)
| Measure | Target | Actual | On Track? |
|---------|--------|--------|-----------|
| ... | ... | ... | ✅ / ⚠️ / ❌ |

### 2. Rock Check (5 min)
| Rock | % Complete | Status | Notes |
|------|-----------|--------|-------|
| ... | ...% | On track / At risk / Off track | ... |

### 3. Kanban Review (5 min)
- Items completed this week:
- Items in progress:
- Items blocked (Waiting On):

### 4. IDS — Top 3 Issues (10 min)
Pick the 3 most important from the issues list. For each:
- **Identify:** What exactly is the problem?
- **Discuss:** What are the options?
- **Solve:** What's the decision? Who acts? By when?

### 5. Next Week (5 min)
- Pull items from Backlog → This Week
- Commitments for this week (3-5 specific to-dos):
  1.
  2.
  3.
```

### Step 7: Output the Full Plan

Present the complete execution plan:

```markdown
# Execution Plan — [Client / Project Name]

## Rocks (Q_ 2026)
[Rocks from Step 2]

## Scorecard
[Table from Step 3]

## Kanban Board
[Board from Step 4]

## Issues List
[List from Step 5]

## Weekly Pulse Template
[Template from Step 6]

## Key Dates
| Milestone | Date | Owner | Rock |
|-----------|------|-------|------|
| ... | ... | ... | ... |
```

Ask: "Does this plan match the scope? Ready to execute, or need to adjust?"

### Step 8: Save

On approval:
- Save to `projects/[client-name]/YYYY-MM-DD-execution-plan-[client-name].md`
- Create the folder if it doesn't exist
- Update `.coworker/index.md` with a one-liner (e.g., "GreenLeaf Consulting — execution plan saved 2026-03-31")
- This is a living document — update it during weekly pulses.

## Rules

- **Rocks are quarterly, not weekly.** If it can be done in a week, it's a task, not a Rock.
- **WIP limit of 3 is sacred.** Don't let anyone (including yourself) override this. Three in progress, max.
- **Lead measures over lag measures.** You can't control revenue but you can control proposals sent. Track what you can act on.
- **Issues list is not a to-do list.** Issues are problems or decisions. Tasks go on the Kanban board.
- **Every task tags back to a Rock.** If a task doesn't connect to a Rock, ask why it exists. It might be whirlwind (daily operations), not strategic.
- **The weekly pulse is the heartbeat.** If the client skips it for 2 weeks, flag it. Projects that lose their pulse die quietly.
- **Don't plan more than 90 days out.** Beyond one quarter, you're guessing. Set Rocks for this quarter, backlog items for next.
- **Match the format to the client.** If they use Notion, format for Notion. If they use a whiteboard, format for print. If they have nothing, markdown works everywhere.
- **Be explicit about client vs consultant tasks.** Every item has an owner. Ambiguous ownership = nobody does it.
- Always save to `projects/[client-name]/` — never to workspace root.
- Always update `.coworker/index.md` after saving.
