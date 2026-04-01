---
name: meeting-to-content
description: Turn today's meetings into content. Pulls meeting transcripts and notes, extracts the best moments, interviews you about angles, then drafts posts in your voice. Say "content from meetings", "what did I talk about today", "turn my meetings into posts", "end of day content review", "meeting content scan", "what's worth posting from today", or "mine my meetings".
user-invocable: true
---

# Meeting to Content

Closes the loop between your calendar, your files, and your content pipeline. Meetings are where your best thinking happens—this skill surfaces it before it disappears.

**The loop:**
- Session 1 (File Master) → files your transcripts and notes
- Session 2 (Content Creator) → writes in your voice
- Session 3 (Calendar Ninja) → **this skill** — meetings generate the raw material

## Workflow

### Step 1: Gather Today's Meetings

Pull today's calendar events using the Google Calendar connector.

For each meeting found, search in this order:
1. **File Master index** — search workspace for transcript files matching attendee names or meeting title
2. **Gmail** — threads with meeting attendees from today (subject lines, summaries)
3. **Fathom/Otter/Zoom** — ask the user if any summary links are available
4. **Manual notes** — ask if the user took notes anywhere

If transcripts or notes are found, proceed. If not, ask:
> "I found [N] meetings today but no transcripts or notes. Did you write anything down? Paste it here or point me to the file."

If no meetings exist today, stop here: "No meetings found for today. Nothing to extract."

### Step 2: Extract Content-Worthy Moments

Read `references/extraction-patterns.md` before scanning.

For each transcript or set of notes, identify:
- Strong opinions or hot takes stated with conviction
- Stories or anecdotes with a beginning, a middle, and a point
- Frameworks or mental models explained in the meeting
- Surprising data points or stats mentioned
- Contrarian positions or pushback the user gave
- Moments where the user explained something clearly—"the way I think about it..."
- Topics that appeared in two or more meetings today

Skip: internal politics, logistics, confidential business details, small talk, anything that doesn't generalize beyond this meeting.

Compile a ranked shortlist. Lead with the strongest angle.

### Step 3: Interview the User

Read `references/interview-questions.md` before starting.

Do not dump a list. Present each extracted moment as a potential post and ask a targeted question:

> "You said [paraphrase] in your meeting with [person/company]. Is that something your audience would find surprising?"
> "The story about [X]—could you tell that publicly? It would make a strong LinkedIn post."
> "You explained [concept] really clearly to [attendee]. Want to write that up?"
> "[Topic] came up twice today. Seems like it's on your mind—worth a post?"

Rules:
- Max 5 questions per session. Stop after 5, even if there are more angles.
- Lead with the strongest angle first.
- Accept "skip" or "no" gracefully. Move on without re-asking.
- If the user says "that's internal"—drop it immediately, never reference it again.
- If the user expands on an answer with energy—that's the post. Say "That's the angle. Let me draft that."

### Step 4: Generate Content

For each approved angle:

1. Suggest a platform: stories → LinkedIn, sharp takes → Twitter/X, frameworks → newsletter
2. Load the platform reference from content-creator's `references/platforms/{platform}.md` if available
3. Load the user's voice profile if a `config.md` exists in the workspace
4. Write a draft using the extraction as the source material—not generic prose
5. Present the draft for approval before doing anything with it

If content-creator is not installed, write the draft inline using the platform's standard format.

### Step 5: File Everything

After the user approves content:
- Save drafts to the user's content workspace or Notion
- File the raw meeting notes in the workspace index (File Master can find them later)
  - Use path: `meetings/YYYY-MM-DD/[meeting-name].md`
- Log what was created:
  > "Created [N] content pieces from today's meetings: [list with platform and source meeting]"

## Scheduled Task Mode

When triggered automatically at end of day:
- Steps 1–2 run in the background
- Step 3 presents the interview questions when the user opens the session
- Steps 4–5 run after the user responds
- If no meetings today, skip silently—no notification needed

## Rules

- Never publish without explicit user approval
- Always ask before treating anything as public—default assumption is internal
- Don't overwhelm. The best sessions produce 1–2 content pieces, not 10
- Voice profile first. If no config exists, write clean and direct, offer to set up voice after
- File the raw notes regardless of whether content gets created—transcripts are always worth keeping
