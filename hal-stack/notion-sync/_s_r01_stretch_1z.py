"""S-R01-STRETCH-1z — 4-6 Creative-Making: Making something together —
sharing ideas and giving credit even as a little creator.

2nd row in the 4-6 × Creative-Making cell. Companion to "Making my own
thing first, then watching." Where that row teaches the value of original
creation (try it yourself before copying), this row addresses what happens
when you make something *with* someone else: collaborative creation,
sharing credit, and the earliest introduction to the idea that when
you use someone else's idea, you say where it came from.

This is the developmental foundation for the 10-12 "When I remix, I name
who made the original" row. Without this 4-6 root, the attribution ethic
arrives too late — at 10-12 when the habits are already formed.

Run once:   python _s_r01_stretch_1z.py
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
    skill="Making something together — sharing ideas and giving credit even as a little creator",
    category="Creative-Making",
    age_ranges=["4-6"],
    priority="P1-Important",
    status="Research",
    demonstration_method="Show-and-Tell",
    learning_profile=["Standard", "Dyslexia"],
    language_version=["en-CA"],
    ar_showcase="None",
    description=(
        "Young children aged 4-6 are beginning to create collaboratively — "
        "drawing with a friend, building together, making up songs or "
        "stories in groups. Digital tools (drawing apps, shared story "
        "builders, voice recorders) extend this into digital spaces. "
        "This row plants two foundational seeds: (1) when you make "
        "something together, both people's names go on it — the social "
        "norm of shared credit is introduced as a natural part of "
        "collaborative creation, not as a rule imposed after the fact; "
        "(2) when you use someone else's idea (a picture you saw, a "
        "song you heard, a story someone told you), you say 'I got "
        "this idea from...' — the earliest, simplest form of attribution. "
        "These concepts are taught at a concrete, story-level abstraction "
        "appropriate for pre-operational and early concrete-operational "
        "thinkers. No copyright law, no formal Creative Commons — just "
        "the social norm that ideas come from people, and those people "
        "deserve a mention."
    ),
    research_source=(
        "Piaget, J. (1952). The Origins of Intelligence in Children. "
        "International Universities Press. Pre-operational stage (2-7): "
        "children understand the world through concrete, personal "
        "experience. The concept of 'this idea came from you, and "
        "you deserve credit' must be taught through concrete, "
        "story-level examples — not abstract rules about intellectual "
        "property. Piaget's research on moral development shows that "
        "4-6 year olds are beginning to move from ego-centric to "
        "social-rules understanding; attribution is best framed as "
        "a social norm ('we always say whose idea it was') rather "
        "than a law. "
        "Vygotsky, L. S. (1978). Mind in Society. Harvard University "
        "Press. Scaffolded social learning: collaborative creation "
        "is a natural Vygotskian activity — the child operates in "
        "the zone of proximal development when creating with a more "
        "capable peer or adult. Attribution is modelled by the adult "
        "and absorbed by the child through the collaborative process "
        "itself ('You drew the sun, so it is your sun. We will put "
        "both our names on the whole picture.'). "
        "Common Sense Media — Copyright & Creativity: Elementary "
        "K-6 Curriculum. Specific lessons for Grades K-2 ('Who "
        "Made That?', 'Fair Use for Kids') frame attribution as "
        "a kindness and a social norm, not a legal requirement. "
        "Appropriate for this age group's developmental stage. "
        "Lessig, L. (2004). Free Culture. Penguin Press. The "
        "foundational text on remix culture and attribution. At "
        "4-6, only the simplest concept applies: 'if you build on "
        "someone else's idea, you say so.' Lessig's broader argument "
        "becomes relevant at 10-12 (the remix row). This row plants "
        "the seed. "
        "Bers, M. U. (2018). Coding as a Playground: Programming and "
        "Computational Thinking in the Early Childhood Classroom. "
        "Routledge. Documents how 4-6 year olds engage in "
        "collaborative digital creation and the social norms they "
        "naturally develop around shared work when given scaffolded "
        "opportunities."
    ),
    threat_addressed=(
        "The 4-6 × Creative-Making threat is not primarily a digital "
        "safety threat in the direct-harm sense; it is a cultural "
        "formation threat: if children are not introduced to "
        "attribution as a social norm at this age, they arrive at "
        "10-12 (when remix and borrowing become ubiquitous online "
        "behaviours) with no instilled habit of crediting. The habit "
        "of silent borrowing — taking an idea, a sticker, a song "
        "clip, a meme format, and presenting it without attribution "
        "— forms in early childhood and is extremely hard to reverse "
        "in adolescence. This row addresses that formation threat "
        "by introducing attribution as a natural social norm during "
        "the developmental window when social norms are most "
        "easily absorbed."
    ),
    psychology_framework=(
        "Pre-operational and early concrete-operational (Piaget): "
        "4-6 year olds think in concrete terms. 'Give credit' is "
        "abstract; 'say whose idea it was' is concrete and "
        "understandable. The row's language must stay at the level "
        "of stories and examples, not principles. "
        "Theory of mind development (4-6): children in this range "
        "are actively developing the capacity to understand that "
        "other people have perspectives, feelings, and experiences "
        "different from their own. Framing attribution as 'imagine "
        "how it would feel if you made something and nobody knew it "
        "was yours' activates this developing capacity appropriately. "
        "Moral development — Piaget's heteronomous morality (rules "
        "come from authority and are absolute): 4-6 year olds are "
        "most receptive to 'this is what we always do' framing. "
        "'In our family/class, when we use someone's idea, we say "
        "where we got it' is more effective than a rule-explanation "
        "('because copyright law says...')."
    ),
    creator_luring_awareness=(
        "The attribution habit has an indirect protective benefit "
        "against creator-luring patterns. Children who are taught "
        "that ideas come from people — and those people deserve "
        "acknowledgement — are primed to notice when content "
        "appears without a clear author or source. At 4-6, this "
        "is not yet a critical-thinking skill; it is a social "
        "pattern that supports later critical-thinking development. "
        "The child who asks 'who made this?' is beginning the "
        "same intellectual move as the teenager who asks 'where "
        "did this information come from?' before sharing it."
    ),
    example_activity=(
        "THE COLLABORATION BOOK (ongoing project, 20-30 min to "
        "start, then lives in the home or classroom). "
        "PART 1 — MAKE SOMETHING TOGETHER. "
        "Sit with the child and make something collaboratively: "
        "draw a picture together, build a block structure and "
        "photograph it, record a story you make up as a pair. "
        "As you work: narrate who is contributing what. 'You "
        "drew the tree. I drew the house. This picture is by "
        "both of us.' "
        "PART 2 — THE NAME PAGE. "
        "When it is finished, add a 'name page' or label: "
        "'Made by [child's name] and [adult's name].' For a "
        "digital drawing, add names in text. For a photo, write "
        "on the back or add a caption. "
        "Ask: 'What would happen if I only put my name on this "
        "and not yours? How would you feel?' Let them answer. "
        "Then: 'That is why we always put both names. "
        "Because both people made it.' "
        "PART 3 — THE IDEA CREDIT GAME. "
        "Show the child something they love: a song, a picture "
        "in a book, a toy design. Ask: 'Who made this?' Find "
        "out together (look at the book cover, ask where the toy "
        "came from). 'Someone had this idea. It came from "
        "their brain. That is pretty cool.' "
        "Then: 'When you use an idea you got from someone else — "
        "like if you draw a rainbow exactly like the one in this "
        "book — what could you say?' "
        "Practice: 'I got this idea from [book name].' Or: "
        "'My friend showed me this and I tried it too.' "
        "That is enough. At 4-6, that is the whole skill. "
        "EXTENSION (ongoing): whenever the child borrows an idea "
        "(a drawing style, a block building pattern, a story "
        "plot from a show), gently prompt: 'Where did you get "
        "that idea from? That is great! You could say: I got "
        "this from [source].' Over time the prompt becomes "
        "internal."
    ),
    gamification_element=(
        "The 'idea jar.' A physical jar or box in the home or "
        "classroom. Whenever someone in the family or class "
        "credits an idea — 'I got this from...' or 'Let's put "
        "both names on this' — they put a small stone or counter "
        "in the jar. When the jar is full, celebrate together. "
        "The jar makes an invisible social norm visible and "
        "collective. It does not reward individual children "
        "for following a rule; it rewards the group for "
        "practising the norm together."
    ),
    screen_time_guidance=(
        "The activity requires no screens and is primarily "
        "in-person. The digital application (naming collaborators "
        "in a shared drawing app, adding a creator tag to a "
        "recorded story) takes 30 seconds. Net screen time: "
        "neutral — the skill is practised in whatever creative "
        "medium the child is already using."
    ),
    parental_controls_component=(
        "Technical supports that extend this skill into digital "
        "spaces: "
        "(a) Co-creation apps for young children: Toca Boca, "
        "Drawing with Friends, StoryBird — these have built-in "
        "sharing and authorship features. Use them as natural "
        "contexts to model naming collaborators. "
        "(b) Photo captioning: when photographing a child's work, "
        "add a caption that names all creators. Modelling "
        "attribution in adult behaviour is the most effective "
        "teacher at this age. "
        "(c) Book credits: when reading with the child, point to "
        "the author and illustrator names on the cover. 'This "
        "story came from [author's name]. She had this idea "
        "and wrote it down.' Normalises attribution as a "
        "natural part of creative work."
    ),
    media_quality_rubric=(
        "GOOD: child spontaneously mentions where an idea came "
        "from when sharing creative work ('I got this from my "
        "friend' / 'We made this together'); child participates "
        "in adding names to collaborative work; child responds "
        "positively when their contribution to a group project "
        "is acknowledged. "
        "AVOID: over-correcting or making attribution a punitive "
        "rule ('you have to say who made that or you're "
        "stealing') — at 4-6, the norm is absorbed through "
        "positive modelling, not enforcement; waiting until a "
        "dispute ('she said I copied her!') to introduce the "
        "concept — the developmental window for natural norm "
        "absorption is the everyday collaborative moment, not "
        "the conflict moment. "
        "The standard: the child has made something collaboratively "
        "and knows that both names belong on it. That is the "
        "whole skill at this age. The deeper concepts (remix, "
        "Creative Commons, copyright) are for the 10-12 row."
    ),
    en_ca_content=(
        "**When you make something with someone else, both "
        "names go on it.** If you and a friend draw a picture "
        "together, it is your picture *and* their picture. "
        "Not just yours. Both names. Always. That is what "
        "fair creators do.\n\n"
        "**Ideas come from people.** When you see something "
        "you love — a drawing, a song, a story — someone "
        "had that idea first. It came from their brain. "
        "That is pretty special. The person who made it "
        "deserves to be known as the person who made it.\n\n"
        "**When you use someone else's idea, you say so.** "
        "Not because you have to — because it is kind. "
        "You could say: 'I got this idea from [friend's name].' "
        "Or: 'I saw this in a book and tried it myself.' "
        "That is all it takes. It tells the other person: "
        "I noticed what you made. It was good enough that "
        "I wanted to try it too.\n\n"
        "**Borrowing an idea is not the same as stealing it.** "
        "If you draw a rainbow the same way your friend drew "
        "theirs, that is okay. Just say where you got the "
        "idea from. That makes everyone feel good — "
        "the person who had the idea, and you for being "
        "the kind of person who says so."
    ),
    ar_description=(
        "No AR application in Phase 1. Future opportunity: an AR "
        "experience where children see a collaborative drawing "
        "with both creators' names 'floating' above their "
        "contributions — making the abstract concept of shared "
        "authorship spatially concrete. Flag for Phase 2 AR sprint."
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
