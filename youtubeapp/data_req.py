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



l = ['UC-lHJZR3Gqxm24_Vd_AJ5Yw', 'UCq-Fj5jknLsUf-MWSy4_brA', 'UC295-Dw_tDNtZXFeAPAW6Aw',
     'UCffDXn7ycAzwL2LDlbyWOTw', 'UCIwFjwMjI0y7PDBVEO9-bkQ', 'UC0v-tlzsn0QZwJnkiaUSJVQ',
     'UCJ5v_MCY6GNUBTO8-D3XoAg', 'UCRijo3ddMTht_IHyNSNXpNQ', 'UCbCmjCuTUZos6Inko4u57UQ',
     'UCZJ7m7EnCNodqnu5SAtg8eQ']

def getchannelstatsdata(request):
    for i in l:
        r=requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id="+i+"&key=AIzaSyCuC7v8wNpETzqFjOKG2zju9wcTQZSt0tg")
        data = json.loads(r.text)['items'][0]['statistics']['viewCount']
        try:
            p=ChannelStats(total_views=data,channel_master=ChannelMaster.objects.get(channel_id=i))
            p.save()
            print("saved",p.__dict__)
        except Exception as e:
            print(e)
    return HttpResponse("done")

def getvideomasterdata(request):
    c=0
    for i in l:
        try:
            c+=1
            print(i,c)
            r = requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyCuC7v8wNpETzqFjOKG2zju9wcTQZSt0tg&channelId=" + i + "&part=snippet,id&order=date&maxResults=5")
            data = json.loads(r.text)
        except Exception as e:
            print("The process has errors",e)
            print("I am at this channel",c)
            break
        for j in range(0,len(data['items'])):
            vid=json.loads(r.text)['items'][j]['id']['videoId']
            vname=json.loads(r.text)['items'][j]['snippet']['title']
            try:
                q = VideoMaster(video_id=vid, video_name=vname, channel_master=ChannelMaster.objects.get(channel_id=i))
                q.save()
                # print("this is saved",q.__dict__)
            except Exception as e:
                print(e)
    if(c==len(l)):
        print("all the channels are processed")
        print(c,len(l))
    else:
        print("%s are not processed",len(l)-c)
    return HttpResponse("Done")

def getvideostats(request):
    for i in VideoMaster.objects.all():
        try:
            r=requests.get('https://www.googleapis.com/youtube/v3/videos?part=statistics&id='+i.video_id+'&key=AIzaSyDTSx96UF4XekNIWM6Vz0UG2TmYuEFwHVs')
            print(r)
            try:
                v_views=json.loads(r.text)['items'][0]['statistics']['viewCount']
            except Exception as e:
                print("there is no Viewcount",e)
        except Exception as e:
            print(i.__dict__)
            print("Process will break 1",e)
            break
        try:
            print("I am in try")
            p = VideoStats(total_views=v_views, video_master=VideoMaster.objects.get(video_id=i.video_id))
            p.save()
            print("this is saved",p)
        except Exception as e:
            print("Process will break",e)
            break
    return HttpResponse("done")
