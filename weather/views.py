import datetime
import os
import requests
from dotenv import load_dotenv
from django.shortcuts import render

# Create your views here.
load_dotenv()


def index(request):
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')

    # порядок формата - API key, latitude, longitude
    weather_url = 'https://api.pirateweather.net/forecast/{}/{},{}?exclude=alerts,currently,minutely,hourly&units=si'
    # порядок формата - Город, API key
    geocode_url = 'https://geocode.maps.co/search?q={}&api_key={}'


