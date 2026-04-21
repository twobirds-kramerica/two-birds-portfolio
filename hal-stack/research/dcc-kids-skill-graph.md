# DCC Kids Research Database — Skill-Graph Index

**Status snapshot:** 20 rows live as of 2026-04-21.
**Notion source:** `DCC Kids Version — Research Database`
(data source `e184382b-b59a-41e7-9152-d90fbee1abe6`).
**Sprint batch:** S-R01-PHASE-1 (Phase-1 target met at 20 rows).
**This document:** bird's-eye view of the database so a reviewer (Aaron,
Brenda, a pilot teacher, a future advisor) can see the skill graph
without opening 20 Notion pages individually.

All 20 rows are **Status=Research** awaiting content review. Every
row has 22 columns populated; citations are verified via WebSearch
against primary government / academic / established-educator
sources.

---

## 1. Coverage matrix — 20/20 cells covered

Rows per `(Age bracket × Category)` cell. Bold = second row in that
cell (added for skill-graph depth, not grid coverage).

| | Tech-Safety | Learning | Emotional-Safety | Critical-Thinking | Creative-Making |
|---|---|---|---|---|---|
| **4-6** | Secret stuff and share stuff | Real / pretend / maybe-made-up pictures | Who is my safe grown-up? | True things and story things | Making my own thing first, then watching |
| **7-9** | **Pause and show when an app asks** | Asking good questions when I search or ask AI `*` | Telling a grown-up when something online feels weird | Is this an ad, or did they really mean it? `*` | Making something useful for someone else |
| **10-12** | **Using a password manager** | Asking good questions when I search or ask AI `*` | **Stepping out of a group pile-on** | Is this an ad, or did they really mean it? `*` | **When I remix, I name who made the original** |
| **10-12** | Creating a strong password I can remember `*` | | Spotting a "please don't tell your parent" message | | Making a story with AI as my helper `*` |
| **13-15** | **Turning on two-factor authentication** | **Using AI as a tutor that grows me** | **Sextortion: what to do if someone pressures me** | **Lateral reading + AI check** | Making a story with AI as my helper `*` |
| **13-15** | Creating a strong password I can remember `*` | Asking good questions when I search or ask AI `*` | Spotting a "please don't tell your parent" message | Is this an ad, or did they really mean it? `*` | |

`*` = multi-age row (one entry covers multiple age brackets).
**Bold** = new row shipped 2026-04-21 (S-R01-PHASE-1c through 1l).

**Grid cell totals**: 4 × 5 = 20 cells, all covered. Second-row depth
in 8 cells (Tech-Safety at 7-9/10-12/13-15; Emotional-Safety at
10-12/13-15; Critical-Thinking at 13-15; Creative-Making at 10-12;
Learning at 13-15).

---

## 2. Three age-spanning ladders

Each ladder walks from 4-6 through 13-15 with one skill per age
bracket. Designed so a child progressing through the curriculum
acquires the same competency at a developmentally-matched level of
abstraction.

### 2a. Tech-Safety ladder

```
4-6   Secret stuff and share stuff
        ↓  (foundational distinction of what info is personal)
7-9   Pause and show a grown-up whenever an app asks
        ↓  (one-rule scaffolding; permissions habit installed)
10-12 Using a password manager so every account gets its own password
        ↓  (direct prerequisite — without unique passwords, 2FA is weaker)
13-15 Turning on two-factor authentication on the accounts I care about
```

### 2b. Emotional-Safety ladder

```
4-6   Who is my safe grown-up?
        ↓  (identify adults the child can tell)
7-9   Telling a grown-up when something online feels weird
        ↓  (gut-feeling → specific action; 4-grown-ups list maintained)
10-12 Stepping out of a group pile-on (without becoming the next target)
       +  Spotting a "please don't tell your parent" message
        ↓  (peer threat ladder + adult-predator pattern-recognition)
13-15 What to do if someone pressures me to send a picture (sextortion)
```

Explicit precursor chain: the 10-12 grooming skill depends on the
7-9 "tell a grown-up" skill being solid; the 13-15 sextortion skill
depends on the 10-12 grooming skill being solid; and all three
depend on the 4-6 "safe grown-up" skill being solid.

### 2c. AI-literacy / info-environment ladder

