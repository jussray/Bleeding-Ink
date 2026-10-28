# Launch gate — listings and reviews before markup

**Status: BLOCKED until actual studio information is checked by an authorized owner.** This document does not claim that any listing was edited, verified, or published.

## 1. Verify the official Google Business Profile

- [ ] Confirm the profile belongs to the real shop; verify it using an authorized account.
- [ ] Profile name matches real sign and public branding: **Bleeding Ink Tattoo**. No keyword additions.
- [ ] Check the available primary category *in Google's profile editor* and pick the most accurate one (do not guess the label).
- [ ] Check exact public-facing street address, suite, phone, customer-facing hours, special hours, website and appointment link.
- [ ] Upload current, authentic interior/exterior and business photos if authorized.
- [ ] Confirm business description, website and booking destinations; no dead links.
- [ ] Match these facts on the site and review Apple Maps, Bing Places and Yelp profiles that actually belong to this shop. Don't create duplicate listings without checking first.

## 2. Real reviews, not manufactured reputation

- [ ] Get the official link to the business's Google review form from the owner-controlled profile.
- [ ] Use the same neutral, optional review invitation for genuine customers, not only those expected to leave high ratings.
- [ ] No incentives, discounts, freebies, negative-review suppression, or pressure to review on the premises.
- [ ] Use a neutral reply process for reviews without exposing sensitive customer details.
- [ ] Never invent a rating count or reviews and never add self-serving review-star JSON-LD.

## 3. Site accuracy and usability

- [ ] Fill all required fields in `studio.json` from confirmed studio information.
- [ ] Rebuild the HTML; visually inspect desktop and mobile layouts in a real browser.
- [ ] Confirm address, phone and hours are present in initial HTML by viewing page source.
- [ ] Confirm booking button and each Google/other listing URL opens the right verified destination.
- [ ] Run `python -m unittest discover -s tests -v` and fix failures.

## 4. Crawl and publish decision, then optional schema later

- [ ] Decide AI-crawler access separately for training crawlers and search crawlers after reviewing the vendors' current policies.
- [ ] Confirm that public Googlebot access, indexing and snippets are intentional at launch; leave `noindex` for drafts.
- [ ] Set `profileVerified`, `categoryConfirmed`, `reviewPolicyApproved` and `crawlerPolicyApproved` to true in `studio.json` **only after those checks are actually complete**.
- [ ] Supply the live `siteUrl`; then generate the local release candidate with `python build.py --release`.
- [ ] Publish only after inspecting the generated file and verifying the website and listing from an external connection.
- [ ] Revisit JSON-LD only afterward as correctness work, not a guaranteed ranking benefit.

**Deferred:** Schema/TattooParlor JSON-LD, FAQPage markup, `llms.txt`, and changes to robots.txt. The draft does not need any of them.

## V3 — offline consistency audit

- [ ] Enter confirmed shop facts into `studio.json` (only from authorized sources).
- [ ] Inspect public listing pages manually, record their actual facts and check date in `listing-snapshots.csv`.
- [ ] Run `python audit_listings.py`; inspect `LISTING-AUDIT.md` for missing or inconsistent values.
- [ ] Investigate conflicts against the business's actual signage, owner records and verified profile; do not automatically sync guesses.
- [ ] See `CRAWLER-DECISION.md`; obtain an explicit owner choice *before* editing robots rules on a deployed site.
- [ ] Confirm booking is a regular HTTPS link visible in generated HTML and is the authorized booking destination.

V3 does not change any online listings, review history, robots policies or public site. Its static comparisons are not independent verification of any public data.