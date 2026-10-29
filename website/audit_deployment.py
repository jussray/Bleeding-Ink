#!/usr/bin/env python3
"""Offline audit for the deployed Bleeding Ink Worker artifact.

This inspects repository files only; it does not fetch the live site or query listings.
Missing owner approvals are reported, never treated as if they had been granted.
"""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SITE = Path(__file__).resolve().parent
REPO = SITE.parent


class SourceParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.images = []
        self.meta_robots = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get('id'):
            self.ids.append(d['id'])
        if tag == 'a' and d.get('href') is not None:
            self.links.append(d['href'])
        if tag == 'img':
            self.images.append(d)
        if tag == 'meta' and d.get('name', '').lower() == 'robots':
            self.meta_robots.append(d.get('content', '').lower())


def parse_html(source):
    parser = SourceParser()
    parser.feed(source)
    return parser


def page_problems(source, site_dir):
    parsed = parse_html(source)
    errors = []
    if not any('noindex' in meta for meta in parsed.meta_robots):
        errors.append('Missing prelaunch noindex robots meta tag')
    ids = set(parsed.ids)
    duplicate_ids = sorted({x for x in parsed.ids if parsed.ids.count(x) > 1})
    if duplicate_ids:
        errors.append('Duplicate IDs: ' + ', '.join(duplicate_ids))
    for href in parsed.links:
        if href.startswith('#') and href != '#' and unquote(href[1:]) not in ids:
            errors.append('Broken in-page link: ' + href)
    for img in parsed.images:
        src = img.get('src', '')
        if not src:
            errors.append('Image is missing src')
        elif not (src.startswith(('https:', 'http:', 'data:', '//'))):
            path = urlsplit(src).path.lstrip('/')
            if not path or not (site_dir / path).is_file():
                errors.append('Missing local image: ' + src)
        if 'alt' not in img:
            errors.append('Image is missing alt attribute: ' + src)
    if 'application/ld+json' in source:
        errors.append('Unverified structured data remains in prelaunch HTML')
    return errors, parsed


def audit(repo=REPO):
    repo = Path(repo)
    site = repo / 'website'
    findings = []
    failures = []
    try:
        config = json.loads((repo / 'wrangler.jsonc').read_text(encoding='utf-8'))
        if config.get('assets', {}).get('directory') != './website':
            failures.append('Cloudflare static-asset directory is not ./website')
        if config.get('assets', {}).get('binding') != 'ASSETS':
            failures.append('Worker ASSETS binding is missing or changed')
        if not (repo / config.get('main', 'missing')).is_file():
            failures.append('Cloudflare Worker entrypoint not found')
    except (OSError, ValueError) as exc:
        failures.append('Cannot inspect Wrangler config: ' + str(exc))

    try:
        rules = [line.strip() for line in (site / '.assetsignore').read_text(encoding='utf-8').splitlines()
                 if line.strip() and not line.strip().startswith('#')]
        if rules != ['*', '!/index.html', '!/assets/', '!/assets/**', '/assets/original-sign.jpg']:
            failures.append('Worker static upload allowlist differs from audited policy')
    except OSError:
        failures.append('Worker .assetsignore missing')

    try:
        rendered = (site / 'index.html').read_text(encoding='utf-8')
        errors, parsed = page_problems(rendered, site)
        failures.extend(errors)
        root = (repo / 'index.html').read_text(encoding='utf-8')
        other_errors, other = page_problems(root, repo)
        failures.extend('Root entrypoint: ' + x for x in other_errors)
        deployed_images = {x.get('src', '') for x in parsed.images}
        root_images = {x.get('src', '') for x in other.images}
        if root_images != deployed_images:
            findings.append(('DESIGN_DRIFT', 'Root and Cloudflare entrypoints use different image sets; root design changes do not automatically deploy.'))
    except OSError as exc:
        failures.append('Cannot inspect site entrypoints: ' + str(exc))

    try:
        studio = json.loads((site / 'studio.json').read_text(encoding='utf-8'))
        missing = [key for key in ('streetAddress', 'cityStateZip', 'phone', 'hours', 'siteUrl',
                                   'bookingUrl', 'googleReviewUrl') if not studio.get(key)]
        if missing:
            findings.append(('LISTINGS_PENDING', 'Unverified/missing studio fields: ' + ', '.join(missing)))
        approvals = [key for key in ('profileVerified', 'categoryConfirmed', 'reviewPolicyApproved',
                                     'crawlerPolicyApproved') if studio.get(key) is not True]
        if approvals:
            findings.append(('APPROVALS_PENDING', 'Owner approvals not recorded: ' + ', '.join(approvals)))
    except (OSError, ValueError) as exc:
        failures.append('Cannot inspect studio configuration: ' + str(exc))

    if (repo / 'robots.txt').is_file() and not (site / 'robots.txt').is_file():
        findings.append(('ROOT_ROBOTS_ONLY', 'Root robots.txt is outside the Cloudflare upload directory; its crawler choices are not deployed through this Worker.'))
    if (repo / 'sitemap.xml').is_file() and not (site / 'sitemap.xml').is_file():
        findings.append(('ROOT_SITEMAP_ONLY', 'Root sitemap.xml is outside the Worker upload directory; site remains noindex.'))
    findings.append(('LIVE_RUNTIME_UNKNOWN', 'No external live-page fetch or visual interaction test performed by this offline audit.'))
    return failures, findings


def markdown(failures, findings):
    lines = ['# Bleeding Ink — parallel deployment audit', '',
             '**Method:** Static, repository-only. No public website, owner account or business listing accessed.', '',
             '## Errors that should fail CI', '']
    lines.extend('- ' + s for s in failures) if failures else lines.append('None detected by the offline checks.')
    lines.extend(['', '## Warnings / launch gates', ''])
    lines.extend('- **' + label + ':** ' + message for label, message in findings)
    lines.extend(['', '**Do not interpret a green build as live-browser or business-profile verification.**', ''])
    return '\n'.join(lines)


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--output', type=Path, help='Write a Markdown report here')
    args = cli.parse_args()
    failures, findings = audit()
    report = markdown(failures, findings)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding='utf-8')
    else:
        print(report)
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())