import requests
from bs4 import BeautifulSoup
from pprint import pformat


def hourbyhour(place_id):
    url = 'https://weather.com/en-IN/weather/hourbyhour/l/' + place_id
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')

    data = {
        "Place and Type of Forecast": soup.select('.locations-title.hourly-page-title > h1')[0].string,
        "Time": soup.select('.locations-title.hourly-page-title .observation-timestamp > span')[0].string,
    }

    title = ''
    for i in soup.select('.panel.item1.forecast-hourly > div > div > table > thead > tr > th'):
        title = title + i.text + '-'

    daily_data = []
    for i in soup.select('.panel.item1.forecast-hourly > div > div > table > tbody > tr > td'):
        if i.text == '':
            i = '-------------'
            daily_data.append(i)
            continue
        daily_data.append(i.text)
    data[title] = daily_data

    return pformat(data)
