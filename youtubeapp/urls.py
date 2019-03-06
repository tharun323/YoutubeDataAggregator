from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . views import *
from . import views
from rest_framework_swagger.views import get_swagger_view
from . charts import *
from . data_req import *
schema_view = get_swagger_view(title='Pastebin API')
router = routers.DefaultRouter()
router.register(r'ChannelMasterViewSet', views.ChannelMasterViewSet, base_name='ChannelMaster')
router.register(r'ChannelStatsViewSet',views.ChannelStatsViewSet,base_name='ChannelStats')
router.register(r'VideoMasterViewSet',views.VideoMasterViewSet,base_name='VideoMaster')
router.register(r'VideoStatsViewSet',views.VideoStatsViewSet,base_name='VideoStats')

app_name="youtubeapp"

urlpatterns = [
    url(r'^$', schema_view),
    url('home',views.home,name='home'),
    url('vidstatsplot',vidstatsplot,name="vidstatsplot"),
    url('getvideostatsui',views.getvideostatsui,name="getvideostatsui"),
    # url('getchannelstatsdata',getchannelstatsdata,name="getchannelstatsdata"),
    # url('getvideomasterdata',getvideomasterdata,name="getvideomasterdata"),
    # url('getvideostats',getvideostats,name="getvideostats"),
    url('getchannelmasterui',views.getchannelmasterui,name='getchannelmasterui'),
    url('getvideomasterui',views.getvideomasterui,name='getvideomasterui'),
    url('getchannelstatsui',views.getchannelstatsui,name='getchannelstatsui'),
    url('api/', include(router.urls)),
]






