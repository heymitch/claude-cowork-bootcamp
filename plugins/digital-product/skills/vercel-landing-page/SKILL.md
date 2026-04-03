---
name: vercel-landing-page
description: Build and deploy a landing page to Vercel from a description, Notion content, or product brief. Say "Build me a landing page for [product]" or "Deploy a sales page".
user-invocable: true
---

# Vercel Landing Page

Build a working landing page and deploy it live to the internet — from a description, product brief, or Notion content.

## How to Run
- "Build me a landing page for [product/offer]"
- "Deploy a sales page for my bootcamp"
- "Turn this Notion page into a live landing page"

---

## Preflight Check (Run Every Time)

Run through this silently. Only speak up if something is missing.

### 1. Load workspace context
Read `.coworker/index.md` for active project context. Then check for the product config at `projects/[product-name]/product-config.md`.

### 2. Does business-blueprint.md exist?
Check `training/references/business-blueprint.md` (also check for legacy `config.md` in workspace root).
- **If missing:** Continue anyway — ask for product details directly. After the page ships, mention: "Tip: Set up your business blueprint so future pages use your voice and branding automatically."
- **If exists:** Load business context.

### 3. Is the Vercel MCP plugin connected?
Check for Vercel MCP tools (deploy_to_vercel, list_projects, etc.). These are cloud-hosted tools available through Cowork's integrations.
- **If not found:** Say: "I need Vercel connected to deploy your page live. Here's the quick setup:\n\n1. Create a free account at [vercel.com](https://vercel.com)\n2. In your Cowork Settings, go to Integrations and connect Vercel\n\nOnce that's done, say 'Build me a landing page' again. Or if you just want me to generate the page code without deploying, say 'Build a landing page but don't deploy it.'"
- **If found:** Continue.

### 4. Is voice training complete? (Optional)
Check `training/voice/voice-template.md` for voice profile.
- **If present:** Use voice profile for page copy.
- **If not present:** Use clean, persuasive copy. Don't block.

### 5. Is Notion connected? (Optional)
Check for Notion MCP tools.
- **If found:** Can pull product content from Notion pages.
- **If not found:** Ask user to provide content directly.

### 6. All clear — proceed silently.

---

## What the Agent Does

Step 1: Gather the content
- Read description, product brief, or Notion page (if connected)
- Pull from `projects/[product-name]/product-config.md` if available
- If nothing provided, ask: What are you selling? Who is it for? What's the price? What's the main benefit?

Step 2: Write the landing page copy
- Hero section: headline + subheadline + CTA button
- Problem section: what pain does your audience have?
- Solution section: what your product does about it
- Features/benefits: 3-5 key points
- Social proof section: placeholder for testimonials (or real ones if provided)
- Pricing section: what it costs + what's included
- Final CTA: closing push + button
- Written in user's voice if trained, persuasive professional tone if not

Step 3: Generate the code
- Clean, single-file HTML with inline CSS
- Mobile-responsive, fast-loading
- No build step, no dependencies — just HTML that works
- Save the file to `projects/[product-name]/landing-page.html`

Step 4: Show preview before deploying
- Write the HTML file using the Write tool (triggers canvas preview panel)
- Review copy, layout, and design with the user
- Make changes if needed

Step 5: Deploy to Vercel
- Use the Vercel MCP plugin's `deploy_to_vercel` tool
- Push the HTML file to Vercel
- Get a live URL back
- Page is live in under a minute

**Present the results:**
```
Your landing page is live!

URL: https://your-project.vercel.app

To connect a custom domain, go to your Vercel dashboard.
```

## Tips
- Better input = better page. A clear product brief produces a stronger page than "make me a landing page."
- You can iterate: "Change the headline" or "Add a testimonial section" and redeploy.
- Free Vercel accounts give you unlimited deploys with a `.vercel.app` domain.

## Handoff

After page is deployed:
1. Update `projects/[product-name]/product-config.md` — check "Landing page live", fill in Landing page URL.
2. Update `.coworker/index.md` — note "Landing page live at [URL]" next to the product.
3. Say: "Page is live at [URL]. Next up: **launch my product** to generate pricing, launch posts, and a promotion plan."

## Rules
- Always show the full page preview before deploying
- Never deploy without explicit approval
- Write copy using voice profile from `training/voice/voice-template.md` and human writing rules
- If critical information is missing (price, offer, audience), ask — don't make it up
- Include placeholder text for sections the user hasn't provided (marked clearly as [PLACEHOLDER])
- Deploy uses the Vercel MCP plugin — this is a cloud-hosted tool, not a local script. It works within Cowork's VM network restrictions.
- Always write to `projects/[product-name]/` — never to workspace root.
