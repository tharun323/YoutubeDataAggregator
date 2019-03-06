import matplotlib
import matplotlib.pyplot as plt
from . models import *
from django.shortcuts import render,redirect,reverse

def vidstatsplot(request):
    if request.method == 'GET':  # If the form is submitted
        search_query = request.GET.get('search_box', None)
        datelist=list()
        valuelist=list()
        for i in VideoStats.objects.all():
            if(i.video_master.video_id==search_query):
                valuelist.append(i.total_views)
                datelist.append(i.time_stamp)
        plt.plot(datelist, valuelist)
        plt.show()
    return render(request,"youtubeapp/video_stats.html")