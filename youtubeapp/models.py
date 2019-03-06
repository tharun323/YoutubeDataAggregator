from django.db import models


class ChannelMaster(models.Model):
    """contains the Master data of the channels"""
    channel_id=models.CharField(default=None,max_length=200)
    channel_name=models.CharField(default=None,max_length=200)
    description=models.TextField(default='entertainment')
    def __str__(self):
        return self.channel_name

class ChannelStats(models.Model):
    """Model contains the Stats of each individual channel with ChannelMaster as Foreign Key"""
    channel_master = models.ForeignKey('ChannelMaster', on_delete=models.CASCADE)
    total_views=models.BigIntegerField(default=None)
    subscriber_count=models.BigIntegerField(default=None)
    time_stamp=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.channel_master.channel_name
    def __unicode__(self):
        return self.channel_master.channel_name

class VideoMaster(models.Model):
    """Model contains videos from all the available channels with Channelmaster as FK"""
    channel_master = models.ForeignKey('ChannelMaster', on_delete=models.CASCADE)
    video_id=models.CharField(default=None,max_length=200)
    video_name=models.CharField(default=None,max_length=200)
    def __str__(self):
        return self.video_name
    def __unicode__(self):
        return self.video_name

class VideoStats(models.Model):
    """Model Contains the details of the individual videos across channels with VideoMaster as Fk"""
    video_master = models.ForeignKey('VideoMaster', on_delete=models.CASCADE)
    total_views=models.BigIntegerField(default=None)
    like_count=models.BigIntegerField(default=None)
    dislike_count=models.BigIntegerField(default=None)
    comment_count=models.BigIntegerField(default=None)
    time_stamp=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.video_master.video_name)
    def __unicode__(self):
        return str(self.video_master.video_name)




