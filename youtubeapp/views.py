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
import matplotlib
import matplotlib.pyplot as plt


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

# data = json.loads(r.text)
# print(data['items'])
# for i in range(0,len(data['items'])):
# # print(data['items'][i]['id']['videoId'])
#     x=data['items'][i]['id']['videoId']
#     r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+x+"&key=AIzaSyBw0grXPH8gNIDwtuUw3Q-HgzGDULN_JkE")
#     print(json.loads(r.text)['items'][0]['statistics']['viewCount'])
#get entire channel statistics
#https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id=UC_x5XG1OV2P6uZZ5FSM9Ttw&key={YOUR_API_KEY}



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

