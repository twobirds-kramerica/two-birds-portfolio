"""S-R01-STRETCH-1u — 13-15 Tech-Safety: Public Wi-Fi, VPNs, and
keeping your data yours when you're not at home.

2nd row in the 13-15 × Tech-Safety cell. Companion to 1d (two-factor
authentication). Where 1d covers account security, this row covers
network security: the specific risks of public Wi-Fi for teens who
use school networks, coffee shops, and mall networks, and the practical
mitigation (VPNs, HTTPS, network hygiene habits).

Run once:   python _s_r01_stretch_1u.py
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
    skill="Public Wi-Fi, VPNs, and keeping your data yours when you're not at home",
    category="Tech-Safety",
    age_ranges=["13-15"],
    priority="P1-Important",
    status="Research",
    demonstration_method="Show-and-Tell",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Teenagers in the 13-15 age group are the heaviest users of "
        "public and semi-public Wi-Fi networks — school networks, "
        "library networks, coffee shops, malls, transit. These "
        "networks present specific risks that do not apply to home "
        "networks. This row delivers: (1) a plain-English model of "
        "what public Wi-Fi risks actually are (evil twin networks, "
        "man-in-the-middle, unencrypted traffic); (2) the HTTPS "
        "padlock check as the baseline habit; (3) VPN basics — what "
        "they do, what free VPNs actually do with user data, and "
        "which free options are trustworthy (Mullvad, Proton VPN); "
        "(4) three habits for public network use: check for HTTPS, "
        "avoid logging into sensitive accounts, use mobile data for "
        "anything banking/medical/identity-related."
    ),
    research_source=(
        "Electronic Frontier Foundation (EFF) — 'Surveillance Self-"
        "Defense for Teens' (ssd.eff.org): practical security guidance "
        "specifically adapted for the 13-17 age group. Public Wi-Fi "
        "section is directly cited as a high-priority risk for this "
        "demographic. "
        "Krombholz, K. et al. (2014) 'Advanced social engineering "
        "attacks' (Journal of Information Security and Applications "
        "22): academic documentation of evil-twin attacks (rogue access "
        "points that impersonate legitimate networks) as a practical "
        "threat on public networks. Requires no special hardware; "
        "demonstrates why 'my school's Wi-Fi is safe because I know "
        "the name' is not a valid security model. "
        "HTTPS Everywhere (EFF) and the broader adoption of TLS: "
        "as of 2024, over 90% of web traffic is HTTPS-encrypted "
        "(Let's Encrypt / Google Transparency Report). However, the "
        "remaining unencrypted traffic is disproportionately on "
        "low-effort sites that teens may visit. The padlock check "
        "remains a valid baseline habit. "
        "Leith, D. (2020) 'Mobile Handset Privacy: Measuring the "
        "Data iOS and Android Send to Apple and Google' (Trinity "
        "College Dublin): baseline data on what phones transmit even "
        "without user action — relevant context for mobile data vs. "
        "public Wi-Fi trade-offs. "
        "Proton VPN (protonvpn.com) and Mullvad (mullvad.net): "
        "two VPN providers with independently audited no-logs policies "
        "and transparent privacy practices. Both offer free or low-cost "
        "tiers that are appropriate for teen use. Contrast with "
        "free VPNs that monetise user traffic data (documented by "
        "CSIRO 2016 'An Analysis of the Privacy and Security Risks "
        "of Android VPN Permission-enabled Apps'). "
        "Canadian Centre for Cyber Security (cyber.gc.ca) — "
        "'Protecting Yourself on Public Wi-Fi': Government of Canada "
        "guidance for individuals, used as a Canadian-specific "
        "authoritative source. "
        "Communications Security Establishment (CSE) Canada — "
        "'Cyber Hygiene for Canadians': the national cyber security "
        "agency's public guidance. Appropriate for citing as "
        "Canadian institutional authority."
    ),
    threat_addressed=(
        "Three threat vectors on public Wi-Fi relevant to 13-15 "
        "year olds: "
        "(a) EVIL TWIN / ROGUE AP — an attacker creates a Wi-Fi "
        "network with the same name as the legitimate one ('Tim "
        "Hortons Wi-Fi'). Any device that auto-connects sends all "
        "its traffic through the attacker's router. The teen "
        "cannot distinguish this from the real network by name. "
        "(b) UNENCRYPTED TRAFFIC INTERCEPTION — on networks without "
        "WPA2/WPA3 encryption (common on legacy school and public "
        "networks), any device on the network can observe unencrypted "
        "HTTP traffic from other devices. Login credentials sent "
        "over HTTP are visible. "
        "(c) CREDENTIAL HARVESTING VIA CAPTIVE PORTAL — some "
        "malicious public networks require 'login' via a fake page "
        "before granting internet access, harvesting credentials "
        "entered on that page. The three-habit framework (HTTPS "
        "check, no sensitive logins, mobile data for sensitive "
        "actions) mitigates all three vectors."
    ),
    psychology_framework=(
        "Formal-operational reasoning (11+): teens can understand "
        "abstract models ('your data travels as packets that can "
        "be intercepted') and reason about risk scenarios. The "
        "public Wi-Fi threat model is teachable at this age as a "
        "simplified network diagram. "
        "Self-determination theory: autonomy is the highest-yield "
        "motivator for teens. Framing network security as 'keeping "
        "your data yours' (autonomy) rather than 'following the "
        "rules' (external control) aligns with the developmental "
        "orientation and produces better habit adoption. "
        "Optimism bias (Sharot 2011): teens systematically "
        "underestimate personal risk ('it won't happen to me'). "
        "The concrete demonstration (showing that a rogue AP is "
        "technically trivial to set up) reduces the optimism bias "
        "more effectively than abstract risk statistics."
    ),
    creator_luring_awareness=(
        "Phishing and luring via fake network portals: some malicious "
        "captive portal attacks are specifically designed to harvest "
        "social media credentials or display content nudging the "
        "user toward a fake 'you've won' page. The evil-twin threat "
        "model covers the network-level version of the same "
        "deception used in creator-luring — a fake trusted "
        "environment designed to capture information or behaviour "
        "the user would not provide to an honest source."
    ),
    example_activity=(
        "THE PADLOCK AUDIT (15-20 min, do once in person, then "
        "ongoing as a 2-second habit). "
        "PART 1 — THE MODEL. Show a simple diagram: your phone → "
        "Wi-Fi router → internet. On public Wi-Fi: your phone → "
        "ATTACKER'S ROUTER → internet (and the attacker can see "
        "your traffic). Ask: 'How would you know if the router "
        "belonged to the attacker, not the coffee shop?' Answer: "
        "you wouldn't. The router has the same name. "
        "This is the evil-twin model. Takes 2 minutes to explain "
        "with a drawing. "
        "PART 2 — THE PADLOCK HABIT. Open a browser and visit "
        "two sites: one HTTPS (padlock visible in address bar) "
        "and one HTTP (some older sites or local resources). "
        "'See the padlock? That means your traffic is encrypted "
        "between your device and the server — even if the router "
        "is rogue, the attacker cannot read it. No padlock: "
        "assume the attacker can read everything you type.' "
        "Habit: before entering any username/password on public "
        "Wi-Fi, check for the padlock. If no padlock: don't type. "
        "PART 3 — THE THREE RULES. "
        "Rule 1: HTTPS padlock before any login. "
        "Rule 2: Never log into banking, government, or medical "
        "accounts on public Wi-Fi. Use mobile data (your carrier's "
        "network, not the Wi-Fi) for those. "
        "Rule 3: If the network requires you to 'log in' on a "
        "weird-looking page before you get internet access — "
        "do not enter your real credentials. Use a throwaway "
        "email or guest login if the service offers one. "
        "OPTIONAL EXTENSION: Show Proton VPN or Mullvad. "
        "'This app encrypts all your traffic before it leaves "
        "your phone — even unencrypted HTTP becomes protected. "
        "Free tier is enough for public Wi-Fi use. Avoid any "
        "VPN that is completely free with no paid option — "
        "they are selling your browsing data.'"
    ),
    gamification_element=(
        "The 'padlock check streak.' For two weeks, every time "
        "the teen logs into something on a non-home network, "
        "they check for the padlock first and give themselves "
        "a point. No padlock = they switch to mobile data or "
        "skip the login. Points tracked on a phone note or "
        "paper. Goal: 14-day streak with zero unpadlocked logins "
        "on public Wi-Fi. After 14 days the habit should be "
        "automatic and the streak is retired."
    ),
    screen_time_guidance=(
        "The padlock check adds 2 seconds to any login on a "
        "public network. The three-rule framework has no screen "
        "time overhead. Installing a VPN app takes 5 minutes "
        "once. Net screen time: neutral to slightly down "
        "(the mobile data rule reduces casual public Wi-Fi "
        "usage for sensitive tasks)."
    ),
    parental_controls_component=(
        "Technical setups that complement this skill: "
        "(a) Proton VPN (protonvpn.com) — free tier, audited no-"
        "logs, Swiss-based, appropriate for teen use. Install "
        "together and configure to auto-connect on non-home "
        "networks. "
        "(b) DNS-over-HTTPS: most modern browsers (Chrome, Firefox, "
        "Edge, Safari) support this by default or in settings. "
        "It encrypts DNS lookups — a common interception vector on "
        "public networks. Enable in browser privacy settings. "
        "(c) 'Ask to join networks' on iOS / 'saved networks' on "
        "Android: review what networks the device auto-connects to. "
        "Remove networks the teen no longer uses regularly. "
        "(d) Canadian Centre for Cyber Security (cyber.gc.ca) "
        "publishes free public-Wi-Fi guidance updated annually — "
        "bookmark as a reference."
    ),
    media_quality_rubric=(
        "GOOD: padlock checked before any login on public Wi-Fi; "
        "mobile data used for banking/government/medical actions; "
        "VPN installed and used on non-home networks; teen can "
        "explain the evil-twin threat model in one sentence; "
        "captive portal logins handled with guest credentials. "
        "AVOID: assuming school or library Wi-Fi is 'safe' because "
        "it is institutional (institutional networks are public "
        "networks with extra branding); using completely free VPNs "
        "with no paid tier or audited privacy policy; treating "
        "the three rules as bureaucratic restrictions rather than "
        "as a model of what is actually happening technically. "
        "The standard: the teen checks for the padlock without "
        "being reminded, and switches to mobile data for sensitive "
        "tasks without prompting. Both behaviours, spontaneous, "
        "are the skill."
    ),
    en_ca_content=(
        "**Public Wi-Fi is not the same as your home network.** "
        "At home, only people you trust have the Wi-Fi password. "
        "At a coffee shop, a school, a mall, or a library: you "
        "have no idea who else is on the network — or whether the "
        "network you connected to is actually the real one.\n\n"
        "**The evil twin.** It takes about five minutes and a "
        "cheap device to set up a Wi-Fi hotspot with the same "
        "name as the coffee shop's network. Your phone connects "
        "automatically. All your traffic flows through the "
        "attacker's router. They can see everything you send "
        "that isn't encrypted. You cannot tell the difference "
        "from the name alone.\n\n"
        "**Three habits that fix most of this:**\n\n"
        "**1. Check the padlock.** Before you type a username or "
        "password anywhere on public Wi-Fi, look for the padlock "
        "in the browser address bar. Padlock = HTTPS = your data "
        "is encrypted between your device and the server, even "
        "on a rogue network. No padlock: do not type credentials.\n\n"
        "**2. Use mobile data for sensitive things.** Banking, "
        "government accounts, medical — do these on your carrier's "
        "network (the LTE/5G signal), not the Wi-Fi. Your carrier's "
        "network has its own encryption. Takes one tap to turn "
        "Wi-Fi off temporarily.\n\n"
        "**3. Treat captive portals carefully.** When a public "
        "network asks you to 'log in' on a welcome page before "
        "you get internet access — do not enter your real "
        "credentials. Use a guest email if one is offered. "
        "Some captive portals harvest whatever you type.\n\n"
        "**On VPNs.** A VPN encrypts all your traffic before it "
        "leaves your device. Even unencrypted HTTP becomes "
        "protected. Proton VPN (free tier) and Mullvad are both "
        "independently audited and do not sell your data. "
        "Avoid any VPN that is 100% free with no paid option — "
        "if you're not paying for the product, your browsing "
        "data is the product."
    ),
    ar_description=(
        "No AR application in Phase 1. Future opportunity: an AR "
        "overlay that shows an animated 'network path' from the "
        "device to the internet, highlighting the router as a "
        "potential interception point — makes the abstract "
        "network model tangible. Show-and-Tell application. "
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
