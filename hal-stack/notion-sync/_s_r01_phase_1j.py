"""S-R01-PHASE-1j — 10-12 Emotional-Safety: stepping out of a pile-on.

2nd row in 10-12 x Emotional-Safety. Pairs as a peer-peer threat
counterpart to the existing grooming row 'Spotting a please don't
tell your parent message'. Addresses the higher-frequency peer-
cruelty / group-chat pile-on threat using agency-based framing
(step out, don't amplify) rather than the preachy 'be an upstander'
default kids this age explicitly reject.

Run once:   python _s_r01_phase_1j.py
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
    skill="Stepping out of a group pile-on (without becoming the next target)",
    category="Emotional-Safety",
    age_ranges=["10-12"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Play-Acting",
    learning_profile=["Standard", "ADHD", "Dyslexia", "Special-Needs"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Pre-teen skill for the most frequent negative social "
        "experience at 10-12: the group-chat or social-feed pile-on "
        "where the friend group turns on one member, or an "
        "outsider, and the child has to decide in seconds whether "
        "to join in, forward the content, stay silent, or exit. "
        "The framing is deliberately modest: NOT 'rescue the "
        "target' (too grandiose for the peer-dynamics reality) "
        "and NOT generic 'be an upstander' (the preachy phrasing "
        "kids this age reject). Instead: three concrete agency-"
        "preserving moves — don't forward, private DM to the "
        "target, change the subject. Pairs with the existing "
        "10-12 Emotional-Safety row ('Spotting a please don't "
        "tell your parent message') by covering the peer-peer "
        "threat alongside the adult-child grooming threat."
    ),
    research_source=(
        "PREVNet — Canadian national research/knowledge mobilisation "
        "hub on bullying (prevnet.ca/bullying/cyberbullying). "
        "Public Safety Canada — 'Overview of Approaches to Address "
        "Bullying and Cyberbullying' "
        "(publicsafety.gc.ca/cnt/rsrcs/pblctns/2018-ddrss-bllyng-"
        "cybrbllyng/index-en.aspx) and 'STOPit: Summary Report' "
        "(publicsafety.gc.ca/cnt/rsrcs/pblctns/2017-r017/"
        "index-en.aspx). "
        "Olweus, D. (1993 + later) — original bullying-research "
        "framework defining bullying as 'repeated negative actions' "
        "and identifying bystander/reinforcer/defender/victim roles "
        "in group dynamics. "
        "Salmivalli et al. (Finnish empirical tradition) - "
        "'Bullying as a Social Process: The Role of Group "
        "Membership' (Academia.edu / Salmivalli 1996 and after): "
        "classrooms with more *defenders* show lower bullying "
        "rates; classrooms with more *reinforcers* show higher. "
        "Defenders specifically differ from bullies on empathy, "
        "responsibility, defending self-efficacy, and moral "
        "disengagement. "
        "Meter & Card empirical work on bystander effectiveness - "
        "peer intervention stops bullying within roughly 10 "
        "seconds in a majority of cases (widely cited in PREVNet "
        "summaries and Common Sense Education). "
        "PMC9015685 - 'School Climate and Bullying Bystander "
        "Responses in Middle and High School'. "
        "Journal of Youth and Adolescence 2025 - 'Trajectories "
        "of Bystander Behaviors in Bullying during Secondary "
        "Education: the Role of Moral Disengagement and "
        "Conformity To Peer Pressure' (link.springer.com/"
        "article/10.1007/s10964-025-02276-8). "
        "Common Sense Education - Upstanders and Allies: Taking "
        "Action Against Cyberbullying "
        "(commonsense.org/education/digital-citizenship/lesson/"
        "upstanders-and-allies-taking-action-against-"
        "cyberbullying). "
        "Cyberbullying Research Center (cyberbullying.org)."
    ),
    threat_addressed=(
        "The dominant peer-peer threat at 10-12. PREVNet + "
        "Public Safety Canada data consistently show cyberbullying "
        "peaks in prevalence between ages 10 and 13, driven by "
        "three factors: (1) Kohlberg's conventional-morality "
        "stage peaks conformity to peer norms; (2) group-chat "
        "platforms (Discord, Snapchat group chats, iMessage "
        "groups) amplify pile-on dynamics — a comment that would "
        "die at a lunch table instead reaches 30 kids and gets "
        "forwarded; (3) the defender role is the single highest-"
        "leverage intervention — in most bullying incidents, one "
        "peer speaking up stops the incident within seconds. "
        "Left unaddressed, children who stay silent during "
        "repeated pile-ons internalise passive reinforcement "
        "norms that carry into adult workplace dynamics. "
        "Addressed proactively with this skill, children "
        "develop what Salmivalli calls 'defending self-efficacy' - "
        "a learnable trait."
    ),
    psychology_framework=(
        "Kohlberg's conventional-morality stage (approx 10-13): "
        "the child's dominant moral motivation is 'what the group "
        "accepts is what is right'. This is EXACTLY the cognitive "
        "moment when pile-ons feel most compelling to join in on "
        "— the child's deepest ethical drive is affiliation. "
        "Ignoring this and preaching 'stand up for what's right' "
        "fails because it demands post-conventional reasoning the "
        "brain isn't wired for yet. The skill works WITH the "
        "developmental grain: it reframes exit as an affiliation "
        "move ('protect the friend group from turning into "
        "something you don't want to be part of') rather than as "
        "individual rebellion. Piaget's concrete-operational (7-"
        "11) / early formal-operational (11+) supplies the "
        "capacity to hold multiple perspectives simultaneously "
        "(the target's, the pile-on's, your own). Bandura's moral "
        "disengagement research: the specific disengagement "
        "mechanism in pile-ons is DIFFUSION OF RESPONSIBILITY "
        "('everyone was doing it') - the skill names and neutralises "
        "this specific cognitive pattern. Salmivalli's defender-role "
        "framework is the operational outcome: we are teaching the "
        "cognitive pattern associated with defenders, not asking "
        "the child to adopt a heroic identity."
    ),
    creator_luring_awareness=(
        "Indirect. Pile-ons can be coordinated by outside "
        "adversaries (groomers, incel-adjacent influencers, "
        "political actors running youth campaigns) who seed "
        "content designed to trigger teen pile-ons as a way to "
        "radicalise participants. A child with the exit-from-"
        "pile-on habit is less susceptible to this coordinated "
        "amplification; they become a point of friction in the "
        "cascade. Complementary to the 13-15 sextortion row "
        "(1f), the 13-15 lateral-reading row (1h) and the 10-12 "
        "grooming row: all protect against the adult adversary "
        "using teen social dynamics as the attack surface."
    ),
    example_activity=(
        "SESSION 1 - NAME THE PATTERN (20 min, family time). "
        "Caregiver describes 3-4 realistic short scenarios of "
        "pile-ons in a fictional group chat (not the child's real "
        "one - pick fictional names). For each, child answers: "
        "(a) what was the trigger? (b) who escalated? (c) who "
        "stayed silent? (d) who forwarded it? The goal is not "
        "judgement but pattern-recognition - the child learns to "
        "SEE the structure of a pile-on in real time. "
        "SESSION 2 - THE THREE MOVES (15 min, same or next day). "
        "Teach the three exit moves explicitly: "
        "  MOVE 1 (the easiest): DON'T FORWARD. Most pile-ons "
        "expand through forwarding. If you get sent a pile-on "
        "target, you stop the cascade by not forwarding. Nobody "
        "knows you got it. Zero social cost. "
        "  MOVE 2 (slightly harder): PRIVATE DM TO THE TARGET. "
        "One-line message: 'I saw what's going on in [chat]. "
        "It's dumb. You good?' Send privately, not in the group. "
        "The target sees it; the pile-on group doesn't. The "
        "target will remember this for years. "
        "  MOVE 3 (hardest, not always possible): CHANGE THE "
        "SUBJECT IN THE GROUP. 'Did anyone do the math homework?' "
        "or 'anyone watching the game tonight?' Doesn't call out "
        "the pile-on; just redirects. Works 40-60% of the time "
        "- a working 'out'. "
        "ROLE-PLAY (optional, 5-10 min): caregiver plays the "
        "pile-on starter; child rehearses each of the 3 moves "
        "aloud. Explicit: rehearsal makes the response automatic. "
        "Under real social pressure at 11, the child is NOT "
        "going to invent the moves - they'll fall back to "
        "whatever they practised."
    ),
    gamification_element=(
        "DELIBERATELY not gamified with stickers or counts. "
        "Pile-ons are charged enough that any scoring feels "
        "like performance. Instead: a private journal entry "
        "(physical or in Notes app) anytime the child used any "
        "of the three moves. Journal is not reviewed by anyone - "
        "it's a private self-tracking habit. Caregiver "
        "occasionally asks 'any moves this week?' and accepts "
        "'yes' or 'no' as the complete answer. The absence of "
        "performance pressure is the design."
    ),
    screen_time_guidance=(
        "The skill applies during the child's existing group-"
        "chat time. No new screen-time rule. The ONE screen-"
        "time policy that complements this skill: child keeps "
        "the screenshot of any pile-on they personally witnessed "
        "for 48 hours before deleting - in case adult "
        "intervention becomes necessary. No obligation to share "
        "the screenshot with anyone; just holding it is "
        "optionality."
    ),
    parental_controls_component=(
        "Technical controls are SECONDARY here - the primary "
        "intervention is the conversation. Useful complements: "
        "(a) teach the child how to mute a group chat without "
        "leaving it (leaves social fabric intact, stops "
        "notification floods); (b) the block / report options "
        "on the main platforms the child uses - but frame these "
        "as the child's own tools, not parental surveillance; "
        "(c) if a pile-on rises to the level of sustained "
        "targeted harassment, Kids Help Phone Canada "
        "(kidshelpphone.ca, 1-800-668-6868, text 686868) is a "
        "named and vetted resource. The caregiver's deepest "
        "role: not a reflex to seize the phone when a pile-on "
        "is reported. The child needs the phone to exit the "
        "pile-on; removing the phone punishes the child for "
        "telling."
    ),
    media_quality_rubric=(
        "GOOD: agency-based framing (your moves, your choices) "
        "not heroic framing (save the victim); three concrete "
        "rehearsed moves; caregiver plays the pile-on starter "
        "in role-play so child practises the response aloud; "
        "private journal (not reviewed); caregiver commits NOT "
        "to confiscate the phone when a pile-on is reported. "
        "AVOID: 'be an upstander' language (kids this age "
        "reject it as adult-moralising); framing exit as "
        "bravery or heroism (overshoots the developmental "
        "reality - defenders are NOT adult rescuers); shaming "
        "the child for past participation in pile-ons (the "
        "skill is prospective, not retrospective); using the "
        "skill as a lever to justify reading the child's "
        "messages; demanding the child report every pile-on to "
        "an adult (cedes the child's social agency)."
    ),
    en_ca_content=(
        "**Pile-ons are the dominant bad experience at your age.** "
        "One person in a group chat makes fun of someone, three "
        "others pile on, someone forwards it outside, the target "
        "feels wrecked. Canadian research (PREVNet) shows this "
        "peaks between 10 and 13. You will see it. You will "
        "maybe be IN one, on either side, this year.\n\n"
        "**Your goal is NOT to be a hero.** It's to not amplify, "
        "and to leave the target less alone. That's the whole "
        "skill. Three moves, in order of difficulty:\n\n"
        "**Move 1 — Don't forward.** The easiest, and the one "
        "that matters most. Pile-ons scale through forwarding. "
        "Screenshot that the group shared, meme of the target, "
        "caption dragging them — if you just DON'T forward it "
        "to anyone else, you shrink the pile-on by one. Zero "
        "social cost. Nobody knows you didn't forward.\n\n"
        "**Move 2 — Private DM to the target.** One line, "
        "privately: **\"I saw what's going on in [chat]. It's "
        "dumb. You good?\"** That's it. Not in the group — "
        "privately, to the target. They will remember you did "
        "this for literal years. This is the move that "
        "teachers talk about when they say 'one person "
        "reaching out can change everything'. They're right, "
        "but you don't need to announce it to make it work.\n\n"
        "**Move 3 — Change the subject in the group.** "
        "\"Anyone watch the game last night?\" \"Did you do the "
        "math hw?\" You're not calling out the pile-on — that "
        "would make you the next target. You're just shifting "
        "the topic. Works maybe half the time. Costs nothing "
        "to try.\n\n"
        "**The psychology (briefly, because it matters).** "
        "Research shows that when even ONE person in a bullying "
        "situation doesn't go along with it, the pile-on stops "
        "within about 10 seconds in most cases. The group was "
        "ALREADY uncomfortable; it was waiting for an exit. You "
        "don't have to be brave — you have to be a single "
        "friction point. Even just not forwarding counts.\n\n"
        "**The bigger thing.** Your brain at 10-12 is wired to "
        "care a LOT about fitting in. That's not a flaw — it's "
        "how you're supposed to work at this age. The instinct "
        "to join the pile-on will feel almost automatic. That's "
        "normal. What you're learning here is a specific "
        "override: you care about the group, AND you don't want "
        "the group to turn into something you'd be embarrassed "
        "by in 3 years. The three moves above are how you "
        "protect the group from itself without making yourself "
        "the target.\n\n"
        "**You will mess this up sometimes.** That's OK. "
        "Practice is everything. The private journal is where "
        "you log it — not for anyone else, just for you. Over a "
        "year, you will get noticeably better at exiting pile-"
        "ons quickly, and your friends will pick up the same "
        "habits by watching.\n\n"
        "**One more thing.** If a pile-on becomes sustained "
        "harassment of one person — not a bad day, but a week+ "
        "pattern — **that's outside your three moves**. Tell an "
        "adult. Or: call or text Kids Help Phone "
        "(**1-800-668-6868** or text **686868**). They're "
        "24/7, free, and confidential. You are not a snitch "
        "for escalating something that has escalated itself."
    ),
    fr_qc_content="",
    ar_description=(
        "Not applicable. The skill is a social-conversational "
        "habit executed in group chats the child already uses. "
        "An AR layer would not add value; the platform itself "
        "(Snapchat, Discord, iMessage, Instagram DMs) is the "
        "tool. Kids Help Phone Canada is the named escalation "
        "channel for situations that exceed the three moves."
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
