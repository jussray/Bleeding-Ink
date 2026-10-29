# Bleeding Ink CI recovery

**Status:** proposed Cloudflare configuration fix; the remote check must still pass. Do not merge or deploy to production while business facts remain unverified.

Cloudflare Workers Builds can use either of these root directories:
- Repository root: `wrangler.jsonc` serves `./website`.
- `website`: `website/wrangler.jsonc` serves `./`.

Both declare the Worker name `bleeding-ink`. `website/.assetsignore` restricts uploaded static assets to `index.html` and `assets/**`, excluding build scripts, tests, and studio configurations. Verify your Cloudflare Worker **Settings > Build** root directory and actual build/preview commands. These account settings were not inspected or changed.

GitHub Actions failed on the previous commit, but step details and logs were not returned. This may be a runner/permission/billing issue, not a Python failure. Inspect the run page and error banner before attributing cause.

Local verification (run from `website/`):
```sh
python -m unittest discover -s tests -v
python build.py --output /tmp/bleeding-ink-preview.html
cmp index.html /tmp/bleeding-ink-preview.html
python audit_listings.py --output /tmp/bleeding-ink-listing-audit.md
```

The site stays `noindex,nofollow` with unverified business contact details. No real profiles or reviews are changed.
