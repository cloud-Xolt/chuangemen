# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class VideoType(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=60, help_text=u"视频种类")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Video(models.Model):
    video_type = models.ForeignKey(VideoType, help_text=u"视频类型")
    name = models.CharField(max_length=200, help_text=u"视频名称", unique=True)
    poster = models.URLField(help_text=u"视频海报", null=True)
    language = models.CharField(max_length=80, help_text=u"语言", null=True)
    area = models.CharField(max_length=80, help_text=u"地区", null=True)
    year = models.CharField(max_length=50, help_text=u"发行时间", null=True)
    actor = models.CharField(max_length=2000, help_text=u"演员", null=True)
    director = models.CharField(max_length=1000, help_text=u"导演", null=True)
    des = models.TextField(help_text=u"介绍", null=True)
    last_sync_time = models.CharField(max_length=50, help_text=u"最后更新时间", null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-last_sync_time', 'name')


class Anthology(models.Model):
    video = models.ForeignKey(Video, help_text=u"视频名称")
    episode = models.CharField(max_length=40, help_text=u"剧集", default=1)
    path = models.URLField(help_text=u"视频播放地址")
    player = models.CharField(max_length=20, help_text=u"播放器", null=True)

    def __str__(self):
        return self.episode

    class Meta:
        ordering = ('episode', "video")
