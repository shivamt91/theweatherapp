import requests
from bs4 import BeautifulSoup
from pprint import pformat


def monthly(place_id):
    url = 'https://weather.com/en-IN/weather/monthly/l/' + place_id
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')

    data = {
        "Place and Type of Forecast": soup.select('.locations-title.monthly-page-title > h1')[0].string,
        "Time": soup.select('.observation-timestamp > span')[0].string,
    }

    my_data = []
    for i in soup.select('.forecast-monthly__calendar > div'):
        my_data.append(i.text)

    data["Monthly_Data"] = my_data

    return pformat(data)
