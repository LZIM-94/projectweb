# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-01 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tourmeApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('tourmeApp', '0031_auto_20160507_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.ImageField(upload_to=tourmeApp.models.upload_scheme_path_handler)),
                ('floor', models.IntegerField(verbose_name='\u042d\u0442\u0430\u0436')),
            ],
            options={
                'verbose_name': '\u0421\u0445\u0435\u043c\u0430 \u044d\u0442\u0430\u0436\u0430',
                'verbose_name_plural': '\u0421\u0445\u0435\u043c\u0430 \u044d\u0442\u0430\u0436\u0435\u0439',
            },
        ),
        migrations.RemoveField(
            model_name='attraction',
            name='BuildingMapSource',
        ),
        migrations.AlterField(
            model_name='artist',
            name='MainPictureSource',
            field=models.ImageField(blank=True, upload_to=tourmeApp.models.upload_mainimage_path_handler, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='AudioGuideSource',
            field=models.FileField(blank=True, upload_to=tourmeApp.models.upload_audio_path_handler, verbose_name='\u0424\u0430\u0439\u043b \u0410\u0443\u0434\u0438\u043e\u0433\u0438\u0434\u0430'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='MainPictureSource',
            field=models.ImageField(blank=True, upload_to=tourmeApp.models.upload_mainimage_path_handler, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u0444\u043e\u0442\u043e'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Model3D',
            field=models.FileField(blank=True, upload_to=tourmeApp.models.upload_3d_path_handler, verbose_name='3D \u043c\u043e\u0434\u0435\u043b\u044c'),
        ),
        migrations.AlterField(
            model_name='attractionimage',
            name='image',
            field=models.ImageField(upload_to=tourmeApp.models.upload_image_path_handler),
        ),
        migrations.AlterField(
            model_name='tour',
            name='MainPictureSource',
            field=models.ImageField(blank=True, upload_to=tourmeApp.models.upload_mainimage_path_handler, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0442\u0443\u0440\u0430'),
        ),
        migrations.AddField(
            model_name='buildingmap',
            name='attraction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='tourmeApp.Attraction'),
        ),
    ]
