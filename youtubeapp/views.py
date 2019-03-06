# Import the modules
import requests
import json
from rest_framework import serializers, viewsets
from . serializer import *
from . models import *
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.views.decorators.cache import cache_page
from . filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ChannelMasterViewSet(viewsets.ModelViewSet):
    serializer_class = ChannelMasterSerializer
    queryset = ChannelMaster.objects.all()
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('@channel_id', '@channel_name')
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('channel_id', 'channel_name')

class ChannelStatsViewSet(viewsets.ModelViewSet):
    serializer_class = ChannelStatsSerializer
    queryset = ChannelStats.objects.all()

class VideoMasterViewSet(viewsets.ModelViewSet):
    serializer_class = VideoMasterSerializer
    queryset = VideoMaster.objects.all()
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('video_id', 'video_name')

class VideoStatsViewSet(viewsets.ModelViewSet):
    serializer_class = VideoStatsSerializer
    queryset = VideoStats.objects.all()

def home(request):
    return render(request,"youtubeapp/home.html")

def getchannelmasterui(request):
    return render(request,"youtubeapp/index.html")

def getvideomasterui(request):
    return render(request,"youtubeapp/video_master.html")

def getchannelstatsui(request):
    return render(request,"youtubeapp/channel_stats.html")

def getvideostatsui(request):
    return render(request,"youtubeapp/video_stats.html")

