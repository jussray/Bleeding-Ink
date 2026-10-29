import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WebsiteBuildTests(unittest.TestCase):
    def run_builder(self, data, release=False):
        with tempfile.TemporaryDirectory() as tmp:
            temp = Path(tmp)
            config = temp / 'studio.json'
            output = temp / 'index.html'
            config.write_text(json.dumps(data), encoding='utf-8')
            command = [sys.executable, str(ROOT / 'build.py'), '--config', str(config), '--output', str(output)]
            if release:
                command.append('--release')
            result = subprocess.run(command, text=True, capture_output=True)
            return result, output.read_text(encoding='utf-8') if output.exists() else ''

    def test_preview_is_not_indexed_and_never_invents_reviews_or_contact_details(self):
        result, html = self.run_builder({})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('content="noindex,nofollow"', html)
        self.assertIn('Not yet confirmed', html)
        self.assertNotIn('href=""', html)
        self.assertNotIn('itemprop="ratingValue"', html)
        self.assertNotIn('application/ld+json', html)
        self.assertIn('id="reviews"', html)
        self.assertIn('id="visit"', html)

    def test_verified_facts_and_review_links_are_server_rendered_into_html(self):
        data = {
            'streetAddress': '18 Fictional Ave',
            'cityStateZip': 'Sampleton, PA 12345',
            'phone': '(555) 010-0200',
            'hours': 'Mon–Fri 11 AM–7 PM',
            'bookingUrl': 'https://booking.example/studio',
            'googleReviewUrl': 'https://g.page/r/example/review',
            'googleMapsUrl': 'https://maps.google.com/?cid=123',
            'instagramUrl': 'https://instagram.com/example',
        }
        result, html = self.run_builder(data)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('18 Fictional Ave', html)
        self.assertIn('Mon–Fri 11 AM–7 PM', html)
        self.assertIn('tel:+15550100200', html)
        self.assertIn('https://g.page/r/example/review', html)
        self.assertIn('https://booking.example/studio', html)
        self.assertIn('Leave an honest Google review', html)
        self.assertIn('content="noindex,nofollow"', html)

    def test_unverified_data_blocks_release(self):
        result, html = self.run_builder({}, release=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Release blocked', result.stderr)
        self.assertFalse(html)

    def test_release_requires_explicit_attestations_and_site_url(self):
        data = {
            'streetAddress': '18 Fictional Ave',
            'cityStateZip': 'Sampleton, PA 12345',
            'phone': '(555) 010-0200',
            'hours': 'Mon–Fri 11 AM–7 PM',
            'bookingUrl': 'https://booking.example/studio',
            'googleReviewUrl': 'https://g.page/r/example/review',
            'googleMapsUrl': 'https://maps.google.com/?cid=123',
            'siteUrl': 'https://example.org/',
        }
        result, html = self.run_builder(data, release=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('profileVerified', result.stderr)
        data.update(profileVerified=True, categoryConfirmed=True, reviewPolicyApproved=True, crawlerPolicyApproved=True)
        result, html = self.run_builder(data, release=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('content="index,follow"', html)
        self.assertIn('rel="canonical" href="https://example.org/"', html)

    def test_booking_is_static_crawlable_link_without_javascript_when_configured(self):
        result, page = self.run_builder({'bookingUrl': 'https://example.org/request/'})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('href="https://example.org/request/"', page)
        self.assertIn('Book your session', page)
        self.assertNotIn('window.open(validBooking', page)

    def test_preview_without_booking_link_shows_nonfunctional_action_not_fake_href(self):
        result, page = self.run_builder({})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('id="bookingButton"', page)
        self.assertNotIn('href="#"', page)
        self.assertNotIn('<code>studio.json</code>', page)
        self.assertIn('Online booking is not available through this page yet.', page)

    def test_release_metadata_and_footer_use_verified_location_not_preview_claim(self):
        data = {
            'streetAddress': '18 Fictional Ave', 'cityStateZip': 'Sampleton, PA 12345',
            'phone': '(555) 010-0200', 'hours': 'Mon–Fri 11 AM–7 PM',
            'bookingUrl': 'https://example.org/request/', 'googleReviewUrl': 'https://g.page/r/example/review',
            'googleMapsUrl': 'https://maps.google.com/?cid=123', 'siteUrl': 'https://example.org/',
            'profileVerified': True, 'categoryConfirmed': True,
            'reviewPolicyApproved': True, 'crawlerPolicyApproved': True,
        }
        result, page = self.run_builder(data, release=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Sampleton, PA 12345', page)
        self.assertIn('name="description" content="Bleeding Ink Tattoo', page)
        self.assertNotIn('Preview concept</span>', page)
        self.assertNotIn('cinematic, glass-and-smoke tattoo studio concept.', page)
        self.assertNotIn('application/ld+json', page)

    def test_escapes_contact_fields(self):
        result, html = self.run_builder({'streetAddress': '<script>bad()</script>'})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('&lt;script&gt;bad()&lt;/script&gt;', html)
        self.assertNotIn('<script>bad()</script>', html)

    def test_invalid_url_rejected(self):
        result, html = self.run_builder({'googleReviewUrl': 'javascript:alert(1)'})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('googleReviewUrl', result.stderr)

if __name__ == '__main__':
    unittest.main()
