# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourmeApp', '0004_auto_20160429_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='AttractionRoot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tourmeApp.Attraction'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='MainPictureSource',
            field=models.TextField(blank=True, verbose_name='Main image'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='ShortInfo',
            field=models.TextField(blank=True, verbose_name='Short information about atrist'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='Wiki_Link',
            field=models.TextField(blank=True, verbose_name='Link to Wikipedia page'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='AdvancedInfo',
            field=models.TextField(blank=True, verbose_name='Advanced information about attraction'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='AnyImagesSource',
            field=models.TextField(blank=True, verbose_name='Any images of attraction'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Artists',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tourmeApp.Artist'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='AudioGuideSource',
            field=models.TextField(blank=True, verbose_name='Audio guide file'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='BuildMapZone',
            field=models.TextField(blank=True, verbose_name='Zone in the building'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='BuildingMapSource',
            field=models.TextField(blank=True, verbose_name="Building's map"),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Longtitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='MainPictureSource',
            field=models.TextField(blank=True, verbose_name='Main image'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='ShortInfo',
            field=models.TextField(blank=True, verbose_name='Short information about attraction'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='xCoord_OnBuildMap',
            field=models.IntegerField(blank=True, null=True, verbose_name="X coordinate on building's map"),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='yCoord_OnBuildMap',
            field=models.IntegerField(blank=True, null=True, verbose_name="Y coordinate on building's map"),
        ),
        migrations.AlterField(
            model_name='tour',
            name='AdvancedInfo',
            field=models.TextField(blank=True, verbose_name='Advanced information about tour'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='MainPictureSource',
            field=models.TextField(blank=True, verbose_name='Main image'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='Route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourmeApp.Attraction'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='ShortInfo',
            field=models.TextField(blank=True, verbose_name='Short information about tour'),
        ),
    ]
