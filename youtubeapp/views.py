# Import the modules
import requests
import json
from rest_framework import serializers, viewsets
from . serializer import *
from . models import *
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.views.decorators.cache import cache_page


class ChannelMasterViewSet(viewsets.ModelViewSet):
    serializer_class = ChannelMasterSerializer
    queryset = ChannelMaster.objects.all()


class ChannelStatsViewSet(viewsets.ModelViewSet):
    serializer_class = ChannelStatsSerializer
    queryset = ChannelStats.objects.all()


class VideoMasterViewSet(viewsets.ModelViewSet):
    serializer_class = VideoMasterSerializer
    queryset = VideoMaster.objects.all()


class VideoStatsViewSet(viewsets.ModelViewSet):
    serializer_class = VideoStatsSerializer
    queryset = VideoStats.objects.all()







# Make it a bit prettier..
# Get the feed
# r = requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyBw0grXPH8gNIDwtuUw3Q-HgzGDULN_JkE&channelId=UCq-Fj5jknLsUf-MWSy4_brA&part=snippet,id&order=date&maxResults=20")
# # print(r.text)
# # Convert it to a Python dictionary
# data = json.loads(r.text)
#
# # print(data['items'])
#
# for i in range(0,len(data['items'])):
#     # print(data['items'][i]['id']['videoId'])
#     x=data['items'][i]['id']['videoId']
#     r = requests.get(
#         "https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+x+"&key=AIzaSyBw0grXPH8gNIDwtuUw3Q-HgzGDULN_JkE")
#     print(json.loads(r.text)['items'][0]['statistics']['viewCount'])
