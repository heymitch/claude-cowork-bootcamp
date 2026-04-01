# Connector Setup Guide

This guide walks through connecting each data source to power meeting prep. You don't need all of them. Even one connector makes briefs dramatically better. Without any connectors, the skill still works — you just paste your own notes.

## Priority Order

If you only connect one thing, connect **Gmail**. It gives you 80% of the value. Here's why:

1. **Gmail** — Email threads + meeting transcript emails (Fireflies, Fathom, etc. all email summaries). One connector, two data sources.
2. **Calendar** — Meeting details, attendees, links. Quick setup, immediate value.
3. **Google Docs/Drive** — Shared proposals, documents, contracts.
4. **Slack** — Channel mentions, threads, DMs about people and projects.
5. **Fireflies** — Full meeting transcripts. Rich data, but Gmail already captures summaries.

---

## Gmail

### What It Enables
- **Email threads** with the person or company (recent conversations, proposals sent, replies)
- **Meeting transcript emails** from services like Fireflies, Fathom, Otter, Zoom, and Read.ai (these services automatically email summaries after every call — Gmail catches them all)
- **Scheduling history** (emails about booking, rescheduling, cancellations)

### How to Connect in Cowork
1. Open Cowork settings
2. Go to Integrations > Gmail
3. Click "Connect Gmail"
4. Sign in with your Google account
5. Grant read-only access to emails

### Permissions Needed
- Read-only access to Gmail messages
- The agent searches your email but never sends, deletes, or modifies anything

### What the Agent Can Do
- Search emails by sender, recipient, subject, or keywords
- Read email content and attachments
- Find meeting transcript emails from recording services

### What the Agent Cannot Do
- Send emails on your behalf
- Delete or modify emails
- Access drafts (unless specifically granted)

### Setup Time
2 minutes

### Troubleshooting
- **"No emails found"** — Check that the person's email address matches what's in your inbox. Try searching by company domain instead.
- **"Permission denied"** — Reconnect the integration and make sure you selected the right Google account.
- **Slow results** — First search after connecting can take 10-15 seconds. Subsequent searches are faster.

---

## Calendar

### What It Enables
- **Meeting details** — title, time, duration, location/link
- **Attendee list** — who's invited, who accepted
- **Meeting description** — agenda notes, prep links
- **Recurring meeting history** — past instances of the same meeting

### How to Connect in Cowork
1. Open Cowork settings
2. Go to Integrations > Google Calendar
3. Click "Connect Calendar"
4. Sign in with your Google account
5. Grant read-only access to calendar events

### Permissions Needed
- Read-only access to calendar events
- The agent reads event details but never creates, modifies, or deletes events

### What the Agent Can Do
- Read upcoming meeting details
- See past meeting dates and times
- Pull attendee lists and meeting descriptions

### What the Agent Cannot Do
- Create or modify calendar events
- Send calendar invitations
- Access other people's calendars

### Setup Time
1 minute

### Troubleshooting
- **"No meeting found"** — Make sure the meeting is on the Google Calendar connected to Cowork, not a secondary calendar.
- **Wrong time zone** — Check your Google Calendar timezone settings.

---

## Google Docs / Drive

### What It Enables
- **Shared documents** — proposals, contracts, project plans you've shared with the person
- **Recent edits** — see if they've been active in shared docs
- **Document content** — pull key sections from relevant files
- **Folder access** — find client folders with organized materials

### How to Connect in Cowork
1. Open Cowork settings
2. Go to Integrations > Google Drive
3. Click "Connect Google Drive"
4. Sign in with your Google account
5. Grant read-only access to files

### Permissions Needed
- Read-only access to Google Drive files
- The agent reads documents but never creates, edits, or deletes them

### What the Agent Can Do
- Search for documents by name or content
- Read document text
- See sharing history (who has access)
- Find recently modified files

### What the Agent Cannot Do
- Create or edit documents
- Delete files
- Share documents with others

### Setup Time
2 minutes

### Troubleshooting
- **"No documents found"** — The person's name might not be in the document title. Try searching by company name or project name.
- **"Can't read file"** — Some file types (PDFs, images) may not be searchable by content. The agent can still find them by name.

---

## Slack

### What It Enables
- **Channel mentions** — times the person or company was mentioned in channels
- **Threads** — conversations about the person, project, or company
- **DMs** — direct message history with the person (if applicable)
- **Shared links and files** — things posted about or shared with the person

### How to Connect in Cowork
1. Open Cowork settings
2. Go to Integrations > Slack
3. Click "Connect Slack"
4. Select your workspace
5. Authorize the app

### Which Workspaces to Connect
- Your primary work workspace (where you talk about clients and projects)
- Client shared workspaces (if you use Slack Connect or shared channels)
- Skip personal or social workspaces — they won't have meeting context

### Permissions Needed
- Read access to channels you're a member of
- Read access to DMs
- The agent searches messages but never sends, edits, or deletes anything

### What the Agent Can Do
- Search messages by person, keyword, or channel
- Read thread conversations
- Find shared files and links

### What the Agent Cannot Do
- Send messages
- Join new channels
- Access channels you're not a member of

### Setup Time
3 minutes

### Troubleshooting
- **"No results"** — Slack search only covers channels you're a member of. If the conversation happened in a channel you left, you won't see it.
- **"Wrong workspace"** — Make sure you connected the right Slack workspace. You can connect multiple workspaces.

---

## Fireflies

### What It Enables
- **Full meeting transcripts** — word-for-word records of past meetings
- **Speaker identification** — who said what
- **Meeting summaries** — AI-generated summaries with action items
- **Topic detection** — key topics discussed

### How to Connect in Cowork
1. Open Cowork settings
2. Go to Integrations > Fireflies
3. Click "Connect Fireflies"
4. Sign in with your Fireflies account
5. Authorize API access

### How Transcripts Flow
Fireflies records your meetings (Zoom, Google Meet, Teams) and does two things:
1. **Emails you a summary** after each call (caught by Gmail connector)
2. **Stores full transcripts** in Fireflies (accessed by Fireflies connector)

Gmail gives you the summary. The Fireflies connector gives you the full word-for-word transcript. Both are useful. The summary is usually enough for brief prep.

### Permissions Needed
- Read access to transcripts
- The agent reads transcripts but never records, deletes, or modifies them

### What the Agent Can Do
- Search transcripts by participant, date, or keyword
- Read full transcript text
- Pull meeting summaries and action items

### What the Agent Cannot Do
- Record meetings
- Delete transcripts
- Modify summaries

### Setup Time
3 minutes

### Troubleshooting
- **"No transcripts found"** — Fireflies only records meetings where the bot was invited. Check your Fireflies dashboard to see which meetings were recorded.
- **"Transcript is empty"** — Sometimes recording fails silently. Check the Fireflies app for recording status.
- **Already have transcripts in Gmail?** — You might not need this connector. Gmail captures the email summaries automatically. The Fireflies connector adds full word-for-word transcripts, which is richer but not always necessary.

---

## No Connectors? No Problem.

The meeting prep skill works without any connectors. Here's what changes:

**With connectors:** The agent automatically pulls emails, messages, documents, and transcripts to build your brief.

**Without connectors:** The agent asks you to paste or describe what you know. You can:
- Paste email threads
- Paste Slack messages
- Describe your relationship and past conversations
- Share any notes you have

The brief quality depends on what you provide, but the structure and analysis are the same. You still get talking points, open item tracking, and watch-for flags.

**Start without connectors, add them later.** Every connector you add makes future briefs faster and more complete.
