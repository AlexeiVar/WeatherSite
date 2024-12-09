from datetime import datetime
import os
import requests
from dotenv import load_dotenv
from django.shortcuts import render

# Create your views here.
load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')


def index(request):
    # порядок формата - API key, latitude, longitude
    weather_url = 'https://api.pirateweather.net/forecast/{}/{},{}?exclude=alerts,minutely,hourly&units=si'
    # порядок формата - Город, API key
    geocode_url = 'https://geocode.maps.co/search?q={}&api_key={}'

    if request.method == 'POST':
        city = request.POST['city']

        current_weather_data, daily_forecast = fetch_forecast(city, weather_url, geocode_url)

        context = {
            'current_weather_data': current_weather_data,
            'daily_forecast': daily_forecast
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def fetch_forecast(city, weather_url, geocode_url):
    geo_response = requests.get(geocode_url.format(city, GEOCODE_API_KEY)).json()
    lat = geo_response[0]['lat']
    lon = geo_response[0]['lon']
    weather_response = requests.get(weather_url.format(WEATHER_API_KEY, lat, lon)).json()

    current_weather_data = {
        "city": city,
        "temperature": weather_response['currently']['temperature'],
        "description": weather_response['currently']['summary'],
        "icon": weather_response['currently']['icon']
    }

    daily_forecast = []
    for daily_data in weather_response['daily']['data'][:5]:
        daily_forecast.append({
            "day": (datetime.fromtimestamp(daily_data['time']).strftime("%A")),
            'min_temp': daily_data['temperatureMin'],
            'max_temp': daily_data['temperatureMax'],
            'description': daily_data['summary'],
            'icon': daily_data['icon']
        })

    return current_weather_data, daily_forecast
