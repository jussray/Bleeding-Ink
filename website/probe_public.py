#!/usr/bin/env python3
"""Read-only HTTP observation of the authorized Bleeding Ink public preview.

HTTP success does not prove browser behavior, Cloudflare release SHA, or listings.
"""
import argparse
import re
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler

SITE = 'https://bleeding-ink.mcgill-raylene.workers.dev/'
ALLOWED_HOST = 'bleeding-ink.mcgill-raylene.workers.dev'


def verify_url(url):
    parts = urlsplit(url)
    if (parts.scheme != 'https' or parts.hostname != ALLOWED_HOST
            or parts.username or parts.password or parts.port not in (None, 443)
            or parts.path not in ('', '/') or parts.query or parts.fragment):
        raise ValueError('Only the known Bleeding Ink public preview URL is permitted')
    return SITE


class PinnedRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new = urlsplit(newurl)
        if new.scheme != 'https' or new.hostname != ALLOWED_HOST or new.port not in (None, 443):
            raise ValueError('Redirect left the authorized preview host')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def read_public(url):
    opener = build_opener(PinnedRedirects())
    request = Request(url, headers={'User-Agent': 'BleedingInk-ReadOnly-Audit/1.0',
                                    'Accept': 'text/html'})
    with opener.open(request, timeout=12) as response:
        return response.status, response.headers.get_content_type(), response.read(262145)


def observe(url=SITE, fetch=read_public):
    url = verify_url(url)
    receipt = {
        'subject': url,
        'probe': 'read-only public HTTP GET, 256 KiB cap, no cookies',
        'http': 'UNKNOWN', 'meta_noindex': 'UNKNOWN',
        'live_browser': 'UNKNOWN', 'provider_release_sha': 'UNKNOWN',
        'listing_accuracy': 'UNKNOWN', 'notes': []
    }
    try:
        status, mime, body = fetch(url)
    except HTTPError as ex:
        receipt['http'] = 'FAIL'
        receipt['notes'].append('HTTP endpoint returned an error status: ' + str(ex.code))
        return receipt
    except (URLError, OSError, TimeoutError, ValueError) as ex:
        receipt['http'] = 'BLOCKED'
        receipt['notes'].append('HTTP probe could not establish a response: ' + type(ex).__name__)
        return receipt
    if status != 200 or mime != 'text/html' or len(body) > 262144:
        receipt['http'] = 'FAIL'
        receipt['notes'].append('Unexpected HTTP status, media type or body size')
        return receipt
    receipt['http'] = 'VERIFIED'
    page = body.decode('utf-8', errors='replace')
    if re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'][^"\']*noindex', page, re.I):
        receipt['meta_noindex'] = 'VERIFIED'
    else:
        receipt['meta_noindex'] = 'FAIL'
        receipt['notes'].append('Expected noindex meta is absent from HTTP response')
    receipt['notes'].append('HTTP response is not proof of animations, assets, booking or visual UX')
    return receipt


def markdown(receipt):
    lines = [
        '# Bleeding Ink — public HTTP observation', '',
        '**Scope:** pinned public URL only. No login, cookies, forms or external listings.', '',
        '| Evidence plane | Status |', '|---|---|',
    ]
    for key in ('http', 'meta_noindex', 'live_browser', 'provider_release_sha', 'listing_accuracy'):
        lines.append(f"| {key} | {receipt[key]} |")
    lines += ['', '## Limits', '']
    lines.extend('- ' + n for n in receipt['notes'])
    lines += ['', 'CI PASS does not establish live rendered UX, provider-SHA parity, or shop facts.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default=SITE)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        receipt = observe(args.url)
    except ValueError as ex:
        parser.error(str(ex))
    report = markdown(receipt)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding='utf-8')
    else:
        print(report)
    return int(receipt['http'] == 'FAIL' or receipt['meta_noindex'] == 'FAIL')


if __name__ == '__main__':
    raise SystemExit(main())
