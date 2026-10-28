# Bleeding Ink — Read-only repository audit and approval plan

Date: 2026-10-28

## Scope / authorization

**Target:** private GitHub repository `jussray/Bleeding-Ink`.

**Requested workflow:** audit existing repository first; implement fixes against the repo's actual contents only after explicit change approval; request separate approval for exporting, merging, and deploying.

**Original pre-export audit performed:** read-only GitHub connector calls for repository metadata, branch identification, file content, and branch comparison; read-only inspection of the local V5 `index.html` supplied in this conversation and the user-provided mobile screenshots. The audit phase made no GitHub writes, commits, branch creation, PR, merge, or publication. This is a historical audit snapshot, before the separately approved Gate A audit export.

## Current repository refresh — supersedes the initial branch snapshot

The GitHub repository **changed after the initial read-only audit**. The following newer observations take precedence over earlier statements that `main` contained only a README or that the named draft branch still existed.

- **OBSERVED:** GitHub commit `5d919be7202c920cc1dd167c05d21f994df5f4d7` is a merge of PR #1 (message: `Merge pull request #1 from jussray/draft/site-v4-keyvisual`), timestamped `2026-10-28T21:08:27Z`. Reference: https://github.com/jussray/Bleeding-Ink/commit/5d919be7202c920cc1dd167c05d21f994df5f4d7
- **OBSERVED:** The repository now lists only `main`; fetching or comparing the former `draft/site-v4-keyvisual` branch by name returns not-found. The absence applies to the refreshed branch listing, not to historical commits.
- **OBSERVED:** The former draft's last website commit `5ef1370932ed9ff2797b732d5355e27703df531f` remains fetchable, and its `index.html` blob SHA `19fbdc04f2f838c0085e2e4fff9aced854551a47` matches the `main` website file observed in this refresh. This revision contains the transparent `skeleton-machine-cutout.webp` asset reference and keeps `noindex,nofollow`. The old finding that *the current repo disables smoke* is therefore **superseded**; it described the older index blob, not this latest file. Reference: https://github.com/jussray/Bleeding-Ink/commit/5ef1370932ed9ff2797b732d5355e27703df531f
- **OBSERVED:** No `wrangler.jsonc`, `wrangler.toml`, `wrangler.json`, or `package.json` was found when explicitly fetched from the earlier draft; the source's change list also contained no such file. These are specific path checks, not a full inventory of every path or Cloudflare account setting.
- **Gate A base adjustment:** Because the agreed draft branch has been deleted, use its preserved last commit `5ef1370932ed9ff2797b732d5355e27703df531f` as the exact starting point for a **new audit-only branch**. This preserves the branch's site content rather than selecting an unrelated baseline. No website changes are authorized.
- **Next implementation audit:** Recheck the current `main` file and the actual deployment environment before proposing patches. Do not use the initial pre-merge website findings as current implementation evidence.

## Evidence snapshot

| Reference | Observed evidence | Classification |
|---|---|---|
| Repository | `jussray/Bleeding-Ink`, private; default branch `main` | OBSERVED via GitHub connector |
| Branches | `main`, `draft/site-v4-keyvisual` | OBSERVED via GitHub connector |
| Branch comparison | Draft is 2 commits ahead of `main`, 0 behind; 11 added files (including `index.html`, image assets, launch and crawler files). | OBSERVED via GitHub connector compare |
| `main` | `README.md` exists, but `index.html` is not found | OBSERVED via GitHub fetch |
| Draft implementation | `index.html` exists; retrieved blob SHA `2ac1d010b2bcd8490bffabf8ad50ac75122df832` | OBSERVED via GitHub fetch |
| Local V5 | `/mnt/data/bleeding-ink-v5-smoke-chamber/index.html` is present in the conversation workspace, with different layout than repo draft | OBSERVED locally; not observed in GitHub |
| Screenshots | User supplied iPhone screenshots of V5 sign crop and control-card overlap | USER-REPORTED visuals; corroborated by V5 CSS, not independently reproduced in a fresh browser run here |

GitHub file: https://github.com/jussray/Bleeding-Ink/blob/draft/site-v4-keyvisual/index.html

## High priority: repo vs. requested design

1. **The earlier draft snapshot disabled the dynamic hero elements.** Its CSS at approximately lines 231–236 sets a static `img/key-visual.jpg` hero and `.hero-art,.hero-smoke,.hero-grid,.tone-picker{display:none!important}`. Smoke cannot be visible through glass under those older rules. **OBSERVED in the superseded earlier file, not the current `main` version.**
2. **The V5 that generated the screenshots is not the repo draft.** V5's local site includes a smoke chamber, smoke density controls, and a different component hierarchy. An exact file replacement would discard unrelated repo choices and could create regressions. **OBSERVED in the two sources; merge risk INFERRED.**
3. **The V5 sign is clipped on phones.** Local V5 CSS sets `.story-image img{aspect-ratio:1.28/1;object-fit:cover;width:100%}`, while the user screenshot shows cut-off lettering on a tall narrow screen. **User screenshot + source observed.**
4. **The V5 smoke control panel overlaps the art.** Local V5 mobile CSS positions `.hero-visual` absolutely and sets `.hero-glass-note{bottom:-87px}` (and `-91px` at <=450px). It has no reserved flow-space for the card. **User screenshot + source observed.**
5. **There are unverified business and publication fields in the draft.** It retains `noindex,nofollow`, placeholder canonical and social URLs, some unresolved address fields, JSON-LD values, and a draft `robots.txt`, `llms.txt` and `sitemap.xml`. The repo's own `LAUNCH-GATE.md` says owner facts and image permissions must be confirmed before release. **OBSERVED.** Do not replace placeholders with guesses or use this draft to publish yet.
6. **The existing README/RECEIPT are out of phase with the GitHub state.** `RECEIPT.md` contains a historical local-only fingerprint and notes about a draft PR; it must not be treated as proof that V5 was installed or verified in GitHub. **OBSERVED.**
7. **Tests:** No test suite was found among the 11 files added to the draft branch comparison. This does not prove there are no tests elsewhere in GitHub; the visible draft tree gives no test evidence. **OBSERVED within compared files; full repository verification limited.**

