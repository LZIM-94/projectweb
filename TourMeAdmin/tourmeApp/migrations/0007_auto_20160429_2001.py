# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourmeApp', '0006_auto_20160429_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='Route',
        ),
        migrations.AddField(
            model_name='tour',
            name='Route',
            field=models.ManyToManyField(to='tourmeApp.Attraction'),
        ),
    ]