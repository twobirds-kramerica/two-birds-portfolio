# LLM Switch Procedure — How to Change AI Provider

**Date:** April 4, 2026
**Applies to:** Career Coach, Clarity (both use `llm-provider.js`)

---

## Current Configuration

Both products default to Anthropic Claude:
- **Career Coach:** `claude-haiku-4-5-20251001` (3 API call sites)
- **Clarity:** `claude-sonnet-4-20250514` (1 API call site)

The LLM portability layer (`llm-provider.js`) abstracts all API calls. Switching provider requires **exactly 1 line of code** or **1 localStorage command in browser console**.

---

## Switch Procedure

### Option A — Change Default in Code (Permanent)

Edit `llm-provider.js` in the target repo. Find this line near the bottom:

```javascript
var providerKey = opts.provider || localStorage.getItem('llm_provider') || 'anthropic';
```

Change `'anthropic'` to `'openai'`, `'gemini'`, or `'ollama'`.

### Option B — Change via localStorage (Per-Browser, No Code Change)

Open the product in a browser. Open DevTools console (F12). Run:

```javascript
// Switch to OpenAI GPT-4o
llmSetProvider('openai', 'sk-your-openai-key-here');

// Switch to Google Gemini (free 1M tokens/min)
llmSetProvider('gemini', 'your-google-ai-key-here');

// Switch to Ollama (local, no key needed)
llmSetProvider('ollama');

// Switch back to Anthropic
llmSetProvider('anthropic', 'sk-ant-your-key-here');
```

### Option C — Emergency Switch (No API Key Available)

If no commercial API keys are available:

1. Install Ollama: download from [ollama.com](https://ollama.com)
2. Run: `ollama pull llama3`
3. Run: `ollama serve` (starts on port 11434)
4. Open the product in browser, open console, run: `llmSetProvider('ollama')`
5. All AI features now run locally. Quality is lower but functional.

---

## Provider Details

| Provider | Key Required | Free Tier | Model | Quality |
|----------|-------------|-----------|-------|---------|
| Anthropic | Yes (`sk-ant-*`) | No (pay-per-token) | claude-haiku/sonnet | Excellent |
| OpenAI | Yes (`sk-*`) | Limited | gpt-4o | Excellent |
| Gemini | Yes (Google AI key) | Yes — 1M tokens/min free | gemini-2.5-flash | Very good |
| Ollama | No | Unlimited (local) | llama3 | Good |

---

## Verification After Switch

After switching, test by running a diagnostic in Clarity or analysing a job in Career Coach. If the response comes back, the switch worked. If you get an error:

1. Check the browser console for error messages
2. Verify the API key is correct for the new provider
3. For Ollama: verify `ollama serve` is running (`curl http://localhost:11434`)

---

## Files Modified

- `career-coach/llm-provider.js` — shared provider abstraction
- `clarity/llm-provider.js` — identical copy
- No other files need changing when switching providers
