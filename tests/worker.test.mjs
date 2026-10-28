import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import worker from '../src/worker.js';

const configText = await readFile(new URL('../wrangler.jsonc', import.meta.url), 'utf8');
const config = JSON.parse(configText.replace(/^\s*\/\/.*$/gm, ''));

test('preserves existing Worker and binds only staged public assets', () => {
  assert.equal(config.name, 'bleeding-ink');
  assert.equal(config.main, 'src/worker.js');
  assert.equal(config.assets.directory, './dist');
  assert.equal(config.assets.binding, 'ASSETS');
  assert.equal(config.observability.enabled, true);
  assert.deepEqual(config.triggers.crons, ['17 13 * * *']);
});

test('fetch forwards incoming requests to the assets binding', async () => {
  const req = new Request('https://bleeding-ink.example/portfolio');
  const expected = new Response('site asset', { status: 200 });
  let forwarded;
  const actual = await worker.fetch(req, {
    ASSETS: {
      async fetch(request) { forwarded = request; return expected; },
    },
  });
  assert.equal(forwarded, req);
  assert.equal(actual, expected);
});

async function checkHeartbeat(status, text, expectedOk) {
  const hits = [];
  const logLines = [];
  const originalLog = console.log;
  console.log = line => { logLines.push(line); };
  try {
    await worker.scheduled(
      { cron: '17 13 * * *', scheduledTime: Date.UTC(2026, 9, 28, 13, 17) },
      { ASSETS: { async fetch(request) { hits.push(request.url); return new Response(text, { status }); } } },
      { waitUntil() { throw Error('Worker is not expected to enqueue extra work'); } },
    );
  } finally {
    console.log = originalLog;
  }
  assert.deepEqual(hits, ['https://bleeding-ink.internal/index.html']);
  assert.equal(logLines.length, 1);
  const logged = JSON.parse(logLines[0]);
  assert.equal(logged.check, 'home-asset-heartbeat');
  assert.equal(logged.cron, '17 13 * * *');
  assert.equal(logged.status, status);
  assert.equal(logged.ok, expectedOk);
  assert.equal(logged.at, '2026-10-28T13:17:00.000Z');
}

test('scheduled heartbeat logs success for the index asset', async () => {
  await checkHeartbeat(200, 'Bleeding Ink Tattoo', true);
});

test('scheduled heartbeat logs failure for missing index', async () => {
  await checkHeartbeat(404, 'not found', false);
});