```
4-6   Real, pretend, and maybe-made-up pictures
        ↓  (visual foundation: pictures can be AI-made)
7-9   Telling a grown-up when something online feels weird
        ↓  (uncomfortable-gut → action, same skill as Emotional-Safety)
10-12 Is this an ad, or did they really mean it?
        ↓  (media-literacy layer: commercial vs editorial intent)
13-15 Reading around something before I believe it (lateral reading + AI check)
       +  Using AI as a tutor that grows me, not a shortcut
```

The 4-6 visual row is the root: kids who absorb "pictures can be
computer-made" at 5 have a cognitive hook for every later layer.
The 13-15 capstone pair (lateral reading + AI tutor) operationalises
the ladder into two specific 2026 practices.

---

## 3. Prerequisite + reinforcement graph

Beyond the three ladders, additional cross-links between rows.
Each row's Creator-Luring-Awareness and Example-Activity fields
name the connections explicitly; this is the consolidated view.

### Prerequisite (→ = required before)

- `Using a password manager` (10-12) **→** `Turning on 2FA` (13-15)
  Without unique per-account passwords, 2FA only patches the hole
  the password would have caused.

- `Pause and show when an app asks` (7-9) **→** all later Tech-Safety
  The permissions-habit prevents accidental camera/mic/location
  grants that later Tech-Safety skills would have to remediate.

- `Telling a grown-up when something feels weird` (7-9) **→** both
  `Please-don't-tell-your-parent` (10-12) **and** `Sextortion` (13-15)
  The act of telling needs to be routine and non-punished BEFORE
  the specific threat-pattern is recognisable to the child.

- `Real / pretend / maybe-made-up pictures` (4-6) **→**
  `Lateral reading + AI check` (13-15)
  The primitive concept "a computer can make a picture that looks
  real" is the cognitive seed for later AI detection.

- `True things and story things` (4-6) **→**
  `Is this an ad?` (7-9+) **→**
  `Lateral reading` (13-15)
  Claim-evaluation foundation walks from 4-6 TRUE/STORY vocabulary
  to 10-12 ad-literacy to 13-15 professional-fact-checker technique.

### Reinforcement (↔ = both rows strengthen each other)

- `Making my own thing first` (4-6) **↔** `Making something useful for
  someone else` (7-9) **↔** `When I remix, I name the original`
  (10-12) **↔** `Making a story with AI as my helper` (10-12, 13-15)
  The Creative-Making ladder is less hierarchical than Tech-Safety;
  each row adds audience-awareness, attribution ethics, or tool-use
  to the prior foundation.

- `Using AI as a tutor` (13-15) **↔** `Lateral reading + AI check`
  (13-15) **↔** `Asking good questions when I search or ask AI`
  (7-9 / 10-12 / 13-15)
  The three AI-interaction rows form a cluster where each
  reinforces the others. Kids who have the "protégé test" reflex
  from the tutor row are less likely to accept AI's first answer
  during a lateral-reading check.

### Indirect protection

Some rows don't directly address online threats but create
conditions that make threats harder to land:

- `Making my own thing first` (4-6) reduces susceptibility to later
  influencer / unboxing / parasocial-pull content.
- `When I remix, I name the original` (10-12) embeds the child in
  an attribution-visible community where groomers' "don't mention
  me" script has a harder environment to gain traction.
- `Stepping out of a pile-on` (10-12) creates defender-posture
  that makes the child a friction point in coordinated harassment
  campaigns (including those with outside adversary seeding).

---

## 4. Research-citation roll-up

Sources cited across the 20 rows, grouped by category. Every source
was verified via WebSearch at composition time. URLs are public.

### Child development & cognitive frameworks

- **Piaget** — preoperational (2-7), concrete-operational (7-11),
  formal-operational (11+) stages. Used in 9 rows as the
  developmental-matching frame. Paraphrase-level citations from
  textbook-standard secondary sources; see follow-up TODO for
  upgrade to primary (Piaget 1952 / 1977 publications).
