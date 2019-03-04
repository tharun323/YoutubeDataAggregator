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

l=['UC-lHJZR3Gqxm24_Vd_AJ5Yw','UCq-Fj5jknLsUf-MWSy4_brA','UC295-Dw_tDNtZXFeAPAW6Aw',
   'UCffDXn7ycAzwL2LDlbyWOTw','UCIwFjwMjI0y7PDBVEO9-bkQ','UCpEhnqL0y41EpW2TvWAHD7Q'
   'UCJ5v_MCY6GNUBTO8-D3XoAg','UCRijo3ddMTht_IHyNSNXpNQ','UCbCmjCuTUZos6Inko4u57UQ'
   'UCZJ7m7EnCNodqnu5SAtg8eQ']


# data = json.loads(r.text)
# print(data['items'])
# for i in range(0,len(data['items'])):
# # print(data['items'][i]['id']['videoId'])
#     x=data['items'][i]['id']['videoId']
#     r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+x+"&key=AIzaSyBw0grXPH8gNIDwtuUw3Q-HgzGDULN_JkE")
#     print(json.loads(r.text)['items'][0]['statistics']['viewCount'])
#get entire channel statistics
#https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id=UC_x5XG1OV2P6uZZ5FSM9Ttw&key={YOUR_API_KEY}


def getchannelstatsdata(request):
    for i in l:
        r=requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id="+i+"&key=AIzaSyBw0grXPH8gNIDwtuUw3Q-HgzGDULN_JkE")
        print(r)

def getvideomasterdata(request):
    for i in l:
        r = requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyBw0grXPH8gNIDwtuUw3Q-HgzGDULN_JkE&channelId=" + i + "&part=snippet,id&order=date&maxResults=10")
        data = json.loads(r.text)
        for j in range(0,len(data['items'])):
            vid=json.loads(r.text)['items'][j]['id']['videoId']
            vname=json.loads(r.text)['items'][j]['snippet']['title']
            q=VideoMaster(video_id=vid,video_name=vname,channel_master=ChannelMaster.objects.get(channel_id=i))
            try:
                q.save()
                print("this is saved",q.__dict__)
            except Exception as e:
                print(e)
    return HttpResponse("Done")

def getvideostats(request):
    for i in VideoMaster.objects.all():
        r=requests.get('https://www.googleapis.com/youtube/v3/videos?part=statistics&id='+i.video_id+'&key=AIzaSyBw0grXPH8gNIDwtuUw3Q-HgzGDULN_JkE')
        v_views=json.loads(r.text)['items'][0]['statistics']['viewCount']
        try:
            p = VideoStats(total_views=v_views, video_master=VideoMaster.objects.get(video_id=i.video_id))
            p.save()
        except Exception as e:
            print(e)
    return HttpResponse("done")











