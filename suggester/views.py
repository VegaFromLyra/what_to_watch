from django.shortcuts import render

import random
import content_source

def content(request):
  posters = content_source.posters()
  selected_poster_index = random.randint(0, len(posters) - 1)
  path = posters.values()[selected_poster_index]

  context = { 'image_source': path }

  return render(request, 'suggester/content.html', context)
