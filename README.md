# theweatherapp
Provides the weather forecast details.

#Getting Started
1. Install the dependencies from the requirements.txt file.
2. Use the following command in the project root directory to get the weather forecast details of any place:
    $ python weather.py <place>
    ex: $ python weather.py bangalore
3. By default the application provides data for the current time, alternatively one of the follwing additional parameters can be used:
    > 'today' | 'hourbyhour' | 'monthly'
    ex: $ python weather.py bangalore today
        $ python weather.py bangalore hourbyhour
        $ python weather.py bangalore monthly
