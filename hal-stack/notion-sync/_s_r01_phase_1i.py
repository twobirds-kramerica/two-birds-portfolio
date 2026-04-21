"""S-R01-PHASE-1i — 10-12 Creative-Making: naming your sources when remixing.

2nd row in the 10-12 x Creative-Making cell. Pairs as the positive-
citizenship counterpart to the 13-15 Tech-Safety 2FA skill: both are
about 'adult internet hygiene you install now so it's automatic later'.

Foundation for later creator-culture skills; also protects the child's
own IP once they start publishing (Wattpad, Roblox creations, TikTok).

Run once:   python _s_r01_phase_1i.py
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
    skill="When I remix something, I name who made the original",
    category="Creative-Making",
    age_ranges=["10-12"],
    priority="P1-Important",
    status="Research",
    demonstration_method="Multi-Modal",
    learning_profile=["Standard", "ADHD", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Pre-teen creator-citizenship skill for the age when kids "
        "actively remix: fan art, meme edits, Minecraft + Roblox "
        "mods, TikTok duets and stitches, music mashups, "
        "fanfiction. The skill is simple and lifelong: whenever "
        "you publish a remix, you name the original creator in "
        "the caption, description, or a visible credit. "
        "Complementary side: learn that Creative Commons is how "
        "creators say 'yes, you can remix this and here's how'. "
        "The framing is explicitly positive — remixing is "
        "good, original creators are good, naming both is how "
        "grown-up creator cultures work."
    ),
    research_source=(
        "Common Sense Education - Copyright, Creative Commons, and "
        "Fair Use in the Classroom (commonsense.org/education/"
        "articles/copyright-creative-commons-and-fair-use-in-the-"
        "classroom): positions Grades 3-6 as the explicit window "
        "where copyright + fair use + public domain + Creative "
        "Commons get taught, with the goal of 'transforming "
        "students into responsible digital citizens'. "
        "Creative Commons - official license documentation "
        "(creativecommons.org/share-your-work/cclicenses): six "
        "license variants (CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, "
        "CC BY-ND, CC BY-NC-ND) plus CC0 and the public domain "
        "mark. CC BY is the simplest: 'you can remix, just name me'. "
        "Copyright & Creativity Elementary School curriculum "
        "(copyrightandcreativity.org/elementary-school) - free K-6 "
        "classroom curriculum on copyright basics. "
        "Lessig, Lawrence - 'Remix: Making Art and Commerce Thrive "
        "in the Hybrid Economy' (2008) - foundational academic "
        "text arguing remix culture is how creativity has always "
        "worked; remix ethics = naming sources. "
        "Edublogger - 'The Ultimate Guide to Copyright, Creative "
        "Commons, and Fair Use' (theedublogger.com/copyright-"
        "fair-use-and-creative-commons) - teacher-facing plain-"
        "language summary. "
        "OER Commons - 'Creative Commons: Taking Ownership of "
        "Creativity' (oercommons.org/courseware/lesson/27432) - "
        "free lesson plan."
    ),
    threat_addressed=(
        "Three interlocking risks this skill addresses: "
        "(1) EDUCATIONAL - the child grows up thinking 'the "
        "internet is free stuff I can take' and hits their first "
        "DMCA takedown / plagiarism incident at age 15-17 with no "
        "framework for what happened; "
        "(2) REPUTATIONAL - the pre-teen years are when kids start "
        "publishing (Roblox games, TikTok remixes, fanfiction on "
        "AO3/Wattpad). Un-credited remixes on public platforms "
        "flag the creator as an amateur and can get the account "
        "flagged or suspended; "
        "(3) SELF-PROTECTIVE - once the child publishes THEIR own "
        "work and understands licensing, they can set terms "
        "explicitly ('CC BY means you can use my Roblox code if "
        "you credit me'). Without this skill, they default to "
        "either over-sharing (anything goes) or under-sharing "
        "(never publish) - both suboptimal."
    ),
    psychology_framework=(
        "Piaget's concrete-operational stage (7-11) extending into "
        "early formal-operational (11+): the child can follow rules "
        "consistently and is beginning to understand abstract "
        "social contracts (copyright as a social agreement, not a "
        "physical property). Kohlberg's conventional-morality stage "
        "(roughly 10-13): children internalise 'what the community "
        "does is what is right' - the skill leverages this by "
        "framing credit-naming as 'how real creators behave'. "
        "Self-determination theory: satisfies competence (concrete "
        "technique), autonomy (child controls their own credit "
        "practice), and relatedness (positions the child inside "
        "an identifiable creator community). Research on pro-social "
        "attribution behaviour (e.g., anthropologists' work on gift "
        "economies): naming the source is a reciprocity signal "
        "that builds community, not a legal compliance move. Frame "
        "the skill that way."
    ),
    creator_luring_awareness=(
        "Indirect but real. Predators in creator-adjacent "
        "communities (fanfic, fan-art Discord servers, Roblox) "
        "sometimes groom teens by offering editorial feedback, "
        "collaboration, or 'free' assets. A teen who already "
        "participates in visible attribution/credit culture is "
        "embedded in a community where transactions are named, "
        "publicly logged, and reputation matters. That's a "
        "harder environment for a predator's private 'I'll help "
        "you, but don't mention me' script to gain traction. "
        "Complements the 10-12 'please don't tell your parent' "
        "row and the 13-15 sextortion row by building "
        "transparency habits in creative contexts specifically."
    ),
    example_activity=(
        "SESSION 1 (20 min, family time): caregiver and child "
        "look at 5 things the child has made or almost made in "
        "the last month - a drawing based on a Pokemon, a "
        "meme edit of a movie scene, a Roblox creation that uses "
        "someone else's assets, a TikTok using a trending song, "
        "a fanfic chapter. For each one, they name every source "
        "involved: the original artist/studio/songwriter. This "
        "is a noticing exercise, not a judgment exercise - most "
        "remixes have 3-5 sources and that's NORMAL. "
        "SESSION 2 (15 min, same or next day): introduce Creative "
        "Commons. Walk through creativecommons.org/share-your-"
        "work/cclicenses together. Pick ONE piece the child made "
        "themselves (a drawing, a Roblox map, a short story) and "
        "the child decides what license they'd put on it if they "
        "published it. CC BY (anyone can remix, just credit me) "
        "is the simplest starting point. "
        "ONGOING HABIT (lifetime): every time the child publishes "
        "something that remixes anyone else's work, they add a "
        "credit line. Format: 'Original X by [creator name], "
        "remixed by [child's handle]'. For Roblox and TikTok this "
        "goes in the description. For physical art, on the back. "
        "For school projects, as a footnote. Make it a default, "
        "not a special event."
    ),
    gamification_element=(
        "A 'sources named' running count - the child tracks how "
        "many sources they've credited across all their "
        "publications over the year. The goal is not 'most "
        "sources' but 'never zero' - every published remix has "
        "at least one named source. Target for year 1: 20 "
        "remixes, 100% credited. Year 2: same bar at any volume. "
        "Credit this explicitly in family conversations: 'you "
        "credited 4 sources on that Roblox game, that's how real "
        "creators behave'. Pair with a public Creative Commons "
        "license on one or two of the child's own originals - "
        "the child gets to see their work in the CC ecosystem "
        "(e.g., searching for their own handle on "
        "search.creativecommons.org once the work is indexed)."
    ),
    screen_time_guidance=(
        "This is a habit applied during existing screen time - "
        "specifically the time the child already spends publishing "
        "creative work. Adds roughly 15 seconds per publication "
        "(typing a credit line). Net screen-time cost: near-zero. "
        "Quarterly 5-min review of the 'sources named' running "
        "count can happen in existing family screen time."
    ),
    parental_controls_component=(
        "No technical parental control needed. The caregiver "
        "role is: (a) model the habit - when the caregiver "
        "shares an article, meme, or song to the family chat, "
        "they credit the source explicitly ('this New Yorker "
        "piece by [author] was wild'); (b) keep the "
        "conversation non-judgmental when the child forgets - "
        "'what's the source on this one?' without shame; (c) "
        "celebrate the first time the child's own work gets "
        "remixed with credit intact (validates the whole system). "
        "Complementary: if the child is on platforms with "
        "Content ID / automatic takedown (YouTube, TikTok), make "
        "sure they know those systems exist and why - a surprise "
        "takedown at age 14 without context can be devastating, "
        "so front-load the explanation."
    ),
    media_quality_rubric=(
        "GOOD: positive framing (remixing is GOOD, crediting is "
        "HOW); every remix credits at least one source; child "
        "picks a CC license for their own originals; caregiver "
        "models the habit; reputation + reciprocity framing "
        "(not just legal compliance). AVOID: framing remixing as "
        "legally risky (it's not, with proper credit in most "
        "cases, and fear-framing kills the creator impulse); "
        "pushing the child to use only public-domain / CC-BY "
        "assets (over-strict, misses how remix actually works); "
        "shaming past un-credited remixes (creates hiding "
        "behaviour); conflating attribution ethics with "
        "copyright law (they overlap but aren't identical); "
        "outsourcing the ethics to a school's 'academic integrity' "
        "system (misses the creator-community dimension entirely)."
    ),
    en_ca_content=(
        "**Remixing is how real creators work.** Every song is "
        "influenced by older songs. Every comic borrows from "
        "earlier comics. Every Minecraft mod stands on the "
        "shoulders of the mod before it. The question isn't "
        "whether to remix - it's how to do it as a real creator, "
        "not as a take-everything amateur.\n\n"
        "**The lifetime skill: name your sources.** Every time "
        "you publish a remix of someone else's thing, name that "
        "someone in the caption, description, or credits. That's "
        "it. Simple, fast, unglamorous, and the single practice "
        "that separates amateurs from actual creator-community "
        "members.\n\n"
        "**What counts as a remix?** A drawing based on a "
        "character someone else invented. A meme that uses a "
        "photo or clip made by someone else. A Roblox game that "
        "uses assets, sounds, or code from the Roblox Marketplace. "
        "A TikTok using a trending song. A fanfic set in someone "
        "else's world. Every one of those is a remix. Every one "
        "of those deserves a credit line.\n\n"
        "**The credit format.** Keep it easy: `Original [thing] "
        "by [creator name]; remix by [your handle].` If there are "
        "multiple sources, list them all. A Roblox game might "
        "have 5-8 credits. That's normal and good.\n\n"
        "**Creative Commons — how real creators say 'yes, remix "
        "me'.** CC is a set of free licenses. The simplest one "
        "is CC BY — 'anyone can use this for anything, as long "
        "as they name me'. Go to creativecommons.org/share-your-"
        "work/cclicenses and browse the options. When YOU post "
        "something original (a drawing, a story, a Roblox map, a "
        "tutorial), pick a CC license for it. That's how you "
        "join the creator ecosystem on the grown-up side.\n\n"
        "**Three reasons this matters:**\n\n"
        "1. **Your reputation.** Platforms (YouTube, TikTok, "
        "Roblox) and communities (AO3, DeviantArt, Reddit) "
        "notice uncredited remixes. One uncredited viral "
        "remix can flag your account. Credit is the cheap, easy "
        "fix that never gets you in trouble.\n\n"
        "**2. Legal stuff (briefly).** Copyright law mostly "
        "protects the creator of an original work. Naming them "
        "doesn't automatically make remix legal - fair use is a "
        "separate legal concept - but credit is the first "
        "signal that you're acting in good faith and is the "
        "single biggest factor in whether a creator contacts you "
        "nicely vs issues a takedown.\n\n"
        "**3. Your own work.** Once you've learned to credit "
        "others, you can set terms on your own originals ('CC "
        "BY: use my Roblox code if you credit me'). That's how "
        "you turn your work into a seed that other creators "
        "build on, and your name spreads.\n\n"
        "**Start small.** Look at the last 5 things you made "
        "online. Are all sources named? If not, add credit now - "
        "most platforms let you edit descriptions after posting. "
        "The habit builds in about three cycles. After that, "
        "credit-naming is as automatic as saying 'thanks' when "
        "someone passes the salt."
    ),
    fr_qc_content="",
    ar_description=(
        "Not applicable - the skill is a caption/description "
        "habit on existing platforms (Roblox, TikTok, YouTube, "
        "AO3). The platforms themselves are the tool; no AR "
        "layer would add value. A future Gamification-Element "
        "could include AR to visualize the creator-credit graph "
        "(who remixed from whom), but that's a separate skill."
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
