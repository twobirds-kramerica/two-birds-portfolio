# Voice Layer — Command Matcher

The keyword command matcher connects voice input (or text input) to the trigger commands defined in CLAUDE.md.

## How It Works

```
[Voice/Text Input] → command-matcher.js → matched action → CLAUDE.md trigger
```

1. Raw text comes in (from STT, or typed by Aaron)
2. `command-matcher.js` fuzzy-matches against `command-map.json`
3. Returns the matched action with a confidence score
4. The action maps to a CLAUDE.md trigger command

## Action → CLAUDE.md Trigger Mapping

| Action | CLAUDE.md Trigger | What Happens |
|--------|------------------|-------------|
| `sprint` | "next sprint" | Read sprint-queue.md, execute top READY sprint |
| `retro` | "retro" | Read and report logs/RETRO.md |
| `state` | "state" | Read SESSION-STATE.md, report top 3 actions |
| `dashboard` | "dashboard" | Read WIP-DASHBOARD.md, report portfolio status |
| `hal` | "hal" | Read HAL-BACKLOG.md, report next item |
| `journey` | "journey" | Read latest journey archive entry |
| `stop` | — | Stop current work, commit, push |
| `status` | — | Run git status |
| `commit` | — | Stage and commit changes |
| `push` | — | Push to origin |
| `backlog` | — | Read human-backlog.md |
| `capture` | — | Append item to pending-capture.md |

## Matching Strategy

1. **Exact match** (confidence 1.0) — input IS the trigger ("retro")
2. **Contains match** (confidence 0.9) — input contains trigger ("show me the retro")
3. **Word match** (confidence 0.7) — all trigger words appear in input in any order

Longer triggers are matched first to prevent "next sprint" matching just "next".

## Files

| File | Purpose |
|------|---------|
| `command-map.json` | Trigger definitions — add new commands here |
| `command-matcher.js` | Matching logic — pure JS, no dependencies |
| `README.md` | This file |

## Testing

```
node command-matcher.js                    # runs 10-input test suite
node command-matcher.js "your text here"   # tests a single input
```

## Layer Compatibility

**L4-native.** Pure JavaScript, no npm dependencies, no network calls. Runs on any machine with Node.js. The command map is a JSON file editable with any text editor.

## Adding New Commands

1. Add an entry to `command-map.json` with trigger, action, and description
2. If the action maps to a CLAUDE.md trigger, update the table above
3. Test with `node command-matcher.js "your new trigger"`

## Future: Voice Integration

When the STT component is built (Whisper API or Whisper.cpp), the flow becomes:

```
[Microphone] → STT → raw text → command-matcher.js → action → execute
```

The matcher doesn't care whether the text came from a keyboard or a microphone. It's the same interface.
