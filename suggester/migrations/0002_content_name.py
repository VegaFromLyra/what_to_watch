# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-28 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggester', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='name',
            field=models.CharField(default='no_name', max_length=200),
        ),
    ]
