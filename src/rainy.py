#!/usr/bin/env python3

# Config

###########################################################################################################################

api_key = "changeme"  # Create an account on OpenWeather (it's free) and get your API token there
city = "changeme"  # Your city
units = "metric"  # you can choose metric or imperial (anything else is kelvin)
timeplus = 0  # Time zone used by default is UTC/GMT so you can define how many hours should be added to the time
timeminus = 0  # Time zone used by default is UTC/GMT so you can define how many hours should be subtracted from the time
showcityname = False  # Show the city name in information, True or False
showdate = False # Shows the date.
datetype = "%x" # Use strftime formats to switch how date is displayed, i.e. "%a, %Y-%d-%m"

###########################################################################################################################

import requests
import datetime
import sys

date = datetime.datetime.now().strftime(datetype)

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


sunrise_datetime = datetime.datetime.fromtimestamp(sourcesunrise, tz=datetime.timezone.utc)
sunset_datetime = datetime.datetime.fromtimestamp(sourcesunset, tz=datetime.timezone.utc)

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
            r"               " + "City: " + city,
            r"     \   /     " + "Weather: clear",
            r"      .-.      " + "Temperature: " + temp,
            r"   ‒ (   ) ‒   " + "Wind speed: " + wind_speed,
            r"      `-᾿      " + "Sunrise: " + sunrisestring,
            r"     /   \     " + "Sunset: " + sunsetstring,
            r"               " + "Date: " + date  if showdate else "",
        ]
        if showcityname
        else [
            r"               ",
            r"     \   /     " + "Weather: clear",
            r"      .-.      " + "Temperature: " + temp,
            r"   ‒ (   ) ‒   " + "Wind speed: " + wind_speed,
            r"      `-᾿      " + "Sunrise: " + sunrisestring,
            r"     /   \     " + "Sunset: " + sunsetstring,
            r"               " + "Date: " + date  if showdate else "",
        ]
    )
elif weather == "Clouds":
    output = (
        [
            r"                 " + "City: " + city,
            r"       .--.      " + "Weather: cloudy",
            r"    .-(    ).    " + "Temperature: " + temp,
            r"   (___.__)__)   " + "Wind speed: " + wind_speed,
            r"                 " + "Sunrise: " + sunrisestring,
            r"                 " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date  if showdate else "",
        ]
        if showcityname
        else [
            r"                 " + "Weather: cloudy",
            r"       .--.      " + "Temperature: " + temp,
            r"    .-(    ).    " + "Wind speed: " + wind_speed,
            r"   (___.__)__)   " + "Sunrise: " + sunrisestring,
            r"                 " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date  if showdate else "",
        ]
    )
elif weather == "Rain":
    output = (
        [
            r"                 " + "City: " + city,
            r"       .--.      " + "Weather: rainy",
            r"    .-(    ).    " + "Temperature: " + temp,
            r"   (___.__)__)   " + "Wind speed: " + wind_speed,
            r"    ʻ‚ʻ‚ʻ‚ʻ‚ʻ    " + "Sunrise: " + sunrisestring,
            r"                 " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date  if showdate else "",
        ]
        if showcityname
        else [
            r"                 " + "Weather: rainy",
            r"       .--.      " + "Temperature: " + temp,
            r"    .-(    ).    " + "Wind speed: " + wind_speed,
            r"   (___.__)__)   " + "Sunrise: " + sunrisestring,
            r"    ʻ‚ʻ‚ʻ‚ʻ‚ʻ    " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date  if showdate else "",
        ]
    )
elif weather == "Snow":
    output = (
        [
            r"                 " + "City: " + city,
            r"       .--.      " + "Weather: snowy",
            r"    .-(    ).    " + "Temperature: " + temp,
            r"   (___.__)__)   " + "Wind speed: " + wind_speed,
            r"    * * * * *    " + "Sunrise: " + sunrisestring,
            r"                 " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date  if showdate else "",
        ]
        if showcityname
        else [
            r"                 " + "Weather: snowy",
            r"       .--.      " + "Temperature: " + temp,
            r"    .-(    ).    " + "Wind speed: " + wind_speed,
            r"   (___.__)__)   " + "Sunrise: " + sunrisestring,
            r"    * * * * *    " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date  if showdate else "",
        ]
    )
elif weather == "Thunderstorm":
    output = (
        [
            r"                 " + "City: " + city,
            r"       .--.      " + "Weather: stormy",
            r"    .-(    ).    " + "Temperature: " + temp,
            r"   (___.__)__)   " + "Wind speed: " + wind_speed,
            r"        /_       " + "Sunrise: " + sunrisestring,
            r"         /       " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date  if showdate else "",
        ]
        if showcityname
        else [
            r"       .--.      " + "Weather: stormy",
            r"    .-(    ).    " + "Temperature: " + temp,
            r"   (___.__)__)   " + "Wind speed: " + wind_speed,
            r"        /_       " + "Sunrise: " + sunrisestring,
            r"         /       " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date  if showdate else "",
        ]
    )
else:
    output = (
        [
            r"                 " + "City: " + city,
            r"       .--.      " + "Weather: " + weather,
            r"    .-(    ).    " + "Temperature: " + temp,
            r"   (___.__)__)   " + "Wind speed: " + wind_speed,
            r"                 " + "Sunrise: " + sunrisestring,
            r"                 " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date  if showdate else "",
        ]
        if showcityname
        else [
            r"                 " + "Weather: " + weather,
            r"       .--.      " + "Temperature: " + temp,
            r"    .-(    ).    " + "Wind speed: " + wind_speed,
            r"   (___.__)__)   " + "Sunrise: " + sunrisestring,
            r"                 " + "Sunset: " + sunsetstring,
            r"                 " + "Date: " + date if showdate else "",
        ]
    )

print(*output, sep="\n")
