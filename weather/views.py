import datetime
import os
import requests
from dotenv import load_dotenv
from django.shortcuts import render

# Create your views here.
load_dotenv()


def index(request):
    API_KEY = os.getenv('API_KEY')
