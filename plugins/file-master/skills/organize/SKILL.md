---
name: organizing-files
description: File Master — index-aware file organizer. Reads .coworker/index.md to understand existing projects and context before organizing. Files go to matching projects first, type-based folders second, inbox/ as fallback. Updates the index after every move. Triggered by "organize my files", "clean up this folder", "sort these files", "help me organize", "file cleanup", "tidy up", "weekly cleanup".
user-invocable: true
---

# Organize Skill

Organize files by where they BELONG, not just what they ARE.

## Core Principle

The index is the brain. Read it first. A PDF about "Project Alpha" goes in
`projects/alpha/`, not `documents/pdfs/`. Generic type buckets are a last
resort. `inbox/` is the honest answer for unknowns---never bury confusion
inside nested generic folders.

## Workflow

```
Progress:
- [ ] Load context (config + index)
- [ ] Scan workspace for loose/unsorted files
- [ ] Classify each file (project-match → type-match → inbox)
- [ ] Propose plan to user
- [ ] Wait for approval
- [ ] Execute moves
- [ ] Update .coworker/index.md
- [ ] Log to .coworker/logs/activity.md
- [ ] Report summary
```

---

### Step 1: Load Context

Read these silently before doing anything:

1. **`.coworker/config.json`** — user name, preferences, org style
2. **`.coworker/index.md`** — the routing table. Parse every entry to build a mental map of:
   - What projects exist (anything under `projects/`)
   - What training categories exist (`training/voice/`, `training/references/`, etc.)
   - What tags are already in use
   - Recent activity patterns

If `config.json` doesn't exist: "Run /setup first so I know your preferences." Stop.
If `index.md` doesn't exist or is empty: note it---you're starting from scratch. Lean heavier on type-based classification and create index sections as you go.

---

### Step 2: Scan the Workspace

Determine scan scope based on context:

**Full organize** (user says "organize my files", "clean up"):
- Scan ALL files and folders in the workspace root
- Include files inside `inbox/`
- Include loose files at root level
- Skip files already in the correct location per the index

**Scheduled/weekly cleanup** (user says "weekly cleanup", or running on schedule):
- ONLY scan `inbox/` and root-level loose files
- Do NOT re-organize files already placed in `projects/`, `training/`, `output/`, `archive/`
- Be conservative---if unsure, leave in `inbox/` and flag for user

**Always ignore:**
- `.coworker/` (internal---never touch)
- `.DS_Store`, `Thumbs.db`, OS junk
- All dotfiles and dotfolders (`.git/`, `.vscode/`, etc.)
- `CLAUDE.md` at root (workspace config)

