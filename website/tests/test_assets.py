"""Regression check: all site-referenced local image assets ship in the repo."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AssetPackagingTests(unittest.TestCase):
    def test_referenced_images_exist_and_are_not_empty(self):
        html = (ROOT / 'template.html').read_text(encoding='utf-8')
        referenced = set(re.findall(r'(?:src|srcset)=["\'](assets/[^"\']+)["\']', html))
        self.assertGreaterEqual(len(referenced), 2)
        for relative in sorted(referenced):
            with self.subTest(asset=relative):
                asset = ROOT / relative
                self.assertTrue(asset.is_file(), f'Missing website image: {relative}')
                if asset.is_file():
                    self.assertGreater(asset.stat().st_size, 1000, f'Unexpectedly empty: {relative}')


if __name__ == '__main__':
    unittest.main()
