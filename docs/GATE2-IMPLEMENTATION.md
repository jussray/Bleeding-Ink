# Gate 2 — Mobile and smoke/glass design (approval-gated)

## Applied on feature branch only

- Keep the original storefront sign fully visible instead of cropping into its lettering.
- Place the caption beneath the sign image.
- Stack title → golden skeletal tattoo machine → glass information/smoke controls → palette footer on phones. No absolute overlap.
- Add smoke Pause/Resume and Whisper/Cinema/Storm controls; silver default; manual-only color changes.
- Keep film-black atmosphere and lighter glass so silver smoke remains visible.
- Preserve the existing `noindex`, unchanged JSON-LD, unchanged `robots.txt`, and all unverified business information.

## Cloudflare build preparation — not a deployment

`npm run build` stages only the explicitly allowed static website content under `dist/`.
`wrangler.jsonc` now targets the existing **`bleeding-ink` Worker** with `src/worker.js`, the `ASSETS` binding, daily `17 13 * * *` cron schedule, observability enabled, and Workers Static Assets staged at `./dist`.
The Cloudflare Git settings must run **build command `npm run build`** before the existing **deploy command `npx wrangler deploy`**; otherwise `dist/` will be missing.
The Worker name and handler were taken from the already-existing architecture in draft PR #3. This approval covers **branch configuration only**; actual Cloudflare build settings, Worker identity in the linked account, and deploy effects still require explicit owner verification and a separate deployment approval.

Do not deploy until owner facts and public listing/review links are verified and a separate release approval is given. The current site remains `noindex`.

## Verification and limits

Run `npm test` for source regression checks and `npm run build` to verify the static asset staging. Browser viewport and motion verification are still required against the actual GitHub branch before merge. No Cloudflare deployment or public business listing was modified.

## Evidence limits

Code checks establish structural properties, not a pixel-perfect iPhone Safari result. The 2026-10-28 Cloudflare failure was user-reported, not reproduced. No tattoo-specific SEO rank lift is claimed. Do not add FAQ rich-result markup, self-reviewed rating markup or `llms.txt` as an optimization.

## Deployment failure analysis (2026-10-28; historical evidence)

- **Worker build 23bdbae8**, commit `aafa6c1d9d9d46f19800105732c3e44482fe921e` is a **receipt commit about the failure**, not the failed deployment itself. The receipt says `npx wrangler preview` failed because Wrangler needed a `previews` block. The failed build's underlying commit was `3165c5c`. This is user/repository-reported evidence, not a fresh reproduction.
- **Later PR #3 receipt** states that the Worker-level `previews_enabled` setting was changed to `false` and read back as `false`. This is a recorded claim in GitHub, **not independently verified in the current Cloudflare account**. Historical failed builds cannot be turned into passing historical runs by changing configuration.
- **Earlier production build** ran `npx wrangler deploy` without finding a directory of static files. At the time of the original audit, PR #3 served `bleeding-ink` from the repository root with a Worker handler, while PR #4 proposed a different preview Worker with `dist/` assets. **Superseded on the feature branch by owner approval:** PR #4 now keeps PR #3's Worker name, exact handler, `ASSETS` binding, cron, and observability, while serving only the staged `dist/` directory. Production behavior has not been tested.
- **Architecture selected for draft PR #4:** preserve the existing Worker, handler, scheduled heartbeat, and observability; stage static assets under `dist/`. **Still blocked before merging:** reconcile PR #3's different asset-directory configuration and its metadata cleanup; verify the Cloudflare account/build command and preview trigger; secure separate approval for merge and deployment.

## Important source divergence — schema remains deferred

PR #3's newer draft `index.html` removed unverified JSON-LD and placeholder canonical/social metadata; that branch's `noindex` remains. PR #4 was created from `main` before that metadata cleanup and **still contains unverified structured data and placeholder metadata inherited from `main`**. PR #4 did not add or change the schema; nevertheless, a future merge can conflict with, or undo, PR #3's cleanup. Keep PR #4 in draft until this divergence is resolved under the listings-and-reviews-first policy. No schema ranking benefit is asserted.

## Added validation

The local build's required-file gate now covers `img/key-visual.jpg` and `img/baskets.jpg`, which were referenced by the page but missing from the previous required list. A repository test was authored for this invariant. Its code is committed; its execution on a fresh GitHub checkout and its Cloudflare behavior remain unverified.

## Worker architecture update — approved on feature branch, not deployed

**Source:** PR #3's `wrangler.jsonc` and `src/worker.js` were inspected through GitHub. The feature branch now combines its original Worker runtime with the static-asset staging approach:

| Property | Feature branch value | Evidence |
| --- | --- | --- |
| Worker name | `bleeding-ink` | Matches PR #3 |
| Entry point | `src/worker.js` | Byte-identical to PR #3 (Git blob `12bdca3e4a83d16a4e5545d929867b0d690f261b`) |
| Binding | `ASSETS` | Matches PR #3 |
| Cron | `17 13 * * *` | Matches PR #3 |
| Observability | `enabled: true` | Matches PR #3 |
| Public asset directory | `./dist` | Local allowlisted build from PR #4 |

**Test evidence, scope-limited:** Node v22 ran **4/4 Worker tests passing** in a local reconstruction of the exact committed Worker/config/test files (Git blob SHA checks matched). The checked fetch path delegates to ASSETS; scheduled success and failure both log expected JSON. `npm run build` also **passed using byte-identical build script in an isolated fixture**, staging eight sample public assets while excluding Worker source and private docs. These are **not** a full production checkout build, Wrangler dry-run, or deployment.

**Still required:** full repo checkout test run, `wrangler deploy --dry-run` (or an equivalent verified dry-run) and branch-specific browser validation; reconcile PR #3's root-assets configuration and approved metadata cleanup, confirm the actual Cloudflare Build settings, and obtain an explicit owner approval before any merge or deploy. Neither the existing account settings nor the live Worker was changed here.
