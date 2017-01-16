from django.shortcuts import render

def index(request):
  context = {
    'message': 'In progress...check back soon!'
  }
  return render(request, 'suggester/index.html', context)

def suggester(request):
  context = {
    'image_source': 'suggester/mock_content.jpeg'
  }

  return render(request, 'suggester/content.html', context)