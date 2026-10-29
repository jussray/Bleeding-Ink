# Bleeding Ink | Parallel audit and launch hold

**As of 2026-10-29.** This is a draft-only technical and public-evidence audit, not a product launch or permission to merge. Earlier proof tied to `b841c86` or `e30a3f7` is historical, not exact-head proof for this branch.

## Current repository and runtime boundaries

- Authoritative `main` at this recheck: `a733717440c44b83342dfb223cbd21201df3eae8`. Current PR #6 is a separate audit branch; PR #4 is an older conflicting design draft and must not overwrite the active V4.
- GitHub API reports the repository **public** (`private:false`), even though it was private earlier. GitHub Pages returning 404 for internal project paths does **not** remove those same files or photos from the public Git repository or prior commit history. The public tree includes `RECEIPT.md`, `LAUNCH-GATE.md`, `website/studio.json` and `website/assets/original-sign.jpg`. Do not call this private or assume GitHub history is retracted.
- Connected GitHub tools can inspect but not switch repository visibility. The alternative authenticated browser workflow was unavailable, so **private visibility is NOT VERIFIED**. Owner should change it in GitHub settings, consider possible GitHub Pages impact, then confirm with a fresh `private:true` readback.
- Worker deployment source: root `wrangler.jsonc` serves the `website/` V4 asset directory. The root `index.html` is a retired customer-facing notice, not the Worker storefront. Do not promote the old root design.
- Cloudflare Worker and GitHub Pages hosting each returned 404 for tested internal-doc/config/source paths in a prior fresh live browser audit; GitHub Pages continues to display the retired notice. These host responses are **not** repository-access controls.
- Current main GitHub preview checks passed at `a733717`. Its Cloudflare build/deploy succeeded and Chromium Playwright checks previously passed at 390×844 (12 assertions) and 1280×800 (10 assertions), including booking-modal truthfulness and no broken image/requests. These are main-runtime witnesses, **not exact PR #6 head checks**.
- Worker root sitemap is not automatically included in `website/` allowlisted assets. Keep `noindex,nofollow` for prelaunch; crawler/search publication remains owner-gated.

## Studio identity, listings and customer-fact gate

The Johnstown Galleria currently identifies a tattoo tenant as **Galleria Ink Tattoo/Piercing**:
- https://johnstowngalleria.com/map/
- https://johnstowngalleria.com/business/get-er-done-tattoo-piercing/

Public directories also refer to **GallaINK** and **Get Er Done Tattoo and Piercings** in the mall. These records do **not** establish that Bleeding Ink is the same business, a rebrand, an authorized storefront there, or entitled to its ratings, contact numbers, suite, or hours. Do not copy third-party listing details to the Bleeding Ink site.

Release remains **BLOCKED** until a shop-authorized source confirms the current trading identity, accurate suite and hours, ownership/consent for artist content, customer contact information, the approved booking destination and review-form identity. Past user-entered figures are inputs for owner confirmation, not automatically verified platform facts. Keep blank fields and false approval flags in `studio.json` unchanged until substantiated.

## CI and governance

This PR supplies read-only offline deployment checks and a bounded public HTTP probe. A successful HTTP response cannot prove owner-controlled listings or actual browser interactions; a blocked transport is not a site outage. Expose only sanitized status and evidence, not internal workflows or technical receipts on customer pages.

**Stop conditions:** Do not merge, deploy, change GitHub visibility without authenticated authority, assert owner confirmation, create or edit external listings, publish reviews, remove noindex, or advertise booking as active while a gate remains unknown.

**Next reversible verification:** owner changes GitHub visibility to private and the GitHub API confirms it; then authenticate the correct Bleeding Ink business identity with an owner-provided source. Recheck GitHub Pages effects and Cloudflare runtime after visibility change. All other workflows remain held.

**Rollback:** Revert this draft documentation-only commit. It changes no production code, published site, business listing, or account setting.
