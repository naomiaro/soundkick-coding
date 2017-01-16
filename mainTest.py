import unittest2
import main as scraper

class Test(unittest2.TestCase):

    def test_parse_venue_location(self):
        [city, venue_name] = scraper.parse_venue_location('LONDON: Brilliant Corners')
        self.assertEqual(city, 'LONDON')
        self.assertEqual(venue_name, 'Brilliant Corners')


if __name__ == '__main__':
    unittest2.main()