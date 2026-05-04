"""S-R01-STRETCH-1q — 13-15 Creative-Making: Publishing your work
responsibly — audience, consent, and permanence.

2nd row in the 13-15 × Creative-Making cell. The existing row(s) for
13-15 Creative-Making address the creative process itself. This row
addresses the publishing decision: once a teen creates something (art,
writing, video, meme, post), what are the responsibilities before
publishing? Covers audience modelling, consent for featuring others,
and the permanence principle (screenshots are forever).

Run once:   python _s_r01_stretch_1q.py
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
    skill="Publishing my work responsibly — audience, consent, and permanence",
    category="Creative-Making",
    age_ranges=["13-15"],
    priority="P1-Important",
    status="Research",
    demonstration_method="Multi-Modal",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "At 13-15, teens are increasingly publishing original creative work "
        "online — short-form video, art, writing, music, photography, memes. "
        "The creative act and the publishing act require different skills. "
        "This row covers the publishing decision framework: (1) AUDIENCE "
        "MODELLING — who will actually see this, including unintended "
        "audiences (employers, future romantic partners, colleges, family); "
        "(2) CONSENT — if the work features other people (photos, videos, "
        "screenshots of conversations), do those people know and agree?; "
        "(3) PERMANENCE — anything published online can be screenshotted "
        "and redistributed regardless of deletion; the teen internalises "
        "the 'screenshot test' before publishing. Also covers platform "
        "terms of service as they relate to creative ownership — most "
        "platforms claim broad licences over uploaded content."
    ),
    research_source=(
        "PIPEDA / CPPA (Canada's Personal Information Protection and "
        "Electronic Documents Act, and the forthcoming Consumer Privacy "
        "Protection Act): Canadian law governing when photographs of "
        "identifiable people can be published without consent. In most "
        "Canadian provinces, publishing an identifiable image of a private "
        "person without consent for non-journalistic purposes is a "
        "privacy violation. Teens are not exempt. "
        "Office of the Privacy Commissioner of Canada (priv.gc.ca) — "
        "'Privacy and Teens' resource: documents the specific privacy "
        "obligations teens have when creating and sharing content featuring "
        "others. Includes consent language and practical guidance. "
        "MediaSmarts (mediasmarts.ca) — 'Privacy, Publicity and the "
        "Internet': Canadian resource addressing the permanence principle "
        "and platform terms of service for the 13-17 age group. "
        "Solove, D. (2007) 'The Future of Reputation: Gossip, Rumor, and "
        "Privacy on the Internet' (Yale University Press): foundational "
        "academic work on online permanence and reputation. Key insight: "
        "the internet does not forget, and the contexts in which content "
        "was created rarely survive the redistribution of that content. "
        "A meme made among friends becomes a screenshot shared to strangers "
        "— the original context evaporates. "
        "Creative Commons (creativecommons.org): framework for licensing "
        "creative work online. Teens who publish creative work should "
        "understand that the default is all-rights-reserved in Canada "
        "(copyright attaches at creation), and that platforms like "
        "Instagram, TikTok, and YouTube claim broad licence rights over "
        "uploaded content that are sometimes broader than the creator "
        "intended. "
        "Canadian Centre for Child Protection (protectchildren.ca) — "
        "documentation of non-consensual intimate image distribution "
        "(NCII) as a specific harm vector for 13-17 year olds. Consent "
        "in creative content featuring others is the upstream prevention."
    ),
    threat_addressed=(
        "Three primary threats in the 13-15 creative publishing space: "
        "(1) FUTURE REPUTATION HARM — content published at 14 is "
        "discoverable at 24. College admissions, employers, and future "
        "partners will find it. What is acceptable in a peer group at "
        "14 may be disqualifying in a professional context at 24. "
        "(2) CONSENT VIOLATIONS — photos and videos of peers published "
        "without consent can cause serious harm to the subject "
        "regardless of the creator's intent. The harm is not offset by "
        "'I didn't mean anything by it.' Canadian privacy law and, in "
        "some cases, criminal law (harassment, non-consensual image "
        "distribution) apply. "
        "(3) PLATFORM LICENCE EXPLOITATION — teens who do not read "
        "terms of service may inadvertently grant platforms perpetual "
        "commercial licences to their creative work. Increasingly "
        "relevant as AI training datasets are built from user-generated "
        "content under broad TOS licence grants."
    ),
    psychology_framework=(
        "Erikson's identity vs. role confusion stage (12-18): "
        "adolescents are actively constructing their public identity. "
        "Publishing creative work is a core identity-formation act at "
        "this age — it is how teens present themselves to the world and "
        "test social responses. The skill does not inhibit this — it "
        "adds the publishing decision layer to the creative act so that "
        "identity construction is intentional rather than reactive. "
        "Elkind's 'imaginary audience' (1967): adolescents "
        "characteristically assume they are being watched and evaluated "
        "by everyone. The audience-modelling exercise in this skill is "
        "a constructive use of this developmental tendency — rather than "
        "being paralysed by the imaginary audience, the teen explicitly "
        "models the actual audience before publishing. "
        "Prefrontal cortex development (ongoing through age 25): the "
        "impulse-to-publish reaction in a teen is a fast, socially "
        "motivated System 1 response. The publishing decision framework "
        "is a deliberate System 2 pause — three questions, 60 seconds, "
        "before the post goes live."
    ),
    creator_luring_awareness=(
        "Publishing frameworks are a direct defence against recruitment "
        "and exploitation vectors that operate through teens' creative "
        "work: (a) 'art challenges' and viral trends that harvest "
        "personal images or information under a creative pretext; "
        "(b) platforms that use broad TOS to claim rights over creative "
        "work for commercial or AI training purposes without transparent "
        "disclosure; (c) romantic or social manipulation that begins "
        "with requests for photos ('you're so talented, can you send "
        "me something?'). The consent-first habit and the screenshot "
        "test apply directly to these vectors."
    ),
    example_activity=(
        "THE PUBLISHING CHECKLIST (5-10 min before any publish, "
        "practised until automatic). Three questions, in order: "
        "  QUESTION 1 — AUDIENCE: 'Who will actually see this?' "
        "Not just 'my followers' but: could a screenshot reach someone "
        "outside my current circle? Could this be found by a college "
        "admissions office in 4 years? Could a future employer find it? "
        "If yes: is that okay with me? "
        "  QUESTION 2 — CONSENT: 'Is anyone else in this?' If the "
        "content features another person — a photo, a video, a "
        "screenshot of a conversation — does that person know this "
        "is being published? Would they be comfortable with the "
        "audience in Question 1 seeing it? If unsure: ask them first. "
        "If asking would feel awkward: that feeling is information. "
        "  QUESTION 3 — PERMANENCE: 'Am I okay with this existing "
        "forever?' Even if I delete it in an hour, someone might have "
        "screenshotted it. Would I be okay if this existed permanently? "
        "If yes to all three: publish. "
        "If no to any: revise, delay, or don't publish. "
        "CAREGIVER DEBRIEF (monthly, 10 min): scroll back through "
        "the teen's public-facing content together — not as surveillance "
        "but as a portfolio review. 'Is there anything here you'd want "
        "to take down now?' Normalise periodic review and voluntary "
        "pruning of old content."
    ),
    gamification_element=(
        "The 'publishing portfolio' review. Once a month, teen reviews "
        "their own published content from the past 30 days and rates "
        "each piece: 'glad I published this / neutral / would think "
        "twice now.' The goal is not to shame past decisions but to "
        "build the feedback loop between publishing choices and "
        "retrospective comfort. Over 3-4 months, the ratings naturally "
        "shift toward 'glad I published this' as the checklist habit "
        "filters publishing decisions upstream. The teen can keep the "
        "ratings private — the exercise is for self-calibration, "
        "not reporting."
    ),
    screen_time_guidance=(
        "The publishing checklist adds 60-90 seconds to any "
        "publishing act. This is not a screen time concern — it "
        "replaces the impulsive 2-second publish with a deliberate "
        "60-second publish. Net screen time: neutral. The monthly "
        "portfolio review takes 10 minutes and is best done with "
        "a caregiver. Total additional time: under 15 minutes per month."
    ),
    parental_controls_component=(
        "Privacy settings review (semi-annual): "
        "(a) Review privacy settings on every platform the teen uses — "
        "who can see posts, who can share them, whether location data "
        "is embedded in photos. Platforms change settings frequently; "
        "a semi-annual check is the minimum. "
        "(b) In Canada, PIPEDA consent requirements apply to images of "
        "identifiable private individuals. If a teen's content features "
        "other minors, those minors' parents may have legal standing "
        "to request removal. Understanding this prevents accidental "
        "legal exposure for the family. "
        "(c) Canadian Centre for Child Protection offers a 'Survivor "
        "Resource' for non-consensual image distribution at "
        "cybertip.ca — relevant if the teen becomes a victim as well "
        "as a creator. "
        "(d) Do NOT monitor the teen's private accounts without "
        "agreement — the trust relationship is more protective long-"
        "term than surveillance. Negotiate which accounts are "
        "public/shared and which are private."
    ),
    media_quality_rubric=(
        "GOOD: publishing checklist applied before any public post; "
        "consent obtained before featuring others; screenshot test "
        "applied to high-stakes content; teen understands that "
        "deletion is not erasure; platform TOS reviewed for at least "
        "the primary creative platform in use; monthly portfolio review "
        "practiced. "
        "AVOID: using the checklist as a censorship tool ('you can't "
        "post that'); requiring parental approval for all posts "
        "(builds resentment, bypassed quickly); treating all online "
        "content as dangerous (inhibits healthy identity formation). "
        "The standard: the teen pauses before publishing anything "
        "that features another person and asks 'do they know?' "
        "That pause, unprompted, is the skill."
    ),
    en_ca_content=(
        "**Making something is one skill. Publishing it is another.** "
        "The creative act and the publishing decision are not the same "
        "thing. Most people learn this the hard way — a post that felt "
        "fine at 14 becomes uncomfortable at 18, or a photo of a friend "
        "that seemed harmless becomes a problem when it reaches the "
        "wrong audience.\n\n"
        "**Three questions before you post.** "
        "They take 60 seconds. They save a lot of regret.\n\n"
        "**1. Who will actually see this?** Not just your current "
        "followers. Screenshots travel. Could this reach your future "
        "self — a college admissions office, a job interview, someone "
        "you'll care about in 5 years? If yes: is that okay?\n\n"
        "**2. Is anyone else in this?** If your content features "
        "another person — a photo, a video, a screenshot of a "
        "conversation — do they know it's being published? Would they "
        "be okay with the audience you identified in question 1? "
        "If you'd feel awkward asking them: that feeling is telling "
        "you something.\n\n"
        "**3. Am I okay with this existing forever?** Deleting a post "
        "does not erase it. Screenshots happen in seconds. If this "
        "post existed permanently — would you still be okay with it?\n\n"
        "**On platform terms of service.** Every platform you upload "
        "to asks you to agree to a licence. Most of them claim broad "
        "rights over your content — the right to use it commercially, "
        "to train AI on it, to redistribute it. You still own your "
        "work, but the platform has rights too. Worth knowing before "
        "you upload something you care about.\n\n"
        "**The monthly review.** Once a month, scroll back through "
        "your public posts from the past 30 days. Anything you'd take "
        "down now? Take it down. No drama. Just periodic maintenance "
        "of your digital presence — the same way you'd edit a portfolio."
    ),
    ar_description=(
        "No AR application in Phase 1 — this is a decision-framework "
        "skill. Future opportunity: an AR 'publishing stamp' tool "
        "where the teen holds up a finished piece of art to the camera "
        "and the AR overlay walks through the three questions before "
        "a simulated 'publish' animation. Could be built as a "
        "gamified pre-publish ritual for younger teens. Flag for "
        "Phase 2 if the audience confirms interest."
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
