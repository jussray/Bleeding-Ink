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
`wrangler.jsonc` points Workers Static Assets to `./dist`.
The Cloudflare Git settings must run **build command `npm run build`** before the existing **deploy command `npx wrangler deploy`**; otherwise `dist/` will be missing.
The Workers project name in the draft config is a **placeholder preview name**. Confirm it with the account owner before enabling any deployment.

Do not deploy until owner facts and public listing/review links are verified and a separate release approval is given. The current site remains `noindex`.

## Verification and limits

Run `npm test` for source regression checks and `npm run build` to verify the static asset staging. Browser viewport and motion verification are still required against the actual GitHub branch before merge. No Cloudflare deployment or public business listing was modified.

## Evidence limits

Code checks establish structural properties, not a pixel-perfect iPhone Safari result. The 2026-10-28 Cloudflare failure was user-reported, not reproduced. No tattoo-specific SEO rank lift is claimed. Do not add FAQ rich-result markup, self-reviewed rating markup or `llms.txt` as an optimization.

## Deployment failure analysis (2026-10-28; historical evidence)

- **Worker build 23bdbae8**, commit `aafa6c1d9d9d46f19800105732c3e44482fe921e` is a **receipt commit about the failure**, not the failed deployment itself. The receipt says `npx wrangler preview` failed because Wrangler needed a `previews` block. The failed build's underlying commit was `3165c5c`. This is user/repository-reported evidence, not a fresh reproduction.
- **Later PR #3 receipt** states that the Worker-level `previews_enabled` setting was changed to `false` and read back as `false`. This is a recorded claim in GitHub, **not independently verified in the current Cloudflare account**. Historical failed builds cannot be turned into passing historical runs by changing configuration.
- **Earlier production build** ran `npx wrangler deploy` without finding a directory of static files. Two incompatible proposals now exist: PR #3 uses the existing `bleeding-ink` Worker with `src/worker.js`, asset binding and cron, serving from repository root; PR #4 uses a different preview Worker name with compiled `dist/` assets and no Worker handler. **No unified architecture is approved or tested.**
- **Decision required before merging any deployment config:** choose whether to preserve the existing Worker, its scheduled handler, and observability (PR #3 direction), or use static-assets-only deployment; confirm the account, Worker name, build command, Git trigger/preview setting and public deployment policy. Do not merge configurations together or deploy without new approval.

## Important source divergence — schema remains deferred

PR #3's newer draft `index.html` removed unverified JSON-LD and placeholder canonical/social metadata; that branch's `noindex` remains. PR #4 was created from `main` before that metadata cleanup and **still contains unverified structured data and placeholder metadata inherited from `main`**. PR #4 did not add or change the schema; nevertheless, a future merge can conflict with, or undo, PR #3's cleanup. Keep PR #4 in draft until this divergence is resolved under the listings-and-reviews-first policy. No schema ranking benefit is asserted.

## Added validation

The local build's required-file gate now covers `img/key-visual.jpg` and `img/baskets.jpg`, which were referenced by the page but missing from the previous required list. A repository test was authored for this invariant. Its code is committed; its execution on a fresh GitHub checkout and its Cloudflare behavior remain unverified.
