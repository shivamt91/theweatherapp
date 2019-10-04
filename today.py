import requests
from bs4 import BeautifulSoup
from pprint import pformat


def today(place_id):
    url = 'https://weather.com/en-IN/weather/today/l/' + place_id
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')

    data = {
        "Location": soup.select('.h4.today_nowcard-location')[0].text,
        "Time": soup.select('.loc-container .today_nowcard-timestamp > span')[1].string,
        "Temperature": soup.select('.today_nowcard-section.today_nowcard-condition .today_nowcard-temp > span')[0].text,
        "Phrase": soup.select('.today_nowcard-section.today_nowcard-condition .today_nowcard-phrase')[0].string,
        "Feels Like": soup.select('.today_nowcard-section.today_nowcard-condition .today_nowcard-feels')[0].text,
    }

    high_low = ''
    for i in soup.select('.today_nowcard-section.today_nowcard-condition .today_nowcard-hilo > span'):
        high_low = high_low + i.text
    data['High_Low'] = high_low

    uv = ''
    for i in soup.select('.today_nowcard-section.today_nowcard-condition .today_nowcard-hilo > div > span'):
        uv = uv + i.text
    data['UV'] = uv

    right_now = dict()
    for i in soup.select('.today_nowcard-sidecar.component.panel > table > tbody > tr'):
        right_now[i.select('th')[0].string] = i.select('td')[0].text
    data['Right_Now'] = right_now

    return pformat(data)
