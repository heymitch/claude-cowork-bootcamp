#!/usr/bin/env python3
"""
Human-Detectable AI Pattern Scorer v3
Strict negative parallelism + comprehensive pattern detection.
Every question mark gets a Haiku check for cringe.

Score 0-100 where 100 = no AI patterns detected.
"""

import re
import subprocess
import json


# ─── Layer 1: Regex Patterns ─────────────────────────────────────

REGEX_PATTERNS = {
    # NEGATIVE PARALLELISM — anything that defines through negation
    "negative_parallelism": [
        # Direct negation in any form
        r"(?i)\bit'?s\s+not\s+",
        r"(?i)\bthat'?s\s+not\s+",
        r"(?i)\bthis\s+isn'?t\s+",
        r"(?i)\bnot\s+because\b",
        r"(?i)\bnot\s+even\s+",
        r"(?i)\bnot\s+the\s+\w+",
        r"(?i)\bwasn'?t\s+\w+",
        r"(?i)\bisn'?t\s+\w+",
        r"(?i)\baren'?t\s+\w+",  # "aren't magic"
        r"(?i)\bdidn'?t\s+\w+",
        r"(?i)\bwon'?t\s+\w+",
        r"(?i)\bcan'?t\s+\w+",
        r"(?i)\bdon'?t\s+\w+[.\n,]",  # "Don't overthink." as fragment
        r"(?i)\bnobody\s+(talk|know|tell|want|see|mention|care|notice|realize|ask|think|read)",
        r"(?i)\bno\s+one\s+(talk|know|tell|want|see|mention|care|notice|ask|think)",
        r"(?i)\bnone\s+of\s+them\s+",
        r"(?i)\bnot\s+\w+\.\s+not\s+",  # stacked
        r"(?i)\bwasn'?t\s+\w+\.\s+wasn'?t",  # stacked
        r"(?i)the\s+\w+\s+that\s+.{3,30}\s+wasn'?t",
        r"(?i)the\s+\w+\s+that\s+.{3,30}\s+isn'?t",
        r"(?i)the\s+\w+\s+that\s+.{3,30}\s+aren'?t",
        # Contrast via stopped/started, old/new
        r"(?i)\bstopped\s+.{3,80}\bstarted\s+",  # "stopped X and started Y"
        r"(?i)\bused\s+to\s+.{3,80}\bnow\s+(I|we|they|he|she)\s+",  # "used to X, now Y"
        r"(?i)\bnobody'?s?\s+\w+",  # "nobody's reading" / "nobody reads"
    ],

    # THROAT-CLEARING — building up before making the point
    "throat_clearing": [
        r"(?i)\bhere'?s\s+what\b",  # "Here's what" anything
        r"(?i)\bhere'?s\s+the\s+\w+",  # "Here's the thing/kicker/secret/etc"
        r"(?i)\bhere'?s\s+why\b",  # "Here's why"
        r"(?i)\bhere'?s\s+how\b",  # "Here's how"
        r"(?i)\bthe\s+(truth|reality|fact)\s+is[,:]",
        r"(?i)\blet\s+me\s+(be\s+)?(clear|honest|real|straight|frank)",
        r"(?i)\bI'?ll\s+be\s+(honest|real|straight|frank)",
        r"(?i)\bthe\s+bottom\s+line\s+is",
        r"(?i)\bin\s+today'?s\s+(rapidly\s+)?(evolving|changing|digital|modern)",
        r"(?i)\bI'?m\s+going\s+to\s+(be\s+)?(honest|real|straight|direct)",
        r"(?i)\bcan\s+we\s+be\s+(honest|real)\b",
    ],

    # CRINGE QUESTIONS / SETUPS
    "cringe_questions": [
        r"(?i)\bsound\s+familiar\??",
        r"(?i)\bwant\s+to\s+know\s+(the\s+secret|what|why|how)",
        r"(?i)\bthe\s+(brutal|hard|uncomfortable|ugly|honest|simple)\s+truth",
        r"(?i)\bready\s+to\s+(level\s+up|take|start|transform|change|scale)",
        r"(?i)\bguess\s+what\??",
        r"(?i)\bwhat\s+if\s+I\s+told\s+you",
        r"(?i)\band\s+the\s+(wildest|craziest|best|worst|biggest|funniest|real)\s+part\??",
        r"(?i)\byou\s+know\s+what'?s?\s+(funny|crazy|wild|interesting|weird)\??",
        r"(?i)\blet\s+that\s+sink\s+in",
        r"(?i)\bread\s+that\s+again",
        r"(?i)\btake\s+a\s+(second|moment|minute)\s+(with|to\s+feel|to\s+sit)",
        r"(?i)\bthat'?s\s+real\b",  # performed empathy
        r"(?i)\bspoiler\s*:?\s",
        r"(?i)\bplot\s+twist\s*:?\s",
    ],

    # DASHES — none allowed, ever
    "dashes": [
        r"—",  # em dash
        r"–",  # en dash
        r"\s+-\s+",  # spaced hyphen used as dash
    ],

    # CORPORATE JARGON
    "corporate_jargon": [
        r"(?i)\b(leverage|synergy|robust|seamless|cutting-?edge)\b",
        r"(?i)\b(thought\s+leader|paradigm|disrupt|innovative|scalable)\b",
        r"(?i)\b(landscape|ecosystem|optimize|streamline|empower)\b",
        r"(?i)\b(utilize|facilitate|framework)\b",
        r"(?i)\b(game.changer|next.level|level.up)\b",
        r"(?i)\b(unlock\s+(your|the|new)|supercharge)\b",
        r"(?i)\b(actionable|impactful|transformative|unprecedented)\b",
    ],

    # FORMULAIC HOOKS
    "formulaic_hooks": [
        r"(?im)^most\s+(people|founders|operators|entrepreneurs|teams|companies|businesses|writers|creators)\s+(think|believe|don'?t|get|make|fail|miss|overthink|overlook|skip|ignore|spend)",
        r"(?im)^everyone\s+(say|think|believe|know|love|want|talk|is)",
        r"(?im)^nobody\s+(talk|tell|mention|want|care|notice|realize|ask|think|read)",
        r"(?im)^no\s+one\s+(talk|tell|mention|want|care|ask|think)",
        r"(?im)^I\s+(spent|wasted|lost|invested)\s+\d",
        r"(?im)^stop\s+(doing|trying|thinking|believing|chasing|overthinking)",
    ],

    # STACCATO RULE OF THREE — consecutive short fragments
    "rule_of_three": [
        r"(?m)^[A-Z][^.]{3,25}\.\s*\n[A-Z][^.]{3,25}\.\s*\n[A-Z][^.]{3,25}\.",  # across newlines
        r"[A-Z].{2,45}\.\s+[A-Z].{2,45}\.\s+[A-Z].{2,45}\.",  # inline triple short
    ],

    # AI TRANSITIONS
    "ai_transitions": [
        r"(?i)\b(furthermore|moreover|additionally|consequently|nevertheless)\b",
        r"(?i)\b(in\s+conclusion|to\s+summarize|in\s+summary|ultimately)\b",
        r"(?i)\b(bottom\s+line|at\s+the\s+end\s+of\s+the\s+day)\b",
    ],
}

