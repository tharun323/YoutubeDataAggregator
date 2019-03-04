from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . views import *
from . import views
router = routers.DefaultRouter()
print("I am in urls \n\n\n\n")
router.register(r'ChannelMasterViewSet', views.ChannelMasterViewSet, base_name='ChannelMaster')
router.register(r'ChannelStatsViewSet',views.ChannelStats,base_name='ChannelStats')
router.register(r'VideoMasterViewSet',views.VideoMaster,base_name='VideoMaster')
router.register(r'VideoStatsViewSet',views.VideoStats,base_name='VideoStats')


urlpatterns = [
    url('api/', include(router.urls)),
]


