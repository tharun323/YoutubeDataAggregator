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
import logging
import schedule
import time
logger = logging.getLogger(__name__)

"""List of 10 youtube channel id's"""
l=[
'UC-lHJZR3Gqxm24_Vd_AJ5Yw',
'UCq-Fj5jknLsUf-MWSy4_brA',
'UC295-Dw_tDNtZXFeAPAW6Aw',
'UCffDXn7ycAzwL2LDlbyWOTw',
'UCIwFjwMjI0y7PDBVEO9-bkQ',
'UCpEhnqL0y41EpW2TvWAHD7Q',
'UCJ5v_MCY6GNUBTO8-D3XoAg',
'UCRijo3ddMTht_IHyNSNXpNQ',
'UCbCmjCuTUZos6Inko4u57UQ',
'UCZJ7m7EnCNodqnu5SAtg8eQ',
]

def getchannelstatsdata():
    """Get the stats for the Channel Master data like the entire views and subs count"""
    for i in l:
    #sends request to the youtube API and collects the statistics
        r=requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id="+i+"&key=AIzaSyCuC7v8wNpETzqFjOKG2zju9wcTQZSt0tg")
        viewscount = json.loads(r.text)['items'][0]['statistics']['viewCount']
        subs_count = json.loads(r.text)['items'][0]['statistics']['subscriberCount']
        try:
            p=ChannelStats(total_views=viewscount,subscriber_count=subs_count,channel_master=ChannelMaster.objects.get(channel_id=i))
            p.save()
            print("saved",p.__dict__)
        except Exception as e:
            logger.error(e)
    return True

def getvideomasterdata():
    """Get the videos across all channels gets 5 videos from each channel
    This sends request to the Channels and collects 5 videos from it and saves in the
    VideoMaster data, Using this Video id we can collect further stats

    run this function online once
    """
    c=0

    for i in l:
        try:
            c+=1
            print(i,c)
            r = requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyCuC7v8wNpETzqFjOKG2zju9wcTQZSt0tg&channelId=" + i + "&part=snippet,id&order=date&maxResults=5")
            data = json.loads(r.text)
        except Exception as e:
            logger.error("The process has errors",e)
            logger.error("I am at this channel",c)
            break
        for j in range(0,len(data['items'])):
            vid=json.loads(r.text)['items'][j]['id']['videoId']
            vname=json.loads(r.text)['items'][j]['snippet']['title']
            try:
                q = VideoMaster(video_id=vid, video_name=vname, channel_master=ChannelMaster.objects.get(channel_id=i))
                q.save()
                print("this is saved",q.__dict__)
            except Exception as e:
                print(e)
    if(c==len(l)):
        logger.error("all the channels are processed")
        logger.error(c,len(l))
    else:
        logger.error("%s are not processed",len(l)-c)
    return True

def getvideostats():
    """Gets individual video stats for various vids that are collected
    sends the request to the youtube api and collects the vid stats using the video id
    collected from the getvideomaster() function

    Saves the collected data in to the VideoStats Model

    """
    for i in VideoMaster.objects.all():
        try:
            r=requests.get('https://www.googleapis.com/youtube/v3/videos?part=statistics&id='+i.video_id+'&key=AIzaSyDTSx96UF4XekNIWM6Vz0UG2TmYuEFwHVs')
            print(r)
            try:
                v_views=json.loads(r.text)['items'][0]['statistics']['viewCount']
            except Exception as e:
                v_views=0
                logger.error("there is error views count", e)
            try:
                like_count=json.loads(r.text)['items'][0]['statistics']['likeCount']
            except Exception as e:
                like_count=0
                logger.error("there is error likes count", e)
            try:
                dislike_count=json.loads(r.text)['items'][0]['statistics']['dislikeCount']
            except Exception as e:
                dislike_count=0
                logger.error("there is error dislike count", e)
            try:
                comment_count=json.loads(r.text)['items'][0]['statistics']['commentCount']
            except Exception as e:
                comment_count=0
                logger.error("there is error comment count",e)
        except Exception as e:
            print(i.__dict__)
            logger.error("Error in requests or Ran out of Limit",e)
            break
        try:
            print("I am in try")
            p = VideoStats(dislike_count=dislike_count,comment_count=comment_count,like_count=like_count,total_views=v_views, video_master=VideoMaster.objects.get(video_id=i.video_id))
            p.save()
            print("this is saved",p)
        except Exception as e:
            logger.error("Process will break",e)
            break
    return True

# This is the scheduler just set arguments when to run (hourly , minute or date wise)
# This will currently run every hour


#
# schedule.every().hour.do(getchannelstatsdata)
# # # schedule.every().hour.do(getvideomasterdata)
# schedule.every().hour.do(getvideostats)
# #

# Set the value here if you wanted it to run Infinitely(set True or give condition)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
