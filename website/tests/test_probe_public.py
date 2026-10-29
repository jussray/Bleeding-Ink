"""Read-only HTTP transport and evidence-separation regression checks."""
import importlib.util
import unittest
from pathlib import Path
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('bleeding_ink_probe', ROOT / 'probe_public.py')
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


class PublicProbeTests(unittest.TestCase):
    def test_http_success_does_not_prove_browser_or_listing(self):
        receipt = probe.observe(fetch=lambda _: (200, 'text/html', b'<meta name="robots" content="noindex,nofollow">'))
        self.assertEqual(receipt['http'], 'VERIFIED')
        self.assertEqual(receipt['meta_noindex'], 'VERIFIED')
        self.assertEqual(receipt['live_browser'], 'UNKNOWN')
        self.assertEqual(receipt['provider_release_sha'], 'UNKNOWN')
        self.assertEqual(receipt['listing_accuracy'], 'UNKNOWN')

    def test_missing_noindex_is_a_failure(self):
        receipt = probe.observe(fetch=lambda _: (200, 'text/html', b'<html><head></head></html>'))
        self.assertEqual(receipt['http'], 'VERIFIED')
        self.assertEqual(receipt['meta_noindex'], 'FAIL')

    def test_dns_outage_is_blocked_not_application_failure(self):
        def down(_):
            raise URLError('PRIVATE_ERROR_DETAIL')
        receipt = probe.observe(fetch=down)
        self.assertEqual(receipt['http'], 'BLOCKED')
        self.assertEqual(receipt['meta_noindex'], 'UNKNOWN')
        self.assertNotIn('PRIVATE_ERROR_DETAIL', probe.markdown(receipt))

    def test_real_http_404_exception_is_failure_not_transport_block(self):
        def missing(_):
            raise HTTPError(probe.SITE, 404, 'not found', {}, None)
        receipt = probe.observe(fetch=missing)
        self.assertEqual(receipt['http'], 'FAIL')
        self.assertEqual(receipt['meta_noindex'], 'UNKNOWN')

    def test_unapproved_url_is_rejected_without_fetch(self):
        for url in ('http://bleeding-ink.mcgill-raylene.workers.dev/',
                    'https://evil.invalid/',
                    'https://bleeding-ink.mcgill-raylene.workers.dev/?token=secret',
                    'https://bleeding-ink.mcgill-raylene.workers.dev@evil.invalid/'):
            with self.subTest(url=url):
                with self.assertRaises(ValueError):
                    probe.observe(url, fetch=lambda _: self.fail('Should not fetch'))

    def test_bad_response_is_a_failed_http_observation(self):
        self.assertEqual(probe.observe(fetch=lambda _: (404, 'text/html', b''))['http'], 'FAIL')
        self.assertEqual(probe.observe(fetch=lambda _: (200, 'application/json', b'{}'))['http'], 'FAIL')
        self.assertEqual(probe.observe(fetch=lambda _: (200, 'text/html', b'a' * 262145))['http'], 'FAIL')


if __name__ == '__main__':
    unittest.main()
