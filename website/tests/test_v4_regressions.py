import datetime
import unittest
from audit_listings import compare
from build import validate

class ReleaseSafetyTests(unittest.TestCase):
    def test_rejects_backslash_in_absolute_url(self):
        with self.assertRaisesRegex(ValueError, 'bookingUrl'):
            validate({'bookingUrl': 'https://trusted.example\\@attacker.example/'}, release=False)

    def test_rejects_url_with_fragment_for_site_canonical(self):
        with self.assertRaisesRegex(ValueError, 'siteUrl'):
            validate({'siteUrl': 'https://studio.example/#foo'}, release=False)

    def test_rejects_http_and_credentials(self):
        for url in ('http://studio.example', 'https://name:pass@studio.example'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                validate({'bookingUrl': url}, release=False)

class AuditDateTests(unittest.TestCase):
    def test_malformed_inspection_date_is_not_a_match(self):
        rows=[{'platform':'Google Business Profile','checked_on':'yesterday', 'business_name':'Bleeding Ink Tattoo'}]
        result=compare({},rows)
        self.assertTrue(all(x['status']=='INVALID_CHECK_DATE' for x in result))

    def test_future_inspection_date_is_not_a_match(self):
        future=(datetime.date.today()+datetime.timedelta(days=2)).isoformat()
        rows=[{'platform':'Yelp','checked_on':future,'business_name':'Bleeding Ink Tattoo'}]
        result=compare({},rows)
        self.assertTrue(all(x['status']=='INVALID_CHECK_DATE' for x in result))

    def test_valid_inspection_date_still_reports_match(self):
        rows=[{'platform':'Yelp','checked_on':datetime.date.today().isoformat(),'business_name':'Bleeding Ink Tattoo'}]
        result=compare({},rows)
        name=[x for x in result if x['field']=='business_name'][0]
        self.assertEqual(name['status'],'MATCH_REPORTED')

if __name__=='__main__': unittest.main()