# Severity weights
SEVERITY = {
    "negative_parallelism": 15,
    "throat_clearing": 15,
    "cringe_questions": 15,
    "dashes": 8,
    "corporate_jargon": 8,
    "formulaic_hooks": 10,
    "rule_of_three": 12,
    "ai_transitions": 8,
}


def _strip_code_blocks(text: str) -> str:
    """Remove fenced code blocks and inline code so templates don't trigger flags."""
    import re
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)
    return text


def regex_scan(text: str) -> list[dict]:
    text = _strip_code_blocks(text)
    found = []
    for category, patterns in REGEX_PATTERNS.items():
        for pattern in patterns:
            for m in re.finditer(pattern, text):
                found.append({
                    "category": category,
                    "match": m.group(0).strip()[:60],
                    "position": m.start(),
                })
    # Deduplicate by position (same match from multiple patterns)
    seen = set()
    deduped = []
    for f in found:
        key = (f["category"], f["position"])
        if key not in seen:
            seen.add(key)
            deduped.append(f)
    return deduped


# ─── Layer 2: Haiku Question Check ───────────────────────────────

def check_question_cringe(sentence: str) -> bool:
    """Ask Haiku if a question is cringe/formulaic or genuine."""
    prompt = f"""Is this question a genuine, thoughtful question OR is it a formulaic/cringe AI writing pattern?

Cringe examples: "Sound familiar?" "Want to know the secret?" "The wildest part?" "Ready to level up?"
Genuine examples: "How do you price that?" "What would you do differently?" "Where does the money go?"

Question: "{sentence}"

Reply with ONLY one word: CRINGE or GENUINE"""
    try:
        r = subprocess.run(["claude", "-p", "--model", "haiku"],
                          input=prompt, capture_output=True, text=True, timeout=30)
        return "CRINGE" in r.stdout.upper()
    except:
        return False  # assume genuine if check fails


# ─── Layer 3: Semantic Structure Check ────────────────────────────

