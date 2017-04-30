from django.conf import settings
import requests
import json

def posters():
  payload = {
    'language': 'en-US',
    'sort_by': 'popularity.desc'
  }

  payload.update(_api_key())

  response = requests.get(_url(), data=payload)

  base = _base_image_url()

  posters = {}

  for item in response.json()["results"]:
    posters[item["title"]] = base + item["poster_path"]

  return posters

def _url():
  return getattr(settings, "MOVIE_DB_URL", None)

def _config_url():
  return getattr(settings, "CONFIG_URL", None)

# TODO: Cache this response
def _base_image_url():
  response = requests.get(_config_url(), data=_api_key())
  parsed_response = response.json()
  return parsed_response["images"]["secure_base_url"] + _image_size() + "/"

def _image_size():
  return "w500"

def _api_key():
  return { 'api_key': getattr(settings, "MOVIE_DB_KEY", None) }
