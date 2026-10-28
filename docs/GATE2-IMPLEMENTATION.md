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
