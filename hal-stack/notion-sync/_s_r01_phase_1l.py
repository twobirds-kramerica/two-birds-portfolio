"""S-R01-PHASE-1l — 13-15 Learning: AI tutor vs AI shortcut.

2nd row in 13-15 x Learning cell. Hits the Phase-1 20+ target.

Defining learning skill for the current teen generation: how to use
ChatGPT / Claude / Gemini as a tutor that grows you, rather than a
homework-completion engine that hollows you out.

Companion to existing 13-15 Learning row ('Asking good questions
when I search or ask AI'). That row is about good questions. This
row is about the interaction pattern that lets the questions actually
produce learning.

Run once:   python _s_r01_phase_1l.py
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

spec = importlib.util.spec_from_file_location(
    "nc", os.path.join(HERE, "notion-client.py")
)
nc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nc)


ROW = dict(
    skill="Using AI as a tutor that grows me, not a shortcut that hollows me out",
    category="Learning",
    age_ranges=["13-15"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Multi-Modal",
    learning_profile=["Standard", "ADHD", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "The defining learning skill for the current teen "
        "generation. Same tool (ChatGPT / Claude / Gemini / "
        "Khanmigo) can either grow the teen's capability or "
        "hollow it out — the difference is the interaction "
        "pattern, not the tool. This skill teaches four "
        "concrete moves that keep the teen in learning mode: "
        "(1) answer first, ask AI second; (2) ask AI to "
        "critique YOUR reasoning, not hand you the answer; (3) "
        "demand 'explain it like I'm in grade 8' when the AI's "
        "response uses concepts the teen doesn't yet hold; (4) "
        "the 'protégé test' — if the teen can't teach it back "
        "in their own words without the AI, they didn't learn "
        "it. Research evidence for each move is strong and "
        "recent (2024-2025)."
    ),
    research_source=(
        "Dartmouth College (November 2025) — 'AI Can Deliver "
        "Personalized Learning at Scale, Study Shows' "
        "(home.dartmouth.edu/news/2025/11/ai-can-deliver-"
        "personalized-learning-scale-study-shows): frames the "
        "core cognitive risk explicitly — 'there is an illusion "
        "of mastery when we cognitively outsource all of our "
        "thinking and learning to AI'. "
        "Nature Scientific Reports (2025) — 'AI tutoring "
        "outperforms in-class active learning: an RCT "
        "introducing a novel research-based design in an "
        "authentic educational setting' "
        "(nature.com/articles/s41598-025-97652-6): randomised "
        "controlled trial showing that AI tutoring, when "
        "designed around learning-science principles "
        "(Socratic questioning, retrieval practice), outperforms "
        "traditional active learning. Not the same as answer-"
        "provision; the design matters. "
        "Khan Academy Blog — 'Khan Academy Efficacy Results, "
        "November 2024' (blog.khanacademy.org/khan-academy-"
        "efficacy-results-november-2024): Khanmigo's early data "
        "showing students using it develop 'better conceptual "
        "understanding than those using traditional answer-"
        "checking tools'. Khan Academy annual report "
        "(annualreport.khanacademy.org) — Khanmigo reach grew "
        "from 68K to 700K+ students in one year. "
        "Frontiers in Education (2025) — 'The cognitive "
        "mirror: a framework for AI-powered metacognition and "
        "self-regulated learning' "
        "(frontiersin.org/journals/education/articles/10.3389/"
        "feduc.2025.1697554/full): academic framework for the "
        "explain-back and self-monitoring patterns this skill "
        "teaches. "
        "Classical learning-science references: the 'generation "
        "effect' (Slamecka & Graf 1978) — learners remember "
        "better what they generated themselves than what was "
        "presented to them. 'Retrieval practice' (Roediger & "
        "Karpicke 2006) — actively recalling material produces "
        "deeper learning than re-reading. 'Protégé effect' "
        "(Fiorella & Mayer 2013 onwards) — learners who "
        "prepare to teach the material learn it more deeply. "
        "All three principles support the four moves this "
        "skill teaches. "
        "EdWeek (July 2025) — 'Can an AI-Powered Tutor Produce "
        "Meaningful Results?' (edweek.org/technology/opinion-"
        "can-an-ai-powered-tutor-produce-meaningful-results/"
        "2025/07) - balanced educator-facing review."
    ),
    threat_addressed=(
        "The 'illusion of mastery' effect (Dartmouth 2025): a "
        "teen who uses ChatGPT to write their paper FEELS like "
        "they understand the material because they read the "
        "output, but scores badly on tests and worse on future "
        "coursework that builds on it. The gap compounds: "
        "year-1 AI-outsourced foundations -> year-2 "
        "coursework feels impossibly hard -> year-2 teen "
        "uses even more AI outsourcing -> year-3 the teen "
        "has an English / math / science grade that does not "
        "match their actual capability. At university / "
        "workplace entry, the gap is exposed. This is NOT a "
        "hypothetical: Dartmouth's 2025 research names it; "
        "Khan Academy's Khanmigo team explicitly designs "
        "against it; Nature's 2025 RCT shows that AI tutoring "
        "CAN improve learning BUT only when the interaction "
        "pattern is right. Without this skill, the default "
        "teen-plus-ChatGPT interaction defaults to outsourcing."
    ),
    psychology_framework=(
        "Piaget's formal-operational stage (11+): teens can "
        "reason metacognitively about their own thinking, "
        "which is the capability this skill leverages ('ask "
        "AI to critique my reasoning' requires the teen to "
        "HOLD their own reasoning as an object to inspect). "
        "Vygotsky's zone of proximal development: AI tutoring "
        "done right is ZPD-scaffolding — the AI is the more-"
        "capable-peer that the teen works with to reach "
        "material just beyond independent reach. Vygotsky's "
        "framework is explicit that the scaffolding must be "
        "REMOVABLE for learning to stick; the protégé test "
        "(move 4) IS the scaffolding-removal check. Cognitive "
        "load theory (Sweller): direct answer-provision by AI "
        "prevents schema-formation because the working memory "
        "never has to construct the schema; Socratic "
        "questioning by AI preserves schema-formation. "
        "Self-determination theory: the four moves preserve "
        "the teen's autonomy (they drive the interaction), "
        "competence (measurable growth), and relatedness "
        "(the AI is framed as a helpful partner, not a "
        "replacement)."
    ),
    creator_luring_awareness=(
        "Indirect but meaningful. Teens who habitually "
        "outsource their thinking to AI are more susceptible "
        "to sophisticated persuasion campaigns (the 'whatever "
        "sounds good in my feed' default). Teens who "
        "internalise the protégé test have a built-in check "
        "for any external source: 'can I restate this in my "
        "own words? does it actually hold up?'. Complements "
        "the 13-15 Critical-Thinking lateral reading row "
        "(1h) and the 4-6 Learning 'real/pretend/maybe-made-"
        "up' row — all three are about not accepting "
        "content at face value, just tuned to age-"
        "appropriate interaction patterns."
    ),
    example_activity=(
        "SESSION 1 - CALIBRATE THE FOUR MOVES (30-40 min, "
        "one-on-one with a caregiver or tutor who has some "
        "AI fluency). Pick ONE homework problem or learning "
        "topic the teen is actually working on. Walk through "
        "all four moves explicitly: "
        "  MOVE 1 (ANSWER FIRST, ASK SECOND): teen writes or "
        "speaks their own best attempt at the answer FIRST. "
        "Even a bad attempt. Even 'I don't know where to "
        "start, but I think it's related to X'. "
        "  MOVE 2 (CRITIQUE MY REASONING): teen pastes their "
        "attempt into the AI and asks literally: 'Here is my "
        "reasoning. What is right about it? What is wrong? "
        "Do NOT give me the final answer; critique my "
        "thinking.' Most AIs will comply if asked explicitly; "
        "some need a nudge like 'You are a Socratic tutor. "
        "Do not reveal the final answer.' "
        "  MOVE 3 (EXPLAIN LIKE I'M IN GRADE 8): when the "
        "AI uses a concept the teen doesn't yet have, teen "
        "says: 'Explain [concept] like I'm in grade 8. Use "
        "a concrete example, not a definition.' This turns "
        "vocabulary-floods into actual scaffolding. "
        "  MOVE 4 (PROTÉGÉ TEST): teen closes the AI window, "
        "waits 10 minutes, then teaches the concept out loud "
        "to the caregiver or into the voice memo app. If "
        "they can't do it in their own words, they haven't "
        "learned it yet — back to move 1. "
        "WEEKLY 20-MIN APPLICATION. Teen picks ONE topic a "
        "week from current coursework and runs the full four-"
        "move sequence. The goal is NOT to cover more "
        "material; it is to learn one topic DEEPLY. Over "
        "time this becomes the teen's default mode and "
        "applies across all AI interactions, not just "
        "homework."
    ),
    gamification_element=(
        "The 'taught it back' journal. Teen logs one-line "
        "entries for each topic they ran through the four "
        "moves + protégé test. Entry format: topic + date + "
        "who they taught it to (sibling, friend, caregiver, "
        "voice memo). Twelve entries in a year is ambitious; "
        "twenty is stretch. The gamified metric is NOT "
        "'topics learned per week' — it is 'topics I can still "
        "teach back a month later'. Quarterly, teen picks "
        "three old journal entries at random and tests "
        "whether they can still teach them. Entries that "
        "survive the 3-month retention check are permanent. "
        "Entries that fail go back into the active learning "
        "queue. This is retrieval-practice-at-scale in the "
        "teen's own life."
    ),
    screen_time_guidance=(
        "Adds roughly 30-45 min per topic to what "
        "otherwise would be a 5-min AI shortcut. The trade "
        "is by design: short-term pain for long-term "
        "retention. Research cited above (Dartmouth, Nature "
        "2025, Khan Academy) all support the trade "
        "quantitatively. Doesn't displace other screen time; "
        "is itself productive screen time. The weekly 20-min "
        "application is the minimum dose for the habit to "
        "stick."
    ),
    parental_controls_component=(
        "No technical control — this is a habit skill. "
        "Complementary: (a) caregiver models the four moves "
        "on the caregiver's OWN AI interactions ('I asked "
        "Claude for a draft, but first let me sketch my "
        "own outline'); (b) when school assignments are "
        "suspected of being AI-outsourced, caregiver asks "
        "'teach me this topic' — not as a gotcha, as a "
        "check-in on the four-move protocol; (c) do NOT "
        "ban AI usage (this trains sneaking); do teach the "
        "protocol openly. Teacher collaboration: if the "
        "school has an AI policy, ensure the teen knows it. "
        "Most school policies in 2025-2026 permit AI use for "
        "learning but prohibit it for final-work submission "
        "without attribution — the four moves support both "
        "sides of that line."
    ),
    media_quality_rubric=(
        "GOOD: teen writes their own best attempt FIRST "
        "(even a bad attempt); AI is explicitly instructed "
        "to critique reasoning, not provide answers; "
        "'explain like I'm in grade 8' used freely; "
        "protégé test (teach it back 10+ min after closing "
        "AI) is non-negotiable; caregiver models the "
        "pattern in their own AI use; journaled retention "
        "check quarterly. AVOID: banning AI use (teaches "
        "sneaking, not discernment); using the protocol as "
        "a gotcha to catch cheating (trust damage); "
        "skipping move 1 because 'it's faster' (removes the "
        "whole learning mechanism); accepting 'I understand' "
        "without the protégé test (self-assessment of "
        "understanding is notoriously unreliable per the "
        "Dunning-Kruger literature); teacher or caregiver "
        "requiring perfect four-move execution on every "
        "homework problem (burnout — one topic a week is "
        "the dose)."
    ),
    en_ca_content=(
        "**Same tool, two completely different outcomes.** A "
        "teen using ChatGPT / Claude / Gemini as a TUTOR "
        "comes out of grade 10 smarter, more capable, with "
        "real knowledge they can apply in grade 11 and "
        "university. A teen using the EXACT SAME TOOL as a "
        "shortcut comes out of grade 10 with good grades "
        "and not much else. The difference is not the tool. "
        "It's the four moves.\n\n"
        "**Why this matters (with evidence).** Dartmouth "
        "researchers (2025) called it the 'illusion of "
        "mastery' — you FEEL like you understand because "
        "you read the AI's output, but you can't actually "
        "do the thing. Your tests prove it. Your grade "
        "11 proves it. Your first university course "
        "proves it. Meanwhile a teen using AI as a real "
        "tutor can outperform traditional in-class active "
        "learning (Nature Scientific Reports, 2025 RCT). "
        "The gap compounds year-on-year.\n\n"
        "**Move 1 — Answer first, ask second.** Before you "
        "type your homework problem into the AI, write "
        "your own best attempt. Even a bad attempt. Even "
        "'I think it's about X but I'm stuck at Y'. The "
        "act of constructing your own answer is where "
        "learning happens — research calls this the "
        "'generation effect' (Slamecka & Graf, 1978) and "
        "it's been replicated for fifty years.\n\n"
        "**Move 2 — Ask AI to critique YOUR reasoning.** "
        "Paste your attempt. Literally type: **'Here is my "
        "reasoning. Tell me what is right, what is wrong, "
        "and what I should rethink. Do NOT give me the "
        "final answer.'** Most AIs will comply if asked "
        "explicitly. For tricky ones, add 'You are a "
        "Socratic tutor. Ask me guiding questions; do not "
        "reveal the final answer.' This is the single move "
        "that flips AI from shortcut to tutor.\n\n"
        "**Move 3 — Explain like I'm in grade 8.** When "
        "the AI uses a concept you don't actually have yet "
        "— big vocabulary, fancy framing — stop and say: "
        "**'Explain [concept] like I'm in grade 8. Use a "
        "concrete example, not a definition.'** This "
        "turns vocabulary-flood into real scaffolding. "
        "Nothing is 'too basic' to ask.\n\n"
        "**Move 4 — The protégé test.** This is the one "
        "that matters most. Close the AI window. Wait 10 "
        "minutes. Then teach the concept OUT LOUD — to a "
        "sibling, a friend, a caregiver, or even into the "
        "voice memo app on your phone. If you can't do it "
        "in your own words, you didn't learn it. Back to "
        "move 1. Research calls this the 'protégé effect' "
        "(Fiorella & Mayer, 2013+) — learners who prepare "
        "to teach the material learn it more deeply.\n\n"
        "**Weekly rhythm.** Pick ONE topic from your "
        "actual coursework each week. Run all four moves. "
        "Log it in a one-line journal entry: topic, date, "
        "who you taught it to. Twelve entries in a year "
        "is good; twenty is exceptional. Quarterly, pick "
        "three old entries at random and see if you can "
        "still teach them. The ones that survive the "
        "3-month check are the ones you actually own.\n\n"
        "**You'll be tempted to skip moves 1 and 4.** "
        "They feel slow. Move 1 feels pointless ('why "
        "write a wrong answer first?') and move 4 feels "
        "weird ('I already read it, why do I need to say "
        "it out loud?'). Those exact two moves are where "
        "the learning lives. Skip them and you are using "
        "a very expensive tool to make yourself dumber. "
        "Do them and you compound.\n\n"
        "**One last thing.** Your school probably has an "
        "AI policy. In 2025-2026, most schools permit AI "
        "use for LEARNING but require attribution (or "
        "prohibit entirely) for final submissions. The "
        "four moves support both sides of that line "
        "cleanly — you learn with the AI, you submit your "
        "own work. No sneaking required. No cheating. "
        "Just leverage."
    ),
    fr_qc_content="",
    ar_description=(
        "Not applicable. The skill is a conversational "
        "protocol with the AI tool (text or voice); any AR "
        "layer would add friction to the exact moments the "
        "protocol wants speed (move 2 critique request, "
        "move 3 explain-like-grade-8 follow-up). The only "
        "tool is the AI itself plus a voice memo app or "
        "notebook for move 4's protégé test."
    ),
)


def main() -> int:
    client = nc.NotionClient()
    print(f"\n--- Creating row: {ROW['skill']} ---")
    try:
        page = nc.create_research_row(client, **ROW)
        url = page.get("url")
        pid = page.get("id")
        print(f"OK: id={pid}")
        print(f"    url={url}")
        return 0
    except Exception as e:
        print(f"FAIL: {type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
