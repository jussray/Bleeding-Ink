# Bleeding Ink — V4 prelaunch staging

The historical note saying this repository is missing images and build scripts is obsolete: `website/assets/`, `build.py`, `audit_listings.py`, `studio.json` and `tests/` now exist in the GitHub repository.

`website/index.html` is the generated, static, **noindex** cinematic glass-and-smoke preview. `template.html` and `studio.json` are its build inputs. The official contact information and approval fields remain incomplete.

## Local verification

From the `website` directory:

```sh
python -m unittest discover -s tests -v
python build.py --output /tmp/bleeding-ink-preview.html
cmp index.html /tmp/bleeding-ink-preview.html
python audit_listings.py --output /tmp/bleeding-ink-audit.md
```

The Worker uses the repository-root `wrangler.jsonc` to serve only `website/`; `.assetsignore` is intended to expose just HTML and image assets. No Google Business Profile, reviews, customers, crawler settings or production publishing controls are changed by the local scripts.

Before removing `noindex`, finish the owner approvals in `LAUNCH-GATE.md`. No schema, FAQPage or `llms.txt` is used as a visibility shortcut.
