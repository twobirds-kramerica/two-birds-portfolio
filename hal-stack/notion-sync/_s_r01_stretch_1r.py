"""S-R01-STRETCH-1r — 4-6 Tech-Safety: My device is mine — understanding
who can see and hear me.

2nd row in the 4-6 × Tech-Safety cell. The youngest DCC age group needs
a concrete, non-scary introduction to device privacy: cameras, microphones,
and location are hardware that can be accessed by apps. At ages 4-6, the
concept is made tangible through a physical lens cover metaphor and a
'cover-and-check' habit for tablet/phone use during private moments.

Run once:   python _s_r01_stretch_1r.py
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
    skill="My device has eyes, ears, and a memory — and I get to choose who uses them",
    category="Tech-Safety",
    age_ranges=["4-6"],
    priority="P0-Core",
    status="Research",
    demonstration_method="Play-Acting",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Children aged 4-6 use tablets, smart speakers, and phones as "
        "natural parts of daily life — but rarely have a conceptual model "
        "for what these devices can observe. This row delivers the simplest "
        "possible version of device privacy: the device has a camera (eye), "
        "a microphone (ear), and storage (memory). Some apps use these. "
        "The child learns: (1) to recognise the camera indicator light on "
        "devices they use; (2) a physical 'cover and check' habit — "
        "covering the camera when not in a video call and checking with a "
        "grown-up before giving an app permission to use the camera or "
        "microphone; (3) that smart speakers are always listening for a "
        "wake word, and that this means choosing when NOT to speak "
        "privately near them. No fear framing. The goal is agency, not "
        "anxiety."
    ),
    research_source=(
        "Radesky, J. et al. (2020) 'Overstimulation and digital media "
        "use in young children' (Pediatrics, AAP): notes that children "
        "aged 4-6 have no conceptual model of how devices work and "
        "therefore cannot evaluate app permission requests that reference "
        "camera or microphone access. The decision must be scaffolded "
        "by the caregiver. "
        "Canadian Centre for Child Protection (protectchildren.ca) — "
        "'Keeping Kids Safe Online' for the early childhood age group: "
        "emphasises that camera-access malware and inadvertent video "
        "activation are documented child safety risks, and that physical "
        "camera habits (covering, awareness) are the most robust "
        "protection at ages where software settings are beyond the child's "
        "management capacity. "
        "Luxton, D. et al. (2012) 'mHealth for Mental Health: Integrating "
        "Smartphone Technology in Behavioral Healthcare' — reference for "
        "the established knowledge that microphone and camera access by "
        "apps is a technical reality, not a paranoid concern. Smart "
        "speaker always-on listening: documented in published research "
        "by Edu et al. (2021) 'The Faraway Near: Smart Speaker Privacy "
        "and the Unanticipated Presence' (IEEE). Wake-word false positive "
        "rates mean ambient conversations are occasionally recorded; "
        "children's voices are over-represented in false positive "
        "activations. "
        "American Academy of Pediatrics / Canadian Paediatric Society "
        "screen time guidelines: both recommend that for 2-5 year olds, "
        "video calling is the one screen activity with clear developmental "
        "benefit (joint attention, social bonding). This creates a natural "
        "anchor: 'the camera is for talking to people we love' — which "
        "makes the 'cover it otherwise' norm easier to explain."
    ),
    threat_addressed=(
        "Primary threats for the 4-6 age group involving device "
        "sensors: "
        "(a) INADVERTENT ACTIVATION — camera or microphone activating "
        "during private family moments (bath time, bedroom) via app "
        "permissions the child or caregiver did not intend to grant. "
        "Physical camera covering is the simplest mitigation. "
        "(b) SMART SPEAKER AMBIENT RECORDING — children's voices and "
        "household conversations captured during false-positive wake "
        "events on Alexa, Google Home, etc. The child learning that "
        "the speaker 'can hear' creates awareness without fear. "
        "(c) PERMISSION GRANT HABIT — children who are allowed to tap "
        "through app permission dialogs without adult involvement "
        "routinely grant camera and microphone access to apps that "
        "do not need them. The 'check with a grown-up' habit installed "
        "at age 5-6 persists into the years when the stakes are higher."
    ),
    psychology_framework=(
        "Piaget's preoperational stage (2-7): children learn through "
        "direct, concrete, physical interaction. Abstract concepts "
        "('app permissions,' 'data collection') are cognitively "
        "unavailable. The physical camera cover, the device-as-robot-"
        "with-eyes metaphor, and the play-acting activity all make "
        "the concept tangible through physical action. "
        "Erikson's initiative vs. guilt stage (3-6): children are "
        "developing their sense of purposeful action. Framing device "
        "privacy as 'you get to choose who uses the camera' gives the "
        "child agency rather than fear — consistent with the "
        "developmental drive toward intentional action. "
        "Attachment theory (Bowlby/Ainsworth): the 'check with a "
        "grown-up' norm positions the caregiver as the reliable "
        "authority for device decisions. This is appropriate at this "
        "age (executive function for independent technology decisions "
        "develops much later) and maintains the attachment-security "
        "model without creating dependency on the device itself."
    ),
    creator_luring_awareness=(
        "Foundational. Children who understand that devices have "
        "sensors and that those sensors can be accessed by apps have "
        "a conceptual model that supports later understanding of "
        "tracking, surveillance, and targeted advertising. A child "
        "who at age 6 understands 'the tablet has a camera, and some "
        "apps use it' is far better equipped at age 10 to understand "
        "'this app wants to know where I am and what I do.' The "
        "earliest layer of the DCC Tech-Safety ladder."
    ),
    example_activity=(
        "THE DEVICE INTRODUCTION (15-20 min, one-time activity, "
        "then brief reminders). "
        "PART 1 — MEET YOUR DEVICE. Hold up the tablet or phone with "
        "the child. Name each part: 'This is the eye (camera). "
        "This is the ear (microphone). There is a memory inside that "
        "can save what the eye and ear see and hear.' "
        "Point to the camera lens. Point to the microphone port "
        "(it is usually a small hole; show a photo of it). "
        "Optional: open the front-facing camera app and show the child "
        "their own face — 'See? The eye is working right now. When "
        "the app is closed, the eye is resting.' "
        "PART 2 — THE COVER HABIT. Get a small sticky note or "
        "adhesive webcam cover (available for a few dollars). "
        "Put it over the front camera together. 'Now the eye is closed. "
        "We open it when we want to video call Grandma. We close it "
        "the rest of the time.' Make it a routine: tablet goes on "
        "the charger, camera is covered. "
        "PART 3 — THE PERMISSION CHECK. Next time an app asks for "
        "camera or microphone access, show the child the dialog. "
        "'An app is asking if it can use the eye and the ear. "
        "Should it? Let us think together.' Walk through: does this "
        "app need a camera? (A drawing app: no. A video call app: yes.) "
        "The habit: child says 'let us check' instead of tapping alone. "
        "PART 4 — THE SMART SPEAKER. If the family has a smart speaker, "
        "stand next to it with the child. 'This one has a very good "
        "ear. It listens all the time for its wake word. When it hears "
        "its name, it wakes up and listens more carefully. So we do "
        "not say private things near it — like a birthday surprise, "
        "or when we do not want it to know something.'"
    ),
    gamification_element=(
        "The 'camera check' sticker. For two weeks, the child earns "
        "a sticker each time they check that the camera cover is "
        "in place before putting the tablet away. The caregiver can "
        "also earn a sticker when the child catches them forgetting. "
        "After two weeks, the habit should be automatic and the "
        "sticker chart is retired. The goal is not ongoing reward — "
        "it is habit installation in 14 days."
    ),
    screen_time_guidance=(
        "The camera cover habit adds less than 5 seconds to each "
        "device session. The permission-check habit adds 30-60 seconds "
        "when a new app requests access (infrequent). Net screen time: "
        "neutral. The smart speaker awareness piece requires no "
        "additional screen time."
    ),
    parental_controls_component=(
        "Technical actions that complement this skill: "
        "(a) REVIEW APP PERMISSIONS on all devices the child uses. "
        "For iOS: Settings → Privacy & Security → Camera / Microphone. "
        "For Android: Settings → Privacy → Permission Manager. "
        "Revoke camera and microphone from apps that do not need them. "
        "(b) PHYSICAL CAMERA COVER: inexpensive adhesive covers "
        "(search 'webcam cover' on Amazon, typically CA$5-10 for a "
        "pack of 10) work on tablets and laptops. "
        "(c) SMART SPEAKER MUTE: all major smart speakers (Alexa, "
        "Google Home, HomePod) have a hardware mute button. Show "
        "the child where it is and when to use it. "
        "(d) CANADIAN PRIVACY CONTEXT: PIPEDA and provincial privacy "
        "laws apply to apps that collect video and audio data from "
        "Canadian users, including children. Apps marketed to children "
        "under 13 are subject to additional restrictions. Review app "
        "stores' child safety ratings before installation."
    ),
    media_quality_rubric=(
        "GOOD: camera cover habit installed and used consistently; "
        "child checks with caregiver before tapping app permission "
        "dialogs; child understands the camera/microphone concept "
        "at a level appropriate to age (device has eyes and ears); "
        "smart speaker mute used during private conversations; "
        "caregiver has reviewed app permissions on all child-used "
        "devices. "
        "AVOID: fear framing ('the camera is always watching you'); "
        "requiring the child to manage technical settings independently "
        "(inappropriate for this age group); treating all apps as "
        "threats (normalises paranoia rather than agency). "
        "The standard: the child reaches for the camera cover "
        "unprompted when putting the tablet away. That physical "
        "habit is the skill."
    ),
    en_ca_content=(
        "**Your device has three things worth knowing about.** "
        "An eye (camera), an ear (microphone), and a memory (storage). "
        "Some apps use these. This is not scary — it is just something "
        "to know, the same way you know that a lamp needs to be plugged "
        "in to give light.\n\n"
        "**The eye.** The camera takes photos and videos. When you are "
        "on a video call with Grandma, the eye is working. When you are "
        "playing a drawing game, the eye does not need to be working — "
        "but some apps ask if they can use it anyway. Covering the "
        "camera when you are not on a call is a simple habit. A small "
        "sticky note works fine.\n\n"
        "**The ear.** The microphone picks up voices. Smart speakers "
        "(like the little cylinder in the kitchen that plays music) "
        "have a very good ear — they listen all the time for their "
        "wake word. This means they sometimes hear things they were "
        "not meant to hear. When you want to say something private, "
        "move away from the speaker — or use the mute button on top.\n\n"
        "**The check habit.** When an app asks if it can use the "
        "camera or the microphone, that is worth a pause. Does this "
        "app actually need an eye or an ear? A drawing app: probably "
        "not. A video call app: yes. When your child is unsure, "
        "'let us check together' is the right answer. That habit — "
        "pause and check rather than tap and accept — is one of the "
        "most protective things a small person can learn."
    ),
    ar_description=(
        "AR opportunity: a Toy-to-Life application where the child "
        "holds a physical toy 'robot' up to the tablet camera; the "
        "AR overlay shows the robot's 'eye' (camera), 'ear' (mic), "
        "and 'brain' (memory) lighting up to demonstrate the concept "
        "concretely. Matches the play-based learning profile of this "
        "age group. Flag for Phase 2 AR sprint."
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
