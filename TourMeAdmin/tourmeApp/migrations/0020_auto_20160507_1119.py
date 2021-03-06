# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import tourmeApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('tourmeApp', '0019_auto_20160506_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='Type',
            field=models.IntegerField(choices=[(0, '\u041e\u0431\u044a\u0435\u043a\u0442 \u043d\u0430 \u043c\u0438\u0440\u043e\u0432\u043e\u0439 \u043a\u0430\u0440\u0442\u0435'), (1, '\u041e\u0431\u044a\u0435\u043a\u0442 \u043d\u0430 \u043a\u0430\u0440\u0442\u0435 \u0432 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0438'), (2, '\u041e\u0431\u044a\u0435\u043a\u0442-\u0437\u043e\u043d\u0430 (\u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0435, \u043a\u043e\u043c\u043d\u0430\u0442\u0430)')], default=0, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='MainPictureSource',
            field=models.ImageField(blank=True, upload_to=tourmeApp.models.upload_path_handler, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='AudioGuideSource',
            field=models.FileField(blank=True, upload_to=tourmeApp.models.upload_path_handler, verbose_name='\u0424\u0430\u0439\u043b \u0410\u0443\u0434\u0438\u043e\u0433\u0438\u0434\u0430'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='BuildingMapSource',
            field=models.ImageField(blank=True, upload_to=tourmeApp.models.upload_path_handler, verbose_name='\u041a\u0430\u0440\u0442\u0430 \u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='MainPictureSource',
            field=models.ImageField(blank=True, upload_to=tourmeApp.models.upload_path_handler, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u0444\u043e\u0442\u043e'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Model3D',
            field=models.FileField(blank=True, upload_to=tourmeApp.models.upload_path_handler, verbose_name='3D \u043c\u043e\u0434\u0435\u043b\u044c'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='MainPictureSource',
            field=models.ImageField(blank=True, upload_to=tourmeApp.models.upload_path_handler, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0442\u0443\u0440\u0430'),
        ),
    ]
