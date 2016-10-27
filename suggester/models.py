from __future__ import unicode_literals

from django.db import models

class User(models.Model):
  username = models.CharField(max_length=200)

class Content(models.Model):
  name = models.CharField
  type = models.CharField(max_length=200)
  user = models.ForeignKey(User)

