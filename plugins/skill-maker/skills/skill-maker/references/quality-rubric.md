# Skill Quality Rubric

The "High Protein" test. Use this to evaluate any skill before it ships.

---

## The 5-Second Test

Read the SKILL.md frontmatter description. In 5 seconds, can you answer:
1. What does this skill do?
2. When would I use it?

If either answer is unclear, rewrite the description. No jargon. No vague language. A new user should get it instantly.

**Pass example:** "Turn meeting transcripts into organized action items with owners and deadlines. Say 'process my meeting notes' or 'what were the action items from today's call'."

**Fail example:** "A comprehensive tool for optimizing workflow productivity through intelligent meeting analysis." (What does it actually DO?)

---

## High Protein Checklist: Standard Skills

Run through every item. Be honest.

- [ ] **Saves real hours.** Would this save at least 30 minutes per week? If it's a party trick or demo, it's not a real skill.
- [ ] **Does work, not describes work.** Run the skill. Does it produce actual output (a file, a post, an email)? Or does it just tell you what you *could* do?
- [ ] **One-sentence trigger.** Can someone run it by saying one natural sentence? No setup steps, no "first configure X, then run Y."
- [ ] **Uses config.md.** Does it read the user's business context? Or does it produce generic output that could be for anyone?
- [ ] **SKILL.md under 100 lines.** Count them. If it's over, move content to references/.
- [ ] **Trigger phrases in frontmatter.** The `description` field includes 2-3 natural phrases that would invoke this skill.
- [ ] **Specific rules.** The Rules section has actual guardrails. Not "be helpful" or "be thorough" — things like "always show the draft before sending" or "never include prices without checking the rate sheet."
- [ ] **Shows before saving.** Output is shown to the user for approval before writing files or sending messages.
- [ ] **Handles missing tools.** If a connector isn't available, does the skill explain what's needed and offer an alternative? Or does it just crash?
- [ ] **Weekly use test.** Would you actually use this every week? If not, is it solving a real problem?

---

## High Protein Checklist: Tutor Skills

Everything from the Standard checklist, PLUS:

- [ ] **SKILL.md is conductor only.** Under 500 lines. Contains zero lesson content. Just routing, rules, and progress tracking.
- [ ] **curriculum-map.md is complete.** Every module has: ID, name, description, deliverable, prerequisite. No gaps.
- [ ] **Lessons are student-facing.** Read a lesson file. Does it sound like a teacher talking to a student? Or does it sound like agent notes? ("Here's the deal..." = good. "This module covers..." = bad.)
- [ ] **Exercises are fillable.** Open an exercise file. Are there blank fields to fill in? Clear instructions? Examples of good answers? A "done" checklist?
- [ ] **Flow works end-to-end.** Walk through: student says "Module 3" -> right lesson loads -> right exercise runs -> progress updates. No broken links, no missing files.

---

## Common Failures

### "Skill" that's actually a reference doc
**Symptom:** SKILL.md describes a framework or process but never takes action.
**Fix:** Add a workflow section with action verbs. "Read the file" not "The file should be read." "Generate 3 options" not "Options can be generated."

### SKILL.md over 200 lines
**Symptom:** Everything is crammed into one file.
**Fix:** Extract templates, examples, and domain knowledge into references/. If it's still too long, split into sub-skills.

### Generic output
**Symptom:** The skill produces the same output regardless of who runs it.
**Fix:** Add a config.md read step. Use business name, voice, industry, and tools in the output.

### No error handling
**Symptom:** Skill says "Post to LinkedIn" but crashes if Ayrshare isn't connected.
**Fix:** Check tool availability first. Offer alternatives: "Ayrshare isn't connected. I'll generate the post and you can copy-paste it instead."

### "Helpful" rules instead of guardrails
**Symptom:** Rules section says "Be thorough and helpful" or "Provide high-quality output."
**Fix:** Replace with specific constraints: "Never send without showing draft first." "Always include a subject line under 60 characters." "If no deadline is given, default to end of week."

### Tutor with lesson content in SKILL.md
**Symptom:** SKILL.md is 800 lines because lessons are embedded.
**Fix:** Move every lesson to references/lessons/. SKILL.md should only know which lesson file to load, not what's in it.

---

## Rating Scale

### A: Ship it
Passes all checklist items. You'd use it weekly. It saves real hours. The output is personalized and specific. Rules are tight. Error handling works.

### B: Almost there
Passes most checks. Useful but needs one or two fixes — maybe the rules are vague, or it's missing config.md personalization. Quick polish and it's an A.

### C: Needs work
Missing key elements. Maybe it doesn't personalize output, or error handling is absent, or SKILL.md is too long. Functional but not ready to ship.

### D: Describes, doesn't do
The skill explains what it would do but doesn't actually do it. Running it produces advice, not output. Needs a fundamental rewrite to become action-oriented.

### F: Start over
Not a real skill. It's a reference doc, a wall of text, or a description of a concept. Delete and rebuild from scratch using the architecture guide.

---

## Quick Evaluation Template

Use this when testing a skill:

```
Skill: [name]
Type: Standard / Tutor

5-Second Test: PASS / FAIL
Reason: [one sentence]

Checklist Score: [X/10] standard or [X/15] tutor
Failed items:
- [list specific failures]

Simulated Run:
- Trigger used: "[what you said to invoke it]"
- Output produced: [describe what happened]
- Issues found: [list any problems]

Grade: [A/B/C/D/F]
Top fix: [the one thing that would improve it most]
```
