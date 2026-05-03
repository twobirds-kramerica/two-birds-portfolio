"""S-R01-STRETCH-1n — 4-6 Emotional-Safety: Big feelings are real;
what I do next is my choice.

2nd row in the 4-6 × Emotional-Safety cell. Companion to whatever the
existing coverage row is for this age/category. This row adds the
foundational emotional-regulation skill for the youngest DCC age group:
the gap between feeling something and acting on it. Rooted in Dan Siegel
and Tina Payne Bryson's 'name it to tame it' framework, adapted for
digital contexts where emotional stimulation is algorithmically amplified.

Run once:   python _s_r01_stretch_1n.py
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
    skill="Big feelings are real; I get to choose what I do next",
    category="Emotional-Safety",
    age_ranges=["4-6"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Play-Acting",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "The foundational emotional-regulation skill for 4-6 year olds "
        "in digital contexts. Screens — and algorithms — are optimised to "
        "produce emotional arousal: excitement, fear, longing, and "
        "frustration. Children aged 4-6 are still developing the prefrontal "
        "cortex capacity to hold a feeling without immediately acting on it. "
        "This skill plants three concepts: (1) feelings are real and valid; "
        "(2) feelings and actions are not the same thing; (3) a pause "
        "between feeling and action is possible, even for small people. "
        "Practical anchors: the 'name it to tame it' labelling protocol "
        "(Dan Siegel), a physical pause gesture the caregiver and child "
        "agree on, and a three-item 'feelings menu' the child can reach "
        "for when overwhelmed by screen content."
    ),
    research_source=(
        "Siegel, D. & Payne Bryson, T. (2011) The Whole-Brain Child "
        "(chapter 2: 'Name It to Tame It'): the act of labelling an "
        "emotional state activates the left prefrontal cortex, which "
        "modulates the right amygdala's arousal response. Naming calms "
        "the neurological circuit responsible for impulsive action. "
        "Application: when a child sees something upsetting, frightening, "
        "or over-exciting on screen, the caregiver names the feeling "
        "first ('that looks really scary'), then the child echoes it. "
        "Kopp, C.B. (1982) 'Antecedents of self-regulation: a developmental "
        "perspective' (Developmental Psychology 18(2)): foundational work "
        "establishing that self-regulation emerges in early childhood and "
        "is heavily scaffolded by caregiver interaction. Children aged 4-6 "
        "are in the middle of this developmental window — they CAN learn "
        "basic regulatory strategies but they require external scaffolding "
        "(the caregiver as the pause model). "
        "Eisenberg, N. et al. (2000) 'Dispositional emotionality and "
        "regulation' (Psychological Bulletin 125(6)): shows that emotional "
        "regulation capacity in early childhood is predictive of peer "
        "relations, academic outcomes, and mental health across the "
        "following decade. Early investment in this skill has compound "
        "returns. "
        "Radesky, J. et al. (2020) 'Overstimulation and digital media use "
        "in young children' (Pediatrics, AAP): algorithmic content "
        "recommendation systems optimise for emotional engagement in ways "
        "that systematically bypass the slow-developing self-regulation "
        "capacity of 4-6 year olds. The 'autoplay' design pattern is "
        "specifically harmful to this age group because it removes the "
        "natural pause point between content pieces. "
        "Common Sense Media 'Children, Teens, and Screen Time' annual "
        "report series: consistent finding that children under 8 are "
        "the most commercially valuable and least cognitively defended "
        "digital audience. Their emotional responses are more extreme, "
        "their attention is more capturable, and their regulatory capacity "
        "is lowest."
    ),
    threat_addressed=(
        "The primary threat is not specific dangerous content (handled "
        "by parental controls) but the REGULATORY CAPACITY erosion "
        "produced by high-stimulation, algorithmically optimised content "
        "at an age when regulatory capacity is still forming. A 4-6 year "
        "old who spends 2-3 hours daily in high-stimulation content without "
        "regulatory practice develops a default operating mode of "
        "'stimulus → immediate reaction' that persists as the pattern "
        "for digital interaction in later years. Secondary threats: "
        "(a) content that produces fear (age-inappropriate horror, news "
        "violence) leading to nightmares and generalised anxiety; "
        "(b) content that produces intense longing/coveting (toy "
        "unboxing, lifestyle content) modelling acquisitiveness; "
        "(c) content that produces aggression (poorly moderated comments "
        "visible even in children's content) normalising reactive anger."
    ),
    psychology_framework=(
        "Piaget's preoperational stage (2-7): children in this stage "
        "think concretely and are highly egocentric — emotional events "
        "feel total and overwhelming because children cannot yet "
        "perspective-take ('everyone feels this way') or time-shift "
        "('this feeling will pass'). The skill must be concrete, physical, "
        "and caregiver-scaffolded. Abstract concepts like 'manage your "
        "emotions' are cognitively inaccessible at this stage. "
        "Vygotsky's zone of proximal development: the child cannot "
        "self-regulate alone in high-stimulation digital contexts yet "
        "can do so with caregiver scaffolding. The caregiver is the "
        "'pause' until the child internalises the pause. "
        "Erikson's autonomy vs. shame/doubt stage (18 months-3 years) "
        "transitions into initiative vs. guilt (3-6 years): children "
        "aged 4-6 are developing a sense of their OWN agency. Framing "
        "the pause as 'you get to choose what you do next' directly "
        "feeds the initiative/agency drive rather than imposing external "
        "control. The skill is permission-giving, not prohibitory."
    ),
    creator_luring_awareness=(
        "Foundational and indirect. Children who learn early that "
        "feelings and actions are separate — that they can feel excited "
        "about something and still pause — are developing the basic "
        "neurological wiring for the resistance-to-luring skills that "
        "apply throughout childhood. A 13-year-old who has never practiced "
        "the feeling-action gap is significantly more vulnerable to "
        "engineered outrage, designed longing, and social pressure than "
        "one who has practiced it since age 5. This is the earliest "
        "layer of the DCC emotional-safety ladder."
    ),
    example_activity=(
        "THE FEELINGS MENU (5-10 min, do 3-4 times in the first week, "
        "then as needed). "
        "Step 1 — BUILD THE MENU TOGETHER. Draw or print three faces on "
        "a piece of paper: one excited/happy, one sad/scared, one mad/"
        "frustrated. Let the child name each face. Add a fourth if the "
        "child suggests one. These are the 'feelings menu' — things that "
        "screens can make them feel. "
        "Step 2 — PRACTICE WITH A SHOW. During a regular screen session, "
        "pause the content 2-3 times and ask: 'What is your body feeling "
        "right now?' Child points to the face on the menu or names it. "
        "Caregiver mirrors: 'Yes, that part was really exciting.' "
        "No correction, no minimising. "
        "Step 3 — PRACTISE THE PAUSE. Agree on a physical gesture for "
        "'pause' — hands up like stop signs, or a slow breath together. "
        "When the screen produces a big feeling, the caregiver does the "
        "gesture first. Child mirrors. Then together: 'We felt [feeling]. "
        "What do we want to do next?' Options might be: keep watching, "
        "take a break, have a hug, talk about it. Child chooses. "
        "Step 4 — DEBRIEF AFTER SCREEN TIME. One question: 'Did you "
        "notice any feelings today?' Not an interrogation — a casual "
        "curiosity. Over weeks, the child starts naming feelings during "
        "screen time without the prompt. That is the skill taking root."
    ),
    gamification_element=(
        "The 'Feelings Collector' sticker chart. For children 4-6, "
        "sticker charts work best when the sticker is for the ATTEMPT "
        "not the perfect execution. One sticker for: 'I noticed a "
        "big feeling today and named it.' The caregiver awards the "
        "sticker — the standard is only that the child tried to name "
        "something. Over 4-6 weeks, the chart fills. The child can "
        "see the pattern: 'I notice my feelings a lot now.' This is "
        "metacognitive development at 4-6 — noticing one's own "
        "inner states — and it is genuinely remarkable at this age. "
        "Do NOT make the sticker contingent on having the 'right' "
        "reaction. The skill is noticing and naming, not suppressing."
    ),
    screen_time_guidance=(
        "This skill is most effective as a practice embedded IN screen "
        "time, not as a replacement for it. Recommended: 2-3 caregiver-"
        "accompanied pauses per 30-minute session during the first few "
        "weeks while the habit is forming. After 4-6 weeks, spot-check "
        "once per session. The skill complements AAP screen time "
        "guidelines (ages 2-5: 1 hour/day of high-quality programming "
        "with co-viewing whenever possible) by making co-viewing more "
        "emotionally educational rather than purely supervisory."
    ),
    parental_controls_component=(
        "The primary parental control here is CO-VIEWING — watching "
        "with the child, especially during the first weeks of the "
        "practice. Technical controls recommended in parallel: "
        "(a) disable autoplay on all platforms the child uses (YouTube "
        "Kids, Netflix) — the autoplay design specifically removes the "
        "pause point between content pieces; "
        "(b) use platform age-filters rigorously (YouTube Kids, "
        "Disney+, CBC Gem Kids) to reduce the likelihood of fear-"
        "inducing or anger-inducing content reaching this age group; "
        "(c) schedule screen time at predictable, bounded times rather "
        "than on-demand — the predictable ending reduces the meltdown "
        "risk at screen-off time. The skills approach and the technical "
        "controls are complementary: controls reduce the severity of "
        "what the child encounters; skills build the capacity to handle "
        "what gets through."
    ),
    media_quality_rubric=(
        "GOOD: caregiver co-views during the skill-building period; "
        "feelings are named without judgment or minimising ('that part "
        "was scary — it is okay to feel scared'); the pause gesture is "
        "applied by the caregiver FIRST as a model, not imposed on the "
        "child; the child's choice of next action (keep watching, take "
        "break, etc.) is genuinely respected; skill practice is low-"
        "pressure and brief. AVOID: minimising feelings ('it's just a "
        "cartoon, don't be scared'); requiring the 'right' feeling; "
        "using the technique as a screen-off tool (the child learns to "
        "suppress rather than regulate); applying the technique "
        "inconsistently (once a month won't build the habit). "
        "The standard: the child names a feeling unprompted during "
        "screen time. That is the skill."
    ),
    en_ca_content=(
        "**Feelings are real, even about cartoons.** When your child "
        "sees something exciting, scary, or frustrating on a screen, "
        "their body reacts as if it is really happening. That is not "
        "being babyish — it is how brains work at every age, including "
        "yours. The skill we are building together is noticing that "
        "feeling, naming it, and then choosing what to do next.\n\n"
        "**Why this matters.** Screens — especially apps and websites "
        "designed for children — are built to produce big feelings. "
        "Exciting games, funny videos, cliffhanger endings. That is "
        "not an accident. The people who design these apps know that "
        "excited children watch longer. Teaching your child to notice "
        "the feeling is the first step in staying in the driver's seat.\n\n"
        "**The feelings menu.** Draw three faces together: one happy/"
        "excited, one sad/scared, one mad/frustrated. Put it somewhere "
        "near the screen. During screen time, point to the menu "
        "occasionally: 'Which one are you feeling right now?' No right "
        "answer. Just practice noticing.\n\n"
        "**The pause.** Agree on a signal together — hands up like "
        "stop signs, or one slow breath. When something on screen "
        "causes a big feeling, you do the signal first. Your child "
        "mirrors you. Then: 'We felt [feeling]. What do we want to "
        "do next?' Options: keep watching, take a snack break, have "
        "a hug, turn it off for now. Your child picks.\n\n"
        "**The key word: choose.** At ages 4-6, children are developing "
        "their sense of their own power. 'You get to choose what you "
        "do next' is not permissiveness — it is the exact framing that "
        "builds agency. A child who practices choosing at 5 is better "
        "equipped to choose at 13, when the stakes are higher and you "
        "are not in the room."
    ),
    ar_description=(
        "AR applications for 4-6 emotional safety: feelings-menu "
        "AR overlay (animated faces that the child can point a tablet "
        "at and see 'come alive') could reinforce the menu concept. "
        "Technically feasible with DCC stack if AR showcase priority "
        "is assigned. Cup-Animation showcase could display an animated "
        "feelings menu on a physical cup the child uses during screen "
        "time — novel association that may help with recall. Flag for "
        "Phase 2 AR sprint if the wizard POC is approved."
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
