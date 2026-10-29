# Bleeding Ink — repository guide

This repository contains **two separate prelaunch HTML entrypoints**:

- `website/index.html` is the Cloudflare Workers static asset entrypoint. The root `wrangler.jsonc` intentionally points to `./website` and its `.assetsignore` excludes configuration, tests and private studio data from static assets.
- `index.html` at repository root is the earlier cinematic draft and is **not** the Worker deployment target. It also stays `noindex,nofollow` and carries no unverified structured data.

The shop's real contact details, prices, booking link, review URL, photo permissions and launch approvals are **not fully verified**. Do not claim the deployed site is launch-ready, or remove `noindex`, until `website/LAUNCH-GATE.md` is cleared.

## Validate

```sh
cd website
python -m unittest discover -s tests -v
python build.py --output /tmp/bleeding-ink-preview.html
cmp index.html /tmp/bleeding-ink-preview.html
python audit_listings.py --output /tmp/bleeding-ink-listing-audit.md
```

Cloudflare build success alone verifies a deployment check, **not** the storefront's business facts or the live customer experience. No off-site business listings or reviews are changed by these commands.
