# Handoff receipt: Bleeding Ink Tattoo site draft

Fingerprint: repo:jussray/Bleeding-Ink|branch:draft/site-v4-keyvisual|head:60194fc0422f99a064ce9c662960842f0ae1ac20|subject:tattoo-shop-site/website/index.html|evidence:sha256=5a6b6e0b55d768354247a7f983409fd80c095518879582eba35b46f600a1fd8e|runtime:alt-text-playwright-desktop-mobile-reduced
Proof cookie: 188d32b40812707d
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
- Real-site Playwright Chromium verification **passed** in an isolated network-accessible browser runner on 2026-10-28 at 23:53:17 UTC (Chromium 153.0.8010.12). Mobile 390×844: 12/12 assertions passed. Desktop 1280×800: 11/11 assertions passed. Verified HTTP 200, correct H1, valid navigation anchors, no horizontal overflow, four decoded images, booking dialog open/close, tone selection, and responsive menu behavior. No browser page errors, console errors, or failed requests were captured. Screenshots and a JSON result were captured in the runner. The original local sandbox navigation was blocked by egress restrictions; it is superseded by this successful remote Playwright run.
- **Public exposure found in parallel:** `RECEIPT.md` and `LAUNCH-GATE.md` returned HTTP 200 on both the Cloudflare Worker and GitHub Pages hosts. The Worker also served `wrangler.jsonc` with HTTP 200. This violates the intended customer-facing Sauce Guard boundary. These are factual exposure checks, not evidence of stolen credentials.
- **Containment staged only in this draft PR:** `.assetsignore` commit `8c9e1915473ee307feba1a8ff913f3ecee0b40b5` switches to explicit public asset allowlisting. `_config.yml` commit `bc6ac99be3021697096a54079e77f042c9ebd2e3` excludes internal docs and Worker files from future Jekyll output. Git-style ignore pattern selection and YAML parsing were checked locally; actual deployment and Pages rebuild were NOT executed or certified. Both public exposures remain live until each hosting path is remediated and rechecked.
- **Post-merge correction (23:58 UTC):** PR #2 was merged by GitHub account `jussray` at 23:54:46 UTC, moving `main` to `b2ceae4df824e8d267697a737316a37556ba63dc`. Cloudflare automatically deployed this exact commit at approximately 23:55 UTC. On the new Worker, `RECEIPT.md`, `LAUNCH-GATE.md`, `wrangler.jsonc`, and `website/studio.json` now return HTTP 404; the live V4 page has two successfully loaded images, review sections, no business JSON-LD, and still has `noindex,nofollow`.
- **Playwright V4 recheck (23:58:20 UTC):** Chromium 153, same mobile (390×844) and desktop (1280×800) suite, passed 12/12 and 11/11 assertions with no captured browser errors or failed network requests. This supersedes the earlier Playwright pass against the previous production site.
- **Remaining public exposure:** GitHub Pages at `jussray.github.io/Bleeding-Ink` still returned 200 for root receipts, `wrangler.jsonc`, `website/studio.json`, and `website/build.py`. The newly staged `_config.yml` exclusion of root docs, Worker sources and the entire `website/` tree is committed at `81cb4b7aea02ac8075c17efa26f995a5068827ae`; it has not been merged or deployed to GitHub Pages.
- **Merge safety:** PR #3 remains a draft with a dirty merge state against the new `main`. Do not merge the old Worker root configuration over the deployed V4. Resolve host exposure and reconcile branch/base separately before considering deployment.
- **Next security gate:** Contain the still-public GitHub Pages source and receipt paths, recheck that they return 404 or 403, preserve the PR #3 draft hold, and require exact-head checks and owner launch facts before a release.
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
- img/og-1200x630.jpg is not created; the draft no longer points og:image at this missing file. Confirm rights and generate an approved image before release.
- Font rendering not verified in sandbox (Pirata One, Cinzel, DM Sans). UNKNOWN.
- Draft structured business schema has been removed until the shop identity, location, hours and site URL are confirmed. Validate approved markup before release.
- Trademark and name check not run.
- SEO/GEO research delivered: /home/claude/reports/Tattoo studio SEO and GEO evidence.md

Next gate: owners' answers and the booking tool link. Repo jussray/Bleeding-Ink holds a draft PR for this build (branch draft/site-v4-keyvisual). Do not merge.
Rollback: copy /home/claude/tattoo-shop-site-pre-zip-merge-backup.html over index.html and delete assets/skeleton-machine-cutout.webp to undo this merge.

## Implant 2026-10-28 (draft head 2c3082b)

Fixes implanted on draft/site-v4-keyvisual (commit 2c3082b, fast-forward, not merged):
- INK title, title drips, ink drop, needle light and header INK pinned to brand red via --brand tokens. Palette smoke still changes per drip. Sampled rgb(209,44,41) across two drip cycles (Playwright, 1440x900 and 390x844).
- Smoke moved to one fixed page-wide layer; section backgrounds made transparent so smoke shows behind glass panels.
- Phone hero hand moved below "Est. in ink" (overlap removed). Hand now sits partly behind the glass card.
- website/index.html regenerated with build.py. 22 unit tests pass. CI cmp matches. Preview check: success on 2c3082b.
- Playwright: no horizontal overflow at either width. Only console errors are blocked Google Fonts requests.

Not verified from this sandbox:
- Public exposure on GitHub Pages and the Worker is NOT re-checked. Egress to jussray.github.io returned 403 (CONNECT tunnel failed), and the Pages API is not permitted through the proxy.
- The Pages exclusion in _config.yml (commit 81cb4b7, on this branch) only takes effect after this branch is merged to whatever branch Pages builds from. That branch is unconfirmed.
- Google Fonts (Pirata One, Cinzel, DM Sans) not rendered.

Still open: owner facts, photo rights, trademark check, Logpush, live rollback target. PR #3 mixes Worker config and site design; consider splitting before merge.
Merge: not approved. Needs exact approval, e.g. "Merge PR #3 at head 2c3082b".

## Implant 2026-10-28 (draft head 8b3f0b9): tap-drip puddle

- Hand taps and each tap releases an ink drip into a smoke puddle at the bottom of the hero. Drip, needle glow, splash ring and puddle smoke change colour together per drip. INK title stays brand red.
- Background pure black. Grain, grid, page-wide smoke, tone picker and decorative colour glows removed.
- Playwright 1440x900 and 390x844: no page errors; INK stays rgb(209,44,41) across 9 seconds; drip colour advances across palette. Desktop needle-to-surface fall 105px.
- Phone: the glass hero card sits over the needle and drip. Not fixed; trade-off.

Not verified: jussco motion and glass match. The jussray/jussray repo is not attached to this session, so its motion source could not be read. Needs attach before that part can be matched.
Merge: not approved. Needs exact approval, e.g. "Merge PR #3 at head 8b3f0b9".

## Implant 2026-10-29 (draft head b1cf1ee): hero parallax and neutral glass

- Jussco motion read from the public repo jussray/jussray (read-only shallow clone, commit f4448d0, site/index.html). Taken: the hero scroll parallax (background moves 0.25x scroll, capped at 800px) and the card glass recipe (translucent top-to-bottom gradient, 1px border, inset top highlight, deep shadow, blur). Not taken: the violet and cyan palette, starfield, nav highlight and staged step timers.
- Glass tints are neutral white and black so the page stays pure black with colour only from the drip and smoke. Blur is 12px, the value jussco uses on its sticky header.
- Hero content and puddle move together on scroll, so the drip still lands on the surface. Needle-to-surface gap unchanged before and after scroll: 104.6px desktop, 129.3px phone.
- Playwright (desktop 1440x900, mobile 390x844, reduced motion): no page errors, no horizontal overflow, body rgb(0, 0, 0), glass backdrop blur(12px). Reduced motion leaves the transforms unset.
- Build: website/index.html regenerated with build.py; 22 unit tests pass; CI-style cmp matches.
Not verified: the preview check on b1cf1ee, and mergeable state at this head (last gh check was clean at 5be9e41).
Merge: not approved. Needs exact approval, e.g. "Merge PR #3 at head b1cf1ee".

## Implant 2026-10-29 (draft head 66d9b7e): sign-free copy

- Hero line and identity paragraph no longer describe the site as based on the sign. Photo alt text unchanged. Built page has no remaining sign-based copy.
- website/index.html regenerated; 22 unit tests pass; CI-style cmp matches.
- Playwright (desktop 1440x900, mobile 390x844, reduced motion): no page errors, no horizontal overflow, body rgb(0, 0, 0), hero parallax 75px at scroll 300 and off under reduced motion.
Not verified: the preview check on 66d9b7e.
Merge: not approved. Needs exact approval, e.g. "Merge PR #3 at head 66d9b7e".

## Implant 2026-10-29 (draft head 60194fc): alt text without sign

- Sign photo alt text now reads "Skeletal hand with red gothic lettering and antique-gold ornamental details". Built page has no remaining "The original Bleeding Ink Tattoo sign" text.
- Puddle stays at the bottom of the hero (confirmed by Juss).
- website/index.html regenerated; 22 unit tests pass; CI-style cmp matches.
Not verified: the preview check on this head.
Merge: not approved. Needs exact approval, e.g. "Merge PR #3 at head 60194fc0422f99a064ce9c662960842f0ae1ac20".
