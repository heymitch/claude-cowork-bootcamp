---
name: dispatch-chain
description: >
  Authoring tool — invoke this to CREATE a new chain skill that fires from Dispatch (phone → desktop). When invoked, this skill INTERVIEWS the user, SCANS local files for references, MAPS installed skills to steps, then DELEGATES to Skill Maker to write the final SKILL.md. Do NOT write a chain skill file directly — always run the authoring protocol below. Say "create a new dispatch chain", "help me build a chain for [X]", "new chain skill", "/dispatch-chain I want to [...]".
user-invocable: true
---

# Dispatch Chain — Authoring Tool

This skill **creates new chain skills**. It does not run chains itself — that's what the authored skills do.

When invoked, it follows a non-skippable authoring protocol: interview the user, scan local files, map installed skills, delegate to Skill Maker to write the final SKILL.md, verify the install.

---

## AUTHORING PROTOCOL — non-skippable

**Even if the user provides a detailed prompt, you MUST run every step below. Do NOT write a SKILL.md directly from their first message.** A detailed prompt gives you a head start on the interview — it doesn't replace it. The interview surfaces local file references, connector specifics, and HIL preferences that almost always get missed if you skip straight to writing.

### Step 1 — Interview

Gather this intel before anything else. If the user's prompt answered some questions, confirm your reading back to them; ask the rest.

- **Chain name** — short, kebab-case. Example: `aiws-clinic-chain`.
- **Primary purpose** — one sentence on what this chain ships.
- **Trigger phrases** — how they'll fire it from phone. 2–3 phrases, natural to type.
- **Recurring context** — is this tied to a scheduled meeting (day + time)? Pre-existing recording (past Fathom/Zoom ID)? On-demand?
- **Ordered list of outputs** — what gets produced, in what order. For each output:
  - What it is (follow-up email, LinkedIn post, Notion page, etc.)
  - Which connector/surface it lands on
  - **Default: chain auto-ships.** Mark HIL ONLY if the user explicitly wants a human gate (regulatory, high-stakes first-run, or a surface with no undo like payments). Do NOT default to HIL.
  - **Do not offer to generate variants** (2 hook options, 3 draft versions) unless the user explicitly asks. Pick the best one and ship. Variants push work back to the user — that's what they hired the chain to avoid.
- **Voice / writing references** — voice config, writing samples, content rules. Paths or Notion/Drive URLs.
- **Brand / design tokens** — theme files with actual color hex values, typography specs, logo paths, UI design tokens. **Non-negotiable if the chain produces ANY visual output** (Vercel pages, Notion landings, social graphics, decks, emails, floppy assets). Generic descriptors like "cream and brown" are forbidden — the chain must reference actual hex values from the user's theme files. Ask explicitly: *"Where do your theme tokens live?"* Common locations: `training/references/brand-theme/`, `~/brand/tokens/`, `design-system/tokens.json`, or a Notion page with the color palette.
- **Business context** — pricing, services, business blueprint, contact info. Needed for any output that mentions the user's offer (proposals, pricing slides, CTAs).
- **Placeholders** — any values the chain will need that aren't known yet (waitlist URL, pricing tier, etc.) — note them for user to fill in later.

Write the interview summary to scratch before proceeding.

### Step 2 — Reference snapshot (pull content INTO the skill)

**This is the core portability step. Do not skip it.** The chain ships without mounting the user's workspace — it travels with its references baked in. Recording a path is not enough; the path doesn't exist from the dispatch execution context. **Pull the actual content into the new skill's `references/` folder.**

**Where references can live:**

- Local files on disk (`~/Desktop/Coworker/training/references/voice-config.md`)
- Notion pages (voice config, brand guide, business blueprint stored in Notion)
- Google Docs / Drive (via Drive MCP)
- GitHub files (via gh CLI or gh MCP)
- Any other reachable source at build time

**Protocol:**

1. **Interview for reference targets.** Ask the user where their voice config, brand guide, business blueprint, and other reference content live. Accept paths, Notion URLs, Drive URLs, or "skip this one." Don't scan blindly — the user knows where their canonical sources are.

