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

    def test_parse_event(self):
        info = {
            'artists': 'Shabaka Hutchings (sax); Tom Herbert (double bass);  Tom Skinner (drums);  David Okumu (guitar); and Sam Shepherd (keys)',
            'city': 'LONDON',
            'date': 'MON 16TH JAN, 2017 5:30pm',
            'name': 'PLAYED TWICE, PHAROAH SANDERS\' "PHAROAH" - MONDAY 16TH JANUARY 2017',
            'venue': 'Brilliant Corners'
        }

        with open('testEventPage.html', 'r') as f:
            data = f.read().replace('\n', '')
            result = scraper.parse_event(data)
            self.assertEqual(result, info)

if __name__ == '__main__':
    unittest2.main()