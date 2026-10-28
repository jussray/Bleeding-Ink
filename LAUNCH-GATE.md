# Bleeding Ink Tattoo: launch gate

Nothing goes live until every item below is checked. The site ships with `noindex` on purpose, so an unfinished draft cannot be indexed.

## 1. Facts from the owners (blocking)
- [ ] Shop name, legal name, and the owners who sign off. Owner named by Juss 2026-10-28: Leak. Legal name and sign-off still open.
- [ ] Street address, phone, hours, Instagram handle. Supplied by Juss 2026-10-28: 500 Galleria Drive, phone 215-980-1386. Still missing: city, state, ZIP, hours, Instagram. Owners confirm all of it.
- [ ] Artist names, styles, years tattooing, and written consent to show their work and name
- [ ] Booking tool chosen by the owners; deposit amount and whether it applies to the final price
- [ ] Cancellation and no-show policy
- [ ] Walk-in policy
- [ ] Policy for clients under 18, set to match state law and consent forms
- [ ] Pricing method (hourly, minimum, or per size) and consultation terms
- [ ] Basket list, prices, lead time, and pickup rules

## 2. Name and brand (blocking)
- [ ] Trademark and business-name check for "Bleeding Ink Tattoo" (state registry and USPTO). Not run yet.
- [ ] Confirm the tagline "If you ain't tatted you scatted" is theirs to publish.

## 3. Photos (blocking)
- [ ] Sign photo (`img/sign.jpg`): approved.
- [ ] Interior photo (`img/floor.jpg`): a person is visible in the background reflection near the glass cases. Crop or reshoot. Halloween decor and crime-scene tape are in frame. Reshoot without them if the owners agree.
- [ ] Basket photo (`img/baskets.jpg`): approved. Product brand names are visible.
- [ ] Key visual (`img/key-visual.jpg`): supplied by Juss for the hero (stated 2026-10-28); it is not a photo of the shop. Still open before public use: whether it is AI-generated, and the license terms.
- [ ] The other six photos from the chat were NOT reviewed and are NOT used. Review them for people, third-party paintings, and personal items before any use.
- [ ] Artist photos: only with written consent.

## 4. Technical (blocking)
- [ ] Replace every `[bracket]` in index.html, robots.txt, sitemap.xml, and llms.txt. Delete any schema field you cannot fill. Do not leave placeholders in JSON-LD.
- [ ] Remove `<meta name="robots" content="noindex">` from index.html.
- [ ] Replace `[domain]` in canonical, og:url, og:image, robots.txt, sitemap.xml, and llms.txt.
- [ ] Create `img/og-1200x630.jpg` (1200x630) from the sign photo. The og:image tag points to it. Not created yet.
- [ ] Typography is UNVERIFIED. The sandbox could not load Google Fonts (Pirata One, Cinzel, Source Serif 4), so screenshots show fallback serifs. Check the real render on a phone and a desktop before launch.
- [ ] Confirm AI crawler names in robots.txt against each vendor's current documentation. Search and answer bots (OAI-SearchBot, Claude-SearchBot, PerplexityBot) affect visibility; GPTBot and ClaudeBot are training-only (vendor docs).
- [ ] llms.txt is optional. No AI system has confirmed reading it: Google's Mueller said so in an anecdote (June 2025), and one SE Ranking study (about 300k domains) found no effect on citations. Do not present it as a citation lever.
- [ ] FAQ text stays on the page for people. FAQPage markup was removed: Google's FAQ page says the rich result no longer appears in Search (extracted text; trade press agrees). TattooParlor and LocalBusiness markup stays. No study shows schema raises AI citations. Do not present it as one.
- [ ] Confirm JavaScript rendering is not needed for the page's text: the draft is static HTML, so the text is in the initial HTML.
- [ ] Real-browser check at 390px and 1280px: no horizontal scroll, images load, booking link works, FAQ opens.
- [ ] Validate JSON-LD with Google's Rich Results Test and schema.org validator.

## 5. Off-site (decides local ranking more than the site does)
- [ ] Google Business Profile: claimed by the owners, with the same name, address, phone, and hours as the site.
- [ ] Primary category: pick the closest category in the GBP list. Whether a tattoo category exists is UNKNOWN; check the list. Google's own page says category is among the fields to keep accurate.
- [ ] Booking link: set in the GBP interface. Local business links cannot be bulk-uploaded (Google, PRIMARY).
- [ ] Do not change the business name to add keywords until Google's name policy has been read and checked. Not yet checked.
- [ ] Apple Business Connect, Bing Places, Yelp, and Facebook: same NAP (name, address, phone). Use one exact address string everywhere. The on-site research saw a mismatch between one studio's site and its directory listing ("Blvd" on the site, absent in the listing).
- [ ] Ask real clients for Google reviews. No incentivized or fake reviews. No review rating in the schema until reviews are real and verifiable.
- [ ] Ask every client, not only happy ones. Google bans incentivized and biased reviews (PRIMARY). Filtering requests by how happy a client seems is treated as high risk by inference only; Google does not address it directly.
- [ ] Do not add aggregateRating or Review markup to the site. Google says a business that controls its own reviews is ineligible for review stars (PRIMARY, extracted text). Testimonials on the site are not covered by that text; leave them out until the owners and Google's rules are checked.
- [ ] Know the penalty path before launch: Google can stop new reviews for a period, unpublish existing ones, or add a warning label. Durations are not published. Listing suspension is not covered by the fetched text (UNKNOWN).
- [ ] Google Search Console and Bing Webmaster Tools: verify the domain, then submit sitemap.xml.

## 6. What this build does NOT do
- No online checkout for baskets. Orders are by phone or DM until the owners pick a store platform.
- No booking calendar of its own. Booking goes through the tool the owners choose.
- No guaranteed ranking or AI citations. These are the standard on-page and structured-data basics. Results depend on the off-site work above, time, and competitors.

## 7. After launch
- [ ] Measure: calls, booking clicks, Google Business Profile views and direction requests, and search queries in Search Console. Review at 30 and 90 days.
- [ ] Update llms.txt and the "Last updated" date when prices, hours, or artists change.
