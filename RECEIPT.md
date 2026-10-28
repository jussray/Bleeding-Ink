# Handoff receipt: Bleeding Ink Tattoo site draft

Fingerprint: repo:jussray/Bleeding-Ink|branch:draft/site-v4-keyvisual|head:3165c5c902c8985674ce0ad337d70ae5e0ce0fe0|subject:tattoo-shop-site/index.html|evidence:sha256=db653c3960a6e7c28521ee1b69514d2a1a8bdcf5253f20fbcaabd7ff8f43fb75|runtime:workers-build-23bdbae8-preview-failed-2026-10-28
Proof cookie: 7aaad3cac4f7e111
Scope: draft only. Draft PR #3 on branch draft/site-v4-keyvisual. No merge, no production deploy, no publish by this receipt.

Build status (2026-10-28)
- Workers build 23bdbae8 (draft branch, commit 3165c5c) failed. Cause: the non-main build ran `npx wrangler preview`, and Wrangler stopped with "Your Wrangler configuration needs a `previews` block". The failed step was the preview deploy, so nothing was published.
- The live Worker's production trigger remains scoped to `main` with `npx wrangler deploy`; preview builds were enabled at audit start.
- Fix applied on 2026-10-28: Cloudflare Worker-level Builds configuration `previews_enabled` changed from `true` to `false` using the supported API. Read-back confirmed `false`, with production branch `main` and deploy command unchanged. The historical failed preview builds remain historical; no new branch push has been used to prove trigger suppression.
- Draft metadata fix: `index.html` commit `bb3faf7ec6c5d250deb0cb5cd2d8e9b7a533282f` removed unverified LocalBusiness JSON-LD, placeholder canonical/social URLs, and an uncreated OG image reference. Kept `noindex,nofollow`, hero graphics, smoke and booking dialog. Production `main` was not changed.
- Live `main` page still shows bracketed placeholders. Rollback target not confirmed. Owner decision: keep, roll back, or take down.

## Live browser verification (2026-10-28)

Target: deployed Cloudflare Worker at the `bleeding-ink` workers.dev subdomain. This verifies live production behavior, not that the draft-branch code was deployed.

- Cloudflare headless browser rendering at 390×844 (mobile) and 1280×800 (desktop): page and hero loaded; all fragment-navigation targets existed.
- At both widths: navigation control opened and closed when activated; booking placeholder opened the configured dialog and its dismissal closed it; selecting Violet set `aria-pressed=true` and updated the tone label.
- Four live images decoded at both viewport sizes: `/assets/skeleton-machine-cutout.webp`, `/img/key-visual.jpg`, `/assets/sign-detail.webp`, and `/img/baskets.jpg`. Their image natural widths were nonzero.
- No horizontal document overflow at either viewport and no captured script errors during the tested interactions.
- The live page still contains `https://[domain]/` canonical metadata and placeholder business JSON-LD. These were corrected **only in draft PR #3**, not production.
- Playwright Chromium was launched locally and a live navigation was attempted; `Page.goto` was blocked by the sandbox network policy (`net::ERR_BLOCKED_BY_ADMINISTRATOR`). Therefore **no live-site Playwright pass is claimed**. Test execution in a network-authorized Playwright runner remains required for a Playwright-specific gate.
- Release remains held pending owner-confirmed address, artist details/consent, booking URL, rights, reviews/listing policy, and a verified public launch decision.


Decided
- Static HTML over a React artifact bundle, for crawlability by search and AI engines.
- Black hero. The skeleton-machine cutout (transparent) sits over live smoke, so smoke shows through the art and behind the glass cards.
- Smoke palette changes on each ink-drop (SILVER, MOONLIT, VIOLET, BLUE). The INK title and the drip keep brand red. Reduced motion holds on SILVER.
- Smoke palette and cutout come from the attached V4 smoke-first build. That build's README says the palette does not cycle; this draft diverges on purpose, per the latest request for color to change with the drip.
- Key image (img/key-visual.jpg) sits in its own band below the hero.
- Shop photos in use: sign (approved) and baskets (approved). Interior photo not used until cropped.
- Placeholder copy is bracketed and stays until the owners confirm the facts.
- Booking via a hosted tool. Placeholder until the owners choose one.
- noindex stays on until LAUNCH-GATE.md clears.
- Rollbacks kept: /home/claude/tattoo-shop-site-pre-zip-merge-backup.html (before this merge), /home/claude/tattoo-shop-site-keyvisual-hero-backup.html (the red-haze hero).
- Superseded v3 kept at /home/claude/tattoo-shop-site-v3-superseded.html.

Open
- Owners' facts UNKNOWN: artists, prices, deposit, policies, hours, city, state, ZIP. Address (500 Galleria Drive) and phone (215-980-1386) supplied by Juss 2026-10-28; owners to confirm. Owner named by Juss: Leak.
- Booking tool choice. UNKNOWN.
- Photo rights: 3 of 9 reviewed; 6 UNKNOWN. Interior photo needs a crop or reshoot.
- Hero cutout provenance and AI-generation status UNKNOWN (from the attached zip).
- img/og-1200x630.jpg not created; og:image points to it.
- Font rendering not verified in sandbox (Pirata One, Cinzel, DM Sans). UNKNOWN.
- Schema conflict: the attached zip's checklist keeps schema out of the launch; this draft keeps TattooParlor JSON-LD per LAUNCH-GATE section 4. Decide before launch.
- Trademark and name check not run.
- SEO/GEO research delivered: /home/claude/reports/Tattoo studio SEO and GEO evidence.md

Next gate: owners' answers and the booking tool link. Repo jussray/Bleeding-Ink holds a draft PR for this build (branch draft/site-v4-keyvisual). Do not merge.
Rollback: copy /home/claude/tattoo-shop-site-pre-zip-merge-backup.html over index.html and delete assets/skeleton-machine-cutout.webp to undo this merge.
