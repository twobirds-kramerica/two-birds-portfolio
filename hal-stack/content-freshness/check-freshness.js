/**
 * Two Birds Innovation — Content Freshness Checker
 * Scans HTML files for lastmod dates and checks against staleness rules.
 * Pure Node.js, no npm dependencies, L4-compatible.
 *
 * Usage:
 *   node check-freshness.js                        # scan DCC repo
 *   node check-freshness.js C:\twobirds\clarity    # scan specific repo
 */

var fs = require('fs');
var path = require('path');

// --- Staleness rules (days) ---
var rules = {
  'digital-confidence': { warning: 60, stale: 90 },
  'career-coach':       { warning: 90, stale: 180 },
  'clarity':            { warning: 90, stale: 180 },
  'two-birds-innovation': { warning: 120, stale: 180 },
  'aaron-patzalek':     { warning: 120, stale: 180 },
  'default':            { warning: 90, stale: 180 }
};

// --- Config ---
var targetDir = process.argv[2] || path.join(__dirname, '..', '..', '..', 'digital-confidence');
var repoName = path.basename(targetDir);
var rule = rules[repoName] || rules['default'];
var today = new Date();

console.log('Content Freshness Check');
console.log('=======================');
console.log('Repo: ' + repoName);
console.log('Path: ' + targetDir);
console.log('Warning threshold: ' + rule.warning + ' days');
console.log('Stale threshold: ' + rule.stale + ' days');
console.log('Date: ' + today.toISOString().substring(0, 10));
console.log('');

// --- Find HTML files ---
function findHtmlFiles(dir, fileList) {
  fileList = fileList || [];
  try {
    var files = fs.readdirSync(dir);
  } catch (e) { return fileList; }

  files.forEach(function(file) {
    var filePath = path.join(dir, file);
    try {
      var stat = fs.statSync(filePath);
      if (stat.isDirectory()) {
        // Skip hidden dirs, node_modules, .git
        if (file.startsWith('.') || file === 'node_modules') return;
        findHtmlFiles(filePath, fileList);
      } else if (file.endsWith('.html')) {
        fileList.push(filePath);
      }
    } catch (e) { /* skip inaccessible files */ }
  });
  return fileList;
}

// --- Extract lastmod from HTML ---
function extractLastmod(filePath) {
  var content;
  try { content = fs.readFileSync(filePath, 'utf8'); }
  catch (e) { return null; }

  // Check for freshness override
  if (content.indexOf('freshness-override') !== -1) return 'OVERRIDE';

  // Try meta tag: <meta name="lastmod" content="2026-04-01">
  var metaMatch = content.match(/<meta\s+name=["'](?:lastmod|last-modified|date)["']\s+content=["']([^"']+)["']/i);
  if (metaMatch) return new Date(metaMatch[1]);

  // Try HTML comment: <!-- lastmod: 2026-04-01 -->
  var commentMatch = content.match(/<!--\s*lastmod:\s*(\d{4}-\d{2}-\d{2})\s*-->/i);
  if (commentMatch) return new Date(commentMatch[1]);

  // Fallback: file modification time
  try {
    var stat = fs.statSync(filePath);
    return stat.mtime;
  } catch (e) { return null; }
}

// --- Calculate status ---
function getStatus(lastmod) {
  if (lastmod === 'OVERRIDE') return 'SKIP';
  if (!lastmod) return 'UNKNOWN';
  var diffMs = today - lastmod;
  var diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
  if (diffDays > rule.stale) return 'STALE';
  if (diffDays > rule.warning) return 'WARNING';
  return 'FRESH';
}

function daysSince(lastmod) {
  if (!lastmod || lastmod === 'OVERRIDE') return '—';
  return Math.floor((today - lastmod) / (1000 * 60 * 60 * 24));
}

// --- Run ---
var htmlFiles = findHtmlFiles(targetDir);
if (htmlFiles.length === 0) {
  console.log('No HTML files found in ' + targetDir);
  process.exit(1);
}

var results = { FRESH: 0, WARNING: 0, STALE: 0, SKIP: 0, UNKNOWN: 0 };
var staleFiles = [];
var warningFiles = [];

htmlFiles.forEach(function(filePath) {
  var relative = path.relative(targetDir, filePath);
  var lastmod = extractLastmod(filePath);
  var status = getStatus(lastmod);
  results[status]++;

  var days = daysSince(lastmod);
  var icon = status === 'FRESH' ? '✅' : status === 'WARNING' ? '⚠️' : status === 'STALE' ? '🔴' : status === 'SKIP' ? '⏭️' : '❓';

  if (status === 'STALE') staleFiles.push(relative);
  if (status === 'WARNING') warningFiles.push(relative);

  // Only print non-fresh items to keep output manageable
  if (status !== 'FRESH' && status !== 'SKIP') {
    console.log(icon + '  ' + status.padEnd(7) + ' | ' + String(days).padStart(4) + ' days | ' + relative);
  }
});

// --- Summary ---
console.log('');
console.log('Summary');
console.log('-------');
console.log('Total files: ' + htmlFiles.length);
console.log('✅ Fresh:   ' + results.FRESH);
console.log('⚠️  Warning: ' + results.WARNING);
console.log('🔴 Stale:   ' + results.STALE);
console.log('⏭️  Skipped: ' + results.SKIP);
console.log('❓ Unknown: ' + results.UNKNOWN);

if (staleFiles.length > 0) {
  console.log('');
  console.log('🔴 STALE FILES (need update):');
  staleFiles.forEach(function(f) { console.log('   - ' + f); });
}

if (warningFiles.length > 0) {
  console.log('');
  console.log('⚠️  WARNING FILES (aging):');
  warningFiles.forEach(function(f) { console.log('   - ' + f); });
}

// Exit code: 1 if any stale files found
process.exit(staleFiles.length > 0 ? 1 : 0);
