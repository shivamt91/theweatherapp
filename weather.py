import sys
import requests
import json
from today import today
from hourbyhour import hourbyhour
from monthly import monthly


def the_weather():
    arguments = sys.argv

    if len(arguments) == 2:
        place = arguments[1]
        type_of_forecast = 'today'
    elif len(arguments) == 3:
        place = arguments[1]
        type_of_forecast = arguments[2]
    else:
        return 'Please give valid parameters!'

    api = 'https://api.weather.com/v3/location/search?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&language=en-IN&locationType=locale&query='
    my_api = api + place
    response = requests.get(my_api)

    if response.status_code == 200:
        data = json.loads(response.text)
        cities = data['location']['city']
        i = 0
        for i in range(len(cities)):
            if cities[i].lower() == place.lower():
                break
        place_id = data['location']['placeId'][i]

        if type_of_forecast == 'hourbyhour':
            print(hourbyhour(place_id))
        elif type_of_forecast == 'today':
            print(today(place_id))
        elif type_of_forecast == 'monthly':
            print(monthly(place_id))
        else:
            return 'Please enter a valid type_of_forecast!'

    else:
        return 'Please enter a valid place!'


the_weather()
