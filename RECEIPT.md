# Handoff receipt: Bleeding Ink Tattoo site draft (local, not a repo receipt)

Fingerprint: repo:NONE|branch:NONE|head:NONE|subject:tattoo-shop-site/index.html|evidence:sha256=8f95d055851dd6ebf4f8bcd1b4d8a149f9d8fdd7382c26f6d20e4a6908b1f08d|runtime:playwright-chromium-checks-2026-10-28-smoke-merge
Proof cookie: da9d05fa513e70f2
Scope: local draft only. No repo, no branch, no commit, no deploy, no publish.

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
