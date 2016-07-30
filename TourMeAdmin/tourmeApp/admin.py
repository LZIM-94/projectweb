#coding=utf-8
from django.contrib import admin
from tourmeApp.models import Attraction
from tourmeApp.models import Tour
from tourmeApp.models import Artist
from tourmeApp.models import AttractionImage

class AttractionImageInline(admin.TabularInline):
    model = AttractionImage
    readonly_fields = ( 'image_tag', )


class AttractionAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None,               {'fields': ['Type','Title','Category']}),
                 ('Информация', {'fields': ['ShortInfo','AdvancedInfo','Artists'], 'classes': ['collapse']}),
                 ('Медиа-инфо', {'fields': ['MainPictureSource','image_tag','AudioGuideSource'], 'classes': ['collapse']}),
                 ('Координаты на глобальной карте', {'fields': ['MapCoordinates']}),
                  ('Карта здания', {'fields': ['BuildingMapSource'], 'classes': ['collapse']}),
                  ('Кординаты на карте здания', {'fields': ['AttractionRoot','xCoord_OnBuildMap','yCoord_OnBuildMap'], 'classes': ['collapse']}),
                  ('Зона в помещении (зал,комната)', {'fields': ['BuildMapZone']}),
                  ('3D модель', {'fields': ['Model3D']})
                 ]
    list_display = ('Title', 'Category')
    search_fields = ['Title']
    readonly_fields = ( 'image_tag', )
    inlines = [AttractionImageInline]

class TourAdmin(admin.ModelAdmin):
    list_display = ('Title','Count_of_attraction')
    raw_id_fields = ("Route",)
    readonly_fields = ( 'image_tag', )
    def Count_of_attraction(self, instance):
          return instance.Route.count()



class ArtistAdmin(admin.ModelAdmin):
       list_display = ('Title','MainPictureSource')
       readonly_fields = ( 'image_tag', )



admin.site.register(Attraction,AttractionAdmin)
admin.site.register(Tour,TourAdmin)
admin.site.register(Artist,ArtistAdmin)
