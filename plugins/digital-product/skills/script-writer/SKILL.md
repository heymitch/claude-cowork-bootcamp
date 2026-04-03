---
name: script-writer
description: Write bulleted video scripts for a course or video product — lesson-by-lesson outlines with talking points, screenshot markers, demo cues, and energy transitions. Triggers — "write video scripts", "script my course", "create lesson scripts", "video outline"
user-invocable: true
---

# Script Writer

Turn a completed outline into bulleted video scripts, one per lesson. Adapted from the Cowork Bootcamp session-builder — battle-tested across 6 live sessions.

## Process

### Step 1: Gather Inputs

Load:
- `.coworker/index.md` for active project context
- `projects/[product-name]/outline.md` — completed outline from outline-builder (chapters = lessons)
- `projects/[product-name]/product-config.md` — Strategy Brief (audience, transformation)
- `../digital-product/references/ltl-frameworks.md` for structure
- `training/voice/voice-template.md` — if it exists, use the voice profile

If no outline exists, stop: "You need an outline first. Say **outline my product** to build one."

### Step 2: Confirm Format

Ask:
- **How many lessons?** (Default: 1 per chapter from the outline, typically 5-7)
- **Target length per lesson?** (Options: Short 5-8 min, Standard 10-15 min, Deep 20-30 min)
- **Delivery method?** (Pre-recorded solo, pre-recorded screencast, live with audience)

### Step 3: Write Scripts Lesson by Lesson

For each lesson, output a bulleted script in this format:

```
## Lesson [N]: [Title]
Runtime: ~[X] min | Slides: ~[Y]

### HOOK (30 sec)
- [One sentence naming the problem this lesson solves]
- [What they'll have by the end — specific deliverable]

### CONTEXT (1-2 min)
- Where this fits in the overall product
- What they need to have done before this lesson
- "By the end of this lesson, you will have ___"

---
⚡ ENERGY: "Let's get into it."
---

### CONCEPT: [Framework Name] (3-5 min)
- [Core idea in one sentence — 3rd grade reading level]
- [Why it matters — connect to their pain point]
- [Visual: concept card or diagram]
  [SCREENSHOT REQUIRED: diagram of framework]
- MAX 3 slides on this concept. If you need more, split it.

---
⚡ ENERGY: "Now let's actually do this."
---

### ACTION: [What They're Doing] (X min)
- Step 1: [Verb-first instruction]
  [SCREENSHOT REQUIRED: where to click / what to see]
- Step 2: [Verb-first instruction]
  [SCREENSHOT REQUIRED: expected result]
- Step 3: [Verb-first instruction]
  [VIDEO EMBED: pre-recorded demo, 60-90 sec]

💡 Common mistake: [What people get wrong here + fix]

### ACTION: [Second exercise if needed] (X min)
- ...

---
⚡ ENERGY: "Nice. Here's what you just built."
---

### RECAP (1-2 min)
- [Bullet 1: What they learned]
- [Bullet 2: What they built/did]
- [Bullet 3: What's next — leads into next lesson]

### ASSETS
- [SCREENSHOT REQUIRED: list what needs capturing]
- [VIDEO EMBED: list what needs pre-recording]
- [TEMPLATE: any downloadable template for this lesson]
```

### Step 4: Adapt by Delivery Method

**Pre-recorded solo** (talking head + slides):
- Tighter scripts — no filler, no "um" space
- Every slide needs a visual (no text-only slides)
- Record in sections, not one take
- Mark cut points: `[CUT]` between sections

**Pre-recorded screencast** (screen recording + voiceover):
- Every step needs a `[SCREENSHOT REQUIRED]` or `[VIDEO EMBED]` marker
- Narrate what you're clicking — "Click the blue button in the top right"
- Show the result after each action — "You should now see ___"
- Pause points: `[PAUSE 2 SEC]` to let viewer follow along

**Live with audience** (webinar/bootcamp style):
- Add engagement questions: `DROP IN THE CHAT: [question]`
- Warm-up questions escalate: logistics → broad → narrow → specific
- One question per slide, never stack
- Add `[WAIT FOR RESPONSES: 15 sec]` markers
- Energy transitions between every block

### Step 5: Script Rules

Apply these to every lesson:

**Kill theory.** If the viewer hasn't DONE something by minute 5, there's too much concept. Move theory to a companion PDF or reference doc — the video is for action.

**3 slides per concept max.** If you need more slides to explain it, the concept is too complex. Split it or simplify it.

**One idea per slide.** If a bullet point needs a comma to explain two things, it needs two slides.

**3rd grade reading level** for all on-screen text. Complex ideas, simple words. Viewers are watching, not reading.

**Screenshots > descriptions.** Never say "go to the settings page and find the toggle." Show the settings page with an arrow pointing at the toggle.

**Pre-record demos.** Never script a live demo. Record it in Tella or Loom, embed the clip. Live demos fail, recordings don't.

**Energy transitions are mandatory.** 3-5 per lesson. Full-screen, 1-4 words, giant text. Purpose: give the viewer a breath, signal a shift. Examples:
- "Let's get into it."
- "Now the fun part."
- "Hands on."
- "Almost there."
- "That's it. You did it."

**Every action step needs a companion visual.** No exceptions. If you can't screenshot it, you can't teach it in video.

### Step 6: Compile and Deliver

Save all scripts to `projects/[product-name]/video-scripts.md` with a table of contents at the top.

Include a production checklist:
```
## Production Checklist
- [ ] Screenshots captured for all [SCREENSHOT REQUIRED] markers
- [ ] Demo videos recorded for all [VIDEO EMBED] markers
- [ ] Templates created for all [TEMPLATE] markers
- [ ] Audio quality check (no background noise, consistent volume)
- [ ] Each lesson under target runtime
- [ ] Watched each lesson as a student — did I DO something?
```

## Handoff

After scripts are approved:
1. Save scripts to `projects/[product-name]/video-scripts.md`.
2. Update `projects/[product-name]/product-config.md` — check "Content written", note "Format: video scripts" in Scope.
3. Update `.coworker/index.md` — note "Video scripts complete" next to the product.
4. Say: "Scripts done. Next up: **design my ebook** if you want a companion guide, or **design my product** for cover art, or skip to **launch my product** if the videos are your whole product."

## Rules
- Write ONE lesson at a time. Show it, get approval, then write the next.
- Bullet points only. Never write prose paragraphs — this is a speaking outline, not an essay.
- Every lesson must have at least one ACTION block where the viewer does something.
- Mark every visual asset needed. The script is also the production shot list.
- Match voice from `training/voice/voice-template.md`. If none, use direct and conversational — like explaining to a smart friend.
- If the outline has more than 7 chapters, suggest grouping into modules (3-4 lessons per module).
- Always write to `projects/[product-name]/` — never to workspace root.
