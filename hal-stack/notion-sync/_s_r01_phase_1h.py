"""S-R01-PHASE-1h — 13-15 Critical-Thinking: lateral reading + AI check.

2nd row in the 13-15 x Critical-Thinking cell. Builds on:
  - 4-6  "Real, pretend, and maybe-made-up pictures" (visual foundation)
  - 13-15 "Is this an ad, or did they really mean it?" (media literacy)

Core skill: when a teen encounters a claim / image / video online,
they leave that page and search for what OTHER sources say about it,
AND specifically ask 'could this have been AI-generated?' as a
sub-question. This is Stanford SHEG's 'lateral reading' technique
adapted with AI-literacy overlay.

Run once:   python _s_r01_phase_1h.py
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
    skill="Reading around something before I believe it (lateral reading + AI check)",
    category="Critical-Thinking",
    age_ranges=["13-15"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Multi-Modal",
    learning_profile=["Standard", "ADHD", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Practitioner-level critical-thinking skill for the social-"
        "feed era. Teen learns the explicit habit used by professional "
        "fact-checkers: when encountering a claim / image / video, "
        "STOP reading on the original page. Open a new tab. Search "
        "for what OTHER sources say about the same claim. Include "
        "one extra sub-question that didn't exist pre-2023: 'could "
        "this be AI-generated?'. The technique is called 'lateral "
        "reading' (vs the default 'vertical reading' — staying on the "
        "page and scrutinising it). Direct research evidence from "
        "Stanford's SHEG shows this single technique, taught in 6 "
        "short lessons, doubles high-schoolers' accuracy at spotting "
        "questionable content."
    ),
    research_source=(
        "Stanford History Education Group (SHEG) - Civic Online "
        "Reasoning curriculum - originated the 'lateral reading' "
        "term and the empirical case for it. Stanford Graduate "
        "School of Education - 'Stanford researchers find students "
        "have trouble judging the credibility of information online' "
        "(ed.stanford.edu/news/stanford-researchers-find-students-"
        "have-trouble-judging-credibility-information-online). "
        "Stanford GSE - 'It doesn't take long to learn how to spot "
        "misinformation online' (ed.stanford.edu/news/it-doesn-t-"
        "take-long-learn-how-spot-misinformation-online-stanford-"
        "study-finds) - 6 x 50-min lessons DOUBLED spotting accuracy. "
        "Stanford Report - 'Judging fact from fiction online' "
        "(news.stanford.edu/2020/10/07/judging-fact-fiction-online). "
        "News Literacy Project - Teaching About AI "
        "(newslit.org/ai) + Checkology virtual classroom - the "
        "'Algo and Gen' characters make algorithm + generative-AI "
        "literacy concrete. NLP RumorGuard series + The Sift "
        "newsletter - weekly viral-claim teardowns for classrooms. "
        "UNESCO - 'Deepfakes and the crisis of knowing' "
        "(unesco.org/en/articles/deepfakes-and-crisis-of-knowing). "
        "Huang & Hu 2025 - 'A Warning is Not Enough. Teach Me How "
        "to Spot Deepfakes' (journals.sagepub.com/doi/10.1177/"
        "10755470251382889) - recent empirical work on which "
        "teaching interventions actually work for deepfake "
        "detection. MediaSmarts Canada - various teen media-"
        "literacy resources."
    ),
    threat_addressed=(
        "The 2026 teen information environment is structurally "
        "harder than any prior generation's. Feeds intermix "
        "reliable news, opinion, entertainment, paid promotion, "
        "AI-generated text (ChatGPT-style summaries), AI-generated "
        "images (indistinguishable from photos for most adults), "
        "AI-generated video (deepfakes crossed the 'good enough to "
        "fool teenagers' threshold around 2024-2025), and "
        "algorithmic amplification that rewards engagement over "
        "accuracy. Default vertical reading ('does this page look "
        "legit?') is exactly wrong — sophisticated bad actors "
        "optimise page-surface signals. Lateral reading — leaving "
        "the page to ask other sources — is the only technique that "
        "scales. Deepfakes specifically target teens (including "
        "through non-consensual sexualised imagery in schools, per "
        "the 19thnews.org + UK PSHE Association 2025 reporting); "
        "the AI-check sub-question is specifically about teens not "
        "being targets of manipulated-media scams."
    ),
    psychology_framework=(
        "Piaget's formal-operational stage (11+): teens can reason "
        "about abstract systems (algorithms, source reliability, "
        "generative models) and hold multiple representations in "
        "mind simultaneously (the claim + the evidence + the "
        "source). Metacognition research: the skill is explicitly "
        "metacognitive — the teen notices their own automatic "
        "'feels-true' reaction and overrides it with a deliberate "
        "secondary search. Dual-process theory (Kahneman): "
        "lateral reading is a System-2 override of System-1's "
        "'looks real, is real' default. SHEG research validates "
        "the framework empirically: intervention effects are "
        "robust, fast, and transfer to new topics not in the "
        "curriculum. Self-determination theory: the skill satisfies "
        "competence (concrete, achievable technique) and autonomy "
        "(teen does the verification, not the caregiver)."
    ),
    creator_luring_awareness=(
        "Precision-targeted scams against teens increasingly use "
        "AI-generated profile photos (of the scammer), AI-generated "
        "'proof' screenshots, and LLM-generated conversation scripts "
        "that sound authentic. The lateral-reading + AI-check "
        "pattern specifically defeats: (1) fake 'friend of a friend' "
        "profiles (reverse image search the profile photo → it's "
        "AI); (2) 'leaked' screenshots used as leverage (Google the "
        "exact claim → no other source has it); (3) AI-narrated "
        "'news' videos pushing sextortion / crypto scams / other "
        "teen-targeted frauds. Complements the 13-15 sextortion "
        "row (1f) and the 13-15 2FA row (1d)."
    ),
    example_activity=(
        "PART A - INSTALL THE HABIT (2 x 30-min sessions, one week "
        "apart). Session 1: caregiver pulls up 3 short viral claims "
        "(any recent social-feed trend) and asks the teen 'true? "
        "false? AI?' Teen picks their answer. Then caregiver "
        "demonstrates lateral reading: open a new tab, search for "
        "the CLAIM (not the source), read what 3+ other sources "
        "say, conclude. For images: run a reverse image search "
        "(Google Images → 'search by image'). For AI-check: note "
        "tells (too-smooth fingers in hands, text that doesn't "
        "make words, shadows that go different directions, audio "
        "that drifts out of sync with mouth). Session 2: teen "
        "drives the search on 3 new claims while caregiver watches. "
        "Same process, teen-led. "
        "PART B - WEEKLY 'SIFT ITEM' (5 min, ongoing). Family picks "
        "ONE viral thing a week - a meme, a video clip, a "
        "screenshot - and a teen does the lateral-reading check. "
        "Deliberately low-pressure. Not every item resolves; the "
        "point is practicing the HABIT, not reaching a verdict. "
        "Pair with the News Literacy Project's free weekly "
        "RumorGuard newsletter for pre-curated items."
    ),
    gamification_element=(
        "The 'caught one' journal. Shared family notebook (physical "
        "or in Notes app) where the teen logs any viral thing they "
        "lateral-read-checked and found to be misleading, AI, or "
        "flat-out fake. One entry per month is great. Five in a "
        "year is a badge of honour. Critical non-goal: NOT a "
        "competition to 'catch more'. Catching zero in a given "
        "month means the teen's feed is reliable that month; "
        "catching one means the habit worked. Silver stickers for "
        "'tried the check, answer was inconclusive'. Gold for "
        "'tried the check, found evidence the thing was wrong'. "
        "Both valued equally; the habit is the reward."
    ),
    screen_time_guidance=(
        "Inherently on-screen (lateral reading happens in browser "
        "tabs). Adds roughly 2-5 minutes per week of deliberate "
        "verification time; subtracts some amount of low-quality "
        "scrolling as the teen's bar for 'what's worth my time' "
        "rises. Net effect per SHEG evidence is higher information "
        "quality per minute of screen time, not longer or shorter "
        "overall screen time."
    ),
    parental_controls_component=(
        "No technical control needed; this is a habit skill. "
        "Complementary: ensure the teen's default search engine is "
        "one that surfaces diverse sources (Google, DuckDuckGo, "
        "Kagi) rather than one optimised for ad revenue. Install "
        "one reverse-image-search extension if the teen doesn't "
        "already have Google Lens. Caregiver role: demonstrate "
        "the habit on the caregiver's own questionable-feed items "
        "out loud ('wait, let me check this before I send it to "
        "my sister') - modelling is 80% of adoption in the "
        "SHEG work. Avoid lectures about media literacy; do the "
        "behaviour in front of them instead."
    ),
    media_quality_rubric=(
        "GOOD: teen drives the lateral-reading search themselves; "
        "caregiver models the habit openly on their own items; "
        "reverse image search included in the workflow; AI-check "
        "sub-question explicitly asked; weekly low-pressure "
        "practice on real-world items; catches valued equally "
        "with non-catches. AVOID: caregiver finishing the search "
        "for the teen (defeats autonomy); only practicing on items "
        "the caregiver already knows are fake (removes the real-"
        "world calibration); treating the teen as 'dumb for "
        "believing it initially' (the algorithm is designed by "
        "adults to deceive adults — teen believing it was the "
        "designer's intent, not the teen's failure); using the "
        "skill as a lever to criticise the teen's taste in "
        "content; adding the skill on top of content-filtering "
        "surveillance (mixes protection with lateral-reading "
        "autonomy)."
    ),
    en_ca_content=(
        "**Professional fact-checkers don't scrutinise a page. "
        "They leave it.** And so should you.\n\n"
        "**The default everyone uses is wrong.** When something "
        "shows up in your feed and feels off, most people (adults "
        "included) stay on the page and look harder: does the "
        "website look legit? does the author's name sound real? "
        "do the photos look professional? This is called **vertical "
        "reading** and it's exactly how bad actors want you to "
        "think. Sophisticated scammers optimise the page-surface — "
        "'looks legit' is the first thing they get right.\n\n"
        "**Lateral reading is the working technique.** Stanford "
        "researchers spent years studying how professional fact-"
        "checkers work. The pattern: they read for about 30 "
        "seconds, then leave the original page, open a new tab, "
        "and search for what OTHER sources say about the same "
        "claim. In 6 lessons of 50 minutes each, high-schoolers "
        "who learned this doubled their accuracy at catching "
        "fake content.\n\n"
        "**The four-move routine for 2026:**\n\n"
        "1. **Notice the reaction.** When something feels 'wow' "
        "or 'outrageous' or 'too perfect' — that feeling is "
        "engineered. It's the exact signal to slow down.\n\n"
        "2. **Leave the page.** Literally open a new tab. Don't "
        "analyse the source while you're still in the source.\n\n"
        "3. **Search the claim, not the source.** If the page "
        "says 'Canadian government bans all dogs', search "
        "`Canada dogs banned`. If three reliable sources (CBC, "
        "Globe, Reuters, the Government of Canada's own site) "
        "say nothing about it — it's made up.\n\n"
        "4. **Add the AI check.** Could this have been "
        "AI-generated? For images, reverse-image-search it — if "
        "it appears nowhere else on the internet OR first appeared "
        "on an AI-art site, it's AI. For text claims, check if "
        "any named person actually said the quoted thing. For "
        "videos, look for: hands with too-smooth fingers, text "
        "that doesn't make words, shadows that go in different "
        "directions, audio that drifts out of sync with mouth "
        "movements.\n\n"
        "**Weekly practice.** The News Literacy Project publishes "
        "a free newsletter called **RumorGuard** every week. Pick "
        "one item, do the four moves, see if your call matches "
        "theirs. Five minutes, once a week. The habit builds "
        "faster than you'd think — SHEG's six-lesson study "
        "doubled accuracy, and you're doing it live.\n\n"
        "**Why it matters.** Your feed is the biggest "
        "information source in your life. The people designing "
        "that feed are paid to hold your attention, not to keep "
        "you accurately informed. Lateral reading is the only "
        "technique that scales against a system optimised for "
        "engagement. You can't out-scrutinise a well-designed "
        "lie; you can only out-source it.\n\n"
        "**Keep score.** Every time you catch something that "
        "turns out to be fake or AI-generated, write it in a "
        "'caught one' notebook. One a month is great. The goal "
        "is not 'catch more' — it's 'notice the feeling, do the "
        "check, trust the evidence'."
    ),
    fr_qc_content="",
    ar_description=(
        "Not applicable. The skill is a browser-tab workflow; "
        "any AR overlay would add friction to the exact moment "
        "the teen needs to context-switch (leave the source). "
        "The browser itself is the tool; reverse-image-search "
        "(built into Google Images / Google Lens) is the only "
        "extra capability needed."
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
