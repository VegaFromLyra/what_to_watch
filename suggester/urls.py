from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.content, name='home'),
  url(r'^suggest/', views.content, name='content')
]