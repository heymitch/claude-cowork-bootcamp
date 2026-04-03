---
name: strategy
description: Map a client's delivery pipeline and design a custom engagement strategy. Say "build a strategy", "map their pipeline", "figure out what they need", "design the engagement", "strategy for [client]", or "what should we actually build for them?"
user-invocable: true
---

# Strategy

Understand what a client actually does, how they deliver, and design a custom engagement around their real pipeline — not a generic scope of work.

## How to Run

- "Build a strategy for this client"
- "Map their delivery pipeline"
- "Figure out what they actually need"
- "Design the engagement for [client]"
- "What should we build for them?"

## What the Agent Does

### Step 1: Gather Context

Read `.coworker/index.md` first to check for active projects matching the client and any prior work saved in `projects/`.

Pull from whatever exists in this session:

**Transcript available?** (from transcript-extractor)
- Extract: what the client described about their business, process, pain points, goals

**Documents uploaded?** (company website, pitch deck, service descriptions, org chart)
- Extract: what they sell, how they deliver, team structure, tools they use

**Nothing available?**
- Ask these questions ONE AT A TIME (never dump all at once):

1. "What does this company actually do? Not the elevator pitch — the real work. What happens after someone pays them?"
2. "Walk me through their delivery process. A customer says yes — then what? What are the steps from sale to done?"
3. "Where does it break down? What takes too long, costs too much, or depends on one person?"
4. "What tools and systems are they using today? Spreadsheets, software, whiteboards, phone calls — all of it."
5. "What's the team look like? Who does what, and who's stretched thin?"

### Step 2: Map the Delivery Pipeline

Build a structured map of how their business actually works:

```
TRIGGER (what starts the work)
    ↓
INTAKE (how work enters the system)
    ↓
PROCESSING (the steps to fulfill)
    ↓
DELIVERY (how the client gets the output)
    ↓
FOLLOW-UP (what happens after delivery)
```

For each stage, document:
- **What happens** — the actual steps
- **Who does it** — person or role
- **How long it takes** — real time, not ideal time
- **What breaks** — bottlenecks, single points of failure, manual steps that should be automated
- **Tools used** — current systems, even if it's a whiteboard

### Step 3: Identify the AI Surface Area

Go through each pipeline stage and classify:

| Stage | Can AI Handle? | How |
|-------|---------------|-----|
| ... | **Yes — fully** | AI does this end-to-end (e.g., draft emails, generate reports, write proposals) |
| ... | **Yes — with review** | AI drafts, human approves (e.g., client communications, pricing quotes) |
| ... | **Assist only** | AI speeds it up but human drives (e.g., strategic decisions, creative direction) |
| ... | **No — human required** | Physical work, relationship judgment, legal/compliance (e.g., manufacturing, on-site visits) |

Be honest. Don't oversell what AI can do. The credibility of the proposal depends on this being accurate.

### Step 4: Design the Engagement

Based on the pipeline map and AI surface area, design what you'd actually build:

**Quick Wins** (week 1-2, visible impact):
- What can you automate or improve immediately?
- These build trust and buy time for the bigger work.

**Core Build** (week 2-6, the real value):
- What systems, workflows, or tools would you create?
- What does the client's team need to learn?
- What integrations are needed?

**Ongoing Value** (month 2+, retention play):
- What needs monitoring, optimization, or expansion?
- What new capabilities open up once the foundation is in place?

**Out of Scope** (be explicit):
- What does the client need that you don't do?
- What requires a different vendor, hire, or timeline?

### Step 5: Output the Strategy Brief

Present a clean strategy document:

```markdown
# Strategy Brief — [Client Name]

## The Business
[One paragraph: what they do, how they deliver, scale]

## The Pipeline
[The delivery pipeline map from Step 2]

## The Opportunity
[Where AI creates the most value — ranked by impact]

## AI Surface Area
[The classification table from Step 3]

## Recommended Engagement
### Quick Wins (Week 1-2)
[Bullets]

### Core Build (Week 2-6)
[Bullets with deliverables]

### Ongoing Value (Month 2+)
[Bullets]

## Out of Scope
[What this engagement does NOT include]

## Key Risks
[What could go wrong, what depends on the client, what assumptions we're making]
```

Ask: "Does this match what you're seeing? Anything to add, cut, or reframe before I build the proposal?"

### Step 6: Save and Hand Off

On approval:
- Save to `projects/[client-name]/YYYY-MM-DD-strategy-[client-name].md`
- Create the folder if it doesn't exist. Client name in slug format (e.g., `greenleaf-consulting`)
- Update `.coworker/index.md` with a one-liner (e.g., "GreenLeaf Consulting — strategy brief saved 2026-03-31")
- This brief feeds directly into proposal-builder (custom scope) and project-planner (execution plan)
- Flag anything that needs research before proposing ("I need to verify their current tool supports API access before scoping that integration")

## Rules

- **ONE question at a time.** Never dump a list of questions. Conversation, not interrogation.
- **Use their language.** If they call it "the board" not "the kanban," you call it "the board."
- **Be honest about AI limits.** If something needs a human, say so. Overclaiming kills deals.
- **Pipeline first, solution second.** Understand how they work before you propose what to change.
- **No pricing in the strategy.** That's the proposal's job. Strategy is about what and why, not how much.
- **Don't skip the "out of scope" section.** This prevents scope creep and builds trust.
- **If uploaded documents contradict what the client said in the meeting, flag it.** "Your website says X but in the call you mentioned Y — which is current?"
- **The strategy brief must be approved before building the proposal.** Never skip this step.
- Always save to `projects/[client-name]/` — never to workspace root.
- Always update `.coworker/index.md` after saving.
