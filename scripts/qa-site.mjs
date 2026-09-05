#!/usr/bin/env node
/**
 * Static QA for Grand Turk World 2.0 (Families A–F).
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const fails = [];
const warns = [];

function fail(msg) {
  fails.push(msg);
}
function warn(msg) {
  warns.push(msg);
}

const mustPreserve = [
  'index.html',
  'best-beaches-in-grand-turk.html',
  'gibbs-cay-stingray-excursions.html',
  'governors-beach-excursions.html',
  'best-grand-turk-shore-excursions.html',
  'grand-turk-cruise-port-guide.html',
  'one-day-in-grand-turk.html',
  'grand-turk-beach-breaks.html',
  'grand-turk-snorkelling-tours.html',
  'grand-turk-island-tours.html',
  'grand-turk-golf-cart-tours.html',
  'grand-turk-lighthouse-tours.html',
  'grand-turk-private-tours.html',
  'grand-turk-family-excursions.html',
  'grand-turk-faq.html',
  'about.html',
  'contact.html',
  'privacy.html',
  'terms.html',
  'methodology.html',
  '404.html',
  'worker.js',
  'sitemap.xml',
  'robots.txt',
];

for (const f of mustPreserve) {
  if (!fs.existsSync(path.join(root, f))) fail(`Missing required file: ${f}`);
}

// No schedule page
if (fs.existsSync(path.join(root, 'schedule.html'))) fail('schedule.html must not exist in 8B');

const htmlFiles = fs.readdirSync(root).filter((f) => f.endsWith('.html'));
for (const f of htmlFiles) {
  const html = fs.readFileSync(path.join(root, f), 'utf8');
  if (!html.includes('data-inlined="true"') && f !== '404.html') {
    // 404 may still be inlined
  }
  if (!html.includes('<h1') && f !== '404.html') {
    // trust pages have h1 in content
    if (!html.includes('<h1')) fail(`${f}: missing H1 in delivered HTML`);
  }
  const canon = html.match(/rel="canonical" href="([^"]+)"/);
  if (canon) {
    if (canon[1].includes('.html')) fail(`${f}: canonical still has .html: ${canon[1]}`);
    if (!canon[1].startsWith('https://grandturkshoreexcursion.com')) {
      fail(`${f}: canonical host wrong: ${canon[1]}`);
    }
  } else {
    fail(`${f}: missing canonical`);
  }
  // Forbidden commercial / trust spam
  const banned = [
    />Book Now</i,
  /Book Now!/i,
    /Only \d+ left/i,
    /Selling Fast/i,
    /AggregateRating/,
    /"@type"\s*:\s*"Offer"/,
    /shoreexcursionsgroup/i,
    /viator\.com/i,
    /getyourguide/i,
    /stripe\.com/i,
  ];
  for (const re of banned) {
    if (re.test(html)) fail(`${f}: banned pattern ${re}`);
  }
  if (/Cruise-Friendly Returns/i.test(html)) fail(`${f}: unsupported Cruise-Friendly Returns claim`);
  if (/60[–-]90\s*min/i.test(html) && /buffer/i.test(html)) {
    warn(`${f}: check 60-90 buffer language`);
  }
  if (/friendly stingrays/i.test(html)) fail(`${f}: unsupported 'friendly stingrays' language`);
  if (/\b(?:glide around|swim at)\s+your feet\b/i.test(html)) {
    fail(`${f}: unsupported wildlife certainty language`);
  }
  // Primary content should be present without depending solely on empty slots
  if (f !== '404.html') {
    if (!html.includes('id="page-content"') || html.match(/id="page-content"[^>]*>\s*</)) {
      if (!html.includes('data-inlined="true"')) fail(`${f}: content may not be inlined`);
    }
  }
}

const sitemap = fs.readFileSync(path.join(root, 'sitemap.xml'), 'utf8');
if (sitemap.includes('.html')) fail('sitemap still lists .html URLs');
if (sitemap.includes('/schedule')) fail('sitemap lists /schedule');
for (const route of [
  'best-beaches-in-grand-turk',
  'gibbs-cay-stingray-excursions',
  'governors-beach-excursions',
  'about',
  'contact',
  'privacy',
  'terms',
  'methodology',
]) {
  if (!sitemap.includes(`/${route}</loc>`) && !sitemap.includes(`/${route}"`)) {
    if (!sitemap.includes(`grandturkshoreexcursion.com/${route}`)) {
      fail(`sitemap missing ${route}`);
    }
  }
}

// Images: no active 1x1 stubs referenced
const imgDir = path.join(root, 'images');
const stubs = [];
for (const f of fs.readdirSync(imgDir)) {
  if (!/\.(png|jpe?g|webp)$/i.test(f)) continue;
  const size = fs.statSync(path.join(imgDir, f)).size;
  if (size < 5000) stubs.push(`${f} (${size}b)`);
}
if (stubs.length) fail(`Active tiny/stub images: ${stubs.join(', ')}`);

// ATTRIBUTION exists
if (!fs.existsSync(path.join(imgDir, 'ATTRIBUTION.md'))) fail('images/ATTRIBUTION.md missing');

const allHtml = htmlFiles.map((f) => fs.readFileSync(path.join(root, f), 'utf8')).join('\n');
const imgRefs = [...allHtml.matchAll(/src="(images\/[^"]+)"/g)].map((m) => m[1]);
for (const ref of new Set(imgRefs)) {
  if (!fs.existsSync(path.join(root, ref))) fail(`Broken image ref: ${ref}`);
  const size = fs.statSync(path.join(root, ref)).size;
  if (size < 5000) fail(`Referenced stub image: ${ref} (${size}b)`);
}

// Best beaches must link to governors
const beaches = fs.readFileSync(path.join(root, 'best-beaches-in-grand-turk.html'), 'utf8');
if (!beaches.includes('/governors-beach-excursions')) {
  fail('Best Beaches must link to Governor\'s Beach page');
}
if (!beaches.includes('/gibbs-cay-stingray-excursions')) {
  fail('Best Beaches must link to Gibbs Cay');
}

const gibbs = fs.readFileSync(path.join(root, 'gibbs-cay-stingray-excursions.html'), 'utf8');
if (!/not guaranteed|cannot be guaranteed|never guaranteed|never promised/i.test(gibbs)) {
  fail('Gibbs Cay missing wildlife caveat');
}

const worker = fs.readFileSync(path.join(root, 'worker.js'), 'utf8');
if (!worker.includes('www.')) fail('worker missing www → apex redirect');
if (!worker.includes('.html')) fail('worker missing .html redirect');

console.log('Grand Turk QA');
if (warns.length) {
  console.log('Warnings:');
  warns.forEach((w) => console.log('  -', w));
}
if (fails.length) {
  console.log('FAIL:');
  fails.forEach((f) => console.log('  -', f));
  process.exit(1);
}
console.log('PASS');
