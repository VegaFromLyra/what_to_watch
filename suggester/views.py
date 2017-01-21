from django.shortcuts import render

import random

def content(request):
  if random.randint(0, 1) == 0:
    path = 'suggester/landing.jpeg'
  else:
    path = 'suggester/mock_content.jpeg'

  context = { 'image_source': path }

  return render(request, 'suggester/content.html', context)