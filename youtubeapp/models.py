from django.db import models

class ChannelMaster(models.Model):
    channel_id=models.CharField(default=None,max_length=200)
    channel_name=models.CharField(default=None,max_length=200)

class ChannelStats(models.Model):
    channel_master = models.ForeignKey('ChannelMaster', on_delete=models.CASCADE)
    total_views=models.IntegerField(default=None)
    time_stamp=models.DateTimeField(auto_now=True)


class VideoMaster(models.Model):
    channel_master = models.ForeignKey('ChannelMaster', on_delete=models.CASCADE)
    video_id=models.CharField(default=None,max_length=200)
    video_name=models.CharField(default=None,max_length=200)


class VideoStats(models.Model):
    video_master = models.ForeignKey('VideoMaster', on_delete=models.CASCADE)
    total_views=models.IntegerField(default=None)
    time_stamp=models.DateTimeField(auto_now=True)
