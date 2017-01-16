import requests
import json
from bs4 import BeautifulSoup

def parse_venue_location(location):
    try:
        [city, venue_name] = location.split(':')
        city = city.strip()
        venue_name = venue_name.strip()
    except Exception:
        city = location
        venue_name = location

    return [city, venue_name]

def extract_venue_details(venue):
    venue_details = venue[0].h2.text
    [city, venue_name] = parse_venue_location(venue_details)

    return [city, venue_name, venue[0].h4.text]


def scrape_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    event_links = soup.find_all('a', ['event_link'])
    parsedData = []

    for link in event_links:
        event_request = requests.get(link.attrs['href'])
        event_soup = BeautifulSoup(event_request.text, 'html.parser')

        info = event_soup.find_all('div', ['event-information'])
        venue = event_soup.find_all('div', ['venue-details'])

        [city, venue_name, date] = extract_venue_details()

        event = link.parent.parent

        try:
            price = event.find_all('div', ['searchResultsPrice'])[0].text
        except Exception:
            price = '??'

        parsedData.append({
            'name': info[0].h1.text,
            'date': date,
            'venue': venue_name,
            'city': city,
            'artists': info[0].h4.text,
            'price': price
        })

    next_link = soup.find_all('a', ['nextlink'])

    return [parsedData, next_link]

def dump_concerts(data):
    with open('concert.json', 'a') as outfile:
        json.dump(parsedData, outfile, sort_keys=True, indent=4, ensure_ascii=False)

if __name__ == '__main__':

    [parsedData, next_link] = scrape_page('http://www.wegottickets.com/searchresults/all')
    dump_concerts(parsedData)

    while(len(next_link)):
        [parsedData, next_link] = scrape_page(next_link[0].attrs['href'])
        dump_concerts(parsedData)