2. **Read each one at build time.** Pull actual content using the right tool per source:
   - Local file → `Read` tool
   - Notion page → Notion MCP `fetch`
   - Drive / Docs → Drive MCP
   - GitHub → `gh api` or Grep
   
3. **Snapshot into the new skill's `references/` folder.** For each reference, write a file at `~/Desktop/Coworker/skills/[chain-name]/references/[purpose].md`:
   - Top of file: a header noting source + snapshot date (`Source: notion.so/xyz | Snapshot: 2026-04-15`)
   - Then: the actual content, copied verbatim
   
4. **Optionally add a re-pull schedule.** For references that should stay fresh (e.g., pricing that changes), the chain can include a runtime step that re-pulls from source. Default: no re-pull, snapshot persists until the user re-authors the chain.

5. **In the authored SKILL.md's Local file references section**, write:
   ```
   REFERENCE: references/voice-config.md
   PURPOSE: voice DNA for content outputs
   SOURCE: ~/Desktop/Coworker/training/references/voice-config.md (local, snapshotted 2026-04-15)
   LOADED_AT: when steps 3-5 run
   ```
   Note that `REFERENCE:` points to the **in-skill path**, not the original source.

**Why this matters for Dispatch:**

- Dispatch from phone → desktop loads the skill → reads `references/` from the skill's own folder → no workspace mount required, no Notion round-trip required
- Chain is self-contained. Voice config, brand guide, pricing — all travel with the skill
- Originals can move, change, or go offline — the snapshot survives

**If a reference is legitimately dynamic and must stay live** (e.g., "today's calendar"), don't snapshot — have the chain fetch fresh via the appropriate MCP at runtime, and note it in the skill as a runtime pull, not a snapshot reference.

