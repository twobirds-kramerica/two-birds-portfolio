"""S-R01-STRETCH-1aa — 10-12 Learning: Checking if my AI helper is right —
the verify-before-share habit.

2nd row in the 10-12 × Learning cell. Companion to the existing "Asking
good questions when I search or ask AI" row (multi-age, 7-9/10-12/13-15).
Where that row teaches how to query AI tools effectively, this row
addresses what to do with the answer: AI systems hallucinate, confuse
details, and present false information with the same confident tone as
true information. The 10-12 age group is the earliest cohort actively
using AI tools for schoolwork (homework helpers, research tools, essay
drafters). The verify-before-share habit installed at this age is the
precursor to the 13-15 "lateral reading + AI check" skill.

Run once:   python _s_r01_stretch_1aa.py
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
    skill="Checking if my AI helper is right — the verify-before-share habit",
    category="Learning",
    age_ranges=["10-12"],
    priority="P1-Important",
    status="Research",
    demonstration_method="Show-and-Tell",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Children aged 10-12 are the earliest cohort actively using "
        "AI tools for schoolwork — homework helpers, essay starters, "
        "research tools, and explanation generators. These tools are "
        "powerful learning aids when used well; they are a source of "
        "confident misinformation when used uncritically. AI systems "
        "hallucinate (present invented information as fact), confuse "
        "dates and names, and assert false things with the same "
        "confident tone as true things. This row delivers: (1) a "
        "plain-language model of why AI sometimes gets things wrong "
        "('it predicts what sounds right, not what is true'); "
        "(2) the three-step verify-before-share routine: "
        "Find-it-somewhere-else, Check-the-date, Ask-who-wrote-it; "
        "(3) the distinction between 'AI as a first draft' (appropriate) "
        "and 'AI as a final answer' (risky). This is the 10-12 bridge "
        "between the 7-9 'asking good questions' skill and the 13-15 "
        "'lateral reading + AI check' skill."
    ),
    research_source=(
        "Caulfield, M. (2019). SIFT: Four Moves. Hapgood.us. The "
        "foundational framework for information verification in the "
        "social media era. The four SIFT moves — Stop, Investigate "
        "the source, Find better coverage, Trace claims — are the "
        "basis for the 13-15 lateral-reading row. At 10-12, this "
        "row introduces a simplified precursor: 'find it somewhere "
        "else, check the date, ask who wrote it.' Same intellectual "
        "move, appropriate developmental abstraction. "
        "Stanford History Education Group (SHEG) — Civic Online "
        "Reasoning. Empirical research showing that six 50-minute "
        "lessons on lateral reading and source evaluation doubled "
        "high-school students' accuracy in assessing online "
        "information. The researchers also found that middle-school "
        "students (Grades 6-8 = 11-14) respond well to the lateral "
        "reading technique when it is taught explicitly. "
        "News Literacy Project — Checkology Virtual Classroom "
        "(checkology.org). 'How to Evaluate AI-Generated Content' "
        "module (2024 update): designed for Grades 6-8, teaches "
        "hallucination as a concept, provides verification exercises "
        "using actual AI outputs that contained factual errors. "
        "Laban, G. et al. (2025). 'LLMs Get Lost in Multi-Turn "
        "Conversation.' arXiv:2505.06120. Research showing that AI "
        "systems accumulate errors over multi-turn conversations — "
        "directly relevant to homework-helper use cases where a "
        "student has an extended back-and-forth with an AI tool. "
        "European Parliament (2023). 'Artificial Intelligence Act' — "
        "Article 50 transparency requirements for AI-generated "
        "content. Used as context for why verification is not "
        "paranoia but a recognized societal norm. "
        "MediaSmarts Canada (mediasmarts.ca) — 'AI Literacy for "
        "Youth' (2024 resource package). Canadian-specific, "
        "age-graded resources for Grades 5-8. Includes the "
        "'AI confidence vs. AI accuracy' distinction using "
        "Canadian examples. "
        "OpenAI (2023). 'GPT-4 Technical Report.' Documented "
        "hallucination rates: even the most capable models produce "
        "confident factual errors at a non-trivial rate. Specific "
        "categories of frequent error: biographical details, "
        "recent events, numerical data, citations and quotes. "
        "Used to make the hallucination problem concrete and "
        "non-abstract."
    ),
    threat_addressed=(
        "Three threat vectors in the 10-12 × Learning space: "
        "(a) ACADEMIC INTEGRITY — a student who submits AI-generated "
        "content that contains errors (hallucinated citations, wrong "
        "dates, invented facts) may face academic consequences they "
        "did not anticipate. More importantly, they did not learn "
        "what they were supposed to learn. "
        "(b) CONFIDENT MISINFORMATION SPREAD — 10-12 year olds "
        "share AI-generated facts with peers and adults. An AI "
        "answer that contains an error arrives with the same "
        "confident framing as a correct answer; without a verification "
        "habit, errors propagate. "
        "(c) EPISTEMIC DEPENDENCY — children who habitually accept "
        "AI answers without checking are building a pattern of "
        "outsourcing judgment that becomes harder to reverse as "
        "they move into secondary school. The verify-before-share "
        "habit installs a check that keeps the student's own "
        "critical faculty engaged."
    ),
    psychology_framework=(
        "Concrete-operational reasoning (Piaget, 7-11) to formal "
        "operations (11+): 10-12 year olds are at the transition "
        "between these stages. The hallucination model ('AI predicts "
        "what sounds right') can be taught as an abstract causal "
        "mechanism for older children in this group; younger children "
        "benefit more from concrete examples ('here is an AI answer "
        "that got the year wrong; see if you can find the real year'). "
        "Epistemic development (Kuhn, 2000): children at 10-12 are "
        "moving from 'knowledge is given by an authority' to 'knowledge "
        "can be checked and compared.' The verify-before-share habit "
        "supports this development by giving the child an active role "
        "in verifying rather than passively receiving. "
        "Self-determination theory (Ryan & Deci): framing the "
        "verification habit as 'you are smarter than the AI because "
        "you can actually check' appeals to autonomy and competence "
        "— two of the three basic psychological needs. This framing "
        "is more motivating than 'AI is dangerous, be careful.'"
    ),
    creator_luring_awareness=(
        "The verify-before-share habit has a secondary benefit for "
        "luring-awareness: children who are taught that confident-"
        "sounding content can still be wrong are primed to apply "
        "the same scepticism to confident-sounding messages from "
        "strangers online. The rhetorical pattern of luring — "
        "confident, authoritative-sounding messages presenting false "
        "claims ('I'm a talent scout, I found your profile') — "
        "is structurally similar to AI hallucination. A child who "
        "has practised 'this sounds authoritative but let me verify "
        "it before I act on it' has the right reflex for both "
        "contexts."
    ),
    example_activity=(
        "THE AI FACT-CHECK CHALLENGE (30 min, one setup, then "
        "ongoing as a 60-second habit). "
        "PART 1 — MEET THE HALLUCINATION. "
        "Open an AI tool together (ChatGPT, Claude, Gemini, or "
        "whichever the school uses). Ask it a question that has "
        "a verifiable answer with a specific number or date: "
        "'When was the Trans-Canada Highway completed?' or "
        "'How many goals did Wayne Gretzky score in his career?' "
        "Get the AI answer. Then look it up in an encyclopedia, "
        "textbook, or .gc.ca / .edu source. "
        "Compare. Was the AI right? Was it close but wrong? "
        "Was it wrong by a lot? "
        "This is not to scare the child. It is to show them "
        "that the AI speaks confidently even when it is off. "
        "PART 2 — WHY AI GETS THINGS WRONG. "
        "Plain-language explanation: 'AI reads billions of words "
        "and learns which words come after which other words. "
        "It predicts what sounds right, not what is true. "
        "Most of the time it is right because true things are "
        "written down more often than false things. But sometimes "
        "it guesses wrong and has no idea it guessed wrong. "
        "That is called a hallucination.' "
        "Ask: 'If your friend told you something confidently "
        "but you know they sometimes make things up, what would "
        "you do before repeating it?' "
        "Same move with AI. "
        "PART 3 — THE THREE-STEP CHECK. "
        "Teach the three steps as a habit for AI-assisted research: "
        "Step 1 — FIND IT SOMEWHERE ELSE. Can you find the same "
        "fact in a different source (library database, "
        ".gc.ca, .edu, textbook)? If yes: probably right. "
        "If you can't find it anywhere: red flag. "
        "Step 2 — CHECK THE DATE. AI training data has a cutoff. "
        "For anything that changes over time (statistics, "
        "current events, laws, records) — find a dated source. "
        "Step 3 — ASK WHO WROTE IT. The AI doesn't know. "
        "But the source it's pointing to (if it gives one) "
        "does. Check: is this source trustworthy for this topic? "
        "ONGOING HABIT: before sharing or submitting anything "
        "an AI helped you write — run the three steps on at "
        "least two of the specific facts in it. Takes two "
        "minutes. Makes the whole thing trustworthy."
    ),
    gamification_element=(
        "The 'hallucination hunter' journal. For two weeks, "
        "every time the child uses an AI tool for school or "
        "curiosity, they run the three-step check on one fact "
        "from the AI's answer and record: "
        "(1) What the AI said. "
        "(2) What they found when they checked. "
        "(3) Verdict: right, roughly right, or wrong. "
        "At the end of two weeks, they have a personal data set: "
        "how often was the AI right? Wrong? In what categories? "
        "This transforms verification from a chore into a "
        "genuine scientific observation. The child becomes "
        "an expert on their AI tool's patterns — which is "
        "exactly the right relationship to have with it."
    ),
    screen_time_guidance=(
        "The three-step check takes 2-5 minutes per fact. For "
        "a homework task, checking two facts per AI-assisted "
        "section adds 5-10 minutes to the session. This is "
        "net positive: the child is spending those minutes "
        "in a library database or authoritative site, not "
        "scrolling. Total screen time is likely neutral; "
        "quality of screen time is higher."
    ),
    parental_controls_component=(
        "Technical supports that complement this skill: "
        "(a) Bookmark a verification toolkit together: the school "
        "library database login, a Canadian encyclopedia (Canadian "
        "Encyclopedia at thecanadianencyclopedia.ca), and a general "
        "reference (Britannica, World Book). These are the "
        "'find it somewhere else' destinations. "
        "(b) AI tools to be aware of: ChatGPT (OpenAI, requires "
        "13+ per terms of service in Canada), Google Gemini (13+), "
        "Microsoft Copilot (school-provisioned versions often "
        "have age controls). Ask which AI tools the school "
        "permits and recommends. "
        "(c) News Literacy Project Checkology (checkology.org): "
        "free, school-designed, has a specific AI-verification "
        "module for Grades 6-8. Can be used independently by the "
        "child at this age. "
        "(d) MediaSmarts Canada AI literacy resources "
        "(mediasmarts.ca/ai): Canadian-specific, Grades 4-8, "
        "free printable activities including an AI verification "
        "exercise."
    ),
    media_quality_rubric=(
        "GOOD: child can explain in one sentence why AI sometimes "
        "gets things wrong ('it predicts what sounds right'); "
        "child has run the three-step check on at least one "
        "AI-generated fact; child treats AI output as a starting "
        "point ('first draft') not a final answer; child knows "
        "at least two verification sources for school-relevant "
        "topics. "
        "AVOID: framing the lesson as 'AI is bad, don't use it' "
        "— the goal is appropriate use, not avoidance; framing "
        "every AI answer as suspect (the 10-12 child still needs "
        "to be able to use AI productively — overcorrecting to "
        "total scepticism defeats the purpose); making verification "
        "feel like punishment for using AI ('if you use AI you "
        "have to check everything') — frame it as a two-minute "
        "upgrade that makes the work better. "
        "The standard: the child has checked at least one AI "
        "fact against a non-AI source and formed their own "
        "judgment about the AI's accuracy. That single act — "
        "done once — installs the verify-before-share reflex "
        "at the right developmental moment."
    ),
    en_ca_content=(
        "**AI tools are really useful — and they are not always "
        "right.** When you ask an AI a question, it gives you "
        "an answer that sounds confident and clear. But here "
        "is something important to know: the AI is predicting "
        "what sounds right, not checking what is true. Most "
        "of the time it is right. Sometimes it is not — and "
        "it has no idea.\n\n"
        "This is called a **hallucination**: the AI says something "
        "false with the same confident voice it uses when it "
        "says something true. You cannot tell from the tone. "
        "You have to check.\n\n"
        "**The three-step verify-before-share check:**\n\n"
        "**Step 1 — Find it somewhere else.** Can you find the "
        "same fact in a library database, a .gc.ca website, a "
        ".edu website, or a textbook? If yes: probably right. "
        "If you can only find it in AI: red flag.\n\n"
        "**Step 2 — Check the date.** AI has a training cutoff — "
        "it does not know what happened recently. For anything "
        "that changes (records, statistics, laws, current events) "
        "— find a source with a date on it.\n\n"
        "**Step 3 — Ask who wrote it.** The AI does not know. "
        "But any source it mentions does have an author. Is that "
        "author reliable for this topic?\n\n"
        "**AI is a great first draft.** It can help you start, "
        "help you understand a concept, help you find questions "
        "to ask. It is not a great final answer — not until you "
        "have checked the key facts. The two minutes you spend "
        "checking is what turns an AI output into your work."
    ),
    ar_description=(
        "No AR application in Phase 1. Future opportunity: an AR "
        "experience where an AI answer appears with fact-check "
        "overlays — some facts glow green (verified), some glow "
        "red (contradicted by source), some glow yellow "
        "(unverifiable either way) — making the verification "
        "process spatially concrete. Flag for Phase 2 AR sprint."
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
