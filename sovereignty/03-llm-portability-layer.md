# 03 — LLM Portability Layer

**Date:** April 1, 2026
**Objective:** A single configuration switch that moves Career Coach and Clarity between Claude, GPT-4o, Gemini, and Ollama without changing application code.

---

## Current State

Both products call the Anthropic API directly:

- **Clarity** (`clarity/index.html`, line ~889): `fetch('https://api.anthropic.com/v1/messages', ...)` using `claude-sonnet-4-20250514`
- **Career Coach** (`career-coach/index.html`, line ~1252): `fetch(API_URL, ...)` using `claude-haiku-4-5-20251001`

Both use:
- `x-api-key` header
- `anthropic-version: 2023-06-01`
- `anthropic-dangerous-direct-browser-access: true`
- Messages format: `[{ role: 'user', content: prompt }]`
- User-provided API key stored in localStorage

---

## Design: Provider Abstraction

A single JS file (`llm-provider.js`) that both products include. All API-specific logic lives here. Application code calls one function: `llmChat(prompt)`.

### The Abstraction Pattern

```javascript
/**
 * LLM Portability Layer — Two Birds Innovation
 * Drop this file into any static HTML project.
 * Configure provider in localStorage or in the config object below.
 */

const LLM_PROVIDERS = {
  anthropic: {
    name: 'Claude (Anthropic)',
    url: 'https://api.anthropic.com/v1/messages',
    defaultModel: 'claude-sonnet-4-20250514',
    keyName: 'x-api-key',
    buildHeaders: function(apiKey) {
      return {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
        'anthropic-dangerous-direct-browser-access': 'true'
      };
    },
    buildBody: function(model, prompt, maxTokens) {
      return JSON.stringify({
        model: model,
        max_tokens: maxTokens || 2048,
        messages: [{ role: 'user', content: prompt }]
      });
    },
    parseResponse: function(data) {
      return data.content[0].text;
    }
  },

  openai: {
    name: 'GPT-4o (OpenAI)',
    url: 'https://api.openai.com/v1/chat/completions',
    defaultModel: 'gpt-4o',
    keyName: 'Authorization',
    buildHeaders: function(apiKey) {
      return {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apiKey
      };
    },
    buildBody: function(model, prompt, maxTokens) {
      return JSON.stringify({
        model: model,
        max_tokens: maxTokens || 2048,
        messages: [{ role: 'user', content: prompt }]
      });
    },
    parseResponse: function(data) {
      return data.choices[0].message.content;
    }
  },

  gemini: {
    name: 'Gemini (Google)',
    url: 'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent',
    defaultModel: 'gemini-2.0-flash',
    keyName: 'query',
    buildHeaders: function(apiKey) {
      return { 'Content-Type': 'application/json' };
    },
    buildUrl: function(model, apiKey) {
      return 'https://generativelanguage.googleapis.com/v1beta/models/'
        + model + ':generateContent?key=' + apiKey;
    },
    buildBody: function(model, prompt, maxTokens) {
      return JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }],
        generationConfig: { maxOutputTokens: maxTokens || 2048 }
      });
    },
    parseResponse: function(data) {
      return data.candidates[0].content.parts[0].text;
    }
  },

  ollama: {
    name: 'Ollama (Local)',
    url: 'http://localhost:11434/api/chat',
    defaultModel: 'llama3',
    keyName: null,
    buildHeaders: function(apiKey) {
      return { 'Content-Type': 'application/json' };
    },
    buildBody: function(model, prompt, maxTokens) {
      return JSON.stringify({
        model: model,
        messages: [{ role: 'user', content: prompt }],
        stream: false
      });
    },
    parseResponse: function(data) {
      return data.message.content;
    }
  }
};

/**
 * Main chat function — call this from application code.
 * @param {string} prompt - The user prompt
 * @param {object} opts - Optional: { provider, model, apiKey, maxTokens }
 * @returns {Promise<string>} - The LLM response text
 */
async function llmChat(prompt, opts) {
  opts = opts || {};
  var providerKey = opts.provider
    || localStorage.getItem('llm_provider')
    || 'anthropic';
  var provider = LLM_PROVIDERS[providerKey];
  if (!provider) throw new Error('Unknown LLM provider: ' + providerKey);

  var apiKey = opts.apiKey
    || localStorage.getItem('llm_api_key')
    || '';
  var model = opts.model
    || localStorage.getItem('llm_model')
    || provider.defaultModel;
  var maxTokens = opts.maxTokens || 2048;

  var url = provider.buildUrl
    ? provider.buildUrl(model, apiKey)
    : provider.url;
  var headers = provider.buildHeaders(apiKey);
  var body = provider.buildBody(model, prompt, maxTokens);

  var response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: body
  });

  if (!response.ok) {
    var errText = await response.text();
    throw new Error(provider.name + ' error (' + response.status + '): ' + errText);
  }

  var data = await response.json();
  return provider.parseResponse(data);
}

/**
 * Set provider configuration in localStorage.
 * @param {string} providerKey - 'anthropic', 'openai', 'gemini', or 'ollama'
 * @param {string} apiKey - The API key for that provider
 * @param {string} model - Optional model override
 */
function llmSetProvider(providerKey, apiKey, model) {
  localStorage.setItem('llm_provider', providerKey);
  if (apiKey) localStorage.setItem('llm_api_key', apiKey);
  if (model) localStorage.setItem('llm_model', model);
}
```

---

## Integration into Existing Products

### Clarity — Migration Steps

1. Add `<script src="llm-provider.js"></script>` before the closing `</body>` tag
2. Replace the direct `fetch('https://api.anthropic.com/v1/messages', ...)` call (~line 889) with:
   ```javascript
   var result = await llmChat(prompt, { maxTokens: 4096 });
   ```
3. Migrate API key storage:
   ```javascript
   // On page load, migrate old key format
   var oldKey = localStorage.getItem('clarity_api_key');
   if (oldKey && !localStorage.getItem('llm_api_key')) {
     llmSetProvider('anthropic', oldKey);
   }
   ```
4. Add a provider dropdown to the settings UI (optional — can default to Anthropic)

### Career Coach — Migration Steps

1. Add `<script src="llm-provider.js"></script>` before the closing `</body>` tag
2. Replace both `fetch(API_URL, ...)` calls (~lines 1507, 1758) with:
   ```javascript
   var result = await llmChat(userMsg);
   ```
3. Migrate API key: same pattern as Clarity, using `cc_api_key` as the old key name
4. Career Coach uses Haiku — set default model override:
   ```javascript
   llmSetProvider('anthropic', apiKey, 'claude-haiku-4-5-20251001');
   ```

---

## Testing Checklist

- [ ] Anthropic: both products work as they do today
- [ ] OpenAI: swap provider, enter GPT-4o key, verify response quality
- [ ] Ollama: install locally (`ollama pull llama3`), test with no API key needed
- [ ] Gemini: swap provider, enter Google AI key, verify response
- [ ] Error handling: bad key shows clear error message, not a crash
- [ ] Key migration: old keys carry over without user action

---

## When to Implement

**Trigger:** Any of these events:
- Anthropic raises API prices by more than 20%
- Anthropic introduces rate limits that affect Clarity or Career Coach usage
- A client requests a non-Anthropic provider
- Aaron wants to demo products offline using Ollama

**Effort:** ~2 hours to implement across both products. The abstraction code above is ready to copy.
