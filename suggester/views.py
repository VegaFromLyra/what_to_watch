from django.shortcuts import render

def index(request):
  context = {
    'title': 'What do you want to watch?',
    'message': 'In progress...check back soon!'
  }
  return render(request, 'suggester/index.html', context)