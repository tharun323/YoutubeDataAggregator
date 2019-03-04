from django.contrib import admin

# Register your models here.
from . models import ChannelMaster,ChannelStats,VideoMaster,VideoStats

admin.site.register(ChannelMaster)
admin.site.register(ChannelStats)
admin.site.register(VideoMaster)
admin.site.register(VideoStats)

