from . models import *
from rest_framework import serializers

class ChannelMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChannelMaster
        fields='__all__'

class ChannelStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChannelStats
        fields='__all__'

class VideoMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoMaster
        fields='__all__'

class VideoStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoStats
        fields='__all__'

