"""S-R01-STRETCH-1o — 10-12 Critical-Thinking: Following a story back to
where it started (source tracing).

2nd row in the 10-12 × Critical-Thinking cell. Companion to whatever the
existing coverage row is for this age/category. This row delivers the
SIFT method (Stop, Investigate the source, Find better coverage, Trace
claims) adapted for the 10-12 age group — a practical, four-step
source-tracing protocol that complements the 13-15 lateral-reading row
and builds the groundwork for it.

Run once:   python _s_r01_stretch_1o.py
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
    skill="Following a story back to where it started (source tracing)",
    category="Critical-Thinking",
    age_ranges=["10-12"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Multi-Modal",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Introduces the SIFT method (Stop, Investigate the source, "
        "Find better coverage, Trace claims to origin) adapted for "
        "the 10-12 age group. At this age, children are increasingly "
        "independent consumers of online content — YouTube, TikTok, "
        "Reddit, Wikipedia, and social group chats — but they lack "
        "the systematic 'leave the page' habit that separates fact-"
        "checking from gut-feeling evaluation. This skill teaches one "
        "core behaviour: when a claim matters (for a school project, "
        "a heated conversation, a big decision), leave the page and "
        "find where the claim came from. The skill is concrete, "
        "practised on real content, and sequenced to build toward the "
        "13-15 lateral reading protocol (row 1h)."
    ),
    research_source=(
        "Caulfield, M. (2019) 'SIFT (The Four Moves)' — "
        "(hapgood.us/2019/06/19/sift-the-four-moves): the foundational "
        "media-literacy framework from Washington State University "
        "researcher Mike Caulfield. SIFT is used by Stanford History "
        "Education Group, MediaWise, News Literacy Project, and the "
        "RAND Corporation's Truth Decay initiative. It explicitly rejects "
        "in-page checklist approaches (CRAAP test) in favour of 'lateral "
        "reading': immediately opening new tabs to investigate the SOURCE "
        "before evaluating the CONTENT. "
        "Stanford History Education Group (2021) 'Civic Online Reasoning' "
        "(sheg.stanford.edu/cor): large-scale study of students from "
        "middle school through university; consistent finding that most "
        "students (and most adults) evaluate credibility by reading "
        "within the page — looking for design quality, tone, and stated "
        "credentials — while professional fact-checkers immediately "
        "leave the page to verify the source. Teaching the 'leave the "
        "page' behaviour is the single highest-leverage change. "
        "RAND Corporation (2019-2022) 'Truth Decay' series "
        "(rand.org/research/projects/truth-decay.html): policy framework "
        "documenting the erosion of agreement on facts in American and "
        "Canadian public life. Key cause: insufficient media literacy "
        "infrastructure. SIFT-type skills are the individual-level "
        "intervention that complements the institutional responses. "
        "News Literacy Project / Checkology (newslit.org): US non-profit "
        "delivering SIFT-aligned curricula to middle and high schools; "
        "annual survey 'State of the First Amendment' includes Canadian "
        "comparison data. "
        "Canadian Association for Media Literacy Education (CAMLE) and "
        "MediaSmarts (mediasmarts.ca): Canadian-specific media literacy "
        "resources for the 10-12 age group. MediaSmarts 'Young Canadians "
        "in a Wired World' series (Phase III, 2014-2023) documents the "
        "specific information-evaluation challenges for Canadian 10-12 "
        "year olds."
    ),
    threat_addressed=(
        "The primary threat at 10-12 is the 'looks legit' credibility "
        "heuristic: children this age judge reliability primarily by "
        "visual design quality (professional-looking site = trustworthy), "
        "tone (confident and specific = accurate), and surface authority "
        "(has a Wikipedia article = must be true). These heuristics "
        "are exploited systematically by misinformation producers who "
        "invest in professional design and confident framing. The SIFT "
        "'leave the page' habit replaces the look-at-this-page evaluation "
        "with look-at-what-others-say-about-this-source evaluation — "
        "far more reliable and much harder to fake. Secondary threat: "
        "circular sourcing — a claim supported only by sources that "
        "all trace back to the same original claim (common in fringe "
        "content). Source tracing reveals the circular loop."
    ),
    psychology_framework=(
        "Piaget's concrete-operational stage (7-12): children this age "
        "can handle systematic procedures ('follow these steps') and "
        "logical reasoning, but abstract concepts ('evaluate epistemological "
        "credibility') are still developing. SIFT works at this stage "
        "because it is a PROCEDURE, not an abstraction — four steps, "
        "each with a concrete action. "
        "Vygotsky's ZPD: the 10-12 year old CAN source-trace with "
        "scaffolding (a checklist, caregiver modelling, a shared "
        "practice session) but does not do so spontaneously. The skill "
        "installs the scaffold until the procedure becomes automatic "
        "by age 13. "
        "Dual-process theory (Kahneman): the 'looks legit' heuristic "
        "is System 1 — fast, low-effort, confidence-weighted. SIFT is "
        "a System 2 procedure that is deliberately introduced as a "
        "friction point. Over 4-8 weeks of practice, the procedure "
        "starts to feel fast enough that it becomes the default for "
        "high-stakes claims."
    ),
    creator_luring_awareness=(
        "Direct and specific. Recruiting pipelines — whether political, "
        "commercial, or predatory — rely on 'gateway content': plausible-"
        "looking material that makes a moderate, credible-sounding claim "
        "to establish initial trust before escalating. SIFT applied to "
        "gateway content reveals the organisation behind it in 60-90 "
        "seconds. For 10-12 year olds, common gateway content includes: "
        "health misinformation (supplements, anti-vaccine), environmental "
        "doom content that escalates to nihilism, political conspiracy "
        "lite (gateway before full radicalization content). Source "
        "tracing reveals the full context of the organisation making "
        "the claim before the child has invested emotional trust in it."
    ),
    example_activity=(
        "THE 60-SECOND SOURCE TRACE (20-25 min practice session, then "
        "ongoing as a 60-second habit). "
        "Step 1 — PICK A CLAIM. Caregiver and child pick a claim that "
        "showed up in a news story, a group chat, or a social feed this "
        "week. Something the child actually encountered, not a textbook "
        "example — the real-world hook is critical at this age. "
        "Step 2 — STOP. Before evaluating the content, close the "
        "impulse to judge. Ask: 'What is this page trying to do? Am I "
        "about to make a decision based on it?' If the answer is no "
        "(low-stakes entertainment), SIFT is optional. If yes, proceed. "
        "Step 3 — INVESTIGATE THE SOURCE. Open a new tab. Search the "
        "organisation or person making the claim + 'background' or "
        "'criticism'. Look at Wikipedia for organisations. Look at "
        "who is covering them. Does the source have a track record? "
        "Who funds it? Who runs it? "
        "Step 4 — FIND BETTER COVERAGE. Search the specific claim "
        "in news search (Google News or a library database). Has "
        "CBC, Globe and Mail, Toronto Star, or the Canadian Press "
        "covered this? What did they find? Are multiple independent "
        "outlets reporting the same thing? "
        "Step 5 — TRACE THE CLAIM. Where did the original claim start? "
        "Often: one study, one tweet, one press release. Find it. "
        "Read the original, not the summary. Does the original actually "
        "say what the article claims it says? "
        "DEBRIEF: What did you find? Did the source check out? Did "
        "multiple outlets confirm? Did the original claim match what "
        "was reported? Most important question: would you share this now? "
        "Why or why not?"
    ),
    gamification_element=(
        "The 'where did it start?' challenge. For two weeks, whenever "
        "someone in the family shares something online — a statistic, "
        "a surprising headline, a health claim — the challenge is to "
        "trace it back to its origin. Whoever gets to the original "
        "source first 'wins' the round. Keep a tally. The debrief "
        "question is always the same: 'Did the original say what the "
        "article/post claimed?' Variants: (a) school project check — "
        "every source in a school project gets a 60-second SIFT check "
        "before it goes in the bibliography; (b) family group chat "
        "fact-check — any claim that lands in the family group chat "
        "is fair game for a trace. Normalises the habit and makes it "
        "collaborative rather than corrective."
    ),
    screen_time_guidance=(
        "The SIFT procedure adds 60-90 seconds to any high-stakes "
        "information encounter. For most social content, it is "
        "appropriately NOT applied — source-tracing every meme is "
        "exhausting and trains avoidance. The skill is explicitly "
        "graduated: 'does this claim matter?' If yes (school, "
        "health, decision-affecting), SIFT. If no (low-stakes "
        "entertainment), skip. Teaching the graduation criterion "
        "is as important as teaching the procedure. Net screen "
        "time impact: neutral to slightly down as the child "
        "develops a habit of pausing before sharing."
    ),
    parental_controls_component=(
        "No technical control is appropriate here — source evaluation "
        "is a human skill. Complementary caregiver actions: "
        "(a) narrate your own SIFT use aloud when you encounter a "
        "dubious claim ('I'm going to check where this came from "
        "before I believe it'); "
        "(b) when the child shares something from a group chat, "
        "casually ask 'where do you think that came from?' — not as "
        "a gotcha, as genuine curiosity; "
        "(c) use the family library card to access Canadian newspapers "
        "online (most public libraries provide free access to "
        "Globe and Mail, Toronto Star, CBC digital archive via "
        "Pressreader or equivalent) — this gives the child a "
        "reliable-source comparison point. "
        "MediaSmarts (mediasmarts.ca) provides Canadian-specific "
        "parent guides for this age group. CBC Kids News "
        "(cbc.ca/kidsnews) is an age-appropriate model of "
        "source-cited journalism that children can use as a "
        "reference point for 'what verified reporting looks like'."
    ),
    media_quality_rubric=(
        "GOOD: child applies SIFT to a claim that matters before "
        "sharing or acting on it; investigates the source in a "
        "new tab (not just reads the page carefully); finds at "
        "least one independent source confirming or disconfirming; "
        "traces the claim to its original publication; uses the "
        "graduation criterion ('does this claim matter?') to decide "
        "when to apply SIFT. "
        "AVOID: applying SIFT to everything (burnout); using SIFT "
        "as a tool to 'win' arguments ('you didn't check your source'); "
        "trusting design quality as a substitute for source checking; "
        "treating Wikipedia as a primary source rather than a "
        "starting point for source discovery. "
        "The standard: 'I'm not sure where that came from — let me "
        "check.' That sentence, spoken spontaneously by a 10-12 year "
        "old, is the skill. Everything else builds to that sentence."
    ),
    en_ca_content=(
        "**Where did that come from?** Here is something most people "
        "do not know: professional fact-checkers do not spend a long "
        "time reading an article carefully to decide if it is true. "
        "They leave the page immediately and spend their time "
        "checking the SOURCE. Who published this? Who funds them? "
        "Do other reliable sources report the same thing?\n\n"
        "**The SIFT method — four steps, 60 seconds.** When you see "
        "something that matters (for school, health, a big decision, "
        "a heated conversation), run these four moves:\n"
        "1. **Stop.** Before you react, share, or believe — pause. "
        "Ask: 'Does this claim matter? Am I about to make a decision "
        "based on it?'\n"
        "2. **Investigate the source.** Open a new tab. Search the "
        "name of the website or organisation + 'background' or "
        "'criticism'. What does Wikipedia say about them? Who funds "
        "them? Do they have a track record?\n"
        "3. **Find better coverage.** Search the specific claim in "
        "news search. Has CBC, Globe and Mail, or the Canadian Press "
        "covered it? What did they find? Do multiple independent "
        "outlets agree?\n"
        "4. **Trace claims to origin.** Often, a story traces back to "
        "one study, one tweet, or one press release. Find it. Read "
        "the original. Does it actually say what the article claims? "
        "(Often: no.)\n\n"
        "**You do not need to do this for everything.** A funny video? "
        "No SIFT needed. Something that someone is using to convince "
        "you of a big claim? Yes, absolutely. The skill is knowing "
        "when it matters.\n\n"
        "**The key habit: leave the page.** The one move that "
        "separates good fact-checkers from bad ones is leaving the "
        "page to check the source. Reading the page more carefully "
        "does not help — a fake source can be written very carefully. "
        "Open a new tab. That is the move."
    ),
    ar_description=(
        "No AR application for this skill in Phase 1. Future "
        "opportunity: an AR overlay on a printed newspaper or "
        "magazine article that surfaces SIFT prompts as a "
        "scanning layer — 'tap the byline to investigate this "
        "source' — could be a strong Show-and-Tell application. "
        "Flag for Phase 2 if AR showcase capability expands."
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
