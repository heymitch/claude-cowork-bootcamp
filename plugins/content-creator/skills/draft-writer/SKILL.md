---
name: draft-writer
description: Write a full content draft in your voice for any platform — newsletter, LinkedIn post, Twitter thread, YouTube script, or Substack note. Say "write the draft", "draft this", "write it", "write my newsletter", "write a LinkedIn post", or "write a Twitter thread".
user-invocable: true
---

# Draft Writer

Takes an approved outline and writes a full draft in the user's voice for the specified platform.

## How to Run

- "Write the draft"
- "Draft this"
- "Write my newsletter"
- "Write a LinkedIn post about [topic]"
- "Write a Twitter thread on [topic]"
- "Write a YouTube script for [topic]"
- "Write a Substack note about [topic]"

## Preflight

Check silently. Never block the user from starting.

1. **Platform determined?** If not explicit, ask: "Which platform — newsletter, LinkedIn, Twitter thread, YouTube script, or Substack note?"
2. **config.md exists?** If not → ask: "Want to create a quick business blueprint? Takes 5 minutes." Proceed without if they skip.
3. **Voice trained?** Check for `- [x] Voice Training completed`. If not → write clean and direct. Offer training after first draft.
4. **Outline ready?** If no outline was provided, ask: "What's the topic? I can build a quick outline first, or you can give me a rough structure."

## What the Agent Does

### 1. Determine Platform and Load Rules

Identify the platform from context or the user's request.

Load the matching platform guide:
- Newsletter → `references/platforms/newsletter.md`
- LinkedIn → `references/platforms/linkedin.md`
- Twitter/thread → `references/platforms/twitter.md`
- Substack note → `references/platforms/substack-notes.md`
- YouTube script → `references/platforms/youtube-script.md`

Read the format rules, length targets, and structural patterns before writing a single word.

### 2. Load Voice Profile

Read config.md. Pull Voice Template, Voice DNA, or Voice Samples — whatever voice data exists. Study `references/voice-matching-rules.md`.

Extract:
- Sentence length patterns (short/long mix)
- Vocabulary register (casual vs. formal, specific words they use)
- Tone position (sarcastic, earnest, blunt, etc.)
- Signature phrases
- Power Words / Avoid Words (if voice training completed)

If config.md has no voice data, write clean and direct. Do not ask about voice training mid-draft.

### 3. Write the Draft

Follow the outline section by section. For each section:
- Write in the user's voice, not "AI writing voice"
- Hit the key points in the outline
- Use specific details, examples, stories — never vague claims
- Follow the format rules from the platform guide exactly
- Vary sentence length (mix short punchy sentences with longer ones)

### 4. Show the Draft

Display the full draft. Ask: "How's this? Want me to adjust anything before we save it?"

### 5. Handle Revisions

Make the specific edits requested. Show the updated version. Ask again: "Good to save?" Repeat until approval.

### 6. Save

On approval, save immediately — before hooks or subject lines.

**Try in this order (use the first that works):**
1. Config preference — if config.md specifies a save target, use it
2. Notion — follow `references/notion-navigator.md`. Create a new page, title with working title, content as markdown
3. Local markdown — save as `YYYY-MM-DD-{platform}-{slug}.md` in working directory

### 7. Hooks / Subject Lines

After saving, hand off to `subject-line-generator` for:
- Newsletter → subject line options
- LinkedIn → hook line options (the first line before "see more")
- Twitter → tweet opener options
- YouTube → title options
- Substack note → already short; offer to sharpen the opener instead

## Rules

- Never save without explicit approval. "Looks good" or "save it" counts. Silence does not.
- Use the voice profile for every sentence. Generic prose means you skipped it.
- No AI-tell phrases. See `references/voice-matching-rules.md` Anti-AI Patterns section.
- Hit the length target for the platform. Too short feels thin. Too long loses the reader.
- If the outline is weak, say so before writing: "This outline is missing [X] — want me to add it first?"
