# Bleeding Ink — V4 staging preview

This GitHub branch is a **draft staging import**, not the deployable V4 source-of-truth. The complete V4 package, including verified local build scripts, tests, and original image assets, was delivered as a separate ZIP in the conversation.

## Current branch contents

- `index.html`: generated cinematic **noindex** preview (smoke, changing ink colors, glass interface).
- `template.html`: corresponding source template.
- `studio.json`: blank, owner-controlled contact details and launch approvals.
- `REPO-HANDOFF.md`, `LAUNCH-GATE.md`, `CRAWLER-DECISION.md`: release requirements.

**Blocker:** Original image assets (`assets/skeleton-hand.webp`, `assets/sign-detail.webp`) and the local Python build/audit/test scripts are **not transferred into this repository branch**. The preview's image references will not render correctly until the image assets are added. Do not merge, deploy or represent this branch as production-ready.

Local ZIP package and test evidence remain the source of truth for V4. No public listing, customer review, crawler configuration or site deployment was changed. No schema or llms.txt was added.

Review requests must be neutral and voluntary. Never solicit only happy customers or reward reviews.
