#!/usr/bin/env python3
"""
Punctuation-Based AI Pattern Scanner
Jumps to punctuation landmarks and analyzes what's around them.
Deterministic, instant, zero-cost.

Usage:
    from punctuation_scanner import scan
    result = scan("Your text here")
    print(result['score'], result['flags'])
"""

import re
from dataclasses import dataclass, field


@dataclass
class Flag:
    category: str
    severity: int  # points deducted
    position: int
    landmark: str
    context: str  # what was found
    explanation: str


@dataclass
class ScanResult:
    score: int  # 0-100, 100 = clean
    flags: list[Flag] = field(default_factory=list)
    stats: dict = field(default_factory=dict)


def _build_punctuation_map(text: str) -> list[tuple[str, int]]:
    """Find all punctuation landmarks and their positions."""
    landmarks = []
    for i, c in enumerate(text):
        if c in '.?!:;':
            landmarks.append((c, i))
        elif c in '—–':
            landmarks.append(('dash', i))
        elif c == '-' and i > 0 and i < len(text) - 1 and text[i-1] == ' ' and text[i+1] == ' ':
            landmarks.append(('dash', i))
        elif c == '\n' and i + 1 < len(text) and text[i+1] == '\n':
            landmarks.append(('para', i))
    return landmarks


def _get_sentence_before(text: str, pos: int) -> str:
    """Extract the sentence ending at this position, looking backwards."""
    # Find the start: previous sentence-ending punctuation or start of text
    search_from = max(0, pos - 200)
    chunk = text[search_from:pos]
    # Find last sentence boundary
    for marker in ['. ', '! ', '? ', '\n\n', '\n']:
        last = chunk.rfind(marker)
        if last >= 0:
            return chunk[last + len(marker):].strip()
    return chunk.strip()


def _get_sentence_after(text: str, pos: int) -> str:
    """Extract the sentence starting after this position."""
    chunk = text[pos+1:pos+201]
    # Find next sentence boundary
    for marker in ['. ', '! ', '? ', '\n\n']:
        idx = chunk.find(marker)
        if idx >= 0:
            return chunk[:idx].strip()
    return chunk.strip()


