import django_filters
from . models import *

class ChannelMasterFilter(django_filters.FilterSet):
    class Meta:
        model=ChannelMaster
        fields=['channel_id','channel_name']

