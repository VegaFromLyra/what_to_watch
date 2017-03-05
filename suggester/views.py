from django.shortcuts import render
from django.conf import settings

import random
import requests

def content(request):
  payload = {
    'api_key': getattr(settings, "MOVIE_DB_KEY", None),
    'language': 'en-US',
    'sort_by': 'popularity.desc'
  }

  response = requests.request("GET", url(), data=payload)

  print(response.url)

  if random.randint(0, 1) == 0:
    path = 'suggester/landing.jpeg'
  else:
    path = 'suggester/mock_content.jpeg'

  context = { 'image_source': path }

  return render(request, 'suggester/content.html', context)

# TODO: Make this private
def url():
  return getattr(settings, "MOVIE_DB_URL", None)