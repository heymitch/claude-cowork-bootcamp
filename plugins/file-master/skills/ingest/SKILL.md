---
name: ingesting-files
description: Ingests files into the Coworker knowledge index. Accepts any file — writing samples, company docs, prompts, references — auto-detects the type, files it correctly, tags it with frontmatter metadata, and updates the master index. Trigger phrases include "ingest this", "train on this", "save this reference", "index this file", "add this to my training data".
---

# Ingest

Add files to the Coworker brain. Auto-detect type, file correctly, update the index.

## Workflow

```
Progress:
- [ ] Identify the file(s) to ingest
- [ ] Auto-detect type
- [ ] Confirm type + destination with user
- [ ] Move/copy file to correct location
- [ ] Add frontmatter if markdown
- [ ] Update .coworker/index.md
- [ ] Log the action
```

## Step 1: Identify Files

The user either:
- Points at a specific file: "ingest this" (with a file selected or named)
- Drops files in `inbox/`: "ingest everything in my inbox"
- Pastes content directly: "train on this post I wrote"

If pasted content, save it as a new .md file first.

## Step 2: Auto-Detect Type

Read the file content and classify:

| Type | Signals | Destination |
|------|---------|-------------|
| `voice-sample` | Personal writing, posts, newsletters, emails in the user's voice | `training/voice/` |
| `reference` | Company docs, competitor info, industry data, meeting notes | `training/references/` |
| `prompt` | Instructions, templates, system prompts that worked well | `training/prompts/` |
| `skill` | SKILL.md files, plugin components | `skills/` |
| `project` | Active work documents, drafts, deliverables | `projects/` |
| `output` | Generated content, reports, finished work | `output/` |

## Step 3: Confirm

Tell the user what you detected and where it goes:

> "This looks like a **voice sample** (LinkedIn post, ~400 words, personal tone). I'll file it at `training/voice/linkedin-ai-workflow.md` and tag it as `voice-sample | linkedin, ai, workflow`. Sound right?"

If they correct you, adjust. Never move without approval.

## Step 4: File It

1. Move or copy the file to the correct directory
2. If it's markdown, add frontmatter at the top if not already present:

```yaml
---
type: voice-sample
source: linkedin
tags: [ai, workflow, personal-brand]
date: 2026-03-28
ingested: true
---
```

3. Use a clean filename: lowercase, hyphens, descriptive. `linkedin-ai-workflow-post.md` not `Untitled (3).md`.

## Step 5: Update Index

Append one line to the appropriate section in `.coworker/index.md`:

```
- `training/voice/linkedin-ai-workflow-post.md` | voice-sample | linkedin, ai, workflow | 2026-03-28
```

If the section doesn't exist yet (e.g., first voice sample ever), create the section header:

```
## Voice Samples
- `training/voice/linkedin-ai-workflow-post.md` | voice-sample | linkedin, ai, workflow | 2026-03-28
```

## Step 6: Log It

Append to `.coworker/logs/activity.md`:

```
### 2026-03-28
- Ingested: linkedin-ai-workflow-post.md → training/voice/ (voice-sample)
```

## Batch Ingest

When the user says "ingest everything in inbox" or drops multiple files:

1. Scan all files in `inbox/`
2. Auto-detect each type
3. Show a summary table:

| File | Detected Type | Destination | Tags |
|------|--------------|-------------|------|
| post-draft.md | voice-sample | training/voice/ | writing, draft |
| acme-notes.md | reference | training/references/ | company, acme |
| screenshot.png | reference | training/references/ | image, screenshot |

4. Ask: "This look right? I can adjust any of these before filing."
5. On approval, file all, update index, log everything.

## Non-Markdown Files

For images, PDFs, spreadsheets — file them in the right directory and add an index entry. Don't try to add frontmatter to binary files. The index entry IS the metadata.
