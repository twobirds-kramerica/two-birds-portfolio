"""S-R01-STRETCH-1y — 7-9 Emotional-Safety: Online kindness counts —
words stick longer online than in person.

2nd row in the 7-9 × Emotional-Safety cell. Companion to the existing
"Telling a grown-up when something online feels weird" row. Where that
row teaches protective behaviour (what to do when something bad happens
to you), this row teaches prosocial behaviour: how to be kind online,
why digital words land differently than in-person words, and how to be
an upstander when you see unkind things in a group chat.

Run once:   python _s_r01_stretch_1y.py
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
    skill="Online kindness counts — words stick longer online than in person",
    category="Emotional-Safety",
    age_ranges=["7-9"],
    priority="P1-Important",
    status="Research",
    demonstration_method="Play-Acting",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Children aged 7-9 are entering peer group life in earnest — "
        "group chats, class messages, gaming lobbies, and shared apps "
        "are becoming their primary social spaces alongside the "
        "playground. Unlike in-person words, digital messages carry "
        "no tone of voice, facial expressions, or immediate repair "
        "signals. A joke that would be recovered from in seconds "
        "face-to-face can be re-read, screenshotted, and forwarded "
        "in ways the sender never intended. This row teaches three "
        "things: (1) why digital words land differently than in-person "
        "words; (2) the 'would I say this to their face?' check as a "
        "before-you-send habit; (3) what to do when you see someone "
        "being unkind in a group chat — the upstander move that does "
        "not require confronting the sender directly."
    ),
    research_source=(
        "Valkenburg, P. M., & Peter, J. (2009). 'Social consequences "
        "of the internet for adolescents: A decade of research.' "
        "Current Directions in Psychological Science, 18(1), 1-5. "
        "Core finding: online communication strengthens existing "
        "friendships when used prosocially; the same channels amplify "
        "offline conflict when used unkindly. Used to frame the "
        "double-edged nature of digital communication in this age group. "
        "Common Sense Media (2019). 'Social Media, Social Life: "
        "Tweens and Teens and Technology.' Children aged 8-12 report "
        "that their closest friendships are maintained partly through "
        "messaging; also report that 39% have seen someone be mean or "
        "cruel online in the past year. "
        "PREVNet Canada (prevnet.ca) — Promoting Relationships and "
        "Eliminating Violence Network. Canadian national research hub "
        "on bullying prevention. Prosocial bystander research: children "
        "who are taught upstander moves (redirect, support the target, "
        "leave the group, tell an adult) are 2-3× more likely to "
        "intervene than those who know bullying is wrong but have no "
        "concrete strategy. "
        "MediaSmarts Canada (mediasmarts.ca) — 'Cyberbullying' and "
        "'Connected to What?' resources. Canadian-specific, age-graded "
        "guidance on digital kindness and bystander behaviour for "
        "Grades 2-4. "
        "Kohlberg, L. (1976). 'Moral stages and moralization.' In "
        "T. Lickona (Ed.), Moral Development and Behavior. Holt, "
        "Rinehart and Winston. Conventional morality (Stage 3, "
        "'good boy / nice girl' orientation): 7-9 year olds are "
        "entering Stage 3 and are highly responsive to appeals about "
        "what a good friend or a kind person would do. This is the "
        "developmentally appropriate moral frame for this row's content. "
        "Zarbatany, L., McDougall, P., & Hymel, S. (2000). 'Gender-"
        "differentiated experience in the peer culture: Links to "
        "intimacy in preadolescence.' Social Development, 9(1), 62-79. "
        "Peer acceptance is the primary social driver for 7-9; being "
        "seen as kind and fair by peers is a higher motivator than "
        "rule-following at this age."
    ),
    threat_addressed=(
        "Two threat vectors in the 7-9 × Emotional-Safety space that "
        "this row addresses: "
        "(a) UNINTENTIONAL HARM — children in this age group "
        "frequently say things in digital spaces that they would "
        "not intend as unkind but that land as hurtful without "
        "in-person tone cues. The 'would I say this to their face?' "
        "check intercepts this before it causes relationship damage. "
        "(b) PASSIVE BYSTANDER RISK — when a child witnesses unkind "
        "behaviour in a group chat and says nothing, they implicitly "
        "validate the unkindness. 7-9 year olds are developmentally "
        "capable of upstander moves but frequently do not take them "
        "because they do not have a concrete strategy. This row "
        "provides three specific upstander moves adapted for digital "
        "group contexts that do not require direct confrontation."
    ),
    psychology_framework=(
        "Kohlberg Stage 3 (conventional morality, 'good boy / nice "
        "girl'): 7-9 year olds are highly responsive to 'what would "
        "a good friend do?' framing. This row's content should appeal "
        "to this orientation, not to abstract rules. 'A good friend "
        "checks whether their joke landed' is more effective than "
        "'the rule is: be kind.' "
        "Perspective-taking (Vygotsky's ZPD for social cognition): "
        "7-9 year olds are developing the ability to model what "
        "another person feels, but it requires scaffolding — they "
        "need to be explicitly prompted to take the receiver's "
        "perspective before sending. The 'face-to-face check' is "
        "a practical scaffold for this developmental capacity. "
        "Bystander effect (Latane & Darley, 1968): the classic "
        "'diffusion of responsibility' effect applies in group chats. "
        "Children see 12 people in a group, assume someone else will "
        "say something, and say nothing. Teaching that 'if you see "
        "it, it is partly your responsibility' directly counters "
        "diffusion of responsibility."
    ),
    creator_luring_awareness=(
        "Digital kindness training has a secondary benefit for "
        "creator-luring protection: children who understand that "
        "online words can be screenshotted and used out of context "
        "are also more resistant to 'send me something you wouldn't "
        "want your parents to see' pressure tactics. The concept that "
        "digital content persists and travels beyond the original "
        "audience is taught as a kindness principle here; it also "
        "directly informs why sharing private images or information "
        "at a stranger's request is risky."
    ),
    example_activity=(
        "THE TONE-DEAF MESSAGE GAME (15 min, in person with a trusted "
        "adult; works as a family activity or classroom exercise). "
        "PART 1 — THE SAME WORDS, DIFFERENT WORLD. "
        "Write three sentences on paper: "
        "'You did that wrong.' / 'Ha, nice try.' / 'That's an "
        "interesting choice.' "
        "First, one person says each sentence out loud with a warm, "
        "playful tone and facial expression. Notice how it lands. "
        "Then, show the same sentences as a text on a phone or card — "
        "no tone, no face. Ask: 'How does it feel now? Could it be "
        "mean? Could it be kind? How do you know?' "
        "This makes the missing-tone-cue problem concrete. "
        "PART 2 — THE FACE-TO-FACE CHECK. "
        "Introduce the rule: before you send something that could "
        "be taken two ways, ask: 'Would I say exactly this, in "
        "exactly this way, to their face right now?' "
        "If the answer is 'probably not' or 'I'd say it differently' — "
        "edit it. Add a word that shows you mean it kindly: 'Ha, "
        "nice try though :)' or 'You did that wrong — here, let me "
        "show you what worked for me.' "
        "PART 3 — THE UPSTANDER TOOLBOX. "
        "Three things you can do when you see unkind messages in "
        "a group chat, without confronting the sender directly: "
        "(1) PRIVATE SUPPORT: Send a private message to the person "
        "who got the unkind message: 'Hey, I saw that. That was "
        "not cool. You OK?' "
        "(2) REDIRECT THE ROOM: In the group, post something unrelated "
        "but positive: 'Hey did everyone see [fun thing]?' This "
        "changes the subject without calling anyone out. "
        "(3) LEAVE AND TELL: If the unkindness is serious or ongoing, "
        "you are allowed to leave the group and tell a trusted adult. "
        "You do not have to stay in a group that makes people feel bad. "
        "Practice: role-play a group chat scenario where one person "
        "makes a joke that lands unkindly. Which of the three moves "
        "fits best in this situation?"
    ),
    gamification_element=(
        "The 'kindness receipt.' For one week, every time the child "
        "sends a message that they feel good about — something kind, "
        "supportive, or that they specifically checked with the "
        "face-to-face test — they mark it on a paper receipt strip. "
        "At the end of the week, they have a physical list of kind "
        "messages they sent. The goal is 7 receipts in 7 days (one "
        "per day). Not a competition — a self-observation tool that "
        "makes invisible prosocial behaviour visible and rewarding."
    ),
    screen_time_guidance=(
        "The face-to-face check adds 5-10 seconds to each message. "
        "There is no screen time overhead beyond that. The upstander "
        "private-message move may add a brief message exchange but "
        "is a net positive for the recipient's wellbeing. The 'leave "
        "and tell' move explicitly reduces group-chat exposure."
    ),
    parental_controls_component=(
        "Technical supports that complement this skill: "
        "(a) Review group chats together: periodically ask to see "
        "the group chats the child is in, not to surveil but to "
        "open conversation. 'Anyone in here ever be unkind?' is a "
        "better opener than checking without permission. "
        "(b) Contact list review: know who is in the child's "
        "contacts. Group chats containing unknown adults or older "
        "teens are a risk signal. "
        "(c) Kids Help Phone (kidshelpphone.ca, text 686868, "
        "1-800-668-6868): the Canadian 24/7 support line for "
        "children and teens. Worth bookmarking on the child's "
        "device so they know it is there. "
        "(d) In-platform reporting: most platforms used by this "
        "age group (Roblox, Minecraft, YouTube Kids) have in-app "
        "reporting. Walk through how to use it together once."
    ),
    media_quality_rubric=(
        "GOOD: child uses the face-to-face check before sending "
        "ambiguous messages; child has taken at least one upstander "
        "move in a digital context; child can name all three upstander "
        "strategies (private support, redirect, leave and tell); "
        "child understands that screenshots mean digital words travel "
        "beyond the original recipient. "
        "AVOID: framing kindness as only about avoiding punishment "
        "('don't be mean or you'll get in trouble') — this activates "
        "pre-conventional morality and is less durable than "
        "conventional/'good friend' framing; treating upstander moves "
        "as mandatory confrontation (the 'call out the bully' model "
        "is developmentally inappropriate for 7-9 and often makes "
        "things worse); screen-time shaming as the solution to "
        "unkind digital behaviour (it addresses the channel, not "
        "the skill). "
        "The standard: the child has a concrete strategy for "
        "both sending kindly and being an upstander. Knowing that "
        "online words can be hurtful is not enough — the row "
        "succeeds when the child has practised a move."
    ),
    en_ca_content=(
        "**Online words don't have a face.** When you talk to "
        "someone in person, they can see your face, hear your voice, "
        "and know if you're joking. Online, all they have is the "
        "words. A joke that seems obvious to you can look mean to "
        "them. A teasing message that would be funny out loud can "
        "sting on a screen — especially if it is re-read five times.\n\n"
        "**The face-to-face check.** Before you send something that "
        "could be taken two ways, ask yourself: 'Would I say exactly "
        "this, in exactly this way, to their face right now?' If the "
        "answer is 'probably not,' add a word that shows you mean "
        "it kindly — an emoji, 'just kidding,' 'but seriously though "
        "you did great.' It takes five seconds and it changes how "
        "the message lands.\n\n"
        "**One more thing about digital words: they travel.** What "
        "you type to one person can be screenshotted and shared with "
        "people you never meant to see it. That is not to scare "
        "you — most messages are just messages. But it is worth "
        "knowing that digital words stick around differently than "
        "spoken words.\n\n"
        "**What to do when you see something unkind in a group chat:**\n\n"
        "**Private support** — send a private message to the person "
        "who got the unkind message: 'Hey, I saw that. That was not "
        "cool. You okay?'\n\n"
        "**Redirect the room** — post something positive in the group "
        "to change the subject. You don't have to call anyone out "
        "to change what is happening.\n\n"
        "**Leave and tell** — you are allowed to leave a group chat "
        "that makes people feel bad. And you can tell a trusted "
        "adult. That is not tattling. That is how things get fixed."
    ),
    ar_description=(
        "No AR application in Phase 1. Future opportunity: an AR "
        "experience where the child sees a message 'floating' with "
        "different emotional overlays depending on whether the sender "
        "is smiling, frowning, or neutral — making the tone-cue "
        "problem visually concrete. Flag for Phase 2 AR sprint."
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
