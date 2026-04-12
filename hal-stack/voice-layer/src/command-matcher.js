/**
 * Two Birds Innovation — Voice Command Matcher
 * Takes raw text input, fuzzy-matches against command-map.json.
 * Pure JavaScript, no dependencies, L4-compatible.
 *
 * Usage:
 *   node command-matcher.js "run the next sprint please"
 *   → { action: "sprint", target: "next", trigger: "next sprint", confidence: 1 }
 */

const fs = require('fs');
const path = require('path');

// Load command map
const mapPath = path.join(__dirname, 'command-map.json');
const commandMap = JSON.parse(fs.readFileSync(mapPath, 'utf8'));

/**
 * Match raw text input against known commands.
 * Returns the best match or null.
 *
 * Matching strategy:
 * 1. Exact match (input IS the trigger)
 * 2. Contains match (input contains the trigger as a substring)
 * 3. Word match (trigger words appear in input in any order)
 *
 * Longer triggers are preferred over shorter ones to avoid
 * "next sprint" matching "next" instead of "next sprint".
 */
function matchCommand(rawText) {
  if (!rawText || typeof rawText !== 'string') return null;

  var input = rawText.toLowerCase().trim();
  if (!input) return null;

  // Sort commands by trigger length (longest first) to prefer specific matches
  var sorted = commandMap.commands.slice().sort(function (a, b) {
    return b.trigger.length - a.trigger.length;
  });

  // Pass 1: exact match
  for (var i = 0; i < sorted.length; i++) {
    if (input === sorted[i].trigger) {
      return makeResult(sorted[i], 1.0);
    }
  }

  // Pass 2: input contains trigger as substring
  for (var i = 0; i < sorted.length; i++) {
    if (input.indexOf(sorted[i].trigger) !== -1) {
      return makeResult(sorted[i], 0.9);
    }
  }

  // Pass 3: all trigger words appear in input (any order)
  for (var i = 0; i < sorted.length; i++) {
    var triggerWords = sorted[i].trigger.split(' ');
    var allFound = true;
    for (var j = 0; j < triggerWords.length; j++) {
      if (input.indexOf(triggerWords[j]) === -1) {
        allFound = false;
        break;
      }
    }
    if (allFound) {
      return makeResult(sorted[i], 0.7);
    }
  }

  return null;
}

function makeResult(cmd, confidence) {
  var result = {
    action: cmd.action,
    trigger: cmd.trigger,
    description: cmd.description,
    confidence: confidence
  };
  if (cmd.target) result.target = cmd.target;
  return result;
}

// --- CLI mode: run with node command-matcher.js "some text" ---
if (require.main === module) {
  var testInputs = process.argv.slice(2);

  if (testInputs.length === 0) {
    // Run default test suite
    testInputs = [
      'next sprint',
      'run the next sprint please',
      'retro',
      'show me the retro',
      'state',
      'what is the current state',
      'dashboard',
      'can you push',
      'stop everything',
      'capture this idea'
    ];
    console.log('Running test suite with ' + testInputs.length + ' inputs:\n');
  }

  testInputs.forEach(function (input) {
    var result = matchCommand(input);
    if (result) {
      console.log('INPUT:  "' + input + '"');
      console.log('MATCH:  ' + result.action + ' (trigger: "' + result.trigger + '", confidence: ' + result.confidence + ')');
      console.log('');
    } else {
      console.log('INPUT:  "' + input + '"');
      console.log('MATCH:  (no match)');
      console.log('');
    }
  });
}

module.exports = { matchCommand: matchCommand };
