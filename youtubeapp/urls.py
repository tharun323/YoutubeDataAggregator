from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . views import *
from . import views
from rest_framework_swagger.views import get_swagger_view
from . charts import *
from . data_req import *
schema_view = get_swagger_view(title='YouMarket Youtube Data Aggregator API')
router = routers.DefaultRouter()
router.register(r'ChannelMasterViewSet', views.ChannelMasterViewSet, base_name='ChannelMaster')
router.register(r'ChannelStatsViewSet',views.ChannelStatsViewSet,base_name='ChannelStats')
router.register(r'VideoMasterViewSet',views.VideoMasterViewSet,base_name='VideoMaster')
router.register(r'VideoStatsViewSet',views.VideoStatsViewSet,base_name='VideoStats')

app_name="youtubeapp"

urlpatterns = [
    url(r'^$', schema_view),
    url('home',views.home,name='home'), #home page url
    url('vidstatsplot',vidstatsplot,name="vidstatsplot"), #individual vid stats displayed by MatPlotLib
    url('chanstatplot',chanstatplot,name="chanstatplot"), #individual Channel stats displayed by MatPlotLib
    url('getvideostatsui',views.getvideostatsui,name="getvideostatsui"),# Individual Vid Stats UI
    url('getchannelmasterui',views.getchannelmasterui,name='getchannelmasterui'),# Individual Channel Stats UI
    url('getvideomasterui',views.getvideomasterui,name='getvideomasterui'),# Individual Vid Master details UI
    url('getchannelstatsui',views.getchannelstatsui,name='getchannelstatsui'),# Individual Channel  Stats UI
    url('api/', include(router.urls)), #API root
]






