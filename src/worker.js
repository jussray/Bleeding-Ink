// Bleeding Ink: static site served from assets, plus a daily heartbeat (cron).
export default {
  async fetch(request, env) {
    return env.ASSETS.fetch(request);
  },
  async scheduled(event, env, ctx) {
    const res = await env.ASSETS.fetch(new Request('https://bleeding-ink.internal/index.html'));
    const body = await res.text();
    const ok = res.status === 200 && body.includes('Bleeding Ink');
    console.log(JSON.stringify({ check: 'home-asset-heartbeat', cron: event.cron, status: res.status, ok, at: new Date(event.scheduledTime).toISOString() }));
  },
};
