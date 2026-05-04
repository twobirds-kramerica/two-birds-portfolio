"""S-R01-STRETCH-1s — 7-9 Learning: Remembering what I learned instead
of just watching it go by.

2nd row in the 7-9 × Learning cell. The existing coverage row addresses
learning generally. This row targets the retention gap specific to
screen-based content consumption: children aged 7-9 are heavy consumers
of educational video (YouTube Kids, Khan Academy Kids, school platforms)
but the passive-viewing mode produces very little durable learning.
Delivers four concrete retention moves adapted for this age group:
predict-before-watch, pause-and-say-it-back, draw-what-you-learned,
teach-it-at-dinner.

Run once:   python _s_r01_stretch_1s.py
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
    skill="Watching to learn vs. watching to pass time — four moves that make it stick",
    category="Learning",
    age_ranges=["7-9"],
    priority="P1-Important",
    status="Research",
    demonstration_method="Multi-Modal",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Educational screen content (Khan Academy Kids, YouTube educational "
        "channels, school learning platforms) is pervasive for the 7-9 age "
        "group, but the passive-viewing mode that works for entertainment "
        "produces very little durable learning. The child watches, feels "
        "like they understood, and retains 10-20% three days later. "
        "This row delivers four age-appropriate retention moves that "
        "convert passive watching into active learning: "
        "(1) PREDICT — before the video, the child states one thing they "
        "think they will learn ('I predict it will be about...'); "
        "(2) PAUSE-AND-SAY — at the caregiver's pause prompt, the child "
        "says one thing they just learned in their own words; "
        "(3) DRAW — after the video, the child draws or writes one thing "
        "they remember (no wrong answers — the act of producing a "
        "representation is the learning event); "
        "(4) TEACH-AT-DINNER — that evening, the child tells one family "
        "member one thing they learned. Four moves, applicable to any "
        "educational video, buildable as a household habit."
    ),
    research_source=(
        "Roediger, H.L. & Karpicke, J.D. (2006) 'Test-enhanced learning: "
        "taking memory tests improves long-term retention' (Psychological "
        "Science 17(3)): the retrieval-practice effect — actively recalling "
        "information produces 1.5-2x better retention than re-reading or "
        "re-watching. The pause-and-say and draw moves are retrieval "
        "practice adapted for the 7-9 age group. "
        "Chi, M.T.H. et al. (1989) 'Self-explanations: how students study "
        "and use examples in learning to solve problems' (Cognitive Science "
        "13(2)): the self-explanation effect — students who explain material "
        "to themselves during learning understand it significantly more "
        "deeply than those who read passively. 'Pause-and-say' is the "
        "child-accessible version. "
        "Fiorella, L. & Mayer, R.E. (2015) 'Learning as a Generative "
        "Activity' (Cambridge University Press): comprehensive review of "
        "eight generative learning strategies. Drawing/mapping and teaching "
        "others are consistently the two highest-yield strategies across "
        "age groups and content types. "
        "Richland, L. et al. (2009) 'The pretesting effect: do unsuccessful "
        "retrieval attempts enhance learning?' (Journal of Experimental "
        "Psychology: Applied 15(3)): the prediction/pre-test effect — "
        "attempting to answer a question before learning improves subsequent "
        "retention of the answer even when the initial attempt is wrong. "
        "The 'I predict' move exploits this effect. "
        "National Reading Panel (2000) and subsequent replication: oral "
        "retelling (telling someone else what you learned) is one of the "
        "most reliable retention strategies for the 6-10 age group, "
        "particularly for children who are still developing fluent reading. "
        "The teach-at-dinner move is oral retelling in a naturalistic context."
    ),
    threat_addressed=(
        "The primary threat is not dangerous content but wasted "
        "educational opportunity. Children aged 7-9 in Canada spend "
        "significant time on ostensibly educational screen content (CBC "
        "Kids, TVO Kids, Khan Academy Kids, YouTube educational channels, "
        "school-assigned platforms). Without active-learning moves, this "
        "time produces shallow processing and minimal retention. The "
        "secondary threat is the 'illusion of learning' — the child "
        "feels like they know something because they watched a clear "
        "explanation of it, but cannot recall or apply it the following "
        "day. The same illusion compounds: by grade 4-5, a child who has "
        "done only passive educational screen watching has a significant "
        "retention gap compared to one who has practiced active retrieval. "
        "This connects to the 13-15 Learning row (1l) which addresses the "
        "same dynamic at the teen level with AI tools."
    ),
    psychology_framework=(
        "Piaget's concrete-operational stage (7-12): children this age "
        "can consolidate learning through action — drawing, saying, "
        "building. Abstract reflection is still developing; the four "
        "moves give concrete, physical anchors for what would otherwise "
        "require abstract metacognition. "
        "Vygotsky's ZPD: the caregiver scaffolds the active-learning "
        "moves initially (pressing pause, asking 'what did you just "
        "learn?') until the child internalises the routine. "
        "Information-processing theory (Miller, Atkinson-Shiffrin): "
        "working memory is limited (7±2 chunks for adults; less for "
        "children). Predict-pause-draw-teach moves information from "
        "working memory to long-term memory by creating retrieval routes. "
        "Dual coding theory (Paivio 1971): the draw move combines verbal "
        "and visual representations, creating two retrieval pathways "
        "rather than one. Particularly beneficial for children with "
        "dyslexia or reading challenges."
    ),
    creator_luring_awareness=(
        "Indirect. Children who develop active-learning habits are "
        "practicing metacognition — the habit of asking 'what did I "
        "actually learn from this?' applies beyond educational content "
        "to any persuasive content. A child who pauses an educational "
        "video and says what they learned is developing the same pause "
        "that, at 13, becomes 'what is this video actually trying to "
        "make me believe?' The predict-before-watch move also develops "
        "the habit of approaching content with a prior hypothesis — "
        "which is a weak-form inoculation against content that is "
        "designed to confirm rather than challenge."
    ),
    example_activity=(
        "THE FOUR-MOVE LEARNING SESSION (add 5-10 min to any "
        "educational video session; practice 3x/week for 4 weeks). "
        "BEFORE: 'What do you think this video will teach you?' "
        "Child gives one prediction — doesn't matter if wrong. "
        "Write it on a sticky note or say it aloud. "
        "DURING: At 1-2 natural pause points (caregiver presses pause): "
        "'What did you just learn? Tell me in your own words.' "
        "Child says one thing. No correction needed — the act of "
        "retrieval is the event. Caregiver mirrors: 'So what you heard "
        "was...' and paraphrases back. "
        "AFTER: 'Draw one thing you learned.' "
        "Paper and marker, 5 minutes. No wrong drawings. "
        "The child can draw a diagram, a word with a picture, a comic "
        "strip panel — anything. Stick it to the fridge. "
        "AT DINNER: 'Tell Dad / Grandma / your sister one thing you "
        "learned today.' Child picks one thing. "
        "Caregiver can prompt: 'Do you remember that prediction you "
        "made? Were you right?' "
        "WEEKLY: look at the week's drawings together. 'Can you still "
        "remember what each one is about?' Drawings that the child "
        "can still explain after a week go in a 'things I know' folder. "
        "This is retrieval practice at one week — the interval that "
        "begins to convert short-term to long-term memory."
    ),
    gamification_element=(
        "The 'what I know' folder. A physical folder (or a designated "
        "drawer) where the child's weekly drawings go. Each drawing "
        "is dated. Once a month, pull out all the drawings and have "
        "the child explain each one. Drawings they can still explain: "
        "move to the 'I know this' section. Drawings they can't: "
        "go back in the 'still learning' section and get a quick "
        "re-watch. Over a school year, the 'I know this' section "
        "fills up. The child can see, physically, what they have "
        "learned. This is a tangible portfolio of retained knowledge "
        "that a grade 2-4 student can be proud of."
    ),
    screen_time_guidance=(
        "The four moves add 5-10 minutes to any educational video "
        "session. The caregiver-pause interaction is the most "
        "time-intensive element. Recommend building the habit with "
        "one short educational video per day (10-15 min) rather "
        "than retrofitting it onto long viewing sessions. Over 4-6 "
        "weeks, the child begins applying the predict-and-say moves "
        "spontaneously. Net screen time: neutral — the sessions are "
        "shorter in duration once the child is actively engaged "
        "rather than passively watching."
    ),
    parental_controls_component=(
        "No technical control needed. Complementary settings: "
        "(a) Disable autoplay on educational platforms (YouTube Kids, "
        "Khan Academy) — autoplay undermines the natural pause points "
        "the four moves require. "
        "(b) CBC Kids (cbc.ca/kidsnews, cbckids.ca) and TVO Kids "
        "(tvokids.com) provide Canadian curriculum-aligned content "
        "that pairs well with this framework. "
        "(c) Keep a supply of paper and markers near the screen area — "
        "removing the friction of 'where is the paper?' increases "
        "the draw-move completion rate substantially."
    ),
    media_quality_rubric=(
        "GOOD: child makes a prediction before the video; caregiver "
        "pauses at 1-2 points for a say-back; child draws one thing "
        "after; child reports one thing at dinner; drawings are filed "
        "and reviewed monthly. "
        "AVOID: requiring all four moves every session before the "
        "habit is established (burnout — start with one move for two "
        "weeks, then layer in the next); correcting the child's "
        "drawing or paraphrase (the production is the learning event, "
        "accuracy comes later); making the teach-at-dinner move a "
        "performance rather than a conversation. "
        "The standard: the child unprompted says 'I learned that...' "
        "at dinner about something they watched. That sentence, "
        "spontaneous, is the skill."
    ),
    en_ca_content=(
        "**Watching a video is not the same as learning from it.** "
        "Most people — adults and kids — watch an educational video, "
        "think 'that made sense,' and remember about 20% of it three "
        "days later. The good news: four small moves can change that "
        "completely.\n\n"
        "**Move 1 — Predict.** Before the video starts, ask: 'What "
        "do you think this is going to teach you?' One sentence. "
        "Even a wrong prediction. The act of guessing first makes "
        "the brain pay attention to whether the guess was right.\n\n"
        "**Move 2 — Pause and say.** Once or twice during the video, "
        "press pause and ask: 'What did you just learn? Tell me in "
        "your own words.' Not a quiz — a conversation. The child "
        "can get it partly wrong. The act of putting it into their "
        "own words is where the learning locks in.\n\n"
        "**Move 3 — Draw it.** After the video: paper and marker, "
        "five minutes, draw one thing you learned. It does not have "
        "to be a good drawing. A diagram, a word, a symbol — anything "
        "that represents what they took away. Put it on the fridge.\n\n"
        "**Move 4 — Teach it.** At dinner, or in the car, or at "
        "bedtime: 'Tell someone one thing you learned today.' "
        "One thing. The act of explaining it to another person is "
        "the highest-yield learning move there is. Research shows "
        "it produces deeper understanding than re-watching the video "
        "three times.\n\n"
        "**Why these four?** Each one is a form of retrieval practice "
        "— actively pulling information out of memory rather than "
        "passively receiving it. Retrieval practice is one of the "
        "most replicated findings in learning science (Roediger & "
        "Karpicke, 2006). It works on everything: math, science, "
        "history, French. And at ages 7-9, it builds the learning "
        "habit that compounds for the rest of school."
    ),
    ar_description=(
        "AR opportunity: an animated 'knowledge capture' overlay "
        "that pops up when the child holds their drawing up to the "
        "tablet camera — the drawing 'comes alive' with a related "
        "animation, reinforcing the connection between the drawing "
        "and the concept. Feasible as a Show-and-Tell application. "
        "Flag for Phase 2 AR sprint."
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
