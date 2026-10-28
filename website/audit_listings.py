#!/usr/bin/env python3
"""Compare OWNER-ENTERED listing snapshots to the local canonical shop facts.

Offline only. Does not connect to, verify, or change any public listing.
"""
import argparse
import csv
from datetime import date
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIELDS = {
    'business_name': ('Business name', None),
    'street_address': ('Street address', 'streetAddress'),
    'city_state_zip': ('City/state/ZIP', 'cityStateZip'),
    'phone': ('Phone', 'phone'),
    'hours': ('Hours', 'hours'),
}
PLATFORMS = ('Google Business Profile', 'Yelp', 'Apple Maps', 'Bing Places')


def normalize(field, text):
    text = str(text or '').strip()
    if field == 'phone':
        digits = re.sub(r'\D', '', text)
        return digits[1:] if len(digits) == 11 and digits.startswith('1') else digits
    # Conservative: normalize typography/whitespace only, never equate different addresses or hours.
    return ' '.join(text.casefold().split())


def inspection_date_status(value):
    """Only an actual calendar date on/before today counts as a manual inspection."""
    candidate = str(value or '').strip()
    if not candidate:
        return 'NOT_REVIEWED'
    try:
        inspected = date.fromisoformat(candidate)
    except ValueError:
        return 'INVALID_CHECK_DATE'
    if inspected.isoformat() != candidate or inspected > date.today():
        return 'INVALID_CHECK_DATE'
    return None


def compare(studio, rows):
    expected = {'business_name': 'Bleeding Ink Tattoo'}
    for field, (_, key) in FIELDS.items():
        if key:
            expected[field] = studio.get(key, '')
    results = []
    for row in rows:
        for field, (label, _) in FIELDS.items():
            actual, desired = str(row.get(field, '') or '').strip(), str(expected.get(field, '') or '').strip()
            date_status = inspection_date_status(row.get('checked_on', ''))
            if date_status:
                status = date_status
            elif not desired:
                status = 'NO_CONFIRMED_SOURCE'
            elif not actual:
                status = 'NOT_RECORDED'
            elif normalize(field, actual) == normalize(field, desired):
                status = 'MATCH_REPORTED'
            else:
                status = 'MISMATCH_REPORTED'
            results.append({'platform': row.get('platform', ''), 'field': field, 'label': label,
                            'expected': desired, 'recorded': actual, 'status': status,
                            'checked_on': row.get('checked_on', '')})
    return results


def report(results):
    lines = [
        '# Bleeding Ink — listing consistency review (offline)', '',
        '**Evidence:** USER-ENTERED snapshots ONLY. These comparisons are not independent verification.',
        'No platform was accessed or changed. A `MATCH_REPORTED` result does not prove the public listing is correct.', '',
        '| Platform | Field | Assessment |', '|---|---|---|',
    ]
    for item in results:
        lines.append(f"| {item['platform']} | {item['label']} | {item['status']} |")
    lines += ['', '## Review items', '']
    concerns = [r for r in results if r['status'] != 'MATCH_REPORTED']
    if not concerns:
        lines.append('All manually entered and dated fields match the local source. Independent checks are still required.')
    else:
        for item in concerns:
            lines.append(f"- **{item['platform']} · {item['label']}:** {item['status']}.")
    lines += ['', '## What the labels mean', '',
              '- `NOT_REVIEWED`: no manual inspection date entered.',
              '- `INVALID_CHECK_DATE`: inspection date must be a real YYYY-MM-DD date not in the future.',
              '- `NO_CONFIRMED_SOURCE`: canonical value is missing from `studio.json`.',
              '- `NOT_RECORDED`: a dated inspection has no recorded value for this field.',
              '- `MATCH_REPORTED`: values match after conservative normalization; not independently verified.',
              '- `MISMATCH_REPORTED`: values differ; inspect the listing and the source of truth before changing either.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=ROOT / 'studio.json')
    parser.add_argument('--listings', type=Path, default=ROOT / 'listing-snapshots.csv')
    parser.add_argument('--output', type=Path, default=ROOT / 'LISTING-AUDIT.md')
    args = parser.parse_args()
    with args.config.open(encoding='utf-8') as f:
        config = json.load(f)
    with args.listings.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    platforms = [row.get('platform') for row in rows]
    if len(platforms) != len(set(platforms)) or any(x not in PLATFORMS for x in platforms):
        raise ValueError('Listing CSV contains unknown or duplicate platform labels')
    args.output.write_text(report(compare(config, rows)), encoding='utf-8')
    print(f'Wrote {args.output} based only on local, owner-entered data')


if __name__ == '__main__':
    main()
