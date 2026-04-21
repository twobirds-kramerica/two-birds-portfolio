"""S-R01-PHASE-1f — add 1 high-impact 2nd-row in 13-15 Emotional-Safety.

Row: teen sextortion resistance — specifically the 'send a picture'
coercion pattern + the Take It Down remediation path. This is the
single highest-impact protective skill in the whole DB based on the
FBI / NCMEC / FinCEN threat data. Explicit focus on boys 14-17 who
are the primary financial-sextortion target but less likely to ask
for help.

Grid was completed in S-R01-PHASE-1e (a068564). This adds a 2nd
row in 13-15 x Emotional-Safety because the threat vector is
concrete, well-researched, and fatal when unaddressed.

Run once:   python _s_r01_phase_1f.py
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
    skill="What to do if someone pressures me to send a picture (sextortion)",
    category="Emotional-Safety",
    age_ranges=["13-15"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Multi-Modal",
    learning_profile=["Standard", "ADHD", "Dyslexia", "Special-Needs"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Explicit safety skill for the most-documented online threat "
        "to teens 14-17: financially-motivated sextortion. A stranger "
        "(or someone posing as a peer) convinces or coerces the teen "
        "to share a sexual image, then threatens to release it unless "
        "the teen pays money, sends more images, or does something "
        "else harmful. The skill teaches: (1) warning signs BEFORE "
        "sending, (2) exact steps AFTER sending if that already "
        "happened, and (3) that the NCMEC 'Take It Down' service "
        "can remove the content even once it has been shared. "
        "Critical: framed as non-shaming; the teen is the victim of "
        "a crime, not a participant in wrongdoing."
    ),
    research_source=(
        "NCMEC — Sextortion (ncmec.org/theissues/sextortion) and NCMEC "
        "NetSmartz Sextortion topic page (ncmec.org/netsmartz/topics/"
        "sextortion). NCMEC — Take It Down service "
        "(takeitdown.ncmec.org) — free, anonymous, hash-based removal "
        "of explicit images of persons under 18 from participating "
        "platforms; the image never leaves the teen's device. "
        "NCMEC 2024 data release: 'NCMEC Releases New Sextortion Data' "
        "(missingkids.org/blog/2024/ncmec-releases-new-sextortion-"
        "data). NCMEC No FILTR campaign for teen education. "
        "FBI — Sextortion "
        "(fbi.gov/how-we-can-help-you/scams-and-safety/common-frauds-"
        "and-scams/sextortion). FBI — The Financially Motivated "
        "Sextortion Threat "
        "(fbi.gov/news/stories/the-financially-motivated-sextortion-"
        "threat): in 2024, 55,000+ reports, $33.5M losses, 59% "
        "year-over-year increase. FBI October 2021 - March 2023 data: "
        "13,000+ reports of online financial sextortion of minors, "
        "12,600+ victims (primarily boys 14-17), 20+ suicides "
        "attributed. Report path: 1-800-CALL-FBI, tips.fbi.gov, or "
        "CyberTipline at report.cybertip.org. "
        "FinCEN Notice on Financially Motivated Sextortion, September "
        "2025 (fincen.gov/news/news-releases/fincen-issues-notice-"
        "financially-motivated-sextortion): Treasury alert for "
        "financial institutions on the criminal payment flow; "
        "corroborates scale. Common Sense Media digital citizenship "
        "curriculum covers sextortion at the middle/high-school level."
    ),
    threat_addressed=(
        "Financially-motivated sextortion — FBI categorises it as a "
        "distinct, rapidly growing threat class. Perpetrators are "
        "typically organised criminal groups (often overseas) running "
        "scripts against teenage boys. The social-engineering cycle: "
        "fake peer profile on Instagram / Snapchat / gaming platform; "
        "friendly chat; move to a private app (Snapchat, WhatsApp, "
        "Discord); exchange images (often the perpetrator sends a "
        "real-looking nude first to build reciprocity); as soon as the "
        "teen sends, perpetrator pivots to extortion — pay via gift "
        "cards / Cash App / crypto or the image goes to the teen's "
        "follower list. At least 20 known teen suicides in US data "
        "2021-2023 directly linked. The threat is preventable with "
        "pre-existing knowledge + an explicit remediation path."
    ),
    psychology_framework=(
        "Piaget's formal-operational stage (11+): teens can reason "
        "abstractly about a scripted manipulation sequence once named. "
        "Erikson's identity-vs-role-confusion (12-18): the skill "
        "frames 'I am someone who knows about this and will not be "
        "embarrassed into silence' as a pro-social identity marker. "
        "Dual-process theory (Kahneman System 1 / System 2): sextortion "
        "relies on flooding the teen's System 1 (panic, shame, secrecy) "
        "to bypass System 2 deliberation; the skill explicitly gives "
        "System 2 a script to run ('stop responding — save messages — "
        "tell an adult — Take It Down'). Theories of moral disengagement "
        "(Bandura) + shame research (Brown): shame isolates the victim, "
        "cutting them off from help; the most powerful counter-move is "
        "pre-emptive normalisation ('this happens to thousands of teens; "
        "there is a specific free service; adults who help you will not "
        "think less of you')."
    ),
    creator_luring_awareness=(
        "This IS the luring skill for 13-15. Precursor: the 10-12 row "
        "'Spotting a \"please don't tell your parent\" message' "
        "establishes the general pattern. This row names the specific "
        "escalation vector teens face and the specific service designed "
        "for it. Key facts teens need to hear explicitly: (1) the "
        "perpetrators are adults running scripts, not peers; (2) they "
        "target boys AT LEAST as often as girls for financial "
        "sextortion; (3) paying does NOT make it stop — it identifies "
        "the victim as paying; (4) the image will almost certainly "
        "never actually be sent to followers (threat is leverage); (5) "
        "Take It Down can remove the image from participating platforms "
        "using a hash-only workflow where the image never leaves the "
        "teen's device."
    ),
    example_activity=(
        "TWO-PART CONVERSATION, not a one-time lecture. "
        "PART 1 (15 min, family time, when NOTHING is wrong): "
        "caregiver walks the teen through the FBI / NCMEC pages "
        "together on a laptop. Read the definition out loud. Read the "
        "scale (55,000 reports in 2024). Caregiver explicitly says: "
        "'if this ever happens to you, you will not be in trouble. I "
        "will not take your phone as punishment. I will not think less "
        "of you. We will fix it. The tool is called Take It Down and "
        "it is free.' Write down the URL together: takeitdown.ncmec.org. "
        "Teen adds a note in their Notes app titled 'if it ever happens' "
        "with three bullets: (1) stop answering them; (2) screenshot "
        "everything including their username; (3) show [specific named "
        "adult] — does not have to be mom/dad. PART 2 (5 min, later "
        "that week): caregiver asks 'who is your emergency adult for "
        "this?' Teen names someone — not necessarily a parent. That "
        "person is told by the caregiver: 'you're [teen's] backup. If "
        "they come to you about this, listen, do not lecture, text me.'"
    ),
    gamification_element=(
        "Deliberately NOT gamified. Stickers or points on this topic "
        "would trivialise it. Closing loop: once per year, caregiver "
        "briefly refreshes (2 min) - 'still Take It Down? Yes. Still "
        "your emergency adult? Yes or pick a new one.' That annual "
        "touch keeps the skill live without needing weekly rituals. "
        "The 'game' is that the teen does NOT need to use the skill - "
        "best outcome is the knowledge sits unused for years and "
        "emerges only if the vector hits."
    ),
    screen_time_guidance=(
        "The conversation is 15-20 min total. The skill applies at any "
        "screen time during which the teen uses social / messaging / "
        "gaming platforms - which is most screen time for this age. "
        "Pair with the 2FA skill (S-R01 row 'Turning on two-factor "
        "authentication'): many sextortion scripts start with account "
        "takeover, so 2FA on the social accounts is the first defensive "
        "layer; this skill is the second."
    ),
    parental_controls_component=(
        "Technical controls are secondary to the conversation, but: "
        "(a) Instagram / TikTok / Snapchat all have teen-specific "
        "privacy defaults — confirm they are on. (b) Block message "
        "requests from non-followers where the platform supports it. "
        "(c) Per FBI guidance, avoid sharing location / school / "
        "phone number in bios. (d) The biggest protective control is "
        "relational, not technical: the teen needs to genuinely "
        "believe the named adult will not be angry / will not take "
        "the phone / will not tell their friends' parents. If the "
        "adult cannot honestly commit to that, pick a different adult "
        "(aunt, coach, older cousin, therapist). NCMEC NetSmartz and "
        "Common Sense Media both emphasise the non-shaming adult "
        "relationship is the highest protective factor."
    ),
    media_quality_rubric=(
        "GOOD: non-shaming framing throughout; explicit naming that "
        "boys are ALSO targeted (primarily targeted for financial "
        "sextortion); Take It Down URL memorised or written down; one "
        "named emergency adult beyond the primary caregiver; annual "
        "refresh; no threat of device removal as punishment. AVOID: "
        "fear-based scare tactics that make the teen hide the risk "
        "rather than engage it; assuming only girls are targeted; "
        "framing sending a picture as 'what not to do' (victim-"
        "blaming); using the skill as a lever to justify surveillance "
        "of the teen's messages; telling the teen 'it will never "
        "actually get posted' (teen knows this is a lie - the threat "
        "is real even if release is rare); requiring the teen disclose "
        "if they have already sent an image in the past (retroactive "
        "shame)."
    ),
    en_ca_content=(
        "**This is a skill you might never use. But if you ever need "
        "it, you need it completely - no shame, no delay.**\n\n"
        "**What it is.** Sextortion is when someone online pressures "
        "or tricks a teen into sending a nude or partly-nude picture, "
        "then threatens to release that picture unless the teen pays "
        "money, sends more pictures, or does something else harmful. "
        "The FBI says in 2024 alone there were 55,000+ reports and "
        "at least 20 teen suicides in the US since 2021 are "
        "attributed to it. The victims are usually boys aged 14-17. "
        "(It happens to girls and non-binary teens too, but boys are "
        "the main target because the scripts are built around "
        "financial extortion.)\n\n"
        "**Who is doing this.** Not teens. Organised criminal groups, "
        "usually adults, usually overseas, running the same script "
        "against thousands of teens. They are patient, they sound "
        "friendly, they often send a real-looking 'example' picture "
        "of themselves first to make you feel like it's a normal "
        "exchange. It is not. It is a scripted crime.\n\n"
        "**Before — how to see it coming.** Signs: a new person DMs "
        "you on Instagram / Snapchat / a game; they quickly move the "
        "chat to a 'more private' app; they escalate fast — compliments, "
        "flirting, 'send me something first'. If you feel that quick "
        "escalation, stop. Block. Tell a grown-up. You are not "
        "overreacting.\n\n"
        "**If it already happened — the four steps, in order:**\n\n"
        "1. **Stop replying.** Do NOT pay. Do NOT send more. Paying "
        "tells them you will pay more; sending more gives them more "
        "leverage. The pressure to respond is exactly what the script "
        "is designed to create — that pressure is not real, it's a "
        "tactic.\n\n"
        "2. **Save the evidence.** Screenshot the messages including "
        "their username, the profile photo, and the platform. Don't "
        "delete the account or the chat yet — you need it for step 3.\n\n"
        "3. **Tell an adult you trust.** Does not have to be your "
        "parent. Can be a coach, aunt, older cousin, school counsellor, "
        "family friend. You will not be in trouble. This is a crime "
        "against you.\n\n"
        "4. **Use Take It Down.** Go to **takeitdown.ncmec.org**. "
        "It's a free, anonymous service run by the US National Center "
        "for Missing & Exploited Children — Canadian teens can use it "
        "too. You assign a 'hash' (a digital fingerprint) to the "
        "image on your own device, and participating platforms use the "
        "hash to remove matching images — the image itself never leaves "
        "your phone. Reports work via the CyberTipline at "
        "**report.cybertip.org**.\n\n"
        "**Three things you need to know for real:**\n\n"
        "- **Paying does not make it stop.** It marks you as a paying "
        "victim. Do not send a dollar.\n"
        "- **They almost never actually release the image.** The threat "
        "is their leverage. Once you stop responding and the adults "
        "step in, the leverage is gone.\n"
        "- **This is not your fault.** These criminals run scripts on "
        "thousands of teens. The teens who fall for it are not stupid "
        "or weak. They were targeted by professionals.\n\n"
        "**Save this somewhere in your phone now, when you're not "
        "panicking.** Make a note called 'if it ever happens' with "
        "the four steps, the Take It Down URL, and the name of your "
        "emergency adult. The worst moment to try to remember all "
        "this is during the event itself. Memorize it cold now."
    ),
    fr_qc_content="",
    ar_description=(
        "Deliberately NOT AR. This is a conversation + a saved "
        "reference in the teen's phone; any AR mediation would add "
        "friction at exactly the moment the teen needs to act "
        "instinctively (stop-save-tell-Take It Down). The only tool "
        "is the teen's phone with the Notes app and the Take It Down "
        "URL memorised."
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
