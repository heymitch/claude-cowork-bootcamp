# Cowork Platform Capabilities

What your agent can and can't do inside Cowork. Reference this before designing any skill.

---

## File System

Your agent has full access to your project workspace:
- **Read** any file: text, markdown, JSON, CSV, code, images
- **Write** new files or overwrite existing ones
- **Create** folders and nested directory structures
- **Move, rename, delete** files and folders
- **Access** Desktop, Documents, Downloads on your machine
- **Search** across files by name or content

**Limits:** Cannot access other users' machines or files outside your filesystem.

---

## Tools / MCP Connectors

Each connected tool gives specific capabilities:

| Tool | What It Can Do |
|------|----------------|
| **Gmail** | Read, search, draft, send emails. Manage labels. |
| **Slack** | Read channels, send messages, search history, create canvases |
| **Notion** | Read/write pages, search databases, create entries, update properties |
| **Google Docs** | Read/write documents, format text, insert content |
| **Google Sheets** | Read/write cells, create sheets, format data |
| **Google Slides** | Read slides, create presentations (limited formatting) |
| **Fireflies** | Pull meeting transcripts, search by topic, get summaries |
| **Gamma** | Generate presentations, carousels, slide decks from prompts |
| **Google Calendar** | Read events, create/update calendar entries |
| **Ayrshare** | Post to social media (LinkedIn, Twitter/X, Facebook, Instagram) |
| **Framer** | Read/update site content, manage CMS collections |
| **Supabase** | Query databases, run SQL, manage tables |
| **Vercel** | Deploy sites, check build logs, manage projects |

**Not every user has every tool.** Skills must handle missing connectors gracefully — degrade, don't crash.

---

## Code Execution

- **Run scripts**: bash, Python, Node.js, and more
- **Install packages**: npm, pip, brew (anything CLI-based)
- **Create automation scripts**: write and execute in one flow
- **Process data**: parse CSVs, transform JSON, generate reports
- **Build projects**: scaffold apps, compile code, run tests

**Limits:** Cannot run persistent background processes (daemons, servers that stay running after the conversation ends).

---

## Web Access

- **Search the web** for current information
- **Fetch URLs** and read web page content
- **Download files** from public URLs
- **Read APIs** with public endpoints

**Limits:** Cannot log into websites, fill out web forms, or click buttons in a browser (unless the browser automation tool is connected — most users won't have it).

---

## AI Generation

- **Text**: Write, edit, rewrite, summarize, translate any text content
- **Structured data**: Generate JSON, CSV, tables, outlines from unstructured input
- **Analysis**: Compare documents, find patterns, evaluate quality
- **Presentations**: Use Gamma to generate slides and carousels
- **Images**: Use image generation tools if connected (not default)

---

## What Agents CAN'T Do

Be honest with users about these limits:

- **Can't access apps directly** — no clicking buttons in Figma, Photoshop, Canva, or any desktop app
- **Can't make phone calls or send SMS** — no Twilio, no dialing
- **Can't access hardware** — no camera, microphone, printer, or scanner
- **Can't run persistent background processes** — scripts run and finish, they don't stay alive
- **Can't access other users' machines** — one workspace, one user
- **Can't do real-time monitoring** — no watching for changes continuously
- **Can't process video** — can't edit, trim, or generate video files
- **Can't interact with mobile apps** — no tapping, swiping, or app automation

---

## Skill Constraints

Every skill you build must follow these rules:

- **SKILL.md under 100 lines** for standard skills, under 500 lines for tutor skills
- **Heavy content goes in references/** — templates, examples, domain knowledge
- **Frontmatter required**: `name` and `description` fields. Trigger phrases go in `description`.
- **Skills must DO work by default** — not just describe what could be done
- **Show output before saving** — the user stays in control
- **Handle missing tools gracefully** — check what's available, degrade if needed

---

## "Can I Build a Skill That...?" FAQ

**Q: Can I build a skill that sends emails automatically?**
A: Yes, if Gmail is connected. The skill can draft and send. Best practice: show the draft before sending.

**Q: Can I build a skill that posts to social media?**
A: Yes, if Ayrshare is connected. Supports LinkedIn, Twitter/X, Facebook, Instagram. Show the post for approval first.

**Q: Can I build a skill that reads my meeting notes and creates action items?**
A: Yes. If Fireflies is connected, it pulls transcripts directly. Otherwise, the user pastes or drops a transcript file.

**Q: Can I build a skill that creates presentations?**
A: Yes, if Gamma is connected. It generates full slide decks from a prompt or outline.

**Q: Can I build a skill that edits images or creates graphics?**
A: Limited. If an image generation tool is connected, it can create images from prompts. It cannot edit existing images (no Photoshop-style manipulation).

**Q: Can I build a skill that scrapes websites?**
A: Partially. It can fetch public web pages and extract content. It cannot log into sites, bypass paywalls, or interact with JavaScript-heavy pages.

**Q: Can I build a skill that manages my calendar?**
A: Yes, if Google Calendar is connected. Read events, create new ones, update existing ones.

**Q: Can I build a skill that processes PDFs?**
A: Yes. It can read PDFs, extract text, and work with the content. It cannot edit PDFs in place or fill PDF forms.

**Q: Can I build a skill that talks to my database?**
A: Yes, if Supabase is connected. It can run SQL queries, read/write data, and generate reports from database tables.

**Q: Can I build a skill that automates a multi-step workflow across tools?**
A: Yes. Skills can chain actions: read from Notion, process content, send via Gmail, log to Sheets — all in one flow. Just verify each connector is available.
