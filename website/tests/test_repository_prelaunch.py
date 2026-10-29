"""Repository-level preview checks: both HTML entrypoints must remain safe.
The Worker currently deploys website/, but the root HTML is also a possible
hosting entrypoint, so prevent accidental publication of placeholder metadata.
"""
import json
import re
import unittest
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
REPO = SITE.parent


class RepositoryPreviewSafetyTests(unittest.TestCase):
    def test_all_repository_entrypoints_are_prelaunch_safe(self):
        for entry in (REPO / 'index.html', SITE / 'index.html'):
            with self.subTest(page=str(entry.relative_to(REPO))):
                self.assertTrue(entry.is_file(), f'Missing preview entrypoint: {entry}')
                if not entry.is_file():
                    continue
                page = entry.read_text(encoding='utf-8')
                head = page.split('</head>', 1)[0]
                self.assertIn('content="noindex,nofollow"', head)
                self.assertNotIn('application/ld+json', page)
                self.assertNotIn('https://[domain]', head)
                self.assertNotIn('img/og-1200x630.jpg', head)

    def test_worker_assets_directory_is_not_repo_root(self):
        config = json.loads((REPO / 'wrangler.jsonc').read_text(encoding='utf-8'))
        self.assertEqual(config['name'], 'bleeding-ink')
        self.assertEqual(config['assets']['directory'], './website')


if __name__ == '__main__':
    unittest.main()
