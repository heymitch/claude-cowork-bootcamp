---
name: skill-packager
description: Package a completed skill for distribution. Picks the right format — inline copy, .skill file, or plugin bundle — based on what the skill actually contains. Say "package my skill" or "ship this skill" or "export my skill" or "make this shareable".
user-invocable: true
---

# Skill Packager

Pick the **lowest-overhead** delivery format that fits the skill. Three options. Most skills are Option 1.

## Preflight
1. Get the skill directory path. If not provided, ask: "Which skill folder should I package?"
2. Verify the directory exists and contains SKILL.md.
3. Read SKILL.md and list what's in the skill folder.

## Decision Tree

Pick the format FIRST, then package:

| What the skill has | Option |
|--|--|
| Single SKILL.md, no bundled files | **Option 1: Inline** |
| Single skill with references/, scripts/, or assets | **Option 2: .skill file** |
| 2+ related skills for team distribution | **Option 3: Plugin bundle** |
| Anything else | **Option 1** |

If unsure, default to Option 1. Escalate only when the skill genuinely needs more.

---

## Option 1 — Inline (Default for Most Skills)

If the skill is a single SKILL.md with no references, scripts, or assets, don't package anything at all. Present the full SKILL.md in the conversation.

Cowork automatically shows a **"Copy to your skills"** button when a SKILL.md appears in the chat. The user clicks it once and the skill is installed. No files, no uploads, no manual steps.

### What to do:
1. Read the full SKILL.md content
2. Display it in the conversation as a code block
3. Tell the user: "Click the 'Copy to your skills' button above the code block to install this in Cowork."
4. Suggest a trigger phrase to test it

That's it. Done.

---

## Option 2 — .skill File (For Skills with Bundled Files)

If the skill has a `references/` directory, `scripts/`, `assets/`, or any helper files that need to travel with the SKILL.md, package it as a `.skill` file. This is a validated archive format — not a plain zip.

### Never rename a .zip to .skill. Use the packaging script.

### What to do:

1. Verify structure:
   - SKILL.md exists at the skill folder root
   - Frontmatter has `name` and `description`
   - Any files referenced in SKILL.md actually exist

2. Run the packaging script:
   ```bash
   python -m scripts.package_skill /path/to/skill-folder /path/to/output-dir
   ```

   This runs validation first, then produces `skill-name.skill` in the output directory.

3. If validation fails, fix the errors and re-run. Common issues:
   - Missing `name` or `description` in frontmatter
   - Unknown frontmatter keys (only allowed: name, description, license, metadata, compatibility, allowed-tools)
   - Referenced files that don't exist

4. After packaging, tell the user:
   - The path to the `.skill` file
   - How to install: drag the `.skill` file into Cowork's skill upload area
   - A trigger phrase to test it

---

## Option 3 — Plugin Bundle (Multi-Skill Team Distribution ONLY)

**⚠️ Do NOT add `.claude-plugin/` to single personal skills.** This is the #1 mistake in skill packaging.

Plugin bundles are for:
- 2+ related skills that ship together as a coherent product
- Distribution to multiple users (teams, marketplaces, bootcamps)
- Anything with its own `plugin.json` manifest

Plugin bundles are NOT for:
- Individual personal skills
- First drafts you're testing on yourself
- Skills with a single SKILL.md and no dependencies

### What to do:

1. Verify structure:
   ```
   plugin-name/
   ├── .claude-plugin/
   │   └── plugin.json
   └── skills/
       ├── skill-a/
       │   ├── SKILL.md
       │   └── references/
       └── skill-b/
           └── SKILL.md
   ```

2. Create `plugin.json` with:
   - `name`: lowercase alphanumeric + hyphens only
   - `version`: semver
   - `description`: what the plugin does
   - `author`: name (pull from config.md if available)
   - `license`: UNLICENSED unless specified

   Show the plugin.json for approval before saving.

3. Build the ZIP:
   ```bash
   cd plugin-name && zip -r ../plugin-name.zip .claude-plugin/ skills/ \
     -x "*.DS_Store" -x "*__pycache__*" -x "*.pyc"
   ```

4. Validate by unzipping to a temp directory and checking:
   - `plugin.json` is valid JSON
   - `skills/` exists with all sub-folders
   - No junk files (`.DS_Store`, `.git`, `node_modules`, `dist/`)

5. After packaging, tell the user:
   - The path to the `.zip` file
   - How to install: **Customize > Personal Plugins > + > Upload Plugin**
   - Skill count and the trigger phrases

---

## Rules

- **Default to Option 1.** Most personal skills don't need packaging at all. The inline copy-to-skills button handles them.
- **Never use `.plugin.zip` for single personal skills.** That's Option 3 applied to an Option 1 or 2 skill. Wrong tool.
- **Always validate before shipping.** Broken packages waste everyone's time.
- **Show the user what you're about to do** — read the SKILL.md, explain which option you're picking and why, then execute.
- **If the user asks for a specific format** (e.g., "package this as a plugin"), respect it but explain the trade-off if they're over-escalating.
- **Exclude system files** — `.DS_Store`, `.git`, `node_modules`, `__pycache__`, `dist/`.
