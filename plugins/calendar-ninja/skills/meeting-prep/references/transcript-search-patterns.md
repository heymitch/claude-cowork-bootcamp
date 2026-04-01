# Meeting Recap Search Patterns

How to find meeting recaps and summaries in Gmail. Most recording services email a recap or summary after every call — not a full transcript. The subject line usually says "recap", "summary", or "meeting notes". Search for those terms first, then fall back to "transcript" if nothing comes up.

---

## Service-by-Service Patterns

### Fireflies.ai

**Sender:** `from:fireflies.ai` or `from:app.fireflies.ai`
**Subject patterns:**
- "Meeting notes: [Meeting Title]"
- "[Meeting Title] - Meeting Summary"
- "Your meeting with [Person] is ready"

**Email body contains:**
- Meeting title, date, duration
- Attendee list
- AI-generated summary (key topics)
- Action items
- Link to full transcript on Fireflies

**Gmail search query:**
```
from:fireflies.ai [person name]
from:fireflies.ai [company name]
from:fireflies.ai subject:"meeting notes"
```

---

### Fathom

**Sender:** `from:fathom.video` or `from:app.fathom.video`
**Subject patterns:**
- "Your call with [Person] — Recap"
- "Your call with [Person] — Summary"
- "Meeting recap: [Title]"
- "Meeting summary: [Title]"
- "[Title] — Fathom Recording"

**Email body contains:**
- Call summary with key moments
- Highlighted topics
- Action items
- Link to recording and transcript

**Gmail search query:**
```
from:fathom.video [person name]
from:fathom.video [company name]
from:fathom.video subject:recap
from:fathom.video (recap OR summary)
```

---

### Otter.ai

**Sender:** `from:otter.ai` or `from:app.otter.ai`
**Subject patterns:**
- "Your Otter.ai notes from [Meeting Title]"
- "Meeting notes: [Title]"
- "[Title] — Otter Notes"

**Email body contains:**
- Transcript summary
- Key highlights
- Action items (if detected)
- Link to full Otter transcript

**Gmail search query:**
```
from:otter.ai [person name]
from:otter.ai [company name]
from:otter.ai subject:"meeting notes"
```

---

### Zoom

**Sender:** `from:zoom.us` or `from:no-reply@zoom.us`
**Subject patterns:**
- "Cloud Recording: [Meeting Title]"
- "Recording Available: [Meeting Title]"
- "[Meeting Title] — Transcript Available"

**Email body contains:**
- Recording link (video + audio)
- Transcript download link (if enabled)
- Meeting date, duration, host info
- Passcode for recording access

**Gmail search query:**
```
from:zoom.us subject:recording [person name]
from:zoom.us subject:transcript [person name]
from:zoom.us (recording OR transcript) [company name]
```

---

### Google Meet

**Sender:** `from:meet.google.com` or `from:calendar-notification@google.com`
**Subject patterns:**
- "Meeting notes from [Title]"
- "Transcript for [Title]"
- "Gemini notes: [Title]" (newer Google Meet AI features)

**Email body contains:**
- Meeting summary (if AI notes enabled)
- Transcript link in Google Docs
- Attendee summary
- Key topics detected

**Gmail search query:**
```
from:meet.google.com [person name]
(from:meet.google.com OR from:calendar-notification@google.com) transcript
"meeting notes" from:google.com [company name]
```

---

### Read.ai

**Sender:** `from:read.ai` or `from:app.read.ai`
**Subject patterns:**
- "Meeting Report: [Title]"
- "Your meeting summary — [Title]"
- "[Title] — Read.ai Summary"

**Email body contains:**
- Meeting metrics (talk ratio, engagement)
- Summary and key topics
- Action items with owners
- Sentiment analysis
- Link to full report

**Gmail search query:**
```
from:read.ai [person name]
from:read.ai [company name]
from:read.ai subject:"meeting report"
```

---

### tl;dv

**Sender:** `from:tldv.io` or `from:app.tldv.io`
**Subject patterns:**
- "Your meeting recap: [Title]"
- "[Title] — tl;dv Summary"

**Gmail search query:**
```
from:tldv.io [person name]
from:tldv.io [company name]
```

---

### Grain

**Sender:** `from:grain.com` or `from:grain.co`
**Subject patterns:**
- "Recording ready: [Title]"
- "Your Grain recording — [Title]"

**Gmail search query:**
```
from:grain.com [person name]
from:grain.co [person name]
```

---

## Generic Search (When You Don't Know Which Service)

If you're not sure which recording service someone uses (or if they use one at all), run a broad search:

```
[person name] (recap OR summary OR "meeting notes" OR recording OR transcript)
```

```
[company name] (recap OR summary OR recording OR "meeting notes" OR transcript)
```

```
(from:fireflies.ai OR from:fathom.video OR from:otter.ai OR from:zoom.us OR from:read.ai OR from:meet.google.com OR from:tldv.io OR from:grain.com) [person name]
```

---

## How to Extract Key Info from Transcript Emails

Most transcript emails follow the same structure. Here's what to pull:

1. **Attendees** — Listed at the top. Map names to roles if possible.
2. **Duration** — How long the meeting lasted. Short meetings (15 min) were probably quick check-ins. Long meetings (60+ min) had substance.
3. **Summary** — The AI-generated summary is the highest-value section. Read it first.
4. **Action items** — Most services detect and list these. Check who owns each item.
5. **Key topics** — Services tag main discussion themes. Use these for talking points.
6. **Date** — When the meeting happened. Critical for the "Last Interaction" section of the brief.

---

## Tips

- **Check your spam/promotions folder.** Transcript emails sometimes get filtered. If you find one there, mark it as "Not spam" so future ones land in your inbox.
- **Search by date range.** Add `after:2025/11/01 before:2026/02/20` to limit results to a specific period.
- **Multiple recording services.** Some people use different services for different meeting types (Zoom recordings for sales calls, Fireflies for internal). Search for all of them.
- **Person's name might not appear.** If the meeting title doesn't include their name, search by company name or meeting date instead.
- **Forwarded transcripts.** Sometimes colleagues forward meeting summaries. Search for `[person name] transcript` without the sender filter to catch these.
- **Calendar cross-reference.** If you can see the meeting on your calendar, use the exact meeting title in your Gmail search. That's often the most reliable match.
