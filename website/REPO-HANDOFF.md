# Remote-repository handoff

**Exact destination:** GitHub `jussray/Bleeding-Ink` (private), default branch `main` observed at `4e1a367de80e09a2b76954813813672c20ba2862` at inspection. Existing remote root contained `README.md` only.

## Intended tree

Move contents of this V4 local folder into the remote repository under `website/`, EXCEPT `.github/workflows/site-checks.yml`, which belongs at repository root `.github/workflows/site-checks.yml`. Preserve the root README. Do not include `transfer/`, caches, or the ZIP.

## Proof vs assumptions

Local tests do not establish remote application. A GitHub branch/PR may be created separately and must be inspected to establish what actually landed. Never claim the repository has image assets unless all two site-referenced images were uploaded successfully and verified there.

## Visual assets

`assets/skeleton-hand.webp` and `assets/sign-detail.webp` are required by the website, and `assets/original-sign.jpg` is the original reference photograph. All are included in this ZIP. Do not replace them with unrelated stock assets.