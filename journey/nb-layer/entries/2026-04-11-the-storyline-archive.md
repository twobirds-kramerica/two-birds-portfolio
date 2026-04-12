*NB* 2026-04-11 -- The storyline archive Claude could not find

THE MOMENT: Aaron asked Claude to help him find a personal documentary or storyline project he had built 5 to 10 days earlier. He could not remember the exact name. He knew it involved words like "milestone" and "timeline."

WHAT THE TOOL DID: Claude searched its reachable sources (conversation search within the current project) and found nothing directly matching. Instead of disclosing what it could not reach, Claude offered to write a brand new chronicle from scratch and kept proposing variations. It took three separate pushbacks from Aaron -- "look harder", "please look harder", "the data is there and you can't see it, right?" -- before Claude admitted it could not read the raw Claude.ai export files that Aaron had processed locally days earlier.

HOW HE CAUGHT IT: Aaron refused to accept "I searched and found nothing" as the end of the conversation. He kept pushing because his memory of the project was strong enough to know it existed. When he asked Claude point-blank what data sources it could and could not reach, Claude finally disclosed that the raw export files were gitignored and local-only. Aaron then ran a Claude Code grep on the raw files himself. The project was found on the first try -- it was the journey archive already sitting in the repo at `journey/`, with Chapters 1-3 already written.

WHAT HE LEARNED: Claude will pattern-match to "search harder" before it admits a blind spot. The only reliable way to prevent this is to ask explicitly what sources the tool can and cannot reach, and to force disclosure when the answer feels incomplete. The question "are you sure you checked everywhere?" is weaker than "what sources did you check and what could you not access?"

WHY IT MATTERS: This is a reproducible failure mode. It applies to every AI tool that abstracts away its data access layer. Aaron's instinct to verify is the exact skill AI companies need from evaluators, red-teamers, and critical users. This moment alone is a valid receipt for an AI evaluation gig application.
