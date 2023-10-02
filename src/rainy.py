#!/usr/bin/env python

# Config

###########################################################################################################################

api_key = "changeme"  # Create an account on OpenWeather (it's free) and get your API token there
city = "changeme"  # Your city
units = "metric"  # you can choose metric or imperial (anything else is kelvin)
timeplus = 0  # Timezone used by default is UTC/GMT so you can define how many hours should be added to the time
timeminus = 0  # Timezone used by default is UTC/GMT so you can define how many hours should be subtracted from the time
showcityname = False  # Show the city name in information, True or False

###########################################################################################################################

import requests
import datetime
import sys

if units == "metric":
    windspeedunits = "m/s"
elif units == "imperial":
    windspeedunits = "mph"
else:
    windspeedunits = "m/s"

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&APPID={api_key}"
)

if weather_data.json()["cod"] == 200:
    pass
elif weather_data.json()["cod"] == "404":
    print("No city found.")
    sys.exit()
elif weather_data.json()["cod"] == 401:
    print("Invalid API key.")
    sys.exit()
else:
    print("Unknown error occured.")
    sys.exit()

sourcesunrise = weather_data.json()["sys"]["sunrise"]
sourcesunset = weather_data.json()["sys"]["sunset"]

sunrise_datetime = datetime.datetime.utcfromtimestamp(sourcesunrise)
sunset_datetime = datetime.datetime.utcfromtimestamp(sourcesunset)

adjusted_sunrise = (
    sunrise_datetime
    + datetime.timedelta(hours=timeplus)
    - datetime.timedelta(hours=timeminus)
)
adjusted_sunset = (
    sunset_datetime
    + datetime.timedelta(hours=timeplus)
    - datetime.timedelta(hours=timeminus)
)

sunrisestring = adjusted_sunrise.strftime("%H:%M:%S")
sunsetstring = adjusted_sunset.strftime("%H:%M:%S")

weather = weather_data.json()["weather"][0]["main"]

temp = str(round(weather_data.json()["main"]["temp"])) + "°"

if units == "metric":
    temp += "C"
elif units == "imperial":
    temp += "F"
else:
    temp += "K"

wind_speed = str(round(weather_data.json()["wind"]["speed"])) + " " + windspeedunits

output = []

if weather == "Clear":
    output = (
        [
            "               " + "City: " + city,
            "     \   /     " + "Weather: clear",
            "      .-.      " + "Temperature: " + temp,
            "   ‒ (   ) ‒   " + "Wind speed: " + wind_speed,
            "      `-᾿      " + "Sunrise: " + sunrisestring,
            "     /   \     " + "Sunset: " + sunsetstring,
            "               ",
        ]
        if showcityname
        else [
            "               " + "Weather: clear",
            "     \   /     " + "Temperature: " + temp,
            "      .-.      " + "Wind speed: " + wind_speed,
            "   ‒ (   ) ‒   " + "Sunrise: " + sunrisestring,
            "      `-᾿      " + "Sunset: " + sunsetstring,
            "     /   \     ",
            "               ",
        ]
    )
elif weather == "Clouds":
    output = (
        [
            "                 " + "City: " + city,
            "       .--.      " + "Weather: cloudy",
            "    .-(    ).    " + "Temprature: " + temp,
            "   (___.__)__)   " + "Wind speed: " + wind_speed,
            "                 " + "Sunrise: " + sunrisestring,
            "                 " + "Sunset: " + sunsetstring,
            "                 ",
        ]
        if showcityname
        else [
            "                 " + "Weather: cloudy",
            "       .--.      " + "Temprature: " + temp,
            "    .-(    ).    " + "Wind speed: " + wind_speed,
            "   (___.__)__)   " + "Sunrise: " + sunrisestring,
            "                 " + "Sunset: " + sunsetstring,
            "                 ",
        ]
    )
elif weather == "Rain":
    output = (
        [
            "                 " + "City: " + city,
            "       .--.      " + "Weather: rainy",
            "    .-(    ).    " + "Temprature: " + temp,
            "   (___.__)__)   " + "Wind speed: " + wind_speed,
            "    ʻ‚ʻ‚ʻ‚ʻ‚ʻ    " + "Sunrise: " + sunrisestring,
            "                 " + "Sunset: " + sunsetstring,
            "                 ",
        ]
        if showcityname
        else [
            "                 " + "Weather: rainy",
            "       .--.      " + "Temprature: " + temp,
            "    .-(    ).    " + "Wind speed: " + wind_speed,
            "   (___.__)__)   " + "Sunrise: " + sunrisestring,
            "    ʻ‚ʻ‚ʻ‚ʻ‚ʻ    " + "Sunset: " + sunsetstring,
            "                 ",
        ]
    )
elif weather == "Snow":
    output = (
        [
            "                 " + "City: " + city,
            "       .--.      " + "Weather: snowy",
            "    .-(    ).    " + "Temprature: " + temp,
            "   (___.__)__)   " + "Wind speed: " + wind_speed,
            "    * * * * *    " + "Sunrise: " + sunrisestring,
            "                 " + "Sunset: " + sunsetstring,
            "                 ",
        ]
        if showcityname
        else [
            "                 " + "Weather: snowy",
            "       .--.      " + "Temprature: " + temp,
            "    .-(    ).    " + "Wind speed: " + wind_speed,
            "   (___.__)__)   " + "Sunrise: " + sunrisestring,
            "    * * * * *    " + "Sunset: " + sunsetstring,
            "                 ",
        ]
    )
elif weather == "Thunderstorm" and showcityname == "yes":
    output = (
        [
            "                 " + "City: " + city,
            "       .--.      " + "Weather: stormy",
            "    .-(    ).    " + "Temprature: " + temp,
            "   (___.__)__)   " + "Wind speed: " + wind_speed,
            "        /_       " + "Sunrise: " + sunrisestring,
            "         /       " + "Sunset: " + sunsetstring,
            "                 ",
        ]
        if showcityname
        else [
            "       .--.      " + "Weather: stormy",
            "    .-(    ).    " + "Temprature: " + temp,
            "   (___.__)__)   " + "Wind speed: " + wind_speed,
            "        /_       " + "Sunrise: " + sunrisestring,
            "         /       " + "Sunset: " + sunsetstring,
            "                 ",
        ]
    )
else:
    output = (
        [
            "                 " + "City: " + city,
            "       .--.      " + "Weather: " + weather,
            "    .-(    ).    " + "Temprature: " + temp,
            "   (___.__)__)   " + "Wind speed: " + wind_speed,
            "                 " + "Sunrise: " + sunrisestring,
            "                 " + "Sunset: " + sunsetstring,
            "                 ",
        ]
        if showcityname
        else [
            "                 " + "Weather: " + weather,
            "       .--.      " + "Temprature: " + temp,
            "    .-(    ).    " + "Wind speed: " + wind_speed,
            "   (___.__)__)   " + "Sunrise: " + sunrisestring,
            "                 " + "Sunset: " + sunsetstring,
            "                 ",
        ]
    )

print(*output, sep="\n")
