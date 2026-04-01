---
name: social-hooks
description: Create social media posts to promote your content across platforms. Say "promote my content", "social posts", "share my newsletter", "promote this post", "create share posts", or "help me share this".
user-invocable: true
---

# Social Hooks

Creates 3 social media posts to promote your content. Each post stands alone as valuable content — not just "go read my thing."

## How to Run

- "Promote my content"
- "Social posts for my newsletter"
- "Create share posts for this"
- "Help me share this on social"
- "Promote my LinkedIn article"

## What the Agent Does

### 1. Get the Content

Needs the finished piece or a draft. Can be:
- The draft from this session (if draft-writer just ran)
- A pasted piece
- A link to the published version
- A summary of the key ideas

If given nothing, ask: "Paste the content or tell me what it's about so I can write promo posts."

### 2. Load Voice Profile and Platform Guides

Read config.md for voice and tone. Load:
- `references/platforms/linkedin.md` for the LinkedIn post
- `references/platforms/twitter.md` for the Twitter posts

The social posts must match the same voice as the original content.

### 3. Extract the Hook

Before writing posts, identify:
- **The single most interesting claim** in the piece
- **The most surprising fact or story** that would stop the scroll
- **The key takeaway** a reader would share with a friend

These become the raw material for the posts.

### 4. Write 3 Posts

**Post 1: LinkedIn**
- Length: 800-1,200 characters
- Structure: Hook line (bold claim or question) → 3-5 lines of context → key insight from the content → soft reference to the full piece with link placeholder `[LINK]`
- Must deliver value on its own. Someone who never clicks should still learn something.
- End with a question to drive comments.
- Follow formatting rules from `references/platforms/linkedin.md` (short paragraphs, line breaks, max 3 hashtags).

**Post 2: Twitter/X — Single tweet**
- Length: Under 280 characters including `[LINK]`
- Structure: One punchy line + link
- Should be quotable — something people would retweet without the link
- No hashtags unless their voice profile uses them

**Post 3: Twitter/X — Thread (3 tweets)**

```
Tweet 1: [Hook — boldest claim or most surprising insight. End with "A thread:"]

Tweet 2: [Key argument or story, compressed. One paragraph.]

Tweet 3: [Takeaway + link. "Full breakdown: [LINK]"]
```

Each tweet must be under 280 characters.

### 5. Present All Three

Show all posts clearly labeled. Add:

"These are ready to copy-paste. Want me to adjust the tone, shorten anything, or write alternatives?"

## Rules

- Every post must stand alone as valuable. "New content just dropped, go read it" is lazy and gets no engagement.
- Pull the most interesting or contrarian part. Not the intro. Not the CTA. The MEAT.
- Match the user's voice. Casual on social → keep it casual. More polished → match that.
- No generic engagement bait: "What do you think?" is fine. "Like and share if you agree!" is not.
- LinkedIn and Twitter have different cultures. LinkedIn posts can be longer and story-driven. Twitter rewards compression and wit.
- Include `[LINK]` as a placeholder. Don't invent URLs.
- Don't use emojis unless the user's voice profile shows they use them on social.
