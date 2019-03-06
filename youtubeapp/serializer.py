from . models import *
from rest_framework import serializers

class ChannelMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChannelMaster
        fields='__all__'

class ChannelStatsSerializer(serializers.ModelSerializer):
    channel_master = ChannelMasterSerializer()
    class Meta:
        model=ChannelStats
        fields=('channel_master','total_views','time_stamp','subscriber_count')

class VideoMasterSerializer(serializers.ModelSerializer):
    channel_master = ChannelMasterSerializer(read_only=True)
    class Meta:
        model=VideoMaster
        fields=('channel_master','video_id','video_name')

class VideoStatsSerializer(serializers.ModelSerializer):
    video_master = VideoMasterSerializer(read_only=True)
    class Meta:
        model=VideoStats
        fields=('total_views','time_stamp','video_master','like_count','dislike_count','comment_count')




