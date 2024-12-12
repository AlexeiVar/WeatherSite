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
    if request.method == 'POST':
        city = request.POST['city']
        language = request.POST['language']
        # порядок формата - API key, latitude, longitude
        weather_url = 'https://api.pirateweather.net/forecast/{}/{},{}?exclude=alerts,minutely,hourly&units=si'
        # порядок формата - Город, API key
        geocode_url = 'https://geocode.maps.co/search?q={}&api_key={}'

        current_weather_data, daily_forecast = fetch_forecast(city, weather_url, geocode_url, language)

        context = {
            'current_weather_data': current_weather_data,
            'daily_forecast': daily_forecast,
            'city': city,
            'language': language
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def fetch_forecast(city, weather_url, geocode_url, language):
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
    for daily_data in weather_response['daily']['data'][1:]:
        daily_forecast.append({
            "day": (datetime.fromtimestamp(daily_data['time']).strftime("%A")),
            'min_temp': daily_data['temperatureMin'],
            'max_temp': daily_data['temperatureMax'],
            'description': daily_data['summary'],
            'icon': daily_data['icon']
        })

    if language == 'rus':
        translation_days = {
            'Monday': 'Понедельник',
            'Tuesday': 'Вторник',
            'Wednesday': 'Среда',
            'Thursday': 'Четверг',
            'Friday': 'Пятница',
            'Saturday': 'Суббота',
            'Sunday': 'Воскресенье',
        }
        # К сожалению список не полный, ибо API не предоставляет все возможные варианты, в отличие от icon
        translation_description = {
            'Snow': 'Снег',
            'Clear': 'Чисто',
            'Cloudy': 'Облачно',
            'Partly Cloudy': 'Местами облачно',
            'Rain': 'Дождь',
            'Windy': 'Ветряно'
        }
        for data in daily_forecast:
            data['day'] = translation_days[data['day']]
            if data['description'] in translation_description:
                data['description'] = translation_description[data['description']]

        if current_weather_data['description'] in translation_description:
            current_weather_data['description'] = translation_description[current_weather_data['description']]

    return current_weather_data, daily_forecast
