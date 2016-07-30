#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
import tourmeApp.models
from tourmeApp.models import Artist
from tourmeApp.models import Attraction
from tourmeApp.models import Tour, AttractionImage
from django.core import serializers



# Create your views here.
def getRegion(request):
    if 'region' in request.GET and request.GET['region']:
        region = request.GET['region']
        
        artistJS = serializers.serialize('json',Artist.objects.all())
        attrJS = serializers.serialize('json',Attraction.objects.all())
        toursJS = serializers.serialize('json',Tour.objects.all())
        
        regionmap = 'link to tile'
        
        jsonDict = {
            "attractions": json.loads(attrJS),
                "tours": json.loads(toursJS),
                "artists": json.loads(artistJS),
                "map": regionmap
            }
    
        return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )
    else:
        jsonDict = { "errors": 'No arguments' }
        return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )

def getAttraction(request):
    if 'id' in request.GET:
        id = request.GET['id']
        attrJS = serializers.serialize('json', Attraction.objects.filter(id=id))
        if attrJS == "[]":
            jsonDict = { "errors": 'id not found' }
            return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )
        else:
            return HttpResponse( attrJS, content_type="application/json" )
    else:
        jsonDict = { "errors": 'Need argument: id' }
        return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )

def getTour(request):
    if 'id' in request.GET:
        id = request.GET['id']
        tourJS = serializers.serialize('json', Tour.objects.filter(id=id))
        if tourJS == "[]":
            jsonDict = { "errors": 'id not found' }
            return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )
        else:
            return HttpResponse( tourJS, content_type="application/json" )
    else:
        jsonDict = { "errors": 'Need argument: id' }
        return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )

def syncRegionContent(request):
    if 'region' in request.GET:
        attrJS = json.dumps([dict(item) for item in Attraction.objects.all().values('id', 'Title')])
        toursJS = json.dumps([dict(item) for item in Tour.objects.all().values('id', 'Title')])
        artistJS = json.dumps([dict(item) for item in Artist.objects.all().values('id', 'Title')])
        jsonDict = {
            "attractions": json.loads(attrJS),
                "tours": json.loads(toursJS),
                "artists": json.loads(artistJS),
            }
        return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )
    else:
        jsonDict = { "errors": 'Need argument: region' }
        return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )


def getAnyImage(request):
    if 'id' in request.GET:
        id = request.GET['id']
        imagesJS = serializers.serialize('json', AttractionImage.objects.filter(attraction=id))
        if imagesJS == "[]":
            jsonDict = { "errors": 'id not found' }
            return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )
        else:
            jsonDict = {
                "images": json.loads(imagesJS),
                }
            return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )
    else:
        jsonDict = { "errors": 'Need argument: id' }
        return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )




def getExhibits(request):
    if 'id' in request.GET:
        id = request.GET['id']
        exhibitsJS = serializers.serialize('json', Attraction.objects.filter(AttractionRoot=id))
        if exhibitsJS == "[]":
            jsonDict = { "errors": 'id not found' }
            return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )
        else:
            jsonDict = {
                "exhibits": json.loads(exhibitsJS),
            }
            return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )
    else:
        jsonDict = { "errors": 'Need argument: id' }
        return HttpResponse( json.dumps( jsonDict ), content_type="application/json" )