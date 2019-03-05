from . models import *
from rest_framework import serializers

class ChannelMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChannelMaster
        fields='__all__'

class ChannelStatsSerializer(serializers.ModelSerializer):
    # channel_master = ChannelMasterSerializer()
    class Meta:
        model=ChannelStats
        fields='__all__'
        depth=1

class VideoMasterSerializer(serializers.ModelSerializer):
    # channel_master = ChannelMasterSerializer()
    class Meta:
        model=VideoMaster
        fields='__all__'
        depth=1

class VideoStatsSerializer(serializers.ModelSerializer):
    # video_master = VideoMasterSerializer()
    class Meta:
        model=VideoStats
        fields='__all__'
        depth=1