- **Erikson** — industry-vs-inferiority (6-11), identity-vs-role-
  confusion (12-18). Used in 5 rows.
  [StatPearls / NCBI NBK556096](https://www.ncbi.nlm.nih.gov/books/NBK556096/),
  [Simply Psychology summary](https://www.simplypsychology.org/erik-erikson.html).
- **Vygotsky** — zone of proximal development, scaffolding. Used
  in 4 rows, especially as justification for caregiver-mediated
  practice.
- **Kohlberg** — pre-conventional / conventional / post-conventional
  moral stages. Used in the pile-on row to justify the affiliation-
  preserving framing.
- **Bandura** — moral disengagement research. Used in the pile-on
  row + sextortion row to name the diffusion-of-responsibility and
  shame-isolation mechanisms.
- **Slamecka & Graf (1978)** — generation effect.
  **Roediger & Karpicke (2006)** — retrieval practice.
  **Fiorella & Mayer (2013+)** — protégé effect.
  Together cited in the AI-tutor row as the evidence base for
  move 1 (answer first) and move 4 (protégé test).

### Government / authoritative agency

- **CISA** — Require Multifactor Authentication, Require Strong
  Passwords, Cyber Safety for Teens, Use a Password Manager training.
  Used across the Tech-Safety ladder.
- **NIST** — SP 800-63B Digital Identity Guidelines. Used in the
  password manager + 2FA rows.
- **FTC** — COPPA Rule + FAQ + 2024 Federal Register update. Used
  in the 7-9 app permissions row.
- **FBI** — Sextortion info + Financially Motivated Sextortion
  Threat stories. Used in the sextortion row with 2024 stats
  (55,000+ reports, $33.5M losses, 59% YoY, 20+ teen suicides
  2021-2023).
- **FinCEN** — Notice on Financially Motivated Sextortion
  (September 2025). Used in the sextortion row.
- **UNESCO** — Deepfakes and the crisis of knowing. Used in the
  lateral-reading row.
- **Public Safety Canada** — Overview of Approaches to Address
  Bullying and Cyberbullying + STOPit Summary Report. Used in
  the pile-on row.
- **Office of the Privacy Commissioner of Canada (OPC) + PIPEDA** —
  Canadian privacy context for the 7-9 app permissions row.

### Canadian-specific educator / civil-society

- **MediaSmarts Canada** — Media Safety Tips for Middle Childhood,
  Communicating Safely Online, A Guide for Trusted Adults, Sexual
  Exploitation Safety Tips. Used in 4 rows (7-9 emotional safety,
  10-12 grooming, sextortion, app permissions).
- **Kids Help Phone** (kidshelpphone.ca, 1-800-668-6868, text
  686868). Named as the Canadian 24/7 escalation channel in the
  pile-on row.
- **PREVNet** — Canadian national research/knowledge mobilisation
  hub on bullying. Used in the pile-on row.

### US educator / civil-society

- **Common Sense Media + Common Sense Education** — age rating
  guidance (2-4, 5-7), digital citizenship curriculum, COPPA
  explainer, Privacy & Security topic, Upstanders and Allies lesson,
  Copyright & Creative Commons classroom materials. Used in 10+ rows.
- **NCMEC** — Take It Down service (takeitdown.ncmec.org), main
  sextortion page, NetSmartz topic page, CyberTipline (report.
  cybertip.org), No FILTR campaign, 2024 sextortion data release.
- **News Literacy Project** — Teaching About AI, Checkology virtual
  classroom (Algo + Gen characters), RumorGuard series, The Sift.
- **Stanford History Education Group (SHEG)** — Civic Online
  Reasoning, lateral-reading research. Primary empirical finding
  (6 x 50-min lessons doubled high-schoolers' accuracy) cited in
  the lateral-reading row.
- **Copyright & Creativity** — Elementary K-6 curriculum.
- **Cyberbullying Research Center**.
- **Lessig, Lawrence** — *Remix: Making Art and Commerce Thrive in
  the Hybrid Economy* (2008). Used in the 10-12 remix-credit row.
- **Creative Commons** — official license documentation. Used in
  the 10-12 remix-credit row.

### 2024-2025 primary research

- **Dartmouth (Nov 2025)** — AI personalized learning at scale;
  names "illusion of mastery" cognitive-outsourcing effect.
- **Nature Scientific Reports (2025)** — RCT showing AI tutoring
  outperforms in-class active learning when designed around learning-
  science principles. Used in the AI-tutor row.
- **Khan Academy Khanmigo efficacy (Nov 2024)** — students using
  Khanmigo show better conceptual understanding than those using
  answer-checking tools; reach grew 68K → 700K in one year.
- **Frontiers in Education (2025)** — cognitive-mirror framework
  for AI-powered metacognition.
- **Huang & Hu 2025, SAGE** — "A Warning is Not Enough. Teach Me How
  to Spot Deepfakes" intervention study. Used in the lateral-reading
  row.
- **Journal of Youth and Adolescence (2025)** — Trajectories of
  Bystander Behaviors in Bullying during Secondary Education. Used
  in the pile-on row.
- **Sharon & Woolley (PMC3689871)** — Revisiting Fantasy-Reality
  Distinction. Used in the 4-6 "True things" row.
- **Schonert-Reichl et al. (PMC3790250)** — Middle Years Development
  Instrument. Used in the 7-9 making-for-someone row.

### Vendor / industry

- **Apple App Store Kids Category** — ages 5-under / 6-8 / 9-11
  requirements. Referenced in the 7-9 app permissions row.
- **Google Play Families** — equivalent requirements.
- **Bitwarden + 1Password Families** — recommended password
  managers per CISA's "Use a Password Manager" training.

---

## 5. How to use this document

### For Aaron (primary reviewer)
1. Read the matrix in §1 for coverage at-a-glance.
2. Walk each ladder in §2 — pick the first row where the tone or
   framing feels off; everything below it is calibrated to that one,
   so a tone fix there cascades.
3. For individual rows, open the Notion page via the IDs in the DB
   itself (this doc keeps titles + positioning, not full content).
4. Advance rows from Status=Research → Spec when the content passes
   review. Spec is the hand-off point for Phase 2 (build).

### For a future reviewer (Brenda, teacher, advisor)
1. Start with the matrix; it's the whole curriculum.
2. The three ladders in §2 are the intended progression — a child
   who starts at 4-6 and moves through 13-15 should encounter these
   skills in the order shown.
3. The prerequisite graph in §3 is what makes the ladders actually
   work; skipping a prereq weakens everything downstream.
4. The citation roll-up in §4 is the provenance — every claim in the
   curriculum traces to one of these sources.

### For a developer (Phase 2 build)
1. Each row's Demonstration-Method + Example-Activity fields in
   Notion are the UX spec.
2. Each row's Gamification-Element is the engagement layer.
3. Each row's Media-Quality-Rubric is the do-no-harm guardrail.
4. Rows connected in §3 should be cross-linked in the final app so
   the child can follow the prerequisites.

---

## 6. Known follow-ups (from the session TODO list)

- **Piaget / Erikson primary-source upgrade** — 5 rows currently
  cite textbook-standard secondary sources for these frameworks.
  Low-priority polish pass would add direct publication cites
  (Piaget 1952 *The Origins of Intelligence in Children*; Erikson
  1950 *Childhood and Society*; Erikson 1968 *Identity: Youth and
  Crisis*) to the Research-Source fields.
- **fr-QC bilingual pass** — all 20 rows have fr-QC-Content stubbed
  per Phase 1c+ deferral. Full translation is a dedicated sprint.
- **Cybertip.ca reference in the sextortion row** — pair with the
  US-hosted Take It Down + FBI tips.fbi.gov with Canadian parallel.
- **Status advance Research → Spec** — human review required; 8
  rows reviewed as of 2026-04-21 would be the natural batch.

---

## 7. Session provenance

This database batch was built during a single 2026-04-21 max-mode
autonomous session (sprints S-030 through S-R01-PHASE-RETRO, 19
total). 12 new research rows shipped in that session (1c through
1l); 8 rows predated it. Every new row was composed with WebSearch-
verified citations and auto-filed via the `create_research_row`
helper shipped the same session (S-R01-INFRA, commit `f549242`).

The helper, schema, enums, and chunking logic all live in
`hal-stack/notion-sync/notion-client.py`; the per-sprint row
scripts are preserved as `_s_r01_phase_1c.py` through `1l.py` in
the same directory for reproducibility and audit.

**Commit range:** `bc06753` (first DCC commit of session) through
`5ec3b3b` (this document's precursor log). **Sprints without prior
Notion rows** were retro-filed via `_s_retro_file_2026_04_21.py`
(commit `deabcae`). **Paper trail** is intact end-to-end.
