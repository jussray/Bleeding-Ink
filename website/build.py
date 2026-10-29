#!/usr/bin/env python3
"""Compile the Bleeding Ink static site from verified shop information.

No network requests, business profile edits, review posting, or external side effects.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
URL_FIELDS = ('siteUrl', 'bookingUrl', 'googleReviewUrl', 'googleMapsUrl',
              'instagramUrl', 'yelpUrl', 'appleMapsUrl', 'bingMapsUrl')
TEXT_FIELDS = ('streetAddress', 'cityStateZip', 'phone', 'hours')
RELEASE_FIELDS = (*TEXT_FIELDS, 'bookingUrl', 'googleReviewUrl', 'googleMapsUrl', 'siteUrl')
APPROVALS = ('profileVerified', 'categoryConfirmed', 'reviewPolicyApproved', 'crawlerPolicyApproved')


def e(value):
    return html.escape(str(value), quote=True)


def validate(data, release):
    if not isinstance(data, dict):
        raise ValueError('studio.json must contain a JSON object')
    for key in URL_FIELDS:
        if not data.get(key):
            continue
        value = data[key]
        if not isinstance(value, str):
            raise ValueError(f'{key} must be a URL string')
        parsed = urlparse(value)
        if (parsed.scheme != 'https' or not parsed.netloc or not parsed.hostname
                or parsed.username or parsed.password or any(c.isspace() for c in value)
                or '\\' in value or any(ord(c) < 32 for c in value)
                or (key == 'siteUrl' and (parsed.fragment or parsed.query))):
            raise ValueError(f'{key} must be an absolute HTTPS URL with no credentials or whitespace')
    if release:
        missing = [key for key in RELEASE_FIELDS if not isinstance(data.get(key), str) or not data[key].strip()]
        missing += [key for key in APPROVALS if data.get(key) is not True]
        if missing:
            raise ValueError('Release blocked. Missing verified fields/approvals: ' + ', '.join(missing))
    return data


def value(data, key):
    candidate = data.get(key, '')
    if not isinstance(candidate, str) or not candidate.strip():
        return '<span class="pending">Not yet confirmed</span>'
    return e(candidate.strip())


def anchor(url, label, css=''):
    return f'<a class="{e(css)}" href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(label)}</a>'


def phone_markup(phone):
    cleaned = re.sub(r'[^\d+]', '', phone)
    # A 10-digit US number may be dialed in E.164; other strings remain visible but unlinked.
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        return f'<a href="tel:+1{digits}">{e(phone)}</a>'
    if len(digits) == 11 and digits.startswith('1'):
        return f'<a href="tel:+{digits}">{e(phone)}</a>'
    return e(phone)


def render_facts(data):
    phone = data.get('phone') or ''
    addr = ' '.join(filter(None, [data.get('streetAddress', ''), data.get('cityStateZip', '')]))
    pairs = [
        ('Address', ('<address style="font-style:normal">'+value(data,'streetAddress')+'<br>'+value(data,'cityStateZip')+'</address>')),
        ('Phone', phone_markup(phone) if phone else value(data,'phone')),
        ('Hours', value(data,'hours')),
    ]
    facts = '<dl class="local-facts">' + ''.join(f'<dt>{label}</dt><dd>{markup}</dd>' for label,markup in pairs) + '</dl>'
    links = []
    for key, label in (('googleMapsUrl','View on Google Maps ↗'), ('appleMapsUrl','Apple Maps ↗'), ('bingMapsUrl','Bing Maps ↗'), ('yelpUrl','Yelp ↗')):
        if data.get(key):
            links.append(anchor(data[key], label))
    links_markup = '<div class="local-links">'+''.join(links)+'</div>' if links else ''
    return facts + links_markup


def render_review(data):
    review_url = data.get('googleReviewUrl')
    maps_url = data.get('googleMapsUrl')
    if review_url:
        review_button = anchor(review_url, 'Leave an honest Google review ↗', 'btn btn-red')
    else:
        review_button = """<p class="pending">The studio's official review link isn't available here yet.</p>"""
    read_button = anchor(maps_url, 'Read public reviews ↗', 'btn btn-outline') if maps_url else ''
    return ('''<article class="local-panel glass" id="reviews" aria-labelledby="reviews-title">
        <span class="micro">Real experiences only</span><h3 id="reviews-title">Your voice matters.</h3>
        <p class="review-note">Visited Bleeding Ink? You're welcome to share your genuine experience. All feedback is valued, whether positive or critical.</p>
        <div class="review-actions">''' + review_button + read_button + '''</div>
        <p class="local-footnote">Reviews are optional. No discounts, gifts, or rewards are offered for reviews. Never share personal medical details.</p>
      </article>''')


def render_booking(data):
    url = data.get('bookingUrl')
    if url:
        return anchor(url, 'Book your session ↗', 'btn btn-red')
    return '<button class="btn btn-red" type="button" id="bookingButton">Booking information</button>'


def release_description(data):
    return f"Bleeding Ink Tattoo in {data['cityStateZip'].strip()}. Get studio hours, address, contact details and verified booking information."


def render_sections(data):
    return '''<section class="local-hub" id="visit" aria-labelledby="visit-title">
    <div class="container"><span class="eyebrow">Find us · Share your experience</span>
      <h2 class="section-heading" id="visit-title">The <em>real-world</em> details.</h2>
      <p class="local-intro">Studio address, hours, and official review links will appear here when confirmed.</p>
      <div class="local-grid">
        <article class="local-panel glass">
          <span class="micro">Visit the studio</span><h3>Find Bleeding Ink.</h3>
          ''' + render_facts(data) + '''
        </article>
        ''' + render_review(data) + '''
      </div>
    </div>
  </section>'''


def render_footer(data):
    phone = data.get('phone') or ''
    parts = ['Bleeding Ink Tattoo · Tattoo studio &amp; novelty baskets']
    for key in ('streetAddress', 'cityStateZip', 'phone', 'hours'):
        if data.get(key):
            parts.append(e(data[key]))
    if len(parts) == 1:
        parts.append('Studio contact details coming soon')
    return '<br>'.join(parts)


def build(data, release=False):
    source = (ROOT / 'template.html').read_text(encoding='utf-8')
    substitutions = {
        '@@VISIT_REVIEW_SECTIONS@@': render_sections(data),
        '@@FOOTER_FACTS@@': render_footer(data),
        '@@SOCIAL_LINKS@@': anchor(data['instagramUrl'], 'Instagram ↗') if data.get('instagramUrl') else '',
        '@@BOOKING_CONTROL@@': render_booking(data),
        '@@SITE_STATUS@@': 'Studio website' if release else 'Preview concept',
    }
    for marker, replacement in substitutions.items():
        if marker not in source:
            raise ValueError('Missing template marker: ' + marker)
        source = source.replace(marker, replacement)
    if release:
        source = source.replace('content="noindex,nofollow"', 'content="index,follow"')
        source = source.replace('Bleeding Ink Tattoo — a cinematic, glass-and-smoke tattoo studio concept.', e(release_description(data)))
        source = source.replace('  <title>BLEEDING INK — Tattoo Studio</title>',
                                '  <link rel="canonical" href="'+e(data['siteUrl'])+'">\n  <title>BLEEDING INK — Tattoo Studio</title>')
    if re.search(r'@@[A-Z_]+@@', source):
        raise ValueError('Unrendered template marker remains')
    return source


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=ROOT/'studio.json')
    parser.add_argument('--output', type=Path, default=ROOT/'index.html')
    parser.add_argument('--release', action='store_true', help='Generate indexable HTML only after explicit approvals')
    args = parser.parse_args()
    try:
        data = validate(json.loads(args.config.read_text(encoding='utf-8')), args.release)
        page = build(data, args.release)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(page, encoding='utf-8')
        print(f'Created {args.output} ({"release candidate" if args.release else "noindex preview"})')
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
