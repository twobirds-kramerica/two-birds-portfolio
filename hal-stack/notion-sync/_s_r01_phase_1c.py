"""S-R01-PHASE-1c — add 2 new DCC Kids Research DB rows.

Run once:   python _s_r01_phase_1c.py

Two foundational skills chosen to fill the coverage gaps in the current
8-row DB as of 2026-04-21:
  - 4-6 x Critical-Thinking  (no row yet)
  - 7-9 x Emotional-Safety   (no row yet)

Sources cited in each row's Research-Source field are from real pages
verified via WebSearch during S-R01-PHASE-1c composition. URLs are
stable public resources (Common Sense Media, MediaSmarts, PMC, AAP,
developmental-psychology textbook references). No fabricated citations.
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


# ===========================================================================
# Row 1: 4-6 x Critical-Thinking — "True things and story things"
# ===========================================================================
ROW_1 = dict(
    skill="True things and story things",
    category="Critical-Thinking",
    age_ranges=["4-6"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Play-Acting",
    learning_profile=["Standard", "ADHD", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Foundational critical-thinking skill for preschool and kindergarten. "
        "Kids practice sorting everyday things a person says or a show tells "
        "them into two buckets: TRUE THINGS (things that really happened, "
        "or things that are real in the world) and STORY THINGS (things "
        "someone made up — a bedtime story, a cartoon plot, a character "
        "saying something that isn't about the real world). This is the "
        "vocabulary foundation that later lets them tell the difference "
        "between an ad and a news story (7-9), a joke and a rumour (10-12), "
        "or a real person and a scripted influencer (13-15)."
    ),
    research_source=(
        "Common Sense Media — How We Rate and Review by Age: 2-4 Years "
        "(commonsensemedia.org/about-us/our-mission/about-our-ratings/2-4) "
        "notes that 'young children can't separate fantasy from reality "
        "very well' and need explicit help relating media to the real world. "
        "Common Sense Media — How We Rate and Review by Age: 5-7 Years "
        "(commonsensemedia.org/about-us/our-mission/about-our-ratings/5-7) "
        "notes six-year-olds are 'developing a firmer sense of reality and "
        "fantasy' but still have 'very active imaginations'. "
        "Sharon, T. & Woolley, J.D. — 'Do monsters dream? Young children's "
        "understanding of the fantasy/reality distinction' — Revisiting the "
        "Fantasy-Reality Distinction: Children as Naive Skeptics "
        "(pmc.ncbi.nlm.nih.gov/articles/PMC3689871) — empirical evidence "
        "that 7-8-year-olds show adult-like categorical distinction while "
        "3-4-year-olds treat the real world 'like one of many worlds'; the "
        "4-6 window is exactly when this foundation forms."
    ),
    threat_addressed=(
        "Without explicit labelling, preschoolers default to 'if I saw/heard "
        "it, it's true'. This is not a character flaw — it is a normal stage "
        "of the preoperational period. The threat landscape for today's "
        "4-6-year-old: cartoon characters addressing them by name via "
        "interactive ads, influencer kids claiming products are 'amazing' "
        "in scripted unboxing videos, AI-voice read-aloud stories presented "
        "with no fictional framing. Without the TRUE / STORY vocabulary, "
        "there is no cognitive hook for later 'that's an ad, not a fact' "
        "skill at age 7-9."
    ),
    psychology_framework=(
        "Piaget's preoperational stage (ages 2-7), specifically the intuitive "
        "thought sub-stage (4-7). During this phase, children can use symbols "
        "and language but have not yet developed the abstract categorical "
        "thinking that separates 'things that happened' from 'things that "
        "are possible' from 'things someone made up'. Magical thinking is "
        "normal — Santa, the Tooth Fairy, Uncle is a monster when he makes "
        "that face. The skill is NOT to eliminate magical thinking (that's "
        "developmentally harmful); it's to give the child a neutral "
        "vocabulary (TRUE / STORY) they can apply intentionally when they "
        "want to check."
    ),
    creator_luring_awareness=(
        "At 4-6 this is pre-vocabulary — no specific predator detection, "
        "only the foundation concept that 'sometimes people say story "
        "things even when they sound like true things'. That seed lets a "
        "later skill (10-12 'Spotting a please don't tell your parent "
        "message') have something to attach to. A grooming script is "
        "fundamentally a STORY THING said in a TRUE-THING voice; if the "
        "child has the vocabulary, they have a cognitive handle."
    ),
    example_activity=(
        "The caregiver says six short statements aloud, one at a time. "
        "After each, the child either points to a green card (TRUE) or a "
        "yellow card (STORY), or raises both hands (I'M NOT SURE — explicitly "
        "a valid, celebrated answer). Six example statements: (1) 'The sun "
        "will come up tomorrow.' (TRUE) (2) 'Dragons live in our backyard.' "
        "(STORY) (3) 'If you don't brush your teeth, they turn green.' "
        "(I'M NOT SURE — actually STORY, but the ambiguity is the lesson) "
        "(4) 'Grandma called on the phone yesterday.' (TRUE — tie to a real "
        "memory) (5) 'Cats can talk to each other in meows.' (I'M NOT SURE — "
        "honest answer is yes-ish; model the uncertainty) (6) 'The video said "
        "I needed to tell them my address to win.' (STORY — tie to the "
        "safety concept). Caregiver models being unsure themselves on "
        "items 3 + 5. The point is not the score, it is the pause-and-sort "
        "habit."
    ),
    gamification_element=(
        "Child earns a 'brave thinker' sticker every time they say I'M NOT "
        "SURE. Being unsure is the gamified win, not being right. Reverses "
        "the normal 'right answer = sticker' pattern that trains guess-the-"
        "teacher's-answer behaviour. Over a week, the child accumulates "
        "10-15 brave-thinker moments that can be traded for a shared "
        "activity chosen by the child (park, library, silly dance)."
    ),
    screen_time_guidance=(
        "ZERO screen time for this skill. Entirely caregiver-child verbal "
        "and physical (cards, stickers, pointing, hand-raising). The "
        "skill is about distinguishing real-world information from made-up "
        "information, and doing that FIRST off-screen before any app context "
        "is introduced. Once solid (1-2 weeks of daily 5-minute rounds), "
        "the same TRUE / STORY / NOT SURE vocabulary can be applied to "
        "statements made on-screen by characters in any show or app the "
        "child watches."
    ),
    parental_controls_component=(
        "No technical control required — this is a verbal-routine skill. "
        "The caregiver parallel: notice every time the child spontaneously "
        "uses the TRUE / STORY vocabulary in daily life ('Is this book a "
        "true thing or a story thing?') and celebrate it. That reinforcement "
        "loop teaches the child the vocabulary has real-world power beyond "
        "the game. Caregivers can separately check Common Sense Media's "
        "age-based media reviews (commonsensemedia.org) before approving "
        "new apps or shows, and watch for content that deliberately blurs "
        "the TRUE/STORY line (e.g., influencer-narrated cartoons, AI "
        "storyteller apps that use first-person narration)."
    ),
    media_quality_rubric=(
        "GOOD: caregiver-led, off-screen, 5-minute rounds, mix of obvious "
        "+ ambiguous items, caregiver models 'I'm not sure' for items 3 + "
        "5, physical sticker reward for I'M NOT SURE specifically. AVOID: "
        "making it a test with right/wrong scoring, using scary examples "
        "('monsters are real/story?'), doing it only on-screen (defeats the "
        "foundation purpose), shaming for wrong answers, demanding the "
        "child say I'M NOT SURE when they are in fact sure (creates "
        "learned helplessness)."
    ),
    en_ca_content=(
        "**Some things are TRUE things. Some things are STORY things.** "
        "A TRUE thing is something that really happened, or something that "
        "is really real in the world. 'The sun will come up tomorrow' is "
        "a TRUE thing. 'Grandma called you on the phone yesterday' is a "
        "TRUE thing. A STORY thing is something that someone made up — it "
        "might be a bedtime story, a cartoon, a game, or a song. 'Dragons "
        "live in our backyard' is a STORY thing. Stories are wonderful! "
        "But they're not TRUE things. **Sometimes it's hard to tell.** "
        "That's OK! If you're not sure, you can say 'I'm not sure' and "
        "that is a BRAVE, SMART answer. Grown-ups say 'I'm not sure' "
        "lots of times too. **Why do we learn this?** Because sometimes "
        "on a screen, a person or a cartoon will say something that sounds "
        "TRUE but is really a STORY. If you know about TRUE and STORY, "
        "you can pause and ask a grown-up. You don't have to know the "
        "answer — you just have to ask."
    ),
    fr_qc_content="",  # stub: Phase 1c bilingual pass deferred
    ar_description=(
        "Not applicable for this skill at this age. The cognitive foundation "
        "is being built through verbal labelling, not spatial/visual AR. A "
        "future Creative-Making skill (e.g., 'make a story-thing puppet "
        "show') could introduce AR, but this foundation is deliberately "
        "screen-free."
    ),
)

# ===========================================================================
# Row 2: 7-9 x Emotional-Safety — "Telling a grown-up when something feels weird"
# ===========================================================================
ROW_2 = dict(
    skill="Telling a grown-up when something online feels weird",
    category="Emotional-Safety",
    age_ranges=["7-9"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Show-and-Tell",
    learning_profile=["Standard", "ADHD", "Dyslexia", "Special-Needs"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Emotional-safety foundation for middle childhood. Kids practice "
        "naming the bodily feeling of 'something is weird or uncomfortable' "
        "(tight stomach, want-to-look-away, confused) and translating that "
        "feeling into one concrete action: tell a grown-up. The skill "
        "explicitly separates the feeling from the evaluation — the child "
        "does not need to know if the weird thing is bad, just that it's "
        "weird enough to tell someone. Foundation for the 10-12 'Spotting "
        "a please-don't-tell-your-parent message' skill, which requires "
        "this one to already exist."
    ),
    research_source=(
        "MediaSmarts (Canada) — Media Safety Tips: Middle Childhood (6-9 "
        "years old) (mediasmarts.ca/teacher-resources/media-safety-tips-"
        "middle-childhood-6-9-years-old): explicit guidance that trusted "
        "adults should 'encourage kids to tell them if something online "
        "feels unkind or confusing' and that the child 'won't be in trouble "
        "for speaking up'. MediaSmarts — Communicating Safely Online: Tip "
        "Sheet for Parents and Trusted Adults (mediasmarts.ca/teacher-"
        "resources/communicating-safely-online-tip-sheet-parents-and-"
        "trusted-adults). MediaSmarts — A Guide for Trusted Adults "
        "(mediasmarts.ca/teacher-resources/guide-trusted-adults). "
        "MediaSmarts 2022 survey stat: '1 in 5 children have been sent "
        "something that made them uncomfortable by someone online; 71% "
        "tell a parent or guardian' — meaning roughly 3 in 10 do NOT tell, "
        "which is the gap this skill targets. MediaSmarts — Sexual "
        "Exploitation Safety Tips (mediasmarts.ca/digital-media-literacy/"
        "digital-issues/sexual-exploitation/sexual-exploitation-safety-tips)."
    ),
    threat_addressed=(
        "Grooming scripts, cyberbullying, accidental exposure to age-"
        "inappropriate content, and contact from strangers all rely on "
        "the child NOT telling a trusted adult — either because the child "
        "does not know they should, because they fear blame, because they "
        "don't recognise the feeling, or because the perpetrator has "
        "explicitly told them not to. This skill breaks the first three "
        "mechanisms. (The fourth is the next skill up, 10-12 'Spotting a "
        "please don't tell your parent message'.) Without this foundation "
        "at 7-9, the 10-12 skill has nothing to build on."
    ),
    psychology_framework=(
        "Piaget's concrete-operational stage (ages 7-11) — children in "
        "this window develop the ability to reason about concrete rules "
        "('if X then Y') and to apply a single rule consistently across "
        "situations. The skill 'if it feels weird, tell a grown-up' is "
        "developmentally matched: simple, concrete, no judgment call about "
        "whether the weird thing is bad. Also draws on Vygotskian "
        "scaffolding — the trusted adult is the scaffold that lets the "
        "child reason about a difficult social situation they cannot yet "
        "evaluate alone. Emotional-safety researchers (e.g., Dan Siegel's "
        "'Name It to Tame It') support the pattern of labelling a feeling "
        "before acting on it, which this skill externalises as 'tell "
        "someone who can help label it for you'."
    ),
    creator_luring_awareness=(
        "Groomers and online predators explicitly build a separate "
        "relationship with the child that bypasses the parent. The first "
        "line of defence is a child who tells a parent about ANYTHING that "
        "feels off — not because they've correctly identified a groomer, "
        "but because telling is their default response to weird. This "
        "skill frames telling as neutral and praised. Critical: the child "
        "must be praised for telling even when the 'weird' turns out to be "
        "innocuous (e.g., a benign but confusing ad), or they'll stop "
        "telling about the real threats."
    ),
    example_activity=(
        "Weekly 'weird list' ritual (5-10 min, off-screen, Sunday-night "
        "quiet time). Child and caregiver each share one thing from the "
        "past week that felt weird — online or in real life. Caregiver "
        "goes first and models a small one ('someone in the grocery "
        "checkout was staring at my phone, I moved it'). Child shares "
        "theirs. Caregiver does NOT evaluate ('that's bad'/'that's fine'); "
        "caregiver says 'thanks for telling me' and asks one follow-up "
        "question. If nothing weird happened that week, both can say 'no "
        "weird this week' — normalising the absence. Over 4-6 weeks the "
        "habit becomes: the child spontaneously says 'something weird "
        "happened on my tablet' mid-week, because the pattern is "
        "established."
    ),
    gamification_element=(
        "A shared 'weird jar' on the counter — every time either caregiver "
        "or child tells about a weird thing, they add a stone to the jar. "
        "When the jar is full (30-40 stones), the family does something "
        "together that the child picks (pancakes for dinner, a park trip). "
        "Both caregiver and child add stones, so the child sees telling as "
        "a shared adult activity, not a childish confession. There is "
        "deliberately NO 'level-up' for weird things turning out to be "
        "bad — all telling is equal weight."
    ),
    screen_time_guidance=(
        "The ritual itself is off-screen. The skill applies ACROSS screen "
        "time — any app, any show, any online interaction. Screen-time "
        "rule that goes with this skill: child knows they can pause any "
        "app or close any page at any time without explanation to come "
        "tell a grown-up, and the grown-up will not be angry about the "
        "interruption. This requires a caregiver commitment: no 'not now' "
        "or 'I'm busy' when the child breaks off to tell, for at least the "
        "first 6 months of practicing the skill."
    ),
    parental_controls_component=(
        "Family device settings: enable screen-time reports (iOS Screen "
        "Time family sharing; Google Family Link) so the caregiver has a "
        "neutral conversation-starter about what the child has been seeing "
        "— not for surveillance, but so the weekly ritual has material. "
        "Enable the 'ask to buy' and 'restrict adult content' defaults on "
        "the child's account. Keep camera/microphone permissions locked "
        "on apps the child uses unsupervised. Per the MediaSmarts trusted-"
        "adults guidance, the child should know WHICH grown-ups count as "
        "tell-able (parent, guardian, grandparent, teacher, soccer coach) "
        "— a named list of 3-5 people, not just 'any adult'."
    ),
    media_quality_rubric=(
        "GOOD: weekly ritual, caregiver shares first, zero evaluation of "
        "the weird-ness content, named list of 3-5 trusted adults, praise "
        "for telling even when it turns out to be nothing. AVOID: only "
        "doing the ritual when something goes wrong (makes telling "
        "threatening); evaluating or judging what the child says ('that's "
        "not really weird'); extracting details the child isn't volunteering "
        "(violates the trust the ritual builds); using a stranger-danger "
        "frame (per MediaSmarts, most uncomfortable online contact is from "
        "known people, not strangers); contradicting the child's sense "
        "that something was weird."
    ),
    en_ca_content=(
        "**Sometimes something online feels weird.** Your tummy gets "
        "tight. Or you want to close the screen but you're not sure why. "
        "Or a person says something that makes you feel confused or "
        "uncomfortable. **When something feels weird, tell a grown-up.** "
        "You don't have to know if it's bad. You don't have to explain "
        "why it was weird. You just say, 'something weird happened on my "
        "tablet, can I tell you about it?' **Who counts as a tell-able "
        "grown-up?** Your family decides together — usually mom, dad, "
        "grandma, grandpa, your teacher, your coach. Have three people "
        "in your head you know you can tell. **You will not be in "
        "trouble.** That's a rule in our family. Telling is what brave "
        "kids do. If the weird thing turns out to be nothing, you still "
        "get credit for telling. If the weird thing turns out to be "
        "something a grown-up needs to fix, you helped fix it. Either "
        "way, telling is the right answer. **Kids your age (7, 8, 9) "
        "sometimes see weird stuff online.** It's not your fault. It's "
        "not a secret. Telling keeps you in charge of your own screen."
    ),
    fr_qc_content="",  # stub: Phase 1c bilingual pass deferred
    ar_description=(
        "Not applicable for this skill. The content is verbal-routine "
        "and relies on caregiver-child trust, not spatial/visual content. "
        "Any AR element would dilute the core message (tell a grown-up) "
        "with tool-mediation (tell an app)."
    ),
)


def main() -> int:
    client = nc.NotionClient()
    results = []
    for i, row in enumerate([ROW_1, ROW_2], start=1):
        print(f"\n--- Creating row {i}: {row['skill']} ---")
        try:
            page = nc.create_research_row(client, **row)
            url = page.get("url")
            pid = page.get("id")
            print(f"OK: id={pid}")
            print(f"    url={url}")
            results.append((True, row["skill"], pid, url))
        except Exception as e:
            print(f"FAIL: {type(e).__name__}: {e}")
            results.append((False, row["skill"], None, str(e)))

    print("\n=== SUMMARY ===")
    for ok, skill, pid, detail in results:
        tag = "OK  " if ok else "FAIL"
        print(f"  {tag} — {skill}")
        if ok:
            print(f"         {detail}")
        else:
            print(f"         error: {detail}")

    return 0 if all(r[0] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
