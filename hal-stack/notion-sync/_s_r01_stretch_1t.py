"""S-R01-STRETCH-1t — 10-12 Emotional-Safety: Recognising when I need
help — digital wellness self-check.

2nd row in the 10-12 × Emotional-Safety cell. Companion to 1j (stepping
out of a pile-on). Where 1j is about one acute situation (a pile-on),
this row addresses the broader pattern of digital emotional stress: how
does a 10-12 year old recognise when their digital habits are affecting
their mood, sleep, or relationships, and what is the first move when
they notice?

Run once:   python _s_r01_stretch_1t.py
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
    skill="Noticing when my screen use is affecting how I feel — and knowing my first move",
    category="Emotional-Safety",
    age_ranges=["10-12"],
    priority="P1-Important",
    status="Research",
    demonstration_method="Show-and-Tell",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Children aged 10-12 are developing the metacognitive capacity "
        "to notice their own emotional states and connect them to "
        "environmental triggers. This row builds a digital wellness "
        "self-check: a five-question scan the child can run when they "
        "feel 'off' to determine whether their digital habits are a "
        "contributing factor. The five signals: (1) am I sleeping "
        "worse than usual? (2) am I more irritable in the hour after "
        "screens? (3) do I feel worse about myself after being on "
        "[specific platform]? (4) am I sneaking more device time than "
        "usual? (5) am I avoiding a real-life thing by being on a screen? "
        "If two or more are yes: that is worth a conversation. "
        "Also delivers a tiered first-move ladder: "
        "self-monitoring → voluntary break → caregiver conversation → "
        "school counsellor or Kids Help Phone."
    ),
    research_source=(
        "Twenge, J. & Campbell, W.K. (2018) 'Associations between "
        "screen time and lower psychological well-being among children "
        "and adolescents' (Preventive Medicine Reports 12): large-scale "
        "study (n=40,337) finding that screen time above 2 hours/day "
        "is associated with lower well-being outcomes; the association "
        "is stronger for social media and weaker for video games and "
        "video-watching. Key nuance: it is the TYPE of use, not just "
        "the duration. "
        "Twenge, J. et al. (2018) 'Decreases in psychological well-being "
        "among American adolescents after 2012 and links to screen time "
        "during the rise of smartphone technology' (Emotion 18(6)): "
        "longitudinal data showing the association between smartphone "
        "adoption and adolescent depression/loneliness metrics. The "
        "10-12 age group is entering this window. "
        "Nesi, J. & Prinstein, M. (2015) 'Using social media for social "
        "comparison and feedback-seeking: gender and popularity moderate "
        "associations with depressive symptoms' (Journal of Abnormal "
        "Child Psychology 43): social comparison on social platforms is "
        "a primary mechanism linking social media use to reduced "
        "self-esteem and depressive symptoms in pre-adolescence. "
        "The five-signal check operationalises the known mechanisms. "
        "Kids Help Phone (kidshelpphone.ca): Canadian crisis line for "
        "children and youth under 20. Available 24/7, text and call. "
        "Used as the escalation point in the first-move ladder because "
        "it is specifically designed for the 10-12 demographic and is "
        "Canadian-specific. "
        "Tristan Harris / Center for Humane Technology 'Youth Design "
        "Principles' (humanetech.com): design-intent documentation "
        "showing that variable reward, infinite scroll, and notification "
        "design patterns are deliberately engineered to maximise "
        "engagement at the cost of wellbeing. The 'sneaking device time' "
        "signal (signal 4) is a direct behavioural indicator that the "
        "engagement engineering is overriding the child's own preferences."
    ),
    threat_addressed=(
        "Chronic low-grade digital stress that accumulates without "
        "being named. Unlike acute events (pile-ons, sextortion), "
        "this threat is diffuse: a child who sleeps worse, feels "
        "worse about their appearance after Instagram, and is spending "
        "increasing time on screens may not connect these dots without "
        "a framework. The risk compounds: by the time the pattern is "
        "visible to caregivers (grades dropping, social withdrawal), "
        "the habit is well-established. The self-check skill is "
        "designed for the tipping-point moment — when the child feels "
        "'off' but doesn't know why — and gives them both the "
        "diagnostic tool and the first move."
    ),
    psychology_framework=(
        "Formal-operational thought beginning (11+): older children "
        "in this age group can begin abstract self-reflection. The "
        "five-signal check provides a concrete scaffold for that "
        "reflection until it becomes automatic. "
        "Erikson's industry vs. inferiority (6-11) → identity vs. "
        "role confusion (12-18) transition: children at 10-12 are "
        "acutely sensitive to social comparison and competence signals. "
        "Social platforms exploit this developmental sensitivity; the "
        "self-check gives the child a framework to name what they are "
        "experiencing rather than absorbing it as fact ('I feel bad "
        "after Instagram' vs. 'I am bad compared to those people'). "
        "Self-determination theory (Deci & Ryan): the autonomy-"
        "competence-relatedness triad predicts wellbeing. Screen habits "
        "that undermine relatedness (replacing real-world connection) "
        "or autonomy (sneaking, compulsive use) are the most harmful. "
        "The five signals operationalise SDT risk indicators."
    ),
    creator_luring_awareness=(
        "The 'sneaking device time' signal (signal 4) is a direct "
        "indicator of platform engagement engineering overriding "
        "the child's own preferences. Platforms that produce sneaking "
        "behaviour are using variable-reward mechanics (the same "
        "mechanism as slot machines) on a developing brain. "
        "The self-check skill names this dynamic explicitly: 'am I "
        "doing this because I want to, or because the app is pulling "
        "me back?' That question, applied to a social platform, is "
        "also the luring-resistance question applied to any digital "
        "content that is engineered to maximise engagement."
    ),
    example_activity=(
        "THE WEEKLY FIVE-SIGNAL CHECK (5 min, once a week — "
        "Sunday evening works well as a school-week reset). "
        "Child and caregiver sit together without devices. "
        "Run through the five questions: "
        "1. 'Has your sleep been worse than usual this week?' "
        "2. 'Have you noticed feeling more irritable in the hour "
        "after you use screens?' "
        "3. 'Is there a specific app or platform that makes you "
        "feel worse about yourself after using it?' "
        "4. 'Have you been sneaking screen time — using devices "
        "at times we have agreed are screen-free?' "
        "5. 'Have you been choosing screens to avoid something "
        "you did not want to deal with?' "
        "Score: count the yes answers. "
        "0-1 yes: all good. "
        "2-3 yes: worth a conversation about what specifically "
        "is happening. No blame — curiosity. "
        "4-5 yes: time to make a change together. Could be "
        "a voluntary break from one platform, adjusted bedtime "
        "screen cutoff, or a conversation with a school counsellor. "
        "FIRST-MOVE LADDER (introduced once the check is established): "
        "Step 1 — Self-monitoring: notice the signal and name it. "
        "Step 2 — Voluntary break: try 3 days off the specific app "
        "that is scoring highest on the signals. "
        "Step 3 — Caregiver conversation: 'I think [app] is making "
        "me feel worse. Can we figure this out together?' "
        "Step 4 — Kids Help Phone: if the feelings are intense, "
        "ongoing, or include thoughts of self-harm — "
        "kidshelpphone.ca or text CONNECT to 686868 (Canada). "
        "Free, confidential, 24/7, specifically designed for "
        "young people."
    ),
    gamification_element=(
        "The weekly check-in chart. Simple: 5 columns (one per signal), "
        "4 rows (one per week of the month). Colour each cell: green "
        "(no), yellow (maybe), red (yes). At month end, look for "
        "patterns. Is signal 3 (feel worse after a specific platform) "
        "always red? That is information. Is signal 4 (sneaking) "
        "yellow-to-red every week? That is a pattern worth discussing. "
        "The chart turns the abstract ('I think screens are affecting "
        "me') into a concrete, visual pattern the child can own and "
        "bring to the conversation with the caregiver."
    ),
    screen_time_guidance=(
        "The five-signal check takes 5 minutes per week. The purpose "
        "is not to reduce total screen time as a blunt instrument — "
        "it is to identify whether specific use patterns are "
        "affecting wellbeing. A child who scores 0-1 consistently "
        "is using screens in a way that is working for them. A child "
        "who scores 2+ consistently needs a targeted change, not "
        "a blanket reduction. This is a more accurate and effective "
        "intervention than screen time limits alone."
    ),
    parental_controls_component=(
        "Technical supports that complement this skill: "
        "(a) Screen Time (iOS) / Digital Wellbeing (Android): both "
        "provide app-by-app usage reports. After the weekly check, "
        "looking at actual usage data together can validate or "
        "challenge the self-report. 'You said you spent a lot of "
        "time on Instagram — the app says 3h/day. Does that feel "
        "right?' "
        "(b) Bedtime screen cutoff: the most evidence-backed "
        "technical control for the 10-12 age group. Devices out of "
        "bedrooms by 21:00 or 30 min before sleep. Signal 1 (sleep "
        "quality) is the most reliable wellbeing indicator for "
        "this age group. "
        "(c) Kids Help Phone: kidshelpphone.ca, text CONNECT to "
        "686868 (Canada). Make sure the child knows this exists "
        "and that using it is a sign of strength, not weakness. "
        "Caregivers: normalise by asking 'do you know what Kids "
        "Help Phone is?' in a non-crisis moment."
    ),
    media_quality_rubric=(
        "GOOD: weekly five-signal check is practiced consistently; "
        "child can name which platform specifically affects their "
        "mood; first-move ladder is known and has been rehearsed; "
        "Kids Help Phone number is saved in the child's device; "
        "caregiver responds to self-reports with curiosity rather "
        "than immediate punishment (otherwise child stops reporting). "
        "AVOID: using the check results to immediately impose "
        "restrictions without conversation (kills honesty); treating "
        "all screen time as equally harmful (nuance matters — "
        "video calls with friends are not Instagram); skipping the "
        "check when everything seems fine (the check is most "
        "valuable as a consistent baseline, not a crisis tool). "
        "The standard: the child says unprompted 'I think I need "
        "a break from [app]' and takes one. That is self-regulation."
    ),
    en_ca_content=(
        "**Screens can affect how you feel — and it is worth "
        "noticing.** Not all screen time is the same. Video calls "
        "with friends are different from watching YouTube, which "
        "is different from scrolling Instagram. But for some people, "
        "some apps make them feel worse after using them. Knowing "
        "which ones — and what to do about it — is a skill.\n\n"
        "**The five-signal check.** Once a week, run through these "
        "five questions and count your 'yes' answers:\n"
        "1. Has my sleep been worse than usual?\n"
        "2. Am I more irritable in the hour after I use screens?\n"
        "3. Is there a specific app that makes me feel worse about "
        "myself after I use it?\n"
        "4. Have I been sneaking screen time — using devices at "
        "times I know I shouldn't?\n"
        "5. Have I been using screens to avoid something I don't "
        "want to deal with?\n\n"
        "**What the score means:**\n"
        "- 0-1 yes: screens are working for you right now.\n"
        "- 2-3 yes: worth a conversation about what specifically "
        "is happening.\n"
        "- 4-5 yes: time to make a change — together with someone "
        "you trust.\n\n"
        "**Your first-move ladder:**\n"
        "1. Notice it and name it.\n"
        "2. Try 3 days off the specific app that keeps scoring red.\n"
        "3. Talk to a caregiver: 'I think [app] is making me feel "
        "worse. Can we figure this out?'\n"
        "4. If the feelings are intense or scary: Kids Help Phone "
        "(kidshelpphone.ca) or text CONNECT to 686868. "
        "Free, confidential, any time.\n\n"
        "**On the sneaking signal.** If you are sneaking screen "
        "time — using devices at times you have agreed are screen-"
        "free — that is worth paying attention to. It does not mean "
        "you are bad at self-control. It means the app is designed "
        "to pull you back. Knowing that is useful."
    ),
    ar_description=(
        "No AR application in Phase 1 — the five-signal check is "
        "a reflective conversation tool. Future opportunity: a "
        "Show-and-Tell overlay that displays the five signals as "
        "animated check-in cards when the child scans a printed "
        "weekly chart. Low-priority relative to content-safety rows."
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