def scan(text: str) -> ScanResult:
    """Scan text using punctuation landmarks. Returns ScanResult."""
    # Strip code blocks so templates don't trigger flags
    import re as _re
    text = _re.sub(r'```.*?```', '', text, flags=_re.DOTALL)
    text = _re.sub(r'`[^`]+`', '', text)

    flags: list[Flag] = []
    landmarks = _build_punctuation_map(text)

    # ─── STATS ────────────────────────────────────────────────

    # Sentence lengths (chars between periods)
    periods = [pos for char, pos in landmarks if char == '.']
    sentence_lengths = []
    prev = 0
    for p in periods:
        length = p - prev
        if length > 3:  # skip decimal points, abbreviations
            sentence_lengths.append(length)
        prev = p + 1

    # Paragraph lengths
    para_breaks = [pos for char, pos in landmarks if char == 'para']
    para_lengths = []
    prev = 0
    for p in para_breaks:
        para_lengths.append(p - prev)
        prev = p + 2
    if prev < len(text):
        para_lengths.append(len(text) - prev)

    question_marks = [(char, pos) for char, pos in landmarks if char == '?']
    colons = [(char, pos) for char, pos in landmarks if char == ':']
    dashes = [(char, pos) for char, pos in landmarks if char == 'dash']
    exclamations = [(char, pos) for char, pos in landmarks if char == '!']
    semicolons = [(char, pos) for char, pos in landmarks if char == ';']

    stats = {
        "sentence_count": len(sentence_lengths),
        "avg_sentence_length": sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0,
        "sentence_lengths": sentence_lengths,
        "paragraph_count": len(para_lengths),
        "paragraph_lengths": para_lengths,
        "question_marks": len(question_marks),
        "colons": len(colons),
        "dashes": len(dashes),
        "exclamations": len(exclamations),
        "semicolons": len(semicolons),
    }

    # ─── BURSTINESS CHECK ──────────────────────────────────────

    if len(sentence_lengths) >= 5:
        # Check: are three consecutive sentences within 5 chars of each other?
        for i in range(len(sentence_lengths) - 2):
            a, b, c = sentence_lengths[i], sentence_lengths[i+1], sentence_lengths[i+2]
            spread = max(a, b, c) - min(a, b, c)
            if spread < 8 and min(a, b, c) > 20:  # three similar-length non-trivial sentences
                flags.append(Flag(
                    category="flat_rhythm",
                    severity=8,
                    position=periods[i] if i < len(periods) else 0,
                    landmark="...",
                    context=f"Three sentences within {spread} chars of each other: {a}, {b}, {c}",
                    explanation="Flat rhythm. Vary sentence lengths more dramatically.",
                ))
                break  # only flag once

        # Check: no short sentences (< 30 chars) in the whole piece
        has_short = any(l < 30 for l in sentence_lengths)
        has_long = any(l > 80 for l in sentence_lengths)
        if not has_short and not has_long:
            flags.append(Flag(
                category="monotone_length",
                severity=6,
                position=0,
                landmark="...",
                context=f"All sentences between 30-80 chars. Range: {min(sentence_lengths)}-{max(sentence_lengths)}",
                explanation="Monotone sentence length. Add a very short or very long sentence for burstiness.",
            ))

    # ─── DASH CHECK (instant kill) ────────────────────────────

    for _, pos in dashes:
        context = text[max(0, pos-20):pos+20].strip()
        flags.append(Flag(
            category="dash",
            severity=10,
            position=pos,
            landmark="—/–/-",
            context=context,
            explanation="No dashes allowed. Use commas, periods, or restructure.",
        ))

    # ─── PERIOD ANALYSIS ──────────────────────────────────────

    # Staccato detection: 3+ consecutive short sentences
    SHORT_THRESHOLD = 40  # chars
    consecutive_short = 0
    staccato_start = 0
    for i, length in enumerate(sentence_lengths):
        if length < SHORT_THRESHOLD:
            if consecutive_short == 0:
                staccato_start = i
            consecutive_short += 1
            if consecutive_short >= 3:
                # Get the actual text of these sentences
                start_pos = periods[staccato_start] - sentence_lengths[staccato_start] if staccato_start < len(periods) else 0
                end_pos = periods[min(i, len(periods)-1)] + 1 if i < len(periods) else len(text)
                context = text[max(0,start_pos):min(len(text),end_pos)].strip()[:80]
                flags.append(Flag(
                    category="staccato",
                    severity=12,
                    position=periods[staccato_start] if staccato_start < len(periods) else 0,
                    landmark="...",
                    context=context,
                    explanation=f"Three+ consecutive short sentences ({consecutive_short} found). Vary sentence length.",
                ))
                consecutive_short = 0  # reset after flagging
        else:
            consecutive_short = 0

    # Suspiciously even paragraph lengths
    if len(para_lengths) >= 3:
        avg_para = sum(para_lengths) / len(para_lengths)
        if avg_para > 30:  # meaningful paragraphs
            variance = sum((p - avg_para) ** 2 for p in para_lengths) / len(para_lengths)
            std_dev = variance ** 0.5
            if std_dev < avg_para * 0.2 and len(para_lengths) >= 4:
                flags.append(Flag(
                    category="even_paragraphs",
                    severity=8,
                    position=0,
                    landmark="\\n\\n",
                    context=f"Paragraph lengths: {para_lengths}",
                    explanation=f"Suspiciously even paragraph lengths (std_dev={std_dev:.0f}, avg={avg_para:.0f}). Vary paragraph size.",
                ))

    # ─── QUESTION MARK ANALYSIS ───────────────────────────────

    for _, pos in question_marks:
        sentence = _get_sentence_before(text, pos)
        sentence_lower = sentence.lower()

        # Check for cringe question starters (look backwards from ?)
        cringe_starters = [
            ("sound familiar", "Sound familiar?"),
            ("want to know", "Want to know X?"),
            ("ready to", "Ready to X?"),
            ("guess what", "Guess what?"),
            ("what if i told you", "What if I told you?"),
            ("and the wildest part", "And the wildest part?"),
            ("and the craziest part", "And the craziest part?"),
            ("and the best part", "And the best part?"),
            ("and the worst part", "And the worst part?"),
            ("and the real part", "And the real kicker?"),
            ("you know what", "You know what's X?"),
            ("the brutal truth", "The brutal truth?"),
            ("the hard truth", "The hard truth?"),
            ("the uncomfortable truth", "The uncomfortable truth?"),
            ("let that sink in", "Let that sink in?"),
            ("right?", "Tag question: right?"),
            ("make sense", "Make sense?"),
            ("see the pattern", "See the pattern?"),
            ("see the problem", "See the problem?"),
            ("know what happened", "Know what happened?"),
            ("coincidence", "Coincidence?"),
        ]

        for starter, label in cringe_starters:
            if starter in sentence_lower:
                flags.append(Flag(
                    category="cringe_question",
                    severity=15,
                    position=pos,
                    landmark="?",
                    context=sentence[:60],
                    explanation=f"Cringe question pattern: {label}",
                ))
                break
        else:
            # Not a known cringe pattern — check if it's a rhetorical setup
            # Short questions after a statement are often cringe
            if len(sentence) < 25 and pos > 50:
                prev_sentence = _get_sentence_before(text, pos - len(sentence) - 2)
                if len(prev_sentence) > 50:
                    # Short question after long statement = likely rhetorical/cringe
                    flags.append(Flag(
                        category="suspicious_question",
                        severity=5,
                        position=pos,
                        landmark="?",
                        context=sentence[:60],
                        explanation="Short question after long statement. Possible rhetorical/cringe pattern.",
                    ))

    # ─── COLON ANALYSIS ───────────────────────────────────────

    for _, pos in colons:
        before = _get_sentence_before(text, pos).lower()

        throat_clear_starters = [
            "here's what", "here's the", "here's why", "here's how",
            "here is what", "here is the", "here is why",
            "the truth", "the reality", "the fact",
            "the bottom line", "the answer", "the secret",
            "the problem", "the issue", "the solution",
            "the key", "the trick", "the fix",
            "let me be", "let me tell", "i'll be honest",
            "one word", "two words", "three things",
            "the reason", "the thing is",
        ]

        for starter in throat_clear_starters:
            if starter in before:
                flags.append(Flag(
                    category="throat_clearing",
                    severity=15,
                    position=pos,
                    landmark=":",
                    context=text[max(0,pos-40):pos+1].strip(),
                    explanation=f"Throat-clearing before colon: '{starter}...'",
                ))
                break

    # ─── COMMA + CONJUNCTION = CONTRAST CHECK ─────────────────

    # Find ", but", ", yet", ", however" patterns
    contrast_patterns = [
        (r',\s+but\s+', "Comma-but contrast"),
        (r',\s+yet\s+', "Comma-yet contrast"),
        (r',\s+however\s+', "Comma-however contrast"),
        (r',\s+not\s+', "Comma-not negation"),
    ]

    for pattern, label in contrast_patterns:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            # Check if it's doing "not X, but Y" / negative pivot
            before = text[max(0, m.start()-50):m.start()].lower()
            if any(neg in before for neg in ["not ", "isn't ", "wasn't ", "aren't ", "don't ", "didn't "]):
                flags.append(Flag(
                    category="contrast_pivot",
                    severity=12,
                    position=m.start(),
                    landmark=",",
                    context=text[max(0,m.start()-30):m.end()+30].strip()[:60],
                    explanation=f"Negative-then-pivot: {label}",
                ))

    # ─── NEGATIVE WORD SCAN ───────────────────────────────────

    # Check for sentences that START with negation
    neg_starters = [
        (r'(?im)^(not |never |nobody |no one |none |nothing )', "Sentence starts with negation"),
        (r'(?im)^(wasn\'?t |isn\'?t |aren\'?t |don\'?t |didn\'?t |won\'?t |can\'?t )', "Sentence starts with contraction-negation"),
    ]
    for pattern, label in neg_starters:
        for m in re.finditer(pattern, text):
            context = text[m.start():min(len(text), m.start()+60)].strip()
            flags.append(Flag(
                category="negative_opener",
                severity=15,
                position=m.start(),
                landmark="neg",
                context=context,
                explanation=label,
            ))

    # Negative definitions mid-sentence: "[thing] isn't/wasn't/aren't [thing]"
    neg_defs = [
        r"(?i)\b\w+\s+(isn'?t|aren'?t|wasn'?t|weren'?t)\s+\w+",
    ]
    for pattern in neg_defs:
        for m in re.finditer(pattern, text):
            flags.append(Flag(
                category="negative_definition",
                severity=10,
                position=m.start(),
                landmark="neg",
                context=m.group()[:60],
                explanation="Defining through negation. Say what it IS instead.",
            ))

    # Stopped/started, used-to/now contrast
    contrast_verbs = [
        (r'(?i)\bstopped\s+.{3,80}\bstarted\s+', "stopped X...started Y contrast"),
        (r'(?i)\bused\s+to\s+.{3,80}\bnow\s+', "used to X...now Y contrast"),
        (r'(?i)\bbefore\s+.{3,80}\bafter\s+', "before X...after Y contrast"),
        (r'(?i)\bwent\s+from\s+.{3,40}\bto\s+', "went from X to Y (may be fine if factual)"),
    ]
    for pattern, label in contrast_verbs:
        for m in re.finditer(pattern, text):
            flags.append(Flag(
                category="temporal_contrast",
                severity=8,
                position=m.start(),
                landmark="verb",
                context=m.group()[:60],
                explanation=label,
            ))

    # ─── FORMULAIC HOOKS ──────────────────────────────────────

    hook_patterns = [
        (r'(?im)^most\s+(people|founders|operators|entrepreneurs|teams|companies|businesses|writers|creators)', "Most people/founders..."),
        (r'(?im)^everyone\s+(say|think|believe|know|love|want|talk|is|does)', "Everyone [verbs]..."),
        (r'(?im)^nobody\s+', "Nobody..."),
        (r'(?im)^no\s+one\s+', "No one..."),
        (r'(?im)^I\s+(spent|wasted|lost|invested)\s+\d', "I spent/wasted [number]..."),
        (r'(?im)^stop\s+(doing|trying|thinking|believing)', "Stop [verb]ing..."),
    ]
    for pattern, label in hook_patterns:
        for m in re.finditer(pattern, text):
            flags.append(Flag(
                category="formulaic_hook",
                severity=10,
                position=m.start(),
                landmark="hook",
                context=m.group()[:60],
                explanation=f"Formulaic hook: {label}",
            ))

    # ─── CORPORATE JARGON ─────────────────────────────────────

    jargon = [
        "leverage", "synergy", "robust", "seamless", "cutting-edge",
        "thought leader", "paradigm", "disrupt", "innovative", "scalable",
        "landscape", "ecosystem", "optimize", "streamline", "empower",
        "utilize", "facilitate", "framework", "game-changer", "next-level",
        "level up", "unlock", "supercharge", "actionable", "impactful",
        "transformative", "unprecedented", "holistic", "pivot",
    ]
    text_lower = text.lower()
    for word in jargon:
        if word in text_lower:
            pos = text_lower.index(word)
            flags.append(Flag(
                category="corporate_jargon",
                severity=8,
                position=pos,
                landmark="word",
                context=word,
                explanation=f"Corporate jargon: '{word}'",
            ))

    # ─── AI TRANSITIONS ───────────────────────────────────────

    transitions = [
        "furthermore", "moreover", "additionally", "consequently",
        "nevertheless", "in conclusion", "to summarize", "in summary",
        "at the end of the day", "bottom line",
    ]
    for word in transitions:
        if word in text_lower:
            pos = text_lower.index(word)
            flags.append(Flag(
                category="ai_transition",
                severity=8,
                position=pos,
                landmark="word",
                context=word,
                explanation=f"AI transition word: '{word}'",
            ))

    # ─── EXCLAMATION OVERUSE ──────────────────────────────────

    if len(exclamations) > 1:
        flags.append(Flag(
            category="exclamation_overuse",
            severity=5,
            position=exclamations[1][1],
            landmark="!",
            context=f"{len(exclamations)} exclamation marks",
            explanation="More than 1 exclamation mark per piece. Tone it down.",
        ))

    # ─── SCORE ────────────────────────────────────────────────

    # Deduplicate flags by position (within 5 chars)
    deduped = []
    seen_positions = set()
    for f in sorted(flags, key=lambda x: -x.severity):
        bucket = f.position // 5
        key = (f.category, bucket)
        if key not in seen_positions:
            seen_positions.add(key)
            deduped.append(f)

    total_deductions = sum(f.severity for f in deduped)
    score = max(0, 100 - total_deductions)

    return ScanResult(score=score, flags=deduped, stats=stats)