SEMANTIC_PROMPT = """Analyze this writing for AI patterns. Be STRICT. Check for:

1. NEGATIVE PARALLELISM: ANY sentence that defines through what something ISN'T rather than what it IS.
   "Wasn't skill" = FAIL. Say what it WAS.
   "Not the technology" = FAIL. Say what it WAS.
   "Nobody talks about" = FAIL. Just say the thing.

2. CONTRAST FRAMING: Setting up wrong belief to pivot from.
   "Everyone thinks X. Actually Y." = FAIL.
   "Most people do X. Here's why that's wrong." = FAIL.

3. FORMULAIC STRUCTURE: Does it follow hook → problem → numbered list → CTA?

Reply ONLY in JSON: {"negative_parallelism": true/false, "contrast_framing": true/false, "formulaic_structure": true/false, "details": "what was found"}"""


def semantic_scan(text: str) -> dict:
    try:
        r = subprocess.run(["claude", "-p", "--model", "haiku"],
                          input=SEMANTIC_PROMPT + "\n\n" + text,
                          capture_output=True, text=True, timeout=60)
        output = r.stdout.strip()
        start = output.find("{")
        end = output.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(output[start:end])
        return {"error": "no_json"}
    except Exception as e:
        return {"error": str(e)}


# ─── Combined Scorer ──────────────────────────────────────────────

def score_human_patterns(text: str, use_semantic: bool = True, check_questions: bool = True) -> dict:
    """
    Score text for human-detectable AI patterns.
    100 = clean. 0 = pure slop.
    """
    # Layer 1: Regex
    regex_hits = regex_scan(text)

    # Layer 1.5: Check every question mark with Haiku
    cringe_questions_found = []
    if check_questions:
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for s in sentences:
            if '?' in s and len(s) > 10:
                # Only check if regex didn't already flag it
                already_flagged = any(h["category"] == "cringe_questions" and
                                     h["match"] in s for h in regex_hits)
                if not already_flagged:
                    if check_question_cringe(s):
                        cringe_questions_found.append(s[:60])

    # Layer 2: Semantic
    semantic = {}
    semantic_patterns = []
    if use_semantic:
        semantic = semantic_scan(text)
        if isinstance(semantic, dict) and "error" not in semantic:
            for key in ["negative_parallelism", "contrast_framing", "formulaic_structure"]:
                if semantic.get(key):
                    semantic_patterns.append(key)

    # Calculate score
    deductions = 0
    for hit in regex_hits:
        deductions += SEVERITY.get(hit["category"], 8)
    for _ in cringe_questions_found:
        deductions += 15  # cringe questions are high severity
    for sp in semantic_patterns:
        if sp not in [h["category"] for h in regex_hits]:
            deductions += 12

    score = max(0, 100 - deductions)

    # Compile findings
    all_patterns = []
    for hit in regex_hits:
        all_patterns.append(f"[regex] {hit['category']}: \"{hit['match']}\"")
    for cq in cringe_questions_found:
        all_patterns.append(f"[haiku] cringe_question: \"{cq}\"")
    for sp in semantic_patterns:
        if sp not in [h["category"] for h in regex_hits]:
            all_patterns.append(f"[semantic] {sp}")

    return {
        "score": score,
        "pattern_count": len(regex_hits) + len(cringe_questions_found) + len([sp for sp in semantic_patterns if sp not in [h["category"] for h in regex_hits]]),
        "patterns_found": all_patterns,
        "regex_hits": regex_hits,
        "cringe_questions": cringe_questions_found,
        "semantic": semantic,
        "semantic_patterns": semantic_patterns,
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_text = """Most AI agents fail in production — not because the model is bad, but because the scaffolding around it is fragile. Here's the thing: teams optimize for demos, not for the messy reality of production environments. Sound familiar? The truth is, most failures come down to three things. Poor error handling. No human-in-the-loop. Zero observability. Want to know the secret? It's not about building smarter agents — it's about building boring infrastructure that catches failures before they cascade."""

        print("Testing known AI slop:")
        result = score_human_patterns(test_text, use_semantic=False, check_questions=False)
        print(f"  Score: {result['score']}/100 ({result['pattern_count']} patterns)")
        for p in result["patterns_found"]:
            print(f"    {p}")

    elif len(sys.argv) > 1:
        text = open(sys.argv[1]).read() if sys.argv[1] != "-" else sys.stdin.read()
        result = score_human_patterns(text, use_semantic=True, check_questions=True)
        print(json.dumps(result, indent=2))
    else:
        print("Usage: python3 human-eval.py --test | python3 human-eval.py file.txt")
