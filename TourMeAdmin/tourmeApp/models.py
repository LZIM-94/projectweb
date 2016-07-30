#coding=utf-8


from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
from django.utils.safestring import mark_safe

def upload_path_handler(instance, filename):
    return "Content/Авторы/{id}/{file}".format(id=instance.Title, file=filename)


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField("Имя автора",max_length=128)
    ShortInfo = models.TextField("Краткая информация об авторе",blank=True)
    Wiki_Link = models.URLField("Ссылка на страницу в Википедии",blank=True)
    MainPictureSource = models.ImageField("Изображение автора",blank=True, upload_to = upload_path_handler)
    
    def image_tag(self):
        return mark_safe(u'<style> .imgstyle {   height: auto; width: auto;  max-width: 300px; max-height: 300px;  } </style> <img src="%s" class =  "imgstyle" ></img>' %(self.MainPictureSource.url))
    image_tag.short_description = 'Фото Автора'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.Title
    
  
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('Title',)

def upload_path_handler(instance, filename):
    return "Content/Достопримечательности/{id}/{file}".format(id=instance.Title, file=filename)

class Attraction(models.Model):
    id = models.AutoField(primary_key=True)
    TYPE_CHOICES = (
        (0, 'Объект на мировой карте'),
        (1, 'Объект на карте в помещении'),
        (2, 'Объект-зона (помещение, комната)'),
    )
    Type = models.IntegerField("Тип объекта",default=0, choices = TYPE_CHOICES)
    Title = models.CharField("Название",max_length=128)
    ShortInfo = models.TextField("Краткая информация о достопримечательности",blank=True)
    AdvancedInfo = models.TextField("Подробная информация о достопримечательности",blank=True)
    MainPictureSource = models.ImageField("Основное фото",blank=True,upload_to = upload_path_handler)
    AudioGuideSource = models.FileField("Файл Аудиогида",blank=True,upload_to = upload_path_handler)
    MapCoordinates = GeopositionField("Координаты на карте",null = True,blank=True);
    xCoord_OnBuildMap = models.IntegerField("X координата на карте здания",null = True,blank=True)
    yCoord_OnBuildMap = models.IntegerField("Y координата на карте здания",null = True,blank=True)
    BuildingMapSource = models.ImageField("Карта здания",blank=True,upload_to = upload_path_handler)
    AttractionRoot = models.ForeignKey('self', null = True,blank=True, verbose_name="Помещение или зона где находися объект")
    Artists =  models.ManyToManyField(Artist,null = True,blank=True, verbose_name="Автор творения")
    Model3D = models.FileField("3D модель",blank=True,upload_to = upload_path_handler)
    BuildMapZone = models.TextField("Зона помещения (комната, зал)",blank=True)
    Category = models.CharField("Категория",max_length=128)
    def __unicode__(self):
        return self.Title
    
    def image_tag(self):
        return  mark_safe(u'<style> .imgstyle {   height: auto; width: auto;  max-width: 300px; max-height: 300px;  } </style> <img src="%s" class =  "imgstyle" ></img>' % (self.MainPictureSource.url))
    image_tag.short_description = 'Фото достопримечательности'
    image_tag.allow_tags = True
    
    
    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'
        ordering = ('Title',)

def upload_path_handler(instance, filename):
    return "Content/Туры/{id}/{file}".format(id=instance.Title, file=filename)

class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField("Название тура",max_length=128)
    ShortInfo = models.TextField("Краткая информация о туре",blank=True)
    AdvancedInfo = models.TextField("Подробная информация о туре",blank=True)
    MainPictureSource = models.ImageField("Изображение тура",blank=True,upload_to = upload_path_handler)
    Route = models.ManyToManyField(Attraction, verbose_name="Маршрут (Список достопримечательностей)")
    def __unicode__(self):
        return self.Title
    
    def image_tag(self):
        return  mark_safe(u'<style> .imgstyle {   height: auto; width: auto;  max-width: 300px; max-height: 300px;  } </style> <img src="%s" class =  "imgstyle" ></img>' % (self.MainPictureSource.url))
    image_tag.short_description = 'Фото тура'
    image_tag.allow_tags = True
    
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ('Title',)


def upload_path_handler(instance, filename):
    return "Content/Достопримечательности/{id}/{file}".format(id=instance.attraction.Title, file=filename)

class AttractionImage(models.Model):
   
    attraction = models.ForeignKey('Attraction', related_name='images')
    image = models.ImageField(upload_to = upload_path_handler)
    
    def image_tag(self):
        return  mark_safe(u'<style> .imgstyle {   height: auto; width: auto;  max-width: 300px; max-height: 300px;  } </style> <img src="%s" class =  "imgstyle" ></img>' % (self.image.url))
    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

