# Bleeding Ink - parallel QA audit

Source inspection of GitHub main at b841c86, not live HTTP or browser inspection.

## Tracks

- Infrastructure: GitHub preview/build/deploy and Cloudflare Workers checks reported success at this commit.
- Cloudflare deploy source: root wrangler.jsonc serves the website/ directory, NOT root index.html.
- Design drift: root index.html includes key-visual and baskets images, while deployed website/index.html uses a different hand image and a Visit & Reviews section.
- Business listings: studio.json has empty address, phone, hours, booking/reviews URLs, and four false approval flags. No public listing was accessed.
- Crawler policy: root robots.txt and sitemap.xml are outside the Worker asset directory, while website/.assetsignore only allows index.html and assets. These root files are NOT automatically served by the Worker.
- Prelaunch: both entrypoints are noindex. Keep this status until verified owner release approval.
- Live site: Worker URL could not be fetched from this environment. Mobile/desktop animations, links and live HTTP responses remain UNKNOWN.

## Audit automation

CI now checks prelaunch robots metadata, in-page fragment targets, image references and alt attributes, duplicate IDs, unverified JSON-LD, Worker path/binding and asset allowlist. It records design drift and missing owner approvals as warnings, not fabricated passed checks.

Do not swap root and Worker HTML automatically: website/index.html is generated from template.html and studio.json, while root has a different asset set. Owners must choose the intended design before launch.

No customer data, external listings, public reviews or Cloudflare account settings were changed.
