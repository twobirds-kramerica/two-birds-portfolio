"""S-R01-PHASE-1g — 10-12 Tech-Safety: password-manager setup.

Adds a 2nd row in the 10-12 Tech-Safety cell. Pairs directly with
the 13-15 '2FA on accounts I care about' row shipped in 1d — the
password manager is the prerequisite that makes per-account unique
strong passwords + 2FA actually achievable at teen scale.

Run once:   python _s_r01_phase_1g.py
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
    skill="Using a password manager so every account gets its own password",
    category="Tech-Safety",
    age_ranges=["10-12"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Show-and-Tell",
    learning_profile=["Standard", "ADHD", "Dyslexia", "Special-Needs"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Pre-teen practitioner skill. Child installs a family-plan "
        "password manager (typically Bitwarden or 1Password family) "
        "on their own device, creates a memorable master password, "
        "and from that day forward lets the app generate + autofill "
        "every new account password. The skill explicitly replaces the "
        "childhood default ('remember one or two passwords and reuse "
        "them') with the practitioner default ('let the tool hold 50+ "
        "unique strong passwords; only remember the master'). Direct "
        "prerequisite for the 13-15 2FA skill (S-R01 row 'Turning on "
        "two-factor authentication') — 2FA is only sustainable if the "
        "passwords themselves are unique."
    ),
    research_source=(
        "CISA — Require Strong Passwords (cisa.gov/audiences/small-"
        "and-medium-businesses/secure-your-business/require-strong-"
        "passwords): official US cybersecurity agency position that "
        "password managers 'play a critical role in enabling people "
        "to create, manage, and use custom, unique, and strong "
        "passwords'. CISA training resource — 'Use a Password Manager "
        "to Create and Remember Strong Passwords' (cisa.gov/resources-"
        "tools/training/cyb3rsmrt-use-password-manager-create-and-"
        "remember-strong-passwords). NIST SP 800-63B Digital Identity "
        "Guidelines (csrc.nist.gov) — sets the technical requirements "
        "for memorised secrets and explicitly permits password "
        "managers as the practical path to meeting them. Bitwarden "
        "Families plan documentation (bitwarden.com/products/families) "
        "— up to 6 family members, shared collections, open-source, "
        "free personal tier. Bitwarden blog — 'Parenting with a "
        "password manager' (bitwarden.com/blog/parenting-with-a-"
        "password-manager) covers the exact pre-teen onboarding "
        "pattern this skill teaches. 1Password families reference "
        "(1password.com) — competitor with stronger UX, paid-only, "
        "up to 5 family members at ~CA$5/mo. Common Sense Education "
        "Privacy & Security curriculum "
        "(commonsense.org/education/digital-citizenship/topic/"
        "privacy-and-safety) covers password hygiene at the middle-"
        "school level."
    ),
    threat_addressed=(
        "Credential reuse. A 10-12-year-old typically has 5-20 "
        "accounts (school LMS, family streaming profiles, gaming "
        "platforms, kid-targeted apps, social preliminaries like "
        "Roblox / Discord). Without a password manager the "
        "developmentally-realistic pattern is 1-2 memorable "
        "passwords reused everywhere. A single breach on any one "
        "service then unlocks every other service via credential "
        "stuffing. This is how most teen account takeovers happen: "
        "not sophisticated attacks, just reuse + leaked breach "
        "lists. Installing a password manager at 10-12 breaks the "
        "pattern before the account count explodes at 13-15 when "
        "social platforms enter the mix."
    ),
    psychology_framework=(
        "Piaget's late concrete-operational / early formal-"
        "operational transition (10-12): the child can follow a "
        "multi-step workflow reliably and is starting to reason "
        "about systems abstractly. A password manager is exactly "
        "this cognitive level — concrete workflow (click extension, "
        "click generate, click autofill) with an abstract security "
        "model (one master vs many unique) that the child is "
        "cognitively ready to hold in mind. Self-determination "
        "theory (Deci & Ryan): the skill emphasises competence "
        "('I can handle this grown-up tool') and autonomy ('I hold "
        "my own master password'). Erikson's late industry-vs-"
        "inferiority stage: adopting an adult-grade tool is a "
        "concrete competency win at exactly the age where children "
        "build or fail to build long-term maker/doer identity."
    ),
    creator_luring_awareness=(
        "Not a direct anti-grooming skill; indirect protection via "
        "account-takeover prevention. Groomers sometimes gain "
        "initial access to a child's account (via credential "
        "stuffing from a breach dump) and then use the existing "
        "contact list + message history to approach the child's "
        "friends more credibly. Per-account unique passwords "
        "eliminate the 'once-you-breach-one, you-breach-all' "
        "pivot. Complementary to the 10-12 'Spotting a please "
        "don't tell your parent message' row and the 13-15 "
        "sextortion-resistance row."
    ),
    example_activity=(
        "ONE-TIME SETUP (60-90 min, family time, typically a "
        "Saturday morning). Step 1 (10 min): family picks a "
        "password manager together. Default recommendation: "
        "Bitwarden Families (free personal tier works for the "
        "teaching phase; Families is CA$5.99/year for 6 members). "
        "Alternative: 1Password Families (~CA$5/mo, 5 members, "
        "smoother UX). Step 2 (10 min): child creates their master "
        "password. Use the 'diceware' three-word-plus-number "
        "pattern — 'correct-horse-battery-7' style, memorable, "
        "long, unguessable. Write it ONCE in a physical notebook "
        "the child keeps with their passport/health card. Caregiver "
        "also knows it (so if child forgets, family can recover). "
        "Step 3 (30 min): child walks through every account they "
        "currently use and either imports the password (if manager "
        "supports import) or changes it to a manager-generated one. "
        "Priority accounts first: school LMS, any gaming account "
        "with payment, family streaming profile. Step 4 (10 min): "
        "install the browser extension + mobile app; test autofill "
        "on one account. Step 5 (ongoing): every NEW account the "
        "child opens from this day forward uses a fresh manager-"
        "generated password. Never a 'memorable' one."
    ),
    gamification_element=(
        "Vault count + password age dashboard. Most password "
        "managers show total credential count and flag passwords "
        "that are reused, weak, or old. Child watches their vault "
        "grow over months (first 10 accounts → 30 → 50+) and the "
        "'reused passwords' count stay at zero. The gamified metric "
        "is NOT vault size (some kids will game it by adding junk) "
        "but 'reused passwords = 0' held across months. Once per "
        "quarter the child runs the vault's health/breach report "
        "and reports to a caregiver — 'no compromised passwords '"
        "this quarter, vault has 47 entries, all unique'."
    ),
    screen_time_guidance=(
        "Setup is on-screen (60-90 min one-time). Ongoing usage is "
        "FRICTION-REDUCING, not adding: autofill makes every login "
        "faster than typing a password. Typical long-term overhead: "
        "0 extra seconds per login once the habit forms. Quarterly "
        "5-min vault health check. Does not compete with other "
        "screen time. No screen-time rule change needed — the skill "
        "is about which tools the child uses during existing screen "
        "time, not about new time."
    ),
    parental_controls_component=(
        "The password manager itself IS the parental-controls "
        "component here — but rotated: it's a child-owned tool "
        "that the caregiver has shared-vault access to, not a "
        "caregiver-surveillance tool the child resents. "
        "Implementation details: (a) use Family plan emergency "
        "access — caregiver can recover the child's vault if the "
        "child forgets the master (30-day wait period is a feature, "
        "not a bug); (b) shared collection for family-level "
        "passwords (wifi, streaming, household accounts) — child "
        "sees the same thing caregiver sees; (c) child's personal "
        "vault is NOT visible to caregiver by default; caregiver "
        "respects this to preserve trust. CISA's family-safety "
        "guidance explicitly supports this shared-not-surveilled "
        "model. Complementary: keep device-level parental controls "
        "(Screen Time / Family Link) on separately; the password "
        "manager is about account integrity, not content filtering."
    ),
    media_quality_rubric=(
        "GOOD: diceware-style memorable master password written "
        "physically; caregiver knows master for recovery but does "
        "not read child's personal vault; child completes every "
        "existing password rotation in one session (half-finished "
        "migration defeats the skill); vault health report run "
        "quarterly; reused-passwords count held at 0. AVOID: "
        "caregiver choosing the master password for the child "
        "(defeats autonomy + memorability); sharing the child's "
        "master with siblings or friends; relying only on browser-"
        "built-in password managers without a family-recovery path "
        "(Safari Keychain, Chrome Passwords — fine technically but "
        "no emergency access for a 10-12-year-old who forgets); "
        "skipping the existing-account rotation step (teaches "
        "manager only for future accounts — misses the legacy-"
        "reuse risk); charging the child for the Families plan "
        "(it's a family-level security investment, not a kid-"
        "level discretionary purchase)."
    ),
    en_ca_content=(
        "**Grown-ups can't remember 50 different passwords either.** "
        "We use a tool called a password manager. You're old enough "
        "for one now, and once you have it, you'll never go back.\n\n"
        "**What it is.** An app on your computer and phone that "
        "holds every password you ever make, and generates brand-new "
        "random ones whenever you sign up for something. You remember "
        "ONE master password. The app holds the rest.\n\n"
        "**Why it matters.** Every kid your age has 5 to 20 accounts "
        "already — your school login, your gaming account, the "
        "family Netflix profile, maybe a Roblox or Discord account. "
        "If you use the same password (or almost the same) on all "
        "of them, a leak on ONE of those services leaks ALL of your "
        "accounts. That's how most kids' accounts get hacked. It's "
        "not that they got hacked — it's that one service they used "
        "three years ago leaked, and the leaked password worked "
        "everywhere else too.\n\n"
        "**The master password.** Make it three or four random "
        "words with a number. Example pattern: 'correct-horse-"
        "battery-7'. Long enough to be uncrackable, weird enough "
        "to be memorable. Write it ONCE in a notebook you keep "
        "with your passport — not on your phone, not in a Google "
        "Doc. Your mom or dad should also know it, in case you "
        "forget — that's OK, they can't see your personal vault, "
        "just rescue you if you lock yourself out.\n\n"
        "**The apps to pick from.** Free + open source: "
        "**Bitwarden** (bitwarden.com). Paid + easier: "
        "**1Password** (1password.com). Both work on every device. "
        "Both have Family plans that cover up to 6 people. Don't "
        "use random apps from the App Store that nobody's heard of "
        "— the app holds every password you have, so pick one that "
        "security experts (CISA, NIST) actually recommend.\n\n"
        "**One Saturday morning.** You + a grown-up, 60-90 minutes. "
        "Install the app, make your master password, go through "
        "every account you currently have, let the app generate a "
        "new unique password for each one. From that day on, every "
        "new account uses a brand-new manager-made password. You "
        "don't have to remember any of them. The app does.\n\n"
        "**The gamified goal.** Your vault shows a 'reused "
        "passwords' count. Keep it at **zero**, forever. Once a "
        "quarter, run the vault's health check and tell a grown-up: "
        "'still zero, no compromised passwords, vault has [N] "
        "entries'. That's the win.\n\n"
        "**Why now?** You'll have 2-3x more accounts in two years. "
        "Starting with 10 is easy. Starting with 50 is a project. "
        "Do it this weekend."
    ),
    fr_qc_content="",
    ar_description=(
        "Not applicable — the tool IS the interface. No AR layer "
        "would add value; the password manager apps (Bitwarden, "
        "1Password) already have strong cross-device UX that "
        "doesn't benefit from spatial/visual augmentation."
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
