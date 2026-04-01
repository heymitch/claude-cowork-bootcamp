---
name: topic-scanner
description: Find content topic ideas by scanning recent notes and conversations for any platform. Say "find content topics", "what should I write about", "scan for ideas", "content ideas", "newsletter topics", "LinkedIn post ideas", or "what should I post about".
user-invocable: true
---

# Topic Scanner

Finds your strongest content topic for this week. Scans your recent notes, surfaces patterns, and ranks the best candidates.

## How to Run

- "Find content topics"
- "What should I write about this week?"
- "Scan for ideas"
- "What should I post about?"
- "Content ideas for LinkedIn"
- "Newsletter topics"

## What the Agent Does

### 1. Determine Target Platform

If the user specifies a platform, note it — format suggestions in Step 3 will match. If no platform is specified, generate platform-agnostic topics and suggest which platform fits each one best.

### 2. Gather Raw Material

Do ALL of these automatically. Never ask permission for any source.

**Notion (automatic if tools are loaded):**
- Search for notes, pages, and database entries created or modified in the past 7 days
- Look for highlights, bookmarks, saved articles, and journal entries
- Pull in any draft ideas or "someday" lists
- If Notion tools aren't loaded, skip silently

**Web search (automatic, always):**
- Search for current trends, recent articles, and data points in the user's niche
- Look for what's being discussed right now — fresh angles beat stale takes
- Surface stats, quotes, or examples the user can reference
- Cross-reference with Notion notes (if available) to find where experience meets trend
- Do NOT ask "should I search?" — just search

**User input (only if no Notion notes AND no topic was given):**
- Ask: "What have you been thinking about this week? Drop topics, paste notes, or tell me what conversations keep coming up."
- Also ask: "Anything you disagreed with recently? A post, article, or take that bugged you?"
- Work with whatever they give, then web search to enrich it.

### 3. Find Signal Patterns

Scan raw material for these signals (strongest to weakest):

1. **Repeated mentions** — Topics in 3+ notes or conversations. If you keep coming back to it, it matters.
2. **Emotional energy** — Notes with strong opinions, frustration, excitement, or surprise. Flat observations make flat content.
3. **Contrarian angles** — Ideas where your take disagrees with common wisdom. These get the most engagement.
4. **Teaching moments** — Something you learned recently that your audience hasn't learned yet.
5. **Questions received** — Things people are asking you about. If 3 people ask, 300 are wondering.

### 4. Output Topic Candidates

Present 3-5 ranked candidates. For each one:

```
**[Rank]. [Topic Name]**
- Angle: [The specific take or argument — not just the subject, the POINT]
- Why it's strong: [Which signal pattern? Why now?]
- Potential hook: [A draft opening line showing where this could go]
- Best platform: [Newsletter / LinkedIn / Twitter thread / YouTube / Substack note — with one-line reason]
```

### 5. Let Them Pick

After presenting candidates, ask: "Which one should we build? And which platform?" If they pick one, hand off to outline-builder.

## Rules

- Never suggest a topic without an angle. "AI" is a topic. "Most people use AI wrong because they're automating the wrong tasks" is content.
- If notes are thin, say so. Don't inflate weak ideas into strong candidates.
- Always include at least one contrarian or opinion-driven angle. Safe topics get low engagement.
- Rank by strength, not by what sounds impressive. Simple ideas with emotional energy beat complex ideas with none.
- If they have no notes and no ideas, prompt: "What frustrated you this week? What advice did you give someone? What did you change your mind about?"