# ─── CLI ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test = """Two newsletters. $600k a year. Both built with the same playbook.

Most people overthink newsletters. They spend three months picking a name, six months finding their voice, another six months wondering why nobody's reading.

I skipped all that. Picked a lane, shipped consistently, figured out what worked by watching what readers actually did.

Here's what surprised me: the money didn't come from subscribers. It came from what subscribers proved. Social proof. Trust you can move into paid products, partnerships, consulting fees.

The math gets simple once you see it. A 10,000-subscriber list with 40% open rates beats 100,000 subscribers who barely open. Depth beats width every time.

These five steps aren't magic. They're just what actually happened when I stopped treating the newsletter like content and started treating it like a business."""

        result = scan(test)
        print(f"Score: {result.score}/100 ({len(result.flags)} flags)")
        print()
        for f in sorted(result.flags, key=lambda x: x.position):
            print(f"  [{f.category}] sev:{f.severity} pos:{f.position}")
            print(f"    {f.context}")
            print(f"    → {f.explanation}")
            print()
        print(f"Stats: {result.stats['sentence_count']} sentences, avg {result.stats['avg_sentence_length']:.0f} chars")
        print(f"  Paragraphs: {result.stats['paragraph_count']}, lengths: {result.stats['paragraph_lengths']}")
        print(f"  Questions: {result.stats['question_marks']}, Colons: {result.stats['colons']}, Dashes: {result.stats['dashes']}")

    elif len(sys.argv) > 1:
        text = open(sys.argv[1]).read() if sys.argv[1] != "-" else sys.stdin.read()
        result = scan(text)
        print(f"Score: {result.score}/100")
        for f in result.flags:
            print(f"  [{f.category}] {f.context} → {f.explanation}")
    else:
        print("Usage: python3 punctuation-scanner.py --test | python3 punctuation-scanner.py file.txt")
