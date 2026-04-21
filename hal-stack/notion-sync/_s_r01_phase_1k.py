"""S-R01-PHASE-1k — 7-9 Tech-Safety: pause-and-show when an app asks.

2nd row in 7-9 x Tech-Safety cell. Completes the Tech-Safety ladder
across ages, each matched to developmental capability:
  4-6   'Secret stuff and share stuff'              (foundational distinction)
  7-9   'Pause and show when an app asks'           ← THIS ROW
  10-12 'Using a password manager'                  (1g)
  13-15 'Turning on two-factor authentication'      (1d)

The 7-9 skill lands exactly when kids typically get their first
personal tablet / app-store account / Minecraft-or-Roblox login.

Run once:   python _s_r01_phase_1k.py
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
    skill="Pause and show a grown-up whenever an app asks for something",
    category="Tech-Safety",
    age_ranges=["7-9"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Show-and-Tell",
    learning_profile=["Standard", "ADHD", "Dyslexia", "Special-Needs"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Practitioner-level tech-safety skill for the age when kids "
        "typically get their first personal tablet, app-store account, "
        "or Minecraft/Roblox login. One rule, memorised cold: when ANY "
        "app asks for camera, microphone, location, contacts, photos, "
        "notifications, or tracking — PAUSE and SHOW a grown-up BEFORE "
        "tapping. The child is not expected to know which permissions "
        "are safe; they are expected to know that permissions are a "
        "class of thing that always gets an adult eye first. Over "
        "months the child develops an intuition; meanwhile the "
        "immediate-request bypass is eliminated."
    ),
    research_source=(
        "Federal Trade Commission (USA) — Children's Online Privacy "
        "Protection Rule (ftc.gov/legal-library/browse/rules/childrens-"
        "online-privacy-protection-rule-coppa): the baseline US "
        "regulation — apps directed to children under 13 must obtain "
        "verifiable parental consent before collecting personal "
        "information. Widely adopted by industry globally including "
        "apps available in Canada. FTC — Complying with COPPA: "
        "FAQs (ftc.gov/business-guidance/resources/complying-coppa-"
        "frequently-asked-questions). Federal Register — COPPA Rule "
        "2024 update (federalregister.gov/documents/2024/01/11/"
        "2023-28569/childrens-online-privacy-protection-rule). "
        "Common Sense Education — What Is COPPA "
        "(commonsense.org/education/articles/what-is-coppa): "
        "teacher-facing plain-language summary. "
        "Common Sense Media — 'Improving COPPA: A Road Map for "
        "Protecting Kids' Privacy' "
        "(commonsensemedia.org/kids-action/articles/improving-coppa-"
        "a-road-map-for-protecting-kids-privacy-in-2020-and-beyond). "
        "Apple App Store Kids Category requirements: apps made for "
        "kids must target ages 5-under / 6-8 / 9-11 and follow "
        "strict privacy rules — aligns with the 7-9 window of this "
        "skill. Google Play Families policy enforces equivalent "
        "requirements. "
        "MediaSmarts Canada — Managing media in middle childhood "
        "(mediasmarts.ca/teacher-resources/managing-media-middle-"
        "childhood-6-9-years-old) - Canadian-context guidance for "
        "ages 6-9. "
        "Canadian context: Personal Information Protection and "
        "Electronic Documents Act (PIPEDA) applies commercial "
        "activity nationally; Office of the Privacy Commissioner "
        "of Canada (priv.gc.ca) publishes age-specific guidance."
    ),
    threat_addressed=(
        "Three interlocking threats this skill closes: "
        "(1) DATA HARVESTING - apps built for kids often collect "
        "contacts / location / photos / browsing history well beyond "
        "what the app's core function requires. Even COPPA-compliant "
        "apps commonly push the default permission sets as 'yes to "
        "everything' on first launch. A 7-9-year-old hitting 'Allow' "
        "on every modal unlocks the full harvesting stack in minutes. "
        "(2) IN-APP CONTACT VECTORS - camera + microphone + location "
        "permissions are precisely the ones that enable unsolicited "
        "contact (video-chat features, voice-chat, location-based "
        "matching) in games marketed to this age group. The 10-12 "
        "grooming row and the 13-15 sextortion row both depend on "
        "the child NOT having granted those permissions accidentally "
        "at 7. "
        "(3) NOTIFICATION EXPLOITATION - push notifications at this "
        "age are the dominant re-engagement hook for addictive apps. "
        "Even a 'Notifications: Allow' tap at age 7 commits the "
        "child to months of engineered interruptions. Pause-and-"
        "show catches all three before the damage is locked in."
    ),
    psychology_framework=(
        "Piaget's concrete-operational stage (7-11): children at this "
        "age can reliably follow a simple conditional rule ('IF an app "
        "asks for something THEN I pause and show') but cannot yet "
        "reason abstractly about what 'location tracking' or 'data "
        "harvesting' means. The skill explicitly does NOT require "
        "abstract understanding; it requires ONE concrete "
        "conditional. Vygotsky's zone of proximal development: the "
        "grown-up IS the scaffold that lets the child engage safely "
        "with a system they can't yet evaluate alone. Over months, "
        "as the child sees the adult's reasoning repeated ('this one's "
        "camera — yes because it's a drawing app; this one's "
        "location — no because it's just a game'), the child "
        "internalises the decision framework and exits the "
        "scaffolding stage around 9-10. Kohlberg's pre-conventional "
        "to conventional transition (around 7-9): the rule works "
        "BECAUSE it is the family's rule, then later works because "
        "the child has internalised the reasoning. Both stages are "
        "served."
    ),
    creator_luring_awareness=(
        "Direct link to the 10-12 grooming row and the 13-15 "
        "sextortion row. Groomers in games and messaging apps "
        "exploit the three permission vectors most: camera (for "
        "requested selfies + later-used compromising images), "
        "microphone (for voice-chat-to-private-chat escalation), "
        "and location (for proximity-based 'we're near each other' "
        "openers). A child who habitually PAUSES on every "
        "permission modal until age 9-10 does not accidentally "
        "open those vectors at 7. By the time they DO grant such "
        "permissions (often for legitimate family video calls, "
        "etc.), they are old enough to pair the permission with "
        "the grown-up-awareness context. Complements the "
        "grooming-specific skills without trying to teach 7-9-"
        "year-olds about grooming directly (developmentally "
        "misplaced)."
    ),
    example_activity=(
        "SESSION 1 - INSTALL THE RULE (15 min, family time). "
        "Caregiver sits with child when ANY new app is installed "
        "on the child's device. For the first 10-15 apps, "
        "caregiver reads every permission modal aloud and models "
        "the yes/no decision ('camera - yes, it's a drawing app'; "
        "'location - no, a game doesn't need our location'; "
        "'notifications - no, we don't need pings from this'). "
        "Child says 'pause and show' OUT LOUD every time a modal "
        "appears. The verbal step cements the habit. "
        "SESSION 2 - ROLE-REVERSAL (5 min, after 10-15 apps). "
        "Caregiver pretends to be the child and asks 'what "
        "should I do?' for each modal. Child now leads the "
        "pause-and-show decision. Caregiver provides confirmation "
        "or correction. "
        "ONGOING HABIT (lifetime property). Child brings the "
        "device to a grown-up any time a permission modal "
        "appears, even mid-game. Grown-up provides a decision "
        "in 15 seconds. No punishment if the child forgot and "
        "tapped — the caregiver goes into the OS settings and "
        "revokes the permission together (teaches the child "
        "that permissions are reversible, not a one-way trap). "
        "WEEKLY 5-MIN REVIEW. Family checks Settings > Privacy "
        "on the child's device and reviews which apps currently "
        "have camera / microphone / location / contacts. Revoke "
        "anything that feels excessive. Child watches the "
        "review; caregiver narrates the reasoning."
    ),
    gamification_element=(
        "The 'caught one' stickers for permission modals WHERE "
        "THE CHILD PAUSED AND SHOWED. Not for saying no — "
        "sometimes yes is correct. For NOTICING. One sticker per "
        "pause-and-show event the caregiver observed. After 30 "
        "stickers, the child has clearly internalised the habit "
        "and gets a family celebration (their pick). The weekly "
        "settings-review also yields stickers: one per revoked "
        "permission the child helped identify as excessive."
    ),
    screen_time_guidance=(
        "The skill applies during existing screen time (app "
        "installation + first-run setup of any new app). Adds "
        "roughly 30-60 seconds per app for pause-and-show. "
        "Over time this decreases as the child pre-internalises "
        "common patterns. Weekly 5-min settings review is the "
        "only new screen-time allocation. Net cost: negligible; "
        "benefit: avoided harvest that would otherwise be "
        "permanent. AAP media guidance for ages 6-12 supports "
        "co-viewing and co-setup as the default caregiver "
        "posture; this skill operationalises that."
    ),
    parental_controls_component=(
        "Device-level parental controls are the ESSENTIAL "
        "complement here — not because they replace the skill "
        "but because they make the skill workable: "
        "(a) iOS Screen Time > Content & Privacy Restrictions > "
        "'Allow Apps' with 'Don't Allow Changes' on Location "
        "Services, Camera, Microphone etc. so the child CAN "
        "pause-and-show without accidentally tapping through. "
        "(b) Android Family Link equivalent: 'App permissions "
        "approval required'. "
        "(c) 'Ask to Buy' on both OSes so every purchase is "
        "reviewed before it completes. "
        "(d) Google Family Link + Apple Family Sharing to "
        "centralise the caregiver's approval queue. "
        "Crucially, the caregiver's approval latency should be "
        "SHORT (under 60 seconds when physically co-located). "
        "Long latency trains the child to bypass the system "
        "through workarounds, which defeats the skill. If the "
        "caregiver is unavailable, the child waits — a queued "
        "'pending' state is the right default."
    ),
    media_quality_rubric=(
        "GOOD: caregiver reads every permission modal aloud for "
        "the first 10-15 apps; child says 'pause and show' "
        "verbally; device-level restrictions block silent grant-"
        "all; no punishment for forgetting and tapping (revoke "
        "together instead); weekly settings review; stickers "
        "for noticing (not just for saying no); caregiver "
        "narrates the reasoning for yes/no decisions. "
        "AVOID: reflexive 'always no to everything' (teaches "
        "learned helplessness rather than judgement — some "
        "yeses are correct); shame for a tap-through (makes "
        "the child hide future modals); long caregiver-approval "
        "latency (child invents workarounds); outsourcing the "
        "skill entirely to technical controls (leaves the child "
        "without any intuition for when to pause on a new OS "
        "or device they don't have parental controls on); "
        "forcing the child to read and decide independently at "
        "7-9 (developmentally premature)."
    ),
    en_ca_content=(
        "**One rule.** When any app asks for something — camera, "
        "microphone, location, contacts, photos, notifications, "
        "or anything else — you PAUSE and SHOW a grown-up before "
        "tapping Allow or Don't Allow. That's it. The whole "
        "skill.\n\n"
        "**You don't have to know what's OK and what's not.** "
        "That's what grown-ups are for. Your job is to catch the "
        "question before it gets answered. Grown-ups will help you "
        "decide, and over time you'll learn why certain things are "
        "OK (camera for a drawing app) and why certain things are "
        "not (location for a game that isn't about where you are).\n\n"
        "**Why it matters.** Apps that are made for kids your age "
        "have to follow special rules — in the United States they're "
        "called COPPA, in Canada there's a similar set of rules. "
        "But many apps push the first permission pop-up to say YES "
        "to everything by default. When you're looking at a brand-"
        "new game and excited to play, a 7- or 8-year-old's brain "
        "wants to tap through. That's normal. PAUSE-AND-SHOW is "
        "the override.\n\n"
        "**How to do it:** Say out loud 'pause and show' when you "
        "see the pop-up. Bring the device to a grown-up. The grown-"
        "up takes 15 seconds to read and helps you decide. Tap. "
        "Done. Continue playing.\n\n"
        "**If you mess up.** Sometimes you'll tap before you "
        "remember. That's OK. You are NOT in trouble. Bring the "
        "device to a grown-up and say 'I forgot'. Together you "
        "go to Settings and TAKE BACK the permission. Every "
        "permission can be taken back. Nothing is permanent.\n\n"
        "**The weekly check.** Once a week, you + a grown-up "
        "look at the Privacy page in Settings and see which apps "
        "have camera, microphone, location, or contacts. "
        "Anything that looks weird — a game that shouldn't need "
        "your camera, for example — gets its permission taken "
        "away. This teaches you that permissions are a list you "
        "can manage, not a set of decisions you can't change.\n\n"
        "**The four permissions that matter most:**\n"
        "- **Camera** — can see what you're looking at\n"
        "- **Microphone** — can hear what you say\n"
        "- **Location** — knows where you are\n"
        "- **Contacts** — knows who's in your address book\n"
        "These four are the most valuable things your device knows "
        "about you. Always pause on these. Other permissions "
        "(notifications, photos, Bluetooth) are important too but "
        "these four are the most consequential.\n\n"
        "**As you get older.** When you're 10, you'll know why "
        "most of these decisions go the way they do, and you'll "
        "start making some of them yourself. You'll still pause — "
        "grown-ups pause too. But you'll lead the decision instead "
        "of handing it over. That's the plan. PAUSE-AND-SHOW now; "
        "PAUSE-AND-DECIDE later."
    ),
    fr_qc_content="",
    ar_description=(
        "Not applicable. Permission modals are a built-in OS "
        "feature; any AR layer would add friction at the exact "
        "moment the skill wants friction removed (grab device, "
        "bring to adult). The device itself is the tool; the "
        "weekly settings review is the secondary interface."
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
