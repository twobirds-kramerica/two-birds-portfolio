"""S-R01-STRETCH-1m — 13-15 Critical-Thinking: Spotting AI-generated images,
audio, and video (deepfakes).

2nd row in the 13-15 × Critical-Thinking cell. Companion to 1h (lateral
reading + AI check for text claims). This row addresses synthetic visual/audio
media specifically — the fastest-growing vector for misinformation targeting
teens in 2025-2026.

Run once:   python _s_r01_stretch_1m.py
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
    skill="Reading visual and audio media for signs of AI manipulation",
    category="Critical-Thinking",
    age_ranges=["13-15"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Multi-Modal",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "The fastest-growing misinformation vector for teenagers in "
        "2025-2026 is not false text — it is false images, cloned voices, "
        "and AI-generated video. Teens already have lateral-reading skills "
        "for text (row 1h); this companion row gives them the specific "
        "visual/audio checklist for synthetic media. Skill covers three "
        "detection layers: (1) artifact-based clues visible to the naked "
        "eye (unnatural skin texture, impossible lighting, ear/hair edge "
        "distortion, background incoherence); (2) provenance tools (Adobe "
        "Content Credentials / C2PA metadata, Google reverse image search, "
        "TinEye); (3) institutional verification (AP, Reuters, AFP visual "
        "verification desks). Also covers the 'liar's dividend': the risk "
        "that deepfake awareness causes teens to dismiss real evidence as "
        "fake."
    ),
    research_source=(
        "Content Authenticity Initiative / C2PA standard "
        "(contentauthenticity.org) — industry coalition (Adobe, Microsoft, "
        "BBC, AFP, AP, Canon, Nikon, Leica) building open standard for "
        "cryptographic provenance in images and video. As of 2025, "
        "Adobe Photoshop and Lightroom embed Content Credentials by default; "
        "growing number of cameras (Leica M11-P, Sony Alpha series) sign "
        "at capture. The standard is the infrastructure-layer answer to "
        "synthetic media. "
        "MIT Media Lab — 'Detecting AI-Generated Images' (media.mit.edu) "
        "and DARPA MediFor programme: academic research on artifact-based "
        "detection — GAN fingerprints, neural compression artifacts, "
        "frequency-domain signatures. Key finding: untrained human detection "
        "accuracy on high-quality deepfakes is near chance (52-56%); "
        "brief training on artifact cues raises it to 70-75% (Groh et al. "
        "2022, PNAS). "
        "Sensity AI / Reality Defender: commercial detection tools used by "
        "newsrooms. Detection is an arms race; no single tool is definitive. "
        "Provenance is more reliable than artifact detection. "
        "Poynter / MediaWise for Teens (poynter.org/mediawiseteens): "
        "media literacy curriculum specifically targeting the 13-17 age "
        "group, includes deepfake module. "
        "Europol (2022) — 'Facing Reality: Law Enforcement and the Challenge "
        "of Deepfakes': estimates that deepfake-enabled fraud and non-"
        "consensual intimate image distribution are the two dominant harm "
        "vectors for 13-17 year olds. Cybertip.ca (Canadian Centre for "
        "Child Protection) tracks synthetic intimate image distribution in "
        "Canada. "
        "Roberts, H. (2021) 'The Liar's Dividend': Academic paper coining "
        "the term for the political/social phenomenon where deepfake "
        "awareness lets bad actors deny authentic evidence. Teens need "
        "calibrated skepticism, not blanket skepticism."
    ),
    threat_addressed=(
        "Synthetic media threats cluster in three categories for the "
        "13-15 age group: (a) POLITICAL — manipulated video of politicians, "
        "AI-generated quotes attributed to real people, fabricated 'news' "
        "images that confirm existing biases; (b) PERSONAL — cloned voice "
        "of parent/sibling in a fake emergency call ('grandparent scam' "
        "variant targeting teens via parents), AI-generated intimate images "
        "used for sextortion (companion to row 1f); (c) SOCIAL — fabricated "
        "images purporting to show a peer doing something embarrassing, "
        "used for bullying or social manipulation. The 'liar's dividend' "
        "is a secondary threat: a teen who becomes hyper-skeptical about "
        "synthetic media will also dismiss real evidence ('that video of "
        "me is deepfaked') — the skill must cultivate calibrated skepticism "
        "with provenance-checking, not blanket denial."
    ),
    psychology_framework=(
        "Piaget's formal-operational stage (11+): teens can reason "
        "hypothetically ('what if this image was generated by AI?') and "
        "understand that media production involves intentional choices, "
        "including deceptive ones. Dual-process theory (Kahneman): "
        "synthetic media is designed to trigger System 1 (fast, "
        "emotional) responses — the emotional impact of a realistic "
        "deepfake bypasses deliberate analysis. This skill is explicitly "
        "about building a System 2 pause ('is this real?') before the "
        "emotional response drives a share or reaction. "
        "Third-person effect (Davison 1983): teens consistently "
        "underestimate their own susceptibility to synthetic media while "
        "overestimating others'. The artifact checklist and provenance "
        "tools are the antidote — they create an explicit procedure "
        "that does not rely on trusting one's own 'it looked fake to me' "
        "intuition."
    ),
    creator_luring_awareness=(
        "Direct and high. AI-generated imagery is used actively to "
        "create false credibility in recruiting content: fake screenshots "
        "of celebrity endorsements, fabricated 'evidence' of a product "
        "working, AI-generated profile photos for fake influencer accounts "
        "that nudge teens toward radicalization pipelines or commercial "
        "fraud. The provenance-checking habit (verify the source, not "
        "just the image) applies equally to political and commercial "
        "synthetic media. Complements row 1h (lateral reading for text "
        "claims) — together they cover both text and visual/audio vectors."
    ),
    example_activity=(
        "THE FIVE-SECOND CHECKLIST (15-20 min, can be run in a browser "
        "at the kitchen table). "
        "Caregiver and teen find 5-10 images online — mix of real photos "
        "and AI-generated images (use ThisPersonDoesNotExist.com for "
        "clearly synthetic examples to start, then graduate to subtler "
        "cases). For each image, run the checklist: "
        "  1. SKIN — does the texture look plastic, waxy, or pore-free "
        "in patches? "
        "  2. EDGES — look at hair, ears, glasses, and jewelry. Do edges "
        "blur into the background or have unnatural 'halo' artifacts? "
        "  3. EYES — are the eyes symmetrical? Are reflections in both "
        "eyes physically consistent? "
        "  4. BACKGROUND — do background elements (furniture, signs, "
        "text) make physical sense? Text in AI images is often garbled. "
        "  5. PROVENANCE — right-click → reverse image search. Where has "
        "this image appeared before? If it's being shared as news, does "
        "it appear on the AP, Reuters, or AFP wire? "
        "After the checklist, show teen how to inspect Content Credentials "
        "on contentcredentials.org/verify — upload the image; if C2PA "
        "metadata is present, the page shows the original capture "
        "information. Most AI-generated images have no C2PA metadata "
        "(the absence is informative, not conclusive). "
        "ADVANCED (teens who are interested): introduce Reality Defender "
        "or Hive Moderation's free detection tools. Discuss why no single "
        "detector is reliable and why provenance > artifact detection."
    ),
    gamification_element=(
        "The 'verified vs. suspicious' media log. Teen keeps a simple "
        "tally for one week: every time they see a shareable image or "
        "video, they run the five-second checklist before liking or "
        "forwarding it. They log: (a) flagged it as suspicious — yes/no, "
        "(b) ran a reverse image search — yes/no, (c) found C2PA data — "
        "yes/no/NA. At the end of the week, they bring the log to a "
        "5-min family debrief: how many images did they not even pause "
        "on? That number is the baseline. Goal is to cut the 'no pause' "
        "share rate to under 10% by week 3."
    ),
    screen_time_guidance=(
        "The five-second checklist adds 5-10 seconds to any image "
        "encounter. Reverse image search adds 30-60 seconds. C2PA "
        "verification via contentcredentials.org adds 1-2 minutes. "
        "Total expected overhead per suspicious image: under 2 minutes. "
        "Not a screen-time concern; the skill reduces engagement time "
        "by breaking the share-reflex loop. Net screen time is flat or "
        "down as teens share less impulsively."
    ),
    parental_controls_component=(
        "No technical controls address synthetic media directly — "
        "detection is a human + provenance-tool skill. Complementary "
        "caregiver actions: (a) when sharing any image in family group "
        "chats or social posts, narrate your own verification process "
        "aloud; (b) if an image makes a strong emotional claim (outrage, "
        "shock, disbelief) treat that emotional intensity as a checklist "
        "trigger — the most viral content is engineered for exactly that "
        "emotional response; (c) do NOT mock teens when they share "
        "something that turns out to be AI-generated — the goal is the "
        "habit, not the perfect track record. Discuss, don't shame."
    ),
    media_quality_rubric=(
        "GOOD: five-second checklist applied before sharing; reverse "
        "image search used when provenance is unclear; emotional "
        "intensity treated as a checklist trigger rather than as "
        "validation; C2PA verification attempted for news images; "
        "calibrated skepticism (real evidence can exist alongside "
        "synthetic media — the goal is verification, not blanket "
        "denial). AVOID: blanket 'it's all fake' dismissal (the "
        "liar's dividend); relying solely on gut feeling ('it looked "
        "real to me'); treating any single AI-detector as definitive; "
        "shaming peers for sharing synthetic media (kills discussion). "
        "The standard: 'I don't know if this is real, so I'm going to "
        "check before I share it.' That is the correct answer. "
        "Certainty is not the goal; procedure is."
    ),
    en_ca_content=(
        "**Can you tell if a photo is real?** Here is the truth: most "
        "people cannot. High-quality AI-generated images score around "
        "52-56% detection accuracy from untrained viewers — barely better "
        "than a coin flip. The good news: a short checklist raises your "
        "accuracy significantly, and provenance tools can cut through "
        "the uncertainty entirely.\n\n"
        "**The five-second checklist.** Next time you see an image that "
        "is being shared as news or evidence, check four things:\n"
        "1. **Skin and texture.** Does it look plastic, too smooth, or "
        "pore-free in patches?\n"
        "2. **Edges.** Look at hair, ears, glasses, jewellery. Do they "
        "blur oddly into the background?\n"
        "3. **Eyes.** Are both eyes symmetric? Do light reflections match "
        "in both eyes?\n"
        "4. **Background.** Is anything physically impossible? Text in "
        "the background is often garbled in AI images.\n\n"
        "**Provenance beats artifact detection.** The checklist is a "
        "starting point. The definitive move is asking: where did this "
        "image actually come from? Right-click any image and run a "
        "reverse image search (Google, Bing, or TinEye). See where it "
        "has appeared before. If it is being shared as breaking news, "
        "check whether it appears on the AP, Reuters, or AFP wire.\n\n"
        "**Content Credentials.** Go to contentcredentials.org/verify "
        "and upload any image. If the photographer or news organisation "
        "used C2PA-certified software (an industry standard that "
        "cryptographically signs images at capture), the page will show "
        "you the original capture metadata. Most AI-generated images "
        "have no C2PA data — that absence is informative, though not "
        "conclusive.\n\n"
        "**The liar's dividend.** Here is the dangerous flip side: "
        "knowing that deepfakes exist does NOT mean every uncomfortable "
        "image is fake. Bad actors use deepfake awareness as a defence "
        "('that video is AI-generated') to discredit real evidence. "
        "Calibrated skepticism means: verify before you share, AND "
        "verify before you dismiss. The goal is procedure, not certainty."
    ),
    ar_description=(
        "AR overlay opportunity: a mobile AR tool that runs the "
        "five-second checklist in real time on any image in the phone "
        "camera viewfinder would be high-value for this age group. "
        "Not buildable with DCC current tech stack. Flag for future "
        "phase if Reality Defender or equivalent provides an embeddable "
        "API for educational use."
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