Build an inventory of every file that needs attention:
- Filename and extension
- Location (root, inbox, other)
- Whether it already appears in the index (if yes, it's already tracked---skip unless misplaced)

---

### Step 3: Classify Each File

For every unorganized file, run this classification cascade. **Stop at the first match.**

#### Priority 1: Project Match (check the index)

Read the index for existing projects. For each file, ask:
- Does the filename contain a project name or keyword from an indexed project?
- For text/markdown files: read the first 50 lines. Does the content reference a project, client, or topic that matches an indexed project?

If yes → destination is that project's folder (e.g., `projects/client-rebrand/`)

Examples:
- `acme-proposal-v2.docx` + index has `projects/acme/` → `projects/acme/`
- `meeting-notes.md` mentions "rebrand timeline" + index has `projects/rebrand/` → `projects/rebrand/`
- `logo-draft.png` with "rebrand" in name + index has `projects/rebrand/` → `projects/rebrand/`

#### Priority 2: Training Material Match

If the file looks like training data (writing samples, reference docs, prompts):

| Signals | Destination |
|---------|-------------|
| Personal writing, blog posts, newsletters, social posts in user's voice | `training/voice/` |
| Company docs, competitor info, industry data, meeting notes | `training/references/` |
| Instructions, templates, system prompts | `training/prompts/` |

Use file content (for text files) and filename to determine this. A file named `my-linkedin-post.md` containing first-person writing is a voice sample. A file named `competitor-analysis.pdf` is a reference.

#### Priority 3: Output Match

If the file looks like generated output from a skill or tool:
- Has frontmatter with `type: output` or similar skill metadata
- Filename suggests generation (`generated-`, `output-`, `draft-`, `v1-`, `final-`)
- Located in a path suggesting output

Destination: `output/`

#### Priority 4: Type-Based Fallback

Only if nothing above matched, use file type as a LOOSE guide---but keep it flat:

| File Types | Destination | When |
|-----------|-------------|------|
| `.md`, `.txt`, `.docx`, `.pdf` | `inbox/` | Can't determine purpose from content |
| `.png`, `.jpg`, `.svg`, `.gif` | `inbox/` | Can't associate with a project |
| `.csv`, `.xlsx` | `inbox/` | Can't determine purpose |
| Code files (`.js`, `.py`, etc.) | `projects/` (create a project if pattern is clear) | Has clear project structure |

**Important:** Do NOT create nested type folders like `documents/`, `images/`, `spreadsheets/`. These are the old pattern. Everything that can't be classified goes to `inbox/`.

#### Priority 5: Inbox (the honest fallback)

If classification is unclear, the file goes to `inbox/`. Period.

- NEVER create `inbox/documents/2026/march/` or similar nested structures
- `inbox/` is flat. Files sit at `inbox/filename.ext`
- The user or `/ingest` handles proper classification later
- This is better than guessing wrong

---

### Step 4: Propose the Plan

Present a clear, grouped summary. Group by destination, not by file type.

**Format:**
```
I read your index and scanned {X} files. Here's the plan:

**Matched to existing projects ({N} files):**
- `proposal-v3.md` → projects/acme/ — references Acme Corp (indexed project)
- `wireframe.png` → projects/acme/ — filename matches Acme project

**Training material ({N} files):**
- `linkedin-post-march.md` → training/voice/ — personal writing sample
- `industry-report.pdf` → training/references/ — reference document

**Output ({N} files):**
- `generated-newsletter-draft.md` → output/ — skill output

**Moved to inbox for manual review ({N} files):**
- `random-notes.md` — couldn't determine purpose
- `screenshot-2026.png` — no project match

**Already organized ({N} files):**
- Skipped — already in correct locations per index

Want me to go ahead? You can say "yes", "yes but skip X", or "no".
```

If this is a **weekly cleanup**, add:
```
**Flagged for your review ({N} files in inbox/):**
- `mystery-doc.pdf` — been in inbox 2+ weeks, might need filing
```

---

### Step 5: Wait for Approval

**Do NOT move anything until the user explicitly approves.**

They can:
- "yes" / "go ahead" → execute full plan
- "yes but skip X" / "yes but move Y to Z instead" → execute with modifications
- "no" / "hold on" → stop, no changes
- Ask questions → answer, then re-confirm

---

### Step 6: Execute

For each approved move:

1. Create the target folder if it doesn't exist
2. Move the file
3. Track: `{filename} | {from} | {to} | {reason}`

**Handle collisions:** If a file with the same name exists at the destination, ask the user. Options: rename with suffix (`-2`), replace, or skip. Never silently overwrite.

**Handle failures:** If a move fails (permissions, path issues), log the error and continue. Report all failures at the end.

---

### Step 7: Update the Index

This is non-negotiable. After every move, update `.coworker/index.md`.

For each file that was moved to a tracked location (NOT inbox):

1. Find the appropriate section in the index (or create it)
2. Add an entry in the standard format:

```
- `{new-path}` | {type} | {tags} | {date}
```

**Section mapping:**
| Destination | Index Section | Type |
|------------|---------------|------|
| `projects/{name}/` | `## Projects` | `project` |
| `training/voice/` | `## Voice Samples` | `voice-sample` |
| `training/references/` | `## References` | `reference` |
| `training/prompts/` | `## Prompts` | `prompt` |
| `output/` | `## Output` | `output` |
| `archive/` | `## Archive` | `archive` |

**Files moved to `inbox/` do NOT get index entries.** Inbox is unsorted---it gets indexed when properly filed via `/ingest` or a future organize pass.

**If a file was already in the index at its old path**, update the path in the existing entry. Don't create duplicates.

Generate tags from:
- Filename keywords
- Content keywords (if you read the file)
- Project name it was filed under

---

### Step 8: Log Activity

Append to `.coworker/logs/activity.md`:

```markdown
### {YYYY-MM-DD}
- Organized: {total moved} files sorted, {folders created} folders created
- Project matches: {list brief}
- Training: {count} voice samples, {count} references
- Inbox: {count} files for manual review
- Index updated with {count} new entries
```

---

### Step 9: Report

Show the user a concise summary:

```
Done. Moved {X} files into {Y} folders.

- {N} matched existing projects
- {N} classified as training material
- {N} moved to inbox for manual review
- Index updated with {N} new entries

Here's your folder structure now:
{tree view, 2 levels deep max}

Want me to adjust anything?
```

---

## Rules

- **NEVER delete files.** Organizing means moving, not deleting.
- **NEVER move dotfiles/dotfolders.** `.git/`, `.coworker/`, `.vscode/` are sacred.
- **NEVER move files without explicit approval.** Propose first, act second.
- **NEVER create deeply nested structures.** Two levels max. `projects/acme/` is fine. `documents/pdfs/2026/march/work/` is not.
- **NEVER create generic type-bucket folders.** No `documents/`, `images/`, `spreadsheets/`. Use project folders or inbox.
- **ALWAYS read the index first.** The index tells you what exists. Organizing without it is just shuffling.
- **ALWAYS update the index after moving.** If you moved it, index it. No exceptions.
- **Handle name collisions.** Ask the user---don't overwrite silently.
- **Be honest about uncertainty.** Inbox is the honest answer. "I don't know where this goes" is better than filing it wrong.
- **Explain your reasoning.** "This PDF mentions Acme Corp, which matches your indexed project" beats "Moving PDF to projects/."

## New Project Detection

If you see 3+ unorganized files that clearly relate to the same topic but NO matching project exists in the index:

1. Propose creating a new project folder: "These 4 files all relate to 'website redesign' but I don't see a project for that. Want me to create `projects/website-redesign/` and file them there?"
2. If approved, create the folder, move the files, and add a `## Projects` entry to the index for each file.
3. If declined, move them to `inbox/`.

## Interaction with /ingest

Organize and ingest are complementary:
- **Organize** = bulk sorting of many files by location. Reads content lightly for classification.
- **Ingest** = deep processing of individual files. Reads content fully, adds frontmatter, tags carefully.

After organizing, if files were moved to `training/` directories, suggest: "I moved {N} files to training folders. Want me to run /ingest on them for full tagging and frontmatter?"
