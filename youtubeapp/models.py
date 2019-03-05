from django.db import models

class ChannelMaster(models.Model):
    channel_id=models.CharField(default=None,max_length=200)
    channel_name=models.CharField(default=None,max_length=200)
    def __str__(self):
        return self.channel_name

class ChannelStats(models.Model):
    channel_master = models.ForeignKey('ChannelMaster', on_delete=models.CASCADE)
    total_views=models.BigIntegerField(default=None)
    time_stamp=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.channel_master

class VideoMaster(models.Model):
    channel_master = models.ForeignKey('ChannelMaster', on_delete=models.CASCADE)
    video_id=models.CharField(default=None,max_length=200)
    video_name=models.CharField(default=None,max_length=200)
    def __str__(self):
        return self.video_name

class VideoStats(models.Model):
    video_master = models.ForeignKey('VideoMaster', on_delete=models.CASCADE)
    total_views=models.BigIntegerField(default=None)
    time_stamp=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.video_master)

