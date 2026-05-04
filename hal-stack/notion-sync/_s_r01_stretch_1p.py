"""S-R01-STRETCH-1p — 7-9 Critical-Thinking: Real, made-up, or somewhere
in between — a child's guide to spotting the difference.

2nd row in the 7-9 × Critical-Thinking cell. Bridges the 4-6 'True things
and story things' row (1c) and the 13-15 'Lateral reading + AI check' row
(1h). At age 7-9 children are moving from concrete binary thinking (true/
false) toward recognising a spectrum of reliability. This row teaches three
categories of online content — verified, opinion, and invented — and a
concrete sorting habit.

Run once:   python _s_r01_stretch_1p.py
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
    skill="Real, made-up, or somewhere in between — sorting what I find online",
    category="Critical-Thinking",
    age_ranges=["7-9"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Show-and-Tell",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Children aged 7-9 are cognitively ready to move beyond the binary "
        "'real vs. pretend' of the 4-6 stage toward a three-category sorting "
        "framework: (1) VERIFIED — reported by multiple news sources, backed "
        "by named experts or studies, checkable against reference sources; "
        "(2) OPINION — what someone believes, which can be thoughtful or "
        "careless, but is not the same as a fact; (3) INVENTED — fiction, "
        "satire, jokes, or deliberate misinformation. The skill teaches a "
        "three-bucket sorting habit: when encountering any online content that "
        "makes a factual claim, the child can ask 'which bucket does this go "
        "in?' The framework is deliberately simple — three buckets, not a full "
        "epistemological model — because automaticity at this age requires "
        "repeated practice on a small number of concrete categories."
    ),
    research_source=(
        "Piaget's concrete-operational stage (7-12): children this age develop "
        "classification skills — sorting objects and ideas into categories by "
        "shared properties. The three-bucket framework directly uses this "
        "developmental capacity. Abstract concepts ('epistemic credibility') "
        "are unavailable; concrete categories ('which bucket?') work. "
        "Common Sense Media (commonsensemedia.org) — 'Media Literacy for "
        "Elementary Students': consistent finding that children aged 7-9 can "
        "reliably distinguish opinion from reported fact when given explicit "
        "category labels, but rarely do so spontaneously without prompting. "
        "Prompt frequency drops over 4-6 weeks as the habit automates. "
        "National Association for Media Literacy Education (NAMLE) — "
        "'Key Questions to Ask When Analyzing Media' (namle.net): foundational "
        "framework asking 'who created this and why?' Applied to the 7-9 "
        "age group, the question simplifies to 'is this person trying to "
        "tell me something true, share their opinion, or make something up?' "
        "MediaSmarts (mediasmarts.ca) — 'Break the Fake' toolkit: Canadian "
        "resource designed for the 7-12 age group, includes the verified/"
        "opinion/false distinction as its core sorting mechanism. Available "
        "in English and French. Explicitly Canadian contexts (CBC, Globe and "
        "Mail used as verified-source examples). "
        "Lewandowsky, S. et al. (2012) 'Misinformation and its correction: "
        "continued influence and successful debiasing' (Psychological Science "
        "in the Public Interest 13(3)): foundational paper establishing that "
        "misinformation is harder to correct once believed than to inoculate "
        "against before belief. Teaching the sorting framework at 7-9 is "
        "inoculation-timing — before the teen years when peer-shared "
        "misinformation accelerates."
    ),
    threat_addressed=(
        "The primary threat at 7-9 is unsupported factual claims shared via "
        "peer networks (playground, group chats if the child has a device) "
        "and family social media. Children this age are beginning to cite "
        "'I saw it online' as evidence in arguments with peers and siblings — "
        "a habit that, uncorrected, persists into adult misinformation "
        "vulnerability. Secondary threats: (a) health misinformation "
        "('sugar causes ADHD' type claims heard from peers that the child "
        "repeats at home); (b) advertising presented as fact (particularly "
        "in YouTube influencer content where the line between opinion and "
        "sponsored claim is routinely blurred); (c) age-inappropriate "
        "political content shared by adults in the child's environment "
        "that the child absorbs as fact without category awareness."
    ),
    psychology_framework=(
        "Piaget's concrete-operational stage: classification and seriation "
        "skills are the cognitive highlight of this stage. Children delight "
        "in sorting activities and can apply consistent rules to sort objects "
        "and ideas. The three-bucket framework is a classification game that "
        "matches the available cognitive toolkit. "
        "Vygotsky's ZPD: the caregiver models the sorting process aloud "
        "('I think this goes in the opinion bucket because the person is "
        "saying what they prefer, not what was measured') until the child "
        "can run the sort independently. "
        "Theory of Mind development (7-9): children this age are consolidating "
        "the understanding that other people have beliefs, intentions, and "
        "motivations different from their own. This directly supports "
        "'who made this and why?' — the child can now genuinely wonder "
        "about the creator's intent rather than just the content."
    ),
    creator_luring_awareness=(
        "The 'somewhere in between' category (opinion) is the most important "
        "for luring resistance. Recruiting content rarely presents itself as "
        "fiction — it presents itself as opinion that is 'just asking "
        "questions' or sharing 'what they don't want you to know.' "
        "A child who can place this content in the opinion bucket — as "
        "distinct from verified fact — is significantly more resistant to "
        "treating it as authoritative. The sorting habit also builds the "
        "metacognitive question 'what is this person trying to make me "
        "believe?' which is the foundational creator-luring question."
    ),
    example_activity=(
        "THE SORTING GAME (15-20 min, play 2-3 times per week for 4 weeks). "
        "Print or draw three boxes on paper: VERIFIED (tick mark), OPINION "
        "(speech bubble), INVENTED (magic wand). "
        "Round 1 — EASY EXAMPLES. Read out five statements the child can "
        "immediately sort: 'Ottawa is the capital of Canada' (Verified), "
        "'Chocolate ice cream is better than vanilla' (Opinion), "
        "'Dragons are endangered' (Invented). Child places each in a box "
        "and explains why. Caregiver confirms or offers alternative framing. "
        "Round 2 — REAL CONTENT. Pull 3-4 headlines or social posts from "
        "actual content the child has seen this week — a YouTube video claim, "
        "a news headline, something from a group chat. Child sorts them. "
        "The goal is NOT to sort perfectly — it is to develop the habit of "
        "asking the question. Some items genuinely belong in 'somewhere "
        "in between' (the child can create a fourth catch-all box if needed). "
        "Round 3 — THE FOLLOW-UP QUESTION. For anything that lands in "
        "VERIFIED: can you find one other place that says the same thing? "
        "(Simple: 'Let us Google it together.') For OPINION: whose opinion "
        "is it, and does it matter? (A doctor's opinion on health vs. a "
        "random commenter.) For INVENTED: was it meant to be funny, "
        "or was it pretending to be true? "
        "End with: 'What did we find today that surprised us?'"
    ),
    gamification_element=(
        "The weekly 'Find the Opinion' challenge. At dinner or car rides, "
        "one person in the family shares something they heard or read this "
        "week. The challenge is to sort it together: verified, opinion, or "
        "invented. Keep a family tally on the fridge. Goal: sort 20 items "
        "correctly in a month. The child earns a point for each item they "
        "sort correctly AND explain. Caregiver earns a point when they "
        "change their own initial sort after the child makes a good argument. "
        "This last rule matters: it models intellectual humility and shows "
        "that the game is about thinking, not winning."
    ),
    screen_time_guidance=(
        "The sorting game is best played away from screens (printed "
        "examples, verbal rounds) to reduce distraction and build the "
        "habit as a mental model rather than a screen activity. The "
        "real-content rounds (Round 2) can use screenshots of actual "
        "content printed or shown briefly. Net screen time: neutral. "
        "The skill reduces the child's passive absorption of unquestioned "
        "content over time."
    ),
    parental_controls_component=(
        "No technical control directly addresses the opinion/fact "
        "distinction. Complementary caregiver actions: "
        "(a) narrate your own sorting process aloud when you encounter "
        "a dubious claim ('I think this is someone's opinion, not a "
        "study'); "
        "(b) when a child cites 'I saw it online' as evidence, ask "
        "which bucket — not as a challenge, as a curiosity; "
        "(c) MediaSmarts 'Break the Fake' teacher/parent guide "
        "(mediasmarts.ca/break-fake) provides Canadian-specific "
        "examples and discussion prompts for this age group; "
        "(d) CBC Kids News (cbc.ca/kidsnews) is an age-appropriate "
        "model of what VERIFIED content looks like — using it regularly "
        "builds a reference point."
    ),
    media_quality_rubric=(
        "GOOD: child applies the three-bucket sort spontaneously when "
        "a claim matters; asks 'whose opinion is that?' for clearly "
        "opinion-framed content; knows that verified content requires "
        "more than one source; can explain why something is in the "
        "opinion bucket vs. the invented bucket. "
        "AVOID: treating every opinion as wrong (opinions have value — "
        "the skill is recognising them AS opinions, not dismissing them); "
        "requiring perfect sorts every time (the habit is the goal, not "
        "the score); using the framework as a 'gotcha' when adults share "
        "misinformation (model the sort, don't shame). "
        "The standard: the child asks 'is that real?' when hearing a "
        "surprising factual claim. That question, unprompted, is the skill."
    ),
    en_ca_content=(
        "**Everything you find online goes in one of three buckets.** "
        "Not everything online is a lie. Not everything is true. Most "
        "things are somewhere in between — and knowing which bucket "
        "something belongs in is one of the most useful skills you "
        "can build.\n\n"
        "**Bucket 1: Verified.** Facts that have been checked. Reported "
        "by news organisations that name their sources. Backed by "
        "studies or experts who can be looked up. When you find "
        "something in Bucket 1 from two or three different reliable "
        "sources, you can trust it pretty well.\n\n"
        "**Bucket 2: Opinion.** What someone believes, thinks, or "
        "prefers. Opinions can be thoughtful and worth reading, or "
        "careless and worth ignoring — but they are not the same as "
        "facts. 'Chocolate ice cream is better than vanilla' is an "
        "opinion. 'I think this politician is terrible' is an opinion. "
        "'Studies show that exercise improves focus' — that might be "
        "Bucket 1. The difference: can it be measured?\n\n"
        "**Bucket 3: Invented.** Fiction, jokes, satire, made-up "
        "stories. Sometimes invented things are clearly labelled "
        "(a novel, a comedy video). Sometimes they pretend to be "
        "Bucket 1 when they are actually Bucket 3 — that is the "
        "tricky part.\n\n"
        "**The sorting habit.** When you see something online that "
        "makes a factual claim — especially something surprising or "
        "that someone is using to convince you of something — ask: "
        "which bucket? You do not have to be right every time. "
        "You just have to ask."
    ),
    ar_description=(
        "Show-and-Tell AR opportunity: physical cards with the three "
        "bucket symbols (tick/speech-bubble/wand) that, when held up "
        "to a tablet camera, display an animated sorting example. "
        "Technically feasible as a Toy-to-Life application. Flag for "
        "Phase 2 AR sprint."
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