## Additional evidence supplied after the original audit — Cloudflare build failure

**Source:** user-pasted Cloudflare deployment log, timestamped `2026-10-28T21:05:32.753Z` through `2026-10-28T21:05:49.798Z`. **Classification: USER-REPORTED.** The Cloudflare job, account settings, environment, and deployed state were **not** independently inspected or reproduced. No configuration was changed and no deploy was initiated as part of this audit.

- **Observed in user-supplied log:** the command is `npx wrangler deploy`, which installs/uses `wrangler@4.155.0` and exits with `Could not detect a directory containing static files (e.g. html, css and js) for the project`.
- **Observed independently in the audited repo:** `main` has no `index.html`; `draft/site-v4-keyvisual` does have `index.html` and image assets. Specific `wrangler.jsonc`, `wrangler.json`, `wrangler.toml`, and `package.json` fetches from the draft branch returned not-found responses. The repo draft's branch comparison contains none of these files.
- **INFERRED likely cause:** Cloudflare is deploying from a branch/root that contains no recognized static-site entry point, without an `assets.directory` setting. The log alone does not reveal which Git branch Cloudflare cloned, so that part is **UNKNOWN**. The `No build output detected to cache` line is informational and is not itself the deployment error.
- **Documented platform requirement:** Cloudflare Workers static-assets deployment expects a static assets directory configured via Wrangler's `assets.directory` (or appropriate automatic tooling). Reference: https://developers.cloudflare.com/workers/static-assets/binding/ . Cloudflare Pages has a different build-output setup: https://developers.cloudflare.com/pages/configuration/build-configuration/ .
- **Proposed remediation for separate approval:** first confirm whether the Cloudflare project is Workers Builds or Pages, and which branch/root it builds; then add a minimal Wrangler static-assets configuration **or** adjust the Pages build settings accordingly. Keep the draft `noindex` and unresolved business details protected from release. Do not blindly deploy the current draft.
- **Status:** deployment failure **USER-REPORTED**; reproduction **NOT ATTEMPTED**; remedy **DRAFTED as a recommendation only**, **NOT APPLIED**.

## Proposed changes (not implemented)

### Gate A — Export the audit

With explicit approval (now given), create a **new audit-only branch** from the preserved last draft commit `5ef1370932ed9ff2797b732d5355e27703df531f` and commit this report under `docs/REPO-AUDIT-2026-10-28.md`. Do not overwrite existing files; do not modify `main`; do not merge or deploy. Record the actual new branch and commit hashes after the write.

### Gate B — Fix the mobile website against the audited branch

Requires a **separate approval** after Gate A. Proposed scope:

- Reconcile V5’s silver smoke and transparent gold-hand art with the repo’s existing assets, without bulk replacing unrelated copy, photos, or launch files.
- Make the original sign uncropped at mobile widths: natural aspect ratio (`height:auto`, `object-fit:contain`), and place the caption *outside* the photo.
- Convert the mobile hand/glass card to a vertical grid or flex layout, reserving space for controls so no absolute negative-bottom overlap occurs.
- Maintain the black/silver/antique-gold palette and a minimal red ink accent; preserve user controls for pause/resume, color, and fog density if the user approves bringing them into GitHub.
- Preserve `noindex` and the owner's existing launch gate. Do **not** silently edit business facts, crawler policy, `robots.txt`, sitemap, schema, FAQ or `llms.txt`.
- Add focused regression checks: 375/390/430px viewport coverage, sign fully visible, artwork and controls non-overlapping, smoke animation/pause behavior, reduced motion, no overflow or broken images. Show before/after screenshots for approval.
- Commit only to the approved work branch and propose a PR. **No merge or live deployment without a further explicit approval.**

### Gate C — Review and release

Requires separate approval to merge, then another approval if any deployment/publishing is requested. Confirm shop and booking details, listing/review links, asset rights, and the launch gate before indexing.

## Current status at the close of the original read-only audit (before Gate A export)

- Repository audited: **OBSERVED, read only**.
- Local report: **AUTHORED**, not exported to GitHub.
- Mobile fixes: **NOT STARTED against the repository**.
- GitHub writes, PR, merge and deployment: **NOT STARTED**, awaiting authorization.
- No claim of ranking benefit, live functionality, or V5 repository installation is made.