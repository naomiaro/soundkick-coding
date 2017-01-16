import unittest2
import main as scraper

class Test(unittest2.TestCase):

    def test_parse_venue_location_good(self):
        [city, venue_name] = scraper.parse_venue_location('LONDON: Brilliant Corners')
        self.assertEqual(city, 'LONDON')
        self.assertEqual(venue_name, 'Brilliant Corners')

    def test_parse_venue_location_bad(self):
        [city, venue_name] = scraper.parse_venue_location('CHORLEY LITTLE THEATRE, DOLE LANE, CHORLEY, PR7 2RL')
        self.assertEqual(city, 'CHORLEY LITTLE THEATRE, DOLE LANE, CHORLEY, PR7 2RL')
        self.assertEqual(venue_name, 'CHORLEY LITTLE THEATRE, DOLE LANE, CHORLEY, PR7 2RL')


if __name__ == '__main__':
    unittest2.main()