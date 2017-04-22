from django.shortcuts import render
from django.conf import settings

import random
import requests
import json

def content(request):
  payload = {
    'language': 'en-US',
    'sort_by': 'popularity.desc'
  }

  payload.update(api_key())

  response = requests.get(url(), data=payload)

  base = base_image_url()

  posters = []

  for item in response.json()["results"]:
    posters.append(base + item["poster_path"])

  selected_poster_index = random.randint(0, len(posters) - 1)

  path = posters[selected_poster_index]

  context = { 'image_source': path }

  return render(request, 'suggester/content.html', context)

# TODO: Make this private
def url():
  return getattr(settings, "MOVIE_DB_URL", None)

def config_url():
  return getattr(settings, "CONFIG_URL", None)

def base_image_url():
  response = requests.get(config_url(), data=api_key())
  parsed_response = response.json()
  return parsed_response["images"]["secure_base_url"] + image_size() + "/" 

def image_size():
  return "w500"

def api_key():
  return { 'api_key': getattr(settings, "MOVIE_DB_KEY", None) }
