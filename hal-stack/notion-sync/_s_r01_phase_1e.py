"""S-R01-PHASE-1e — add 1 more DCC Kids Research DB row (DB 12 -> 13).

Fills the last open cell in the age x category grid:
  - 7-9 x Creative-Making.

After this sprint the grid is complete (4 ages x 5 categories = 20
cells, all covered). Remaining Phase-1 work shifts from 'fill the
grid' to 'add additional rows within already-covered cells' to reach
the 20+ total target.

Run once:   python _s_r01_phase_1e.py
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
    skill="Making something useful for someone else",
    category="Creative-Making",
    age_ranges=["7-9"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Art-Creation",
    learning_profile=["Standard", "ADHD", "Dyslexia", "Special-Needs"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Middle-childhood maker skill with prosocial audience. The child "
        "picks ONE specific person (their little brother, Grandma, a "
        "classmate, the family cat) and makes something that person would "
        "actually use, wear, read, or enjoy. The skill is distinct from "
        "the 4-6 'make first, then watch' skill by adding AUDIENCE "
        "awareness, and from later story/AI skills by being physical + "
        "gift-oriented. This lands squarely in Erikson's industry-vs-"
        "inferiority stage window where children are building a lifelong "
        "sense of competence by producing things that matter to real "
        "people around them."
    ),
    research_source=(
        "Erikson's Industry vs Inferiority stage (ages ~6-11). Primary "
        "clinical reference: StatPearls - NCBI Bookshelf - Erikson's "
        "Stages of Psychosocial Development (ncbi.nlm.nih.gov/books/"
        "NBK556096). Academic summary: Simply Psychology - Erikson's "
        "Stages of Development (simplypsychology.org/erik-erikson.html). "
        "Empirical operationalisation: Schonert-Reichl et al., PMC3790250 "
        "- 'Development and Validation of the Middle Years Development "
        "Instrument' (pmc.ncbi.nlm.nih.gov/articles/PMC3790250) - "
        "evidence that competence + connectedness in middle childhood "
        "predict well-being across domains. "
        "Harvard Project Zero - Making & Design (pz.harvard.edu/topics/"
        "making-design) and the Agency by Design framework: the concepts "
        "of 'maker empowerment' and 'sensitivity to design' map directly "
        "onto making-for-someone. Project Zero - Primary/Elementary "
        "School resources (pz.harvard.edu/topics/primary-elementary-"
        "school) include maker-centred learning curricula for the 6-10 "
        "range. "
        "NAEYC Preschoolers at Play (naeyc.org/resources/pubs/books/"
        "preschoolers-at-play) - guidance on open-ended purposeful play "
        "carries into early elementary with audience awareness added."
    ),
    threat_addressed=(
        "Default screen use at 7-9 puts the child in the perpetual "
        "audience role: watching other kids on YouTube, consuming "
        "algorithmically-recommended videos, competing on leaderboards. "
        "This is exactly the moment Erikson's framework predicts "
        "'inferiority' consolidates if the child cannot point to things "
        "they made that matter. Without a counter-balance, the child's "
        "maker-identity ('I make things for people') loses to their "
        "consumer-identity ('I am a fan of X'). That identity split "
        "compounds — 10-12 influencer-aspiration, 13-15 passive social-"
        "media use, adult under-agency around creative tools. Making-for-"
        "someone is the structural intervention at exactly the right "
        "developmental window."
    ),
    psychology_framework=(
        "Erikson's industry-vs-inferiority psychosocial stage (ages ~6-11): "
        "this window is where a child builds (or fails to build) the "
        "virtue of competence. Per StatPearls, the child needs tasks that "
        "are 'interesting, worthwhile, and accomplishable'. Making-for-"
        "someone hits all three. Theory-of-mind is mature enough at 7-9 "
        "for genuine audience-modelling ('what would Grandma actually "
        "like?'). Piaget's concrete-operational stage (7-11) supplies the "
        "planning capacity — the child can hold multi-step processes in "
        "mind. Harvard Project Zero's Agency by Design framework names "
        "the outcome as 'maker empowerment' - belief that one can change "
        "the designed world. Self-determination theory (Deci & Ryan): "
        "the skill satisfies all three basic needs - autonomy (child "
        "picks recipient + idea), competence (finishes + delivers), "
        "relatedness (connects to a specific person)."
    ),
    creator_luring_awareness=(
        "The parasocial pull of influencer content ('I wish I had that "
        "kid's room / toys / followers') depends on the child NOT having "
        "a robust producer-identity. When the child's week includes a "
        "real person saying 'you made this for me, thank you' about a "
        "thing the child made, the imaginary relationship with a "
        "youtuber competes against it on unfair terms. Not bulletproof "
        "- but a protective factor, and cheap to install. Parallel to "
        "the 4-6 'make first, then watch' skill: that one builds maker-"
        "posture; this one builds maker-identity with a name on it."
    ),
    example_activity=(
        "WEEKLY RITUAL (Sunday afternoon, 30-45 min, mostly off-screen). "
        "Step 1 (5 min): child names ONE person they want to make "
        "something for this week. Can be the same person multiple weeks "
        "in a row; variety is not the point. Step 2 (10 min): caregiver "
        "and child brainstorm 2-3 things that person might actually use "
        "or enjoy. The child decides which ONE to make. Step 3 (15-30 "
        "min): child makes it with materials on hand (cardstock, "
        "markers, fabric, glue, clay, etc.). The caregiver is nearby "
        "but does not drive. Step 4 (5 min): delivery. Child gives the "
        "thing to the person in whatever way feels right - handing it "
        "over, leaving it on their pillow, mailing it if the recipient "
        "is far. Step 5 (whenever, within a week): the 'did they use "
        "it?' check. If yes, a gold sticker goes on the made-for-"
        "someone wall next to a photo of the object; if no, the photo "
        "goes on the wall anyway with a silver sticker. Both count."
    ),
    gamification_element=(
        "Made-for-someone wall: photo of each object + name of recipient "
        "+ sticker (gold = recipient used it, silver = recipient liked "
        "it but didn't use it). The wall is visible, shared, and "
        "explicitly praised by multiple adults. The goal is NOT "
        "aesthetic quality (crushes risk-taking); it's a growing "
        "portfolio of 'I made things that mattered to specific people'. "
        "After 20 stickers, family does something the child chose. "
        "Important non-goals: no ranking ('which was the best?'), no "
        "competition with siblings' walls, no public posting to "
        "external platforms."
    ),
    screen_time_guidance=(
        "Mostly off-screen (the making + delivery + conversation). "
        "Optional on-screen step: after the object is made, the child "
        "may use a phone to take a photo for the wall. If the child "
        "asks to search online for 'how to make X for Grandma', "
        "caregiver can assist, but the child does not leave the screen "
        "until the physical making starts (consistent with the 4-6 "
        "'make first, watch second' foundation). Total on-screen time "
        "typically 0-10 min per weekly session."
    ),
    parental_controls_component=(
        "No new technical control required - this is a caregiver-routine "
        "skill. The caregiver commitments: (a) do not redirect the "
        "child's chosen recipient ('maybe make it for your cousin "
        "instead, cousin is coming over'); (b) do not improve the "
        "object mid-make (resist the urge to glue it properly for the "
        "child); (c) celebrate silver stickers as loudly as gold - the "
        "child delivering is the win, the recipient's response is "
        "outside the child's control; (d) ask every 4-6 weeks whether "
        "the wall needs a bigger spot - visible growth is the "
        "reinforcer. Complementary: if the child starts searching for "
        "how-to guides online, caregiver pre-vets the app (prefer "
        "Pinterest's SafeSearch mode or Common Sense Media vetted "
        "craft channels)."
    ),
    media_quality_rubric=(
        "GOOD: one specific recipient (not 'everyone'); child picks; "
        "30-45 min session; physical delivery; photo + sticker on the "
        "wall regardless of recipient reaction; caregiver celebrates "
        "silver (delivered) as much as gold (used). AVOID: caregiver "
        "choosing the recipient; caregiver improving the object; "
        "expecting the child to give the object away when it was "
        "obviously personal; hierarchy between gold and silver stickers; "
        "posting the object to social media without the child's "
        "consent; comparing to other kids' work; demanding a weekly "
        "delivery if the child isn't ready (forcing kills the "
        "identity benefit)."
    ),
    en_ca_content=(
        "**Every week, you're going to make something for one specific "
        "person.** Not 'everyone', not 'people who might like it' - ONE "
        "specific real person. Your little sister. Your grandma. Your "
        "soccer coach. The family cat.\n\n"
        "**Why for a specific person?** Because when you know WHO you're "
        "making something for, you think about what THAT person likes, "
        "what THEY would use, what makes THEM smile. That's called "
        "thinking about your audience, and it's a skill that real "
        "writers, designers, and inventors use their whole lives.\n\n"
        "**The five steps:**\n"
        "1. Say out loud who it's for this week.\n"
        "2. Talk with a grown-up about 2-3 things that person might "
        "actually use or enjoy.\n"
        "3. Pick one. Make it - cardboard, paper, markers, clay, "
        "fabric, whatever you have.\n"
        "4. Give it to the person. Don't wait.\n"
        "5. Take a photo for the Made-for-Someone Wall.\n\n"
        "**What if they don't use it?** That's OK. You still delivered "
        "it. You put thought into who they are, and you made a thing. "
        "That counts. Silver sticker goes on the wall. No sticker only "
        "if you didn't make or didn't deliver - the thing YOU control.\n\n"
        "**What if they really love it?** Even better. Gold sticker. "
        "But silver stickers matter just as much, because you can't "
        "control whether someone loves something - you can only control "
        "whether you make it and give it.\n\n"
        "**Important:** this isn't homework. This isn't a competition. "
        "It's the habit of being someone who makes things for specific "
        "people they care about. Kids who grow up with that habit turn "
        "into adults who build things that matter."
    ),
    fr_qc_content="",
    ar_description=(
        "Not applicable - the core is physical craft for a physical "
        "recipient. An AR layer would pull the skill toward screen-"
        "mediated creativity and away from the tactile-object, real-"
        "human-reaction core that makes it work developmentally. "
        "The only screen element is the optional photo for the wall."
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
