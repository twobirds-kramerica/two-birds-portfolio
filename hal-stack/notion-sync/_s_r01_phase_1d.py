"""S-R01-PHASE-1d — add 2 more DCC Kids Research DB rows (DB 10 -> 12).

Fills the next two coverage gaps after S-R01-PHASE-1c (152c2a5):
  - 4-6 x Creative-Making (no row yet)
  - 13-15 x Tech-Safety   (no row yet)

Citations verified via WebSearch during composition; no fabricated
sources. Sources lean on peer-reviewed, government, and established
educational publishers (Scholastic, NAEYC, CISA, NIST, Common Sense
Education).

Run once:   python _s_r01_phase_1d.py
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
# Row 1: 4-6 x Creative-Making — "Making my own thing first, then watching"
# ===========================================================================
ROW_1 = dict(
    skill="Making my own thing first, then watching other people's",
    category="Creative-Making",
    age_ranges=["4-6"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Art-Creation",
    learning_profile=["Standard", "ADHD", "Dyslexia", "Special-Needs"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Foundational creator-mindset skill for preschool and kindergarten. "
        "Before a child watches someone else's version of a thing (a YouTube "
        "craft tutorial, an AI-generated story, an 'unboxing' video of a toy), "
        "they make their own version of a similar thing first — with whatever "
        "is available — then compare. The skill explicitly inverts the "
        "default-consumer posture of most apps: child is the maker, the "
        "screen is a reference. This age is the peak creativity window and "
        "the foundation for all later maker / critic / author skills."
    ),
    research_source=(
        "Scholastic — Creative Development in 3-5 Year Olds "
        "(scholastic.com/parents/family-life/creativity-and-critical-"
        "thinking/development-milestones/creative-development-3-5-year-"
        "olds.html): 'children begin to create with intention — purposefully "
        "drawing a monster or a flower — and by age 5 many add details and "
        "narrated stories'. NAEYC — Preschoolers at Play: Choosing the Right "
        "Stuff for Learning and Development (naeyc.org/resources/pubs/books/"
        "preschoolers-at-play): guidance on open-ended materials vs closed-"
        "ended consumption. Bright Horizons — Nurturing Creativity & "
        "Imagination for Child Development (brighthorizons.com/resources/"
        "article/nurturing-creativity-and-imagination-for-child-development): "
        "the well-established finding that creativity peaks before age 6 and "
        "declines with the onset of formal schooling and conformity pressure. "
        "Raising Children Network (Australia, an Australian Government-funded "
        "parenting resource) — Creative play & activities: preschoolers "
        "(raisingchildren.net.au/preschoolers/development/creative-"
        "development/preschooler-creative-activities). PMC9590021 — "
        "'Developing Children's Creativity and Social-Emotional Competencies "
        "through Play: Summary of Twenty Years of the Game Program' — "
        "evidence base for structured creative play intervention in early "
        "childhood."
    ),
    threat_addressed=(
        "Apps marketed to preschoolers default them into passive viewing: "
        "short-video feeds, AI-read picture books, 'craft tutorial' videos "
        "the kid watches but does not do. Over months, this rewires the "
        "default response to a screen from 'what can I make?' to 'what is "
        "going to happen next?'. Creativity research (peak at age 5-6, "
        "decline after) suggests this rewiring is cumulative and hard to "
        "undo at 10-12. Without a make-first habit, all later Creative-"
        "Making skills (story-making, art-creation, remix) compete against "
        "a child who has learned watching is easier than making."
    ),
    psychology_framework=(
        "Piaget's preoperational stage (2-7, intuitive thought sub-stage "
        "4-7). Children at this age engage in high-intensity symbolic play "
        "— blocks become castles, a spoon becomes a spaceship. The skill "
        "leverages this natural symbolic substitution by scheduling it "
        "BEFORE screen exposure, not instead of it. Complements Vygotskian "
        "scaffolding: the caregiver sets up materials and provides a prompt "
        "('make a pet that has never been invented before'), then steps "
        "back. Connects to divergent-thinking research (Torrance tests of "
        "creative thinking, 1966 onwards) — divergent thinking peaks in "
        "early childhood then declines; structured make-first practice "
        "appears to slow that decline."
    ),
    creator_luring_awareness=(
        "Influencer kids and 'toy unboxing' channels target preschoolers "
        "specifically; the business model depends on preschoolers watching, "
        "not making. A child who spends 20 minutes making a cardboard "
        "spaceship before watching a 3-minute unboxing video has very "
        "different relationship with the video (it's a reference, not an "
        "authority). Early maker-identity forms resistance to the parasocial "
        "'I want to be THAT kid' dynamic that drives later influencer-"
        "targeting. Not bullet-proof — just harder to hook."
    ),
    example_activity=(
        "WEEKLY RITUAL (20 min, off-screen, before any screen session). "
        "Caregiver puts out 5-7 open-ended everyday materials on a low "
        "table: empty cardboard tubes, scrap paper, a glue stick, tape, "
        "markers, fabric scraps, an empty yogurt container. Caregiver "
        "gives ONE prompt and steps back: e.g., 'make a pet that has "
        "never been invented before.' Variations by week: 'make something "
        "that helps someone else,' 'make a thing that does something when "
        "the wind blows,' 'make a whole family of tiny somethings.' The "
        "child makes for 15-20 minutes. Caregiver photographs the result. "
        "ONLY AFTER THE CHILD IS DONE: they can watch a short (max 5 min) "
        "kid-appropriate video of someone else making something in the "
        "same category. The comparison conversation is the whole point: "
        "'what's the same?' 'what's different?' 'who's older, the "
        "youtuber's thing or yours?'"
    ),
    gamification_element=(
        "A physical 'maker wall' (corkboard or kitchen cabinet) where "
        "photos of the week's creations go. Each week adds one photo; "
        "by month 3 the wall tells a visual story of growing maker "
        "confidence. The gamified goal is NOT quality — it's quantity-of-"
        "makes. 12 makes by month 3, 26 by month 6. The wall is visible "
        "to the kid's grandparents and visitors; praise from multiple "
        "adults reinforces maker identity, which research ('growth "
        "mindset' literature) shows is critical at this age."
    ),
    screen_time_guidance=(
        "Hard rule: make first, watch second. If the child asks to watch "
        "a screen-based craft/art video, the caregiver says 'sure — but "
        "first we make our own thing.' The child cannot skip to the video. "
        "Never punitive; reframe as 'you're the chef of this meal, you "
        "cook it before you see the cookbook.' AAP screen-time "
        "recommendations (ages 2-5: 1 hour per day max, co-viewed) set "
        "the upper bound; this skill sets the STRUCTURE of whatever "
        "screen-time is used."
    ),
    parental_controls_component=(
        "No technical parental control is the mechanism here — the "
        "mechanism is a routine the caregiver keeps. Complementary "
        "technical controls: block autoplay on YouTube Kids / Prime Video; "
        "prefer YouTube Kids playlists the caregiver has pre-vetted; "
        "avoid any app that surfaces 'up next' recommendations on the "
        "child's screen. Raising Children Network and Common Sense Media "
        "both maintain curated app lists for this age range; caregiver "
        "checks quarterly because app quality drifts."
    ),
    media_quality_rubric=(
        "GOOD: 15-20 min of making before ANY screen-watching; one simple "
        "prompt; open-ended materials; caregiver steps back; photographs "
        "the result; comparison conversation afterwards; no quality "
        "judgement of the child's work. AVOID: handing the child a "
        "Pinterest template to 'be creative'; praising only pretty "
        "results (kills risk-taking); skipping the make step when the "
        "child protests (teaches the child resistance works); 'supervised' "
        "craft time that is really caregiver-made with child's hands; "
        "comparing the child's output unfavourably to the video's."
    ),
    en_ca_content=(
        "**You are a MAKER.** Before you watch other people make things "
        "on a screen, you make your own thing first. That's the rule. "
        "**Why?** Because the first person who makes something about a "
        "topic gets to be the inventor. The inventor thinks the hardest "
        "and has the most fun. After you invent yours, you can look at "
        "other people's versions on a screen — and compare them to yours. "
        "**What if my thing looks different?** GOOD. Different is the "
        "whole point. If everyone's rocket looked the same, nobody would "
        "have invented a new kind of rocket ever. **What if my thing is "
        "messy?** Also GOOD. Messy means you really made it, not copied "
        "it. **Who will see my thing?** Whoever you want — mom, dad, "
        "grandma, the fridge. You could even put a photo on the MAKER "
        "WALL. **Most important:** when you sit down at a screen, you're "
        "already a maker. The screen is showing you other makers. You're "
        "not a watcher. You're a maker who is also, sometimes, watching."
    ),
    fr_qc_content="",
    ar_description=(
        "Not applicable — the core of this skill is hands-on physical "
        "material. An AR 'make a pet that doesn't exist' app could "
        "theoretically complement, but would dilute the tactile-materials "
        "foundation that research associates with creativity development. "
        "Photograph-to-maker-wall step is the documentation technology; "
        "no AR layer needed."
    ),
)


# ===========================================================================
# Row 2: 13-15 x Tech-Safety — "Turning on two-factor auth on the
# accounts I care about"
# ===========================================================================
ROW_2 = dict(
    skill="Turning on two-factor authentication on the accounts I care about",
    category="Tech-Safety",
    age_ranges=["13-15"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Multi-Modal",
    learning_profile=["Standard", "ADHD", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Teen practitioner-level tech-safety skill. Teen identifies which "
        "of their accounts are 'the ones I care about' (usually: primary "
        "email, school LMS, social with DMs, gaming store with payment "
        "attached, any account linked to the family plan), then turns on "
        "two-factor authentication (2FA / MFA) on each. The skill is "
        "explicit that 2FA is not 'for paranoid adults' — it is the "
        "minimum standard named by CISA and NIST, and teens are actively "
        "targeted for account takeover because their accounts often hold "
        "payment instruments but have weaker defences than adult accounts."
    ),
    research_source=(
        "CISA — Require Multifactor Authentication "
        "(cisa.gov/secure-our-world/require-multifactor-authentication): "
        "'Multifactor authentication is the best way to prevent somebody "
        "else from accessing your online accounts' — the US Government's "
        "cybersecurity agency position. CISA — Cyber Safety for Teens "
        "(niccs.cisa.gov/training/catalog/ncsta/cyber-safety-teens): "
        "free teen-targeted course covering 2FA + account hygiene. NIST "
        "Special Publication 800-63B — Digital Identity Guidelines "
        "(csrc.nist.gov): sets 2FA/MFA as the baseline authenticator "
        "assurance level for any account with sensitive data. CISA's "
        "accompanying 'Simple Tips to Secure It' MFA how-to guide "
        "(niccs.cisa.gov/sites/default/files/documents/pdf/ncsam_"
        "howtoguidemfa_508.pdf). Common Sense Education — Privacy & "
        "Security digital citizenship curriculum for middle/high school "
        "(commonsense.org/education/digital-citizenship/topic/privacy-"
        "and-safety) covers 2FA, password managers, and terms of service "
        "evaluation in middle-school units. Trend Micro Internet Safety "
        "for Kids — What is 2FA (trendmicro.com/internet-safety/for-kids/"
        "cyber-academy/what-is-two-factor-authentication) — age-appropriate "
        "explainer framing."
    ),
    threat_addressed=(
        "Account takeover (ATO) — a stolen password alone lets an attacker "
        "into the account; 2FA makes the password much less valuable "
        "alone. Teens are disproportionately targeted: their accounts "
        "frequently have saved payment methods (gaming skins, "
        "subscriptions), are linked to parents' payment cards, and teens "
        "typically reuse passwords across services. Also mitigated: "
        "SIM-swap-style takeover of email-connected phones, credential "
        "stuffing from breach databases, and targeted social-engineering "
        "attacks by peers or ex-relationships."
    ),
    psychology_framework=(
        "Piaget's formal-operational stage (11+): teens can reason "
        "abstractly about systems ('if my password leaks, anyone can "
        "read my messages'). This skill matches that capacity — it's not "
        "a rote-procedure task but a small threat-modelling exercise. "
        "Erikson's identity-vs-role-confusion stage (12-18): teens are "
        "actively consolidating an identity, and 'I am a person who "
        "secures my accounts' is a pro-social identity marker. Self-"
        "determination theory (Deci & Ryan): the skill emphasises autonomy "
        "(teen picks which accounts matter), competence (concrete, "
        "achievable), and relatedness (family-level habit)."
    ),
    creator_luring_awareness=(
        "Account takeover is how many luring + sextortion campaigns start: "
        "attacker breaks into one of the teen's accounts, uses DM history "
        "to craft convincing messages, then contacts the teen's contacts "
        "from that account. 2FA on the primary DM-carrying accounts "
        "breaks this pipeline before any conversation begins. Even better "
        "— a teen who has 2FA on their email can recover any other "
        "account they later lose, limiting the blast radius of any single "
        "compromise."
    ),
    example_activity=(
        "SESSION 1 (30 min, family time): teen sits with caregiver and "
        "lists every account they can think of on paper — not on a device. "
        "Mark each with a star if it's 'one I care about' (email, school, "
        "primary social, anything with payment). Usually 3-7 accounts. "
        "SESSION 2 (45 min, same day or next): for each starred account, "
        "teen goes to account settings > security > turn on 2FA. Prefer "
        "authenticator app (Aegis, Google Authenticator, 1Password) over "
        "SMS per NIST guidance (SIM swaps make SMS weaker). Generate "
        "backup codes; write them in a physical notebook the teen keeps "
        "where they keep their passport. Test one 2FA code with caregiver "
        "watching. Log every account in a shared family notepad: account "
        "name / 2FA method / date turned on. This makes 2FA visible as "
        "an adult skill the teen has achieved."
    ),
    gamification_element=(
        "Friends-and-family 2FA audit day. Once per quarter, teen earns "
        "one 'security consultant' credit for: (a) walking a parent or "
        "grandparent through turning on 2FA on one of THEIR accounts, or "
        "(b) checking their own accounts still have 2FA active. Credits "
        "cash in for shared activities chosen by the teen. Reframes 2FA "
        "as teen-teaching-adult rather than adult-enforcing-rule. Aligns "
        "with Erikson identity formation ('I'm the family's security "
        "person') and self-determination theory (competence + autonomy)."
    ),
    screen_time_guidance=(
        "The skill is inherently on-screen (it is configured through "
        "account settings). Setup takes 30-90 min total for a typical "
        "teen; after that, the skill imposes ~5 seconds of friction per "
        "login. Quarterly 10-min audit to review which accounts still "
        "exist and still need 2FA. Does not displace other screen time; "
        "is itself productive screen time that reduces future screen-"
        "time risk (a hijacked account is hours of remediation)."
    ),
    parental_controls_component=(
        "This is a teen-owned skill, not a parental control. The caregiver "
        "role is: (a) co-sit the first session; (b) not handle the teen's "
        "passwords or 2FA codes themselves; (c) keep the shared family "
        "notepad so 2FA status is legible; (d) model the same habit on "
        "the caregiver's own primary accounts (teen watches). Technical "
        "supports: password manager (1Password, Bitwarden, Apple Keychain) "
        "is strongly recommended as a pre-requisite — trying to maintain "
        "unique strong passwords without one is unrealistic for teens. "
        "CISA explicitly recommends password managers alongside 2FA."
    ),
    media_quality_rubric=(
        "GOOD: teen picks which accounts are 'ones I care about'; "
        "authenticator app preferred over SMS; backup codes written "
        "physically and stored with passport/birth-cert; family notepad "
        "tracks which accounts have 2FA on; quarterly audit; caregiver "
        "models the same habit. AVOID: forcing the teen to turn on 2FA "
        "on accounts they don't consider 'theirs' (breaks autonomy); "
        "relying on SMS-only 2FA for anything sensitive (SIM-swap "
        "vulnerable — NIST deprecated SMS for high-assurance in SP "
        "800-63B); caregiver knowing or holding the teen's codes "
        "(defeats the purpose); presenting 2FA as punishment or surveillance."
    ),
    en_ca_content=(
        "**Two-factor authentication (2FA) is the single highest-impact "
        "cyber security thing you can do.** It's what CISA (the US "
        "Government's cyber security agency) and NIST (the people who "
        "write the actual rules) both name as the minimum standard. "
        "Adults who skip it are taking a known, preventable risk.\n\n"
        "**How it works:** A password alone is 'something you know'. "
        "Someone else can steal that. 2FA adds 'something you have' — "
        "usually your phone running an authenticator app — so a stolen "
        "password alone isn't enough. Attackers would need your phone "
        "too, which is much, much harder.\n\n"
        "**Which accounts matter?** Not all of them. Pick the ones that "
        "would hurt to lose: (1) your primary email — because password "
        "resets for everything else go there; (2) any account with a "
        "payment method saved; (3) your main social/DM account — because "
        "a stolen DM history is ammunition for scams; (4) school "
        "platform if it has your marks; (5) gaming store if you have "
        "skins/items. 3-7 accounts for a typical teen.\n\n"
        "**Use an authenticator app, not SMS.** Apps like Aegis, Google "
        "Authenticator, 1Password generate 6-digit codes that rotate "
        "every 30 seconds. SMS codes can be intercepted via SIM-swap "
        "attacks — NIST specifically deprecated SMS for high-security "
        "use.\n\n"
        "**Backup codes — write them on paper.** Every 2FA setup gives "
        "you 8-10 one-time backup codes. Write them in a notebook you "
        "keep with your passport. If you lose your phone, these codes "
        "get you back in.\n\n"
        "**It takes one Sunday afternoon.** 30-90 minutes for a typical "
        "teen. After that, it's ~5 seconds of friction per login. "
        "Compare to the days it takes to recover a hijacked account.\n\n"
        "**Bonus:** Once you have 2FA on your own accounts, you're the "
        "family security consultant. Walk your grandparent through their "
        "email 2FA. That's a real skill."
    ),
    fr_qc_content="",
    ar_description=(
        "Not applicable. The skill is a workflow executed through account "
        "settings screens, not a spatial/visual activity. The authenticator "
        "app itself is the only tool-mediation — no AR layer would add "
        "pedagogical value."
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
