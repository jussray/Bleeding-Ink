import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
const html = await readFile(new URL('../index.html', import.meta.url),'utf8');

test('preview is not indexable while business facts are unverified',()=>{
  assert.match(html,/<meta name="robots" content="noindex,nofollow">/);
});
test('mobile sign uses a fitted natural image instead of cover crop',()=>{
  assert.match(html,/\.intro-image img\{display:block;width:100%;height:auto;object-fit:contain/);
  assert.match(html,/\.image-caption\{position:static;display:block/);
});
test('hand and glass controls use the mobile document flow',()=>{
  assert.match(html,/\.hero-inner\{display:flex;flex-direction:column/);
  assert.match(html,/\.hero-art\{position:relative;top:auto;right:auto;width:100%/);
  assert.match(html,/\.hero-info\{position:relative;top:auto;left:auto;bottom:auto;width:100%/);
});
test('smoke can pause and supports three densities',()=>{
  assert.match(html,/id="smokePause"/);
  for(const level of ['whisper','cinema','storm'])assert.ok(html.includes('data-density="'+level+'"'));
  assert.ok(html.includes('reduced.matches||smokePaused'));
});
test('smoke colors remain manual, and core animation is present',()=>{
  assert.ok(!html.includes("drop.addEventListener('animationiteration'"));
  assert.ok(html.includes('drawWisps(time)'));
});
test('schema and crawler policies were not extended for this UI task',()=>{
  assert.ok(html.includes('application/ld+json')); // Existing, unchanged; not a new SEO feature.
  assert.ok(!html.includes('"@type": "FAQPage"'));
});

test('local build requires every image referenced by the page', async () => {
  const build = await readFile(new URL('../scripts/build.mjs', import.meta.url), 'utf8');
  const requiredLine = build.split('\n').find(line => line.trim().startsWith('const required = '));
  assert.ok(requiredLine, 'build must declare a required-file allowlist');
  const images = [...new Set([...html.matchAll(/src="((?:img|assets)\/[^"]+)"/g)].map(m => m[1]))];
  assert.ok(images.length >= 4, 'expected the actual site image references');
  for (const asset of images) {
    assert.ok(requiredLine.includes("'" + asset + "'"), 'build missing required image: ' + asset);
  }
});