**Scan fallback (only if user doesn't know paths):**

If the user can't tell you where a reference lives, scan these paths as a fallback to surface candidates:

- `~/Desktop/Coworker/` and any other trusted Coworker workspaces
- `~/Documents/`, `~/Desktop/`, `~/workspace/`
- `~/coworker/training/references/` — voice configs, blueprints
- `~/coworker/training/references/brand-theme/` — **design tokens, theme files** (prioritize for any visual-output chain)
- `~/brand/`, `~/voice/`, `~/templates/` — authoring references
- `~/design-system/`, `~/tokens/`, `tokens.json` files — color/typography tokens
- `~/clients/`, `~/projects/`

Filter by name + recency (< 90 days) + size (< 10MB for text). Skip `node_modules`, `.git`, `.next`, `dist`, `__pycache__`, VM-mounted paths. Present the shortlist; user picks. Then snapshot as above.

**Required categories by output type — if the chain produces these, pull these:**

| Chain produces | MUST snapshot |
|----------------|---------------|
| Any visual output (Vercel, Notion landing, social graphic, deck, email, floppy) | Design tokens / brand theme files with actual hex values |
| Any written content (post, email, newsletter, thread) | Voice config + writing samples |
| Any offer mention (proposal, pricing slide, CTA, waitlist copy) | Business blueprint + pricing + contact info |
| Any client-personalized output | Client dossier for that client |

**Test before proceeding:** for every output type in the chain, ask yourself "what reference would the chain need at runtime to produce this correctly instead of generically?" If that reference isn't in the snapshot list, the chain will ship generic output. Go back and snapshot it.

### Step 3 — Skill mapping

Enumerate ALL installed skills from three merged sources (use your own context awareness — don't try to `ls` or read config files):

- **Workspace skills** — `skills/` folder in the mounted Coworker workspace
- **Personal Plugins** — Claude app-level, installed via Customize → Personal Plugins
- **Marketplace skills** — Claude app-level, from installed marketplaces

For each step in the user's ordered list, match to a candidate skill:

- **Exact match** (step names a specific skill) → use it, priority 1
- **Description match** (step describes what a skill does) → best match, priority 2
- **Capability match** (multiple skills cover this) → pick the most specific, priority 3
- **No match** → flag as UNMAPPED; offer MCP-direct fallback (Notion MCP for Notion pages, Gmail MCP for drafts, browser MCP for browser automation) or `skip`

Present the proposed mapping:

```
STEP 1 — "pull transcript from AIWS Tech Clinic" → [candidate skill or MCP direct]
STEP 2 — "personalized Skool DMs per questioner" → [candidate skill or MCP direct]
...
```

User approves / swaps / flags.

### Step 4 — Delegate to Skill Maker

Hand Skill Maker all collected intel in a single structured brief:

- Chain name + trigger phrases
- Ordered list with mapped skills + MCP fallbacks + HIL flags per step
- Local file references with paths, purposes, LOADED_AT tags
- Placeholders for values the user will fill in later
- Scheduled-run spec if applicable (cron schedule, timezone)
- Target install location (default: `~/Desktop/Coworker/skills/[chain-name]/`)

Skill Maker writes the final SKILL.md following the Chain Skill Anatomy (see `references/chain-skill-anatomy.md` — load this reference when delegating). The authored skill MUST include the Never-Stop Contract and Completion Manifest sections verbatim; those are load-bearing.

### Step 5 — Package and install (do NOT stop at "skill written to workspace")

A skill sitting in `workspace/skills/` is a file, not an installed plugin. It won't trigger from Dispatch until it's packaged and installed as a Personal Plugin. **Do not hand this step off to the user as "now you go package and install" — run it.**

#### 5a. Verify skill integrity before packaging

- Folder + SKILL.md exist at target path
- Frontmatter `name:` matches the chain name (kebab-case, no spaces/capitals)
- Trigger phrases are in the description field
- `references/` folder exists and contains actual snapshotted content (NOT blank, NOT `[YOUR_PATH_HERE]` placeholders, NOT just paths)
- Every step in the ordered list maps to a skill or MCP-direct call (no UNMAPPED without a fallback)
- `.claude-plugin/plugin.json` exists at the plugin root (create one if missing — name, version `1.0.0`, description, author, license, keywords)

If any check fails, surface it with specifics and abort. Do not ship a half-authored skill.

#### 5b. Package via skill-packager

Invoke the skill-packager skill (`skill-maker:skill-packager` or equivalent installed packager) with the chain skill folder as input. It produces a `.plugin` or `.skill` archive.

Save the packaged file to a host-visible location the user can reach without mounting:

- **Primary:** `~/Desktop/[chain-name].plugin` (cleanest — user can see it immediately)
- **Fallback:** workspace root at `workspace/[chain-name].plugin` (if Desktop isn't reachable from this execution context)

Verify the archive:
- File size > 0
- Archive unzips cleanly
- `.claude-plugin/plugin.json` is in the archive root
- `skills/[chain-name]/SKILL.md` is inside

#### 5c. Install as Personal Plugin (best-effort auto-install)

**If you have computer-use access** (NavMacro coordinates or `mcp__computer-use__*` tools):

1. Open Claude Desktop (bring to front via `open_application`)
2. Click Customize → Personal Plugins → Upload plugin (use NavMacro route `cowork.upload-plugin` if available)
3. Drag the packaged file into the upload dialog
4. Confirm "installed" state in the Personal Plugins list
5. Report to user: trigger phrases + reminder to start a new chat

**If computer-use is unavailable** (running inside VM without host control):

Print clear, copy-friendly install instructions:

```
INSTALL STEP (one click):
  1. Open Cowork → Customize → Personal Plugins → Upload plugin
  2. Drag this file: ~/Desktop/[chain-name].plugin
  3. Start a NEW CHAT — skill loads at session start
  4. Fire with: [trigger phrases, listed]
```

Also `open -R` the file (reveal in Finder) if you can shell out, so the user doesn't have to navigate.

#### 5d. Post-install confirmation

Regardless of auto-install success or fallback:

- Report the packaged file's full path
- List the trigger phrases students/user will type to fire the chain
- Remind: **skill discovery happens at session start** — the user must open a new Cowork task for the skill to load. This is not negotiable; it's how Cowork loads plugins.
- Offer a test trigger phrase the user can paste into a new chat to verify

Do NOT declare success on a skill file that hasn't been packaged. Do NOT tell the user to "go package it" — run step 5b yourself. Do NOT stop at 5b without attempting 5c.

---

## What the authored chain skill contains (Skill Maker reference)

Every chain skill this tool authors MUST have these sections in its SKILL.md. These are non-negotiable — they're the reason the chain completes without stopping mid-sequence. Load `references/chain-skill-anatomy.md` for the full template.

- **Frontmatter** — name, description with trigger phrases, `user-invocable: true`
- **Ordered list of steps** — each step with skill reference, Input, Action, Output
- **Handoff rules** — explicit "Take [X] from step N, use as [Y] for step N+1" for every transition
- **Reference files snapshotted into `references/` folder** — populated from step 2 of the authoring protocol. Chain reads from its own `references/`, NOT from the user's workspace. Self-contained for dispatch.
- **Never-Stop Contract** — the no-pause, no-clarifying-questions, 3-retry contract
- **Preflight skill mapping** — runs once per invocation, remaps to current installed skills
- **Completion manifest format** — what the chain returns when done

See `references/chain-skill-anatomy.md` for the canonical template Skill Maker writes into.

---

## Rules for you (the authoring agent)

- **Never write a SKILL.md directly from the user's prompt without running steps 1-4.** Detailed prompts are a starting point, not a replacement for the protocol.
- **Never skip local file discovery.** A chain without voice config / brand references produces generic output. Always scan, always present the menu, always record the user's picks.
- **Never assume the user wants every file in scope.** Let them pick.
- **Never silently write to `skills/` if the target location is ambiguous.** Confirm with the user first.
- **Never mark the chain as "ready to ship" without step 5 verification.**

### Bias toward automation — HIL is opt-in, not opt-out

The user is building a chain BECAUSE they want the work done without them. Every HIL step you add takes work back and gives it to them. Defaults matter.

- **Auto-ship is the default** for every output the chain produces. Email → Gmail send. Post → LinkedIn publish. Landing page → published. PR → merged. Skool post → posted.
- **HIL is opt-in per step, justified explicitly** — only if the user names a reason (regulatory gate, first-run trust-building, high-stakes surface with no undo). If they don't name a reason, auto-ship.
- **Do not generate variants** (2 hook options, 3 draft versions, 5 style choices) unless the user explicitly requests it. Decide and ship.
- **Do not add approval gates between steps.** The whole chain runs to completion; the user reviews the manifest at the end, not each step.
- **Do not offer "draft for review" as a default surface.** If the user didn't ask for drafts, ship finished.
- **Browser automation beats "HIL paste to Substack"** every time. If a surface has no API/MCP, use computer-use or Chrome MCP to automate it — don't hand the draft to the user and call it shipped.

**Test for whether a step should be HIL:** can you, the authoring agent, name a specific failure mode that justifies a human gate at this step? If you can't name it, the step should auto-ship. Boilerplate "drafts let the user review" is not a specific failure mode.

**HIL framings to AVOID (these are bias toward manual, not justified gates):**
- "Let the user review the draft before sending" — no. Ship it. Manifest lists what went out.
- "User may want to edit the tone" — no. The chain's voice config handles tone. Ship it.
- "Fallback to HIL if API is unavailable" — fine for genuine infra failure, but don't design the step with HIL as the primary path.

If the user pushes back on the interview ("just write it, I gave you everything you need"), reply with: *"I hear you — most of what you said maps to the brief already. Before I delegate to Skill Maker, I want to run file discovery to catch your voice config and business blueprint paths. 30 seconds."* Then run step 2.

---

## Examples of properly-authored chain skills

- `aiws-clinic-chain` — recurring Tuesday clinic → 8 outputs (DMs, LinkedIn, Substack Notes, newsletter, Notion landing, Vercel route, Skool post)
- `client-weekly-review` — per-client Friday ship → status doc + invoice + health scorecard
- `discovery-to-proposal` — post-sales-call → proposal + deck + follow-up + plan

Each of these has local file references populated (voice config, brand guide, client dossier paths), not just Notion pulls.
