"""Regression tests for offline deployment contract audit."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('audit_deployment', ROOT / 'audit_deployment.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class DeploymentAuditTests(unittest.TestCase):
    def test_finds_broken_navigation_and_missing_images(self):
        with tempfile.TemporaryDirectory() as temp:
            html = '<meta name="robots" content="noindex,nofollow"><a href="#missing">A</a><img src="assets/missing.webp">'
            errors, _ = module.page_problems(html, Path(temp))
            self.assertTrue(any('Broken in-page link' in error for error in errors))
            self.assertTrue(any('Missing local image' in error for error in errors))
            self.assertTrue(any('alt attribute' in error for error in errors))

    def test_accepts_present_image_and_anchor(self):
        with tempfile.TemporaryDirectory() as temp:
            img = Path(temp) / 'assets' / 'hand.webp'
            img.parent.mkdir()
            img.write_bytes(b'fake-image-fixture')
            html = '<meta name="robots" content="noindex,nofollow"><a href="#visit">Visit</a><section id="visit"></section><img src="assets/hand.webp" alt="">'
            errors, _ = module.page_problems(html, Path(temp))
            self.assertEqual(errors, [])

    def test_flags_unapproved_schema_and_missing_noindex(self):
        errors, _ = module.page_problems('<script type="application/ld+json">{}</script>', ROOT)
        self.assertTrue(any('noindex' in error for error in errors))
        self.assertTrue(any('structured data' in error for error in errors))

    def test_warning_does_not_claim_live_verification(self):
        report = module.markdown([], [('LIVE_RUNTIME_UNKNOWN', 'Not inspected')])
        self.assertIn('repository-only', report)
        self.assertIn('Not inspected', report)


if __name__ == '__main__':
    unittest.main()
