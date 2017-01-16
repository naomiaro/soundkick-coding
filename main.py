import requests
import json
from bs4 import BeautifulSoup

#artists playing
#city
#name of the venue
#date
#price

if __name__ == '__main__':

    r = requests.get('http://www.wegottickets.com/searchresults/all')
    soup = BeautifulSoup(r.text, 'html.parser')

    event_links = soup.find_all('a', ['event_link'])

    parsedData = []

    for link in event_links:
        event_request = requests.get(link.attrs['href'])
        event_soup = BeautifulSoup(event_request.text, 'html.parser')

        info = event_soup.find_all('div', ['event-information'])
        venue = event_soup.find_all('div', ['venue-details'])

        venue_details = venue[0].h2.text
        [city, venue_name] = venue_details.split(':')

        event = link.parent.parent

        parsedData.append({
            'name': info[0].h1.text,
            'date': venue[0].h4.text,
            'venue': venue_name,
            'city': city,
            'artists': info[0].h4.text,
            'price': event.find_all('div', ['searchResultsPrice'])[0].text
        })


    with open('concert.json', 'w') as outfile:
        json.dump(parsedData, outfile, sort_keys=True, indent=4, ensure_ascii=False)


    next_link = soup.find_all('a', ['nextlink'])

    print(next_link[0].attrs['href'])