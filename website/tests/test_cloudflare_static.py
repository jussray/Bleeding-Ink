"""Check Cloudflare preview assets are deliberately limited to HTML and image files."""
import json
import unittest
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
REPO = SITE.parent

class StaticDeployConfigTests(unittest.TestCase):
    def test_root_and_site_wranger_configs_match_worker_and_assets_path(self):
        for file, expected in ((REPO / 'wrangler.jsonc', './website'),
                               (SITE / 'wrangler.jsonc', './')):
            with self.subTest(config=str(file)):
                cfg = json.loads(file.read_text(encoding='utf-8'))
                self.assertEqual(cfg['name'], 'bleeding-ink')
                self.assertEqual(cfg['assets']['directory'], expected)
                self.assertEqual((file.parent / expected).resolve(), SITE.resolve())

    def test_only_html_and_images_are_selected_for_upload(self):
        lines = [x.strip() for x in (SITE / '.assetsignore').read_text().splitlines()
                 if x.strip() and not x.strip().startswith('#')]
        self.assertEqual(lines, ['*', '!/index.html', '!/assets/', '!/assets/**'])
        for p in ('index.html', 'assets/skeleton-hand.webp',
                  'assets/sign-detail.webp', 'assets/original-sign.jpg'):
            self.assertTrue((SITE / p).is_file(), p)
        for p in ('studio.json', 'build.py', 'audit_listings.py', 'template.html',
                  'listing-snapshots.csv', 'tests/test_build.py'):
            self.assertTrue((SITE / p).is_file(), p)

if __name__ == '__main__':
    unittest.main()
