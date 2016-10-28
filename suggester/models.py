from __future__ import unicode_literals

from django.db import models

class User(models.Model):
  username = models.CharField(max_length=200)

  def __str__(self):
    return self.username

class Content(models.Model):
  name = models.CharField(max_length=200, default='no_name')
  type = models.CharField(max_length=200)
  user = models.ForeignKey(User)

  def __str__(self):
      return self.type + ":" + self.name

