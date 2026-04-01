---
name: voice-training
description: Train your agent on your unique writing voice using a deep 8-step analysis. Builds a complete Voice Template from your real writing. Say "train on my voice", "learn my writing style", or "build my voice profile".
user-invocable: true
---

# Voice Training (Builder)

Runs the full voice training pipeline. The student should feel like they're having a conversation with Cole, not filling out a form. Each step flows naturally into the next. Never say "Step 1" — just guide them.

## Preflight

Run silently. Never block.

1. **Voice samples exist?** Read `.coworker/index.md` to check if voice samples exist in `training/voice/`. If none found, no preflight message needed — proceed to gathering.
2. **Already trained?** Check if `training/voice/voice-template.md` exists. If yes: "Oh nice, you already have a voice profile from before. Want to start fresh with new samples, or just tune up what we've got?"

## Flow

Execute skills in sequence. Each step builds on previous outputs.

### 1. Gather Samples
Execute `skills/voice-dna-extractor/sub-skills/sample-gatherer/SKILL.md`.

### 2. Extract Voice DNA
Execute `skills/voice-dna-extractor/SKILL.md` (skip sample gathering — already done).

### 3. Profile Archetypes
Execute `skills/archetype-analyzer/SKILL.md`.

### 4. Analyze Vocabulary
Execute `skills/vocabulary-analyzer/SKILL.md`.

### 5. Map Sentence Fingerprint
Execute `skills/sentence-fingerprint/SKILL.md`.

### 6. Find Quirks
Execute `skills/quirk-injector/SKILL.md`.

### 7. Calibrate Tone
Execute `skills/tone-grid-calibrator/SKILL.md`.

### 8. Compile Voice Template
Execute `skills/voice-template-compiler/SKILL.md`.

### 9. Test & Refine
Execute `skills/mimic-and-modify/SKILL.md`.

### Save
Save the complete Voice Template to `training/voice/voice-template.md`.
Update `.coworker/index.md` with voice sample count and a note that the voice template exists.
Say: "And we're done! Your Voice Template is saved. From now on, everything I write will use it. The cool thing is, this isn't locked in forever — you can say 'update my vocabulary' or 'recalibrate my tone' anytime to fine-tune it."

## Rules

- Execute ALL pipeline steps in sequence
- Do not skip steps to reduce processing time
- Save only after full pipeline completion and user approval
- Flag weak results honestly with recommended remediation (more samples, re-analysis, etc.)
- Preserve analysis quality across all steps
