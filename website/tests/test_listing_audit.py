import unittest

from audit_listings import compare, normalize


class ListingAuditTests(unittest.TestCase):
    def test_blank_rows_are_unverified_not_matches(self):
        canonical = {'streetAddress': '', 'cityStateZip': '', 'phone': '', 'hours': ''}
        rows = [{'platform': 'Google Business Profile', 'checked_on': '', 'business_name': '', 'phone': ''}]
        results = compare(canonical, rows)
        self.assertTrue(all(x['status'] == 'NOT_REVIEWED' for x in results))

    def test_known_difference_is_flagged_and_phone_is_normalized(self):
        canonical = {'streetAddress': '123 Main St', 'cityStateZip': 'Fiction City, PA 12345',
                     'phone': '(555) 123-4567', 'hours': 'Mon–Fri 10–6'}
        rows = [{'platform': 'Google Business Profile', 'checked_on': '2026-10-28',
                 'business_name': 'Bleeding Ink Tattoo', 'street_address': '123 Main St',
                 'city_state_zip': 'Fiction City, PA 12345', 'phone': '+1 555 123 4567',
                 'hours': 'Mon–Fri 11–7', 'profile_url': 'https://example.org', 'evidence_note': 'Manually checked'}]
        results = compare(canonical, rows)
        statuses = {x['field']: x['status'] for x in results}
        self.assertEqual(statuses['phone'], 'MATCH_REPORTED')
        self.assertEqual(statuses['hours'], 'MISMATCH_REPORTED')
        self.assertEqual(statuses['business_name'], 'MATCH_REPORTED')

    def test_unchecked_row_does_not_get_a_false_pass(self):
        canonical = {'streetAddress': '123 Main St'}
        rows = [{'platform': 'Yelp', 'checked_on': '', 'street_address': '123 Main St'}]
        statuses = [r['status'] for r in compare(canonical, rows)]
        self.assertEqual(statuses, ['NOT_REVIEWED'] * 5)

    def test_name_normalization_is_conservative(self):
        self.assertNotEqual(normalize('business_name', 'Bleeding Ink Tattoo near me'),
                            normalize('business_name', 'Bleeding Ink Tattoo'))


if __name__ == '__main__':
    unittest.main()
