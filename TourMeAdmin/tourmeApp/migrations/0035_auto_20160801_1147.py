# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-01 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import tourmeApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('tourmeApp', '0034_auto_20160801_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='MainPictureSource',
            field=models.ImageField(blank=True, upload_to=tourmeApp.models.upload_mainimage_path_handler, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='MainPictureSource',
            field=models.ImageField(blank=True, upload_to=tourmeApp.models.upload_mainimage_path_handler, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u0444\u043e\u0442\u043e'),
        ),
    ]
