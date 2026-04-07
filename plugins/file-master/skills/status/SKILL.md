---
name: workspace-status
description: Quick status check — shows what's in your workspace folder, recent activity from logs, and your config summary. A snapshot of your workspace at a glance. Triggered by "status", "what's in my folder", "show me my files", "workspace overview", "what have we done", "catch me up".
user-invocable: true
---

# Status Skill

## Workflow

### Step 1: Load context

Read `.coworker/config.json` silently. If it doesn't exist, show a minimal status (just the folder tree) and suggest running `/setup`.

### Step 2: Build the status report

Gather three sections in parallel:

**A. Folder Contents (always show)**

List the workspace directory as a clean tree view. Show folders and files, but:
- Collapse `.coworker/` to just `.coworker/ (workspace brain)`
- Skip OS junk (`.DS_Store`, `Thumbs.db`)
- If more than 30 files, summarize by folder instead of listing every file

**B. Recent Activity (if logs exist)**

Read the 3 most recent files from `.coworker/logs/` (sorted by filename date). For each, extract:
- Date
- What was done (one-liner summary)
- Key stats (files moved, etc.)

If no logs exist, say "No activity logged yet."

**C. Config Summary (if config exists)**

From `.coworker/config.json`, show:
- Name and role
- Organization preference
- Any notes

### Step 3: Present the report

Format as a clean, scannable block:

```
## Workspace Status

**{name}** — {role}
Organization: {preference}

### Folder Contents
{tree view}

### Recent Activity
- {date}: {summary}
- {date}: {summary}
- {date}: {summary}

### Quick Stats
- {total files} files across {total folders} folders
- Last organized: {date or "never"}
```

### Step 4: Offer next actions

Based on what you see, suggest 1-2 things:
- If lots of loose files at root → "Looks like some files could use organizing. Want me to run /organizing-files?"
- If no logs yet → "Your workspace is fresh — try /organizing-files to get started."
- If everything's tidy → "Looking clean. Nothing to flag."
- If config is missing → "Run /setup to personalize your workspace."

## Rules

- **Read-only.** Status never modifies files, folders, or config.
- **Fast.** This should feel instant. Don't over-explain.
- **Scannable.** Bullet points and short lines. No paragraphs.
- **Honest.** If the folder is messy, say so (nicely). That's what organize is for.
