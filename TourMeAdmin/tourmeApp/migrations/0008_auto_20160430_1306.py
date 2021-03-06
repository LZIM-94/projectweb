# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourmeApp', '0007_auto_20160429_2001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': '\u0410\u0432\u0442\u043e\u0440', 'verbose_name_plural': '\u0410\u0432\u0442\u043e\u0440\u044b'},
        ),
        migrations.AlterModelOptions(
            name='attraction',
            options={'verbose_name': '\u0414\u043e\u0441\u0442\u043e\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u0414\u043e\u0441\u0442\u043e\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': '\u0422\u0443\u0440', 'verbose_name_plural': '\u0422\u0443\u0440\u044b'},
        ),
        migrations.AlterField(
            model_name='artist',
            name='MainPictureSource',
            field=models.TextField(blank=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='ShortInfo',
            field=models.TextField(blank=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='Title',
            field=models.CharField(max_length=128, verbose_name='\u0418\u043c\u044f \u0430\u0432\u0442\u043e\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='Wiki_Link',
            field=models.URLField(blank=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u0432 \u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='AdvancedInfo',
            field=models.TextField(blank=True, verbose_name='\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0434\u043e\u0441\u0442\u043e\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='AnyImagesSource',
            field=models.TextField(blank=True, verbose_name='\u0414\u0440\u0443\u0433\u0438\u0435 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Artists',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tourmeApp.Artist', verbose_name='\u0410\u0432\u0442\u043e\u0440 \u0442\u0432\u043e\u0440\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='AttractionRoot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tourmeApp.Attraction', verbose_name='\u041f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0438\u043b\u0438 \u0437\u043e\u043d\u0430 \u0433\u0434\u0435 \u043d\u0430\u0445\u043e\u0434\u0438\u0441\u044f \u043e\u0431\u044a\u0435\u043a\u0442'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='AudioGuideSource',
            field=models.TextField(blank=True, verbose_name='\u0424\u0430\u0439\u043b \u0410\u0443\u0434\u0438\u043e\u0433\u0438\u0434\u0430'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='BuildMapZone',
            field=models.TextField(blank=True, verbose_name='\u0417\u043e\u043d\u0430 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f (\u043a\u043e\u043c\u043d\u0430\u0442\u0430, \u0437\u0430\u043b)'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='BuildingMapSource',
            field=models.TextField(blank=True, verbose_name='\u041a\u0430\u0440\u0442\u0430 \u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Category',
            field=models.CharField(max_length=128, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Longtitude',
            field=models.FloatField(blank=True, null=True, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='MainPictureSource',
            field=models.TextField(blank=True, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u0444\u043e\u0442\u043e'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Model3D',
            field=models.TextField(blank=True, verbose_name='3D \u043c\u043e\u0434\u0435\u043b\u044c'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='ShortInfo',
            field=models.TextField(blank=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0434\u043e\u0441\u0442\u043e\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='Title',
            field=models.CharField(max_length=128, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='xCoord_OnBuildMap',
            field=models.IntegerField(blank=True, null=True, verbose_name='X \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430 \u043d\u0430 \u043a\u0430\u0440\u0442\u0435 \u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='yCoord_OnBuildMap',
            field=models.IntegerField(blank=True, null=True, verbose_name='Y \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430 \u043d\u0430 \u043a\u0430\u0440\u0442\u0435 \u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='AdvancedInfo',
            field=models.TextField(blank=True, verbose_name='\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0442\u0443\u0440\u0435'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='MainPictureSource',
            field=models.TextField(blank=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0442\u0443\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='Route',
            field=models.ManyToManyField(to='tourmeApp.Attraction', verbose_name='\u041c\u0430\u0440\u0448\u0440\u0443\u0442 (\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0441\u0442\u043e\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0435\u0439)'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='ShortInfo',
            field=models.TextField(blank=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0442\u0443\u0440\u0435'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='Title',
            field=models.CharField(max_length=128, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0443\u0440\u0430'),
        ),
    ]
