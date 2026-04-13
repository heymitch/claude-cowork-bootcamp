---
name: skill-packager
description: Package a completed skill into a Cowork plugin ZIP ready for upload. Say "package my skill" or "zip my skill" or "export skill as plugin" or "make this a plugin".
user-invocable: true
---

# Skill Packager

## Preflight
1. Get the skill directory path. If not provided, ask: "Which skill folder should I package?"
2. Verify the directory exists and contains SKILL.md.

## What the Agent Does

### Step 1: Verify Structure
Check required files:
- SKILL.md exists with frontmatter (`name` and `description`)
- references/ directory exists (if the skill uses reference files)
- All files referenced in SKILL.md actually exist

If SKILL.md is missing, stop: "No SKILL.md found. This isn't a skill yet."

### Step 2: Build Plugin Layout
Create the `.claude-plugin/` directory if it doesn't exist:
```
[plugin-name]/
├── .claude-plugin/plugin.json
└── skills/[skill-name]/
    ├── SKILL.md
    └── references/
```

### Step 3: Generate or Update plugin.json
Create with: name (from frontmatter), version 1.0.0, description (from frontmatter), author (from config.md or ask), license UNLICENSED, skills array listing all SKILL.md paths.

If plugin.json exists, update skills array and description only. Preserve name, author, version. Increment version if re-packaging.

Show plugin.json for approval before saving.

### Step 4: Bundle Into ZIP
Create `dist/` at the plugin root. Build `dist/[plugin-name].zip`.

**CRITICAL: ZIP must be FLAT — `.claude-plugin/` and `skills/` at the ZIP root, no wrapper folder.**

```bash
mkdir -p dist
TEMP=$(mktemp -d)
mkdir -p "$TEMP/.claude-plugin" "$TEMP/skills"
cp .claude-plugin/plugin.json "$TEMP/.claude-plugin/"
cp -R skills/* "$TEMP/skills/"
find "$TEMP" -name ".DS_Store" -delete
find "$TEMP" -name ".git" -type d -exec rm -rf {} + 2>/dev/null
find "$TEMP" -name "node_modules" -type d -exec rm -rf {} + 2>/dev/null
cd "$TEMP" && zip -r "$OLDPWD/dist/$(basename "$OLDPWD").zip" . -x "*.DS_Store"
rm -rf "$TEMP"
```

If you zip from inside the plugin directory instead of a temp dir, Cowork won't find plugin.json and upload will fail with a `.json` error.

### Step 5: Validate
Unzip to temp and verify: plugin.json is valid JSON, skills/ exists, every SKILL.md in plugin.json is present, all references included, no junk files. Fix anything broken.

### Step 6: Summary
Report: plugin name, version, path to .zip, skill count, file count. "Ready to upload to Cowork."

## Rules
- Never package without SKILL.md frontmatter — won't work in Cowork
- Always validate the ZIP after creating — don't ship broken packages
- Exclude system files (.DS_Store, .git, node_modules)
- If untested, suggest: "Want to run skill-tester first?"
- Show plugin.json before saving — user verifies metadata
