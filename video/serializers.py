#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ********************************************************
# (C) 2000-2018 NSFOCUS Corporation. All rights Reserved *
# ********************************************************
from rest_framework import serializers

from video.models import VideoType, Anthology, Video


class VideoTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoType
        fields = ('name', 'id')


class VideoSerializer(serializers.ModelSerializer):
    video_type = serializers.SerializerMethodField()

    def get_video_type(self, obj):
        return obj.video_type.name

    class Meta:
        model = Video
        fields = ('video_type', 'id', 'name', "poster", 'language', 'area',
                  'year', 'actor', 'director', 'des', 'last_sync_time')


class AnthologySerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        return obj.video.name

    class Meta:
        model = Anthology
        fields = ('video', 'episode', 'path', "player", 'id')


class AnthologyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anthology
        fields = ('episode', 'id')
