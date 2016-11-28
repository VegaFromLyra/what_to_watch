from django.shortcuts import render

def index(request):
  context = { 'title': 'What do you want to watch?'}
  return render(request, 'suggester/index.html', context)