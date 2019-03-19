#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ********************************************************
# (C) 2000-2018 NSFOCUS Corporation. All rights Reserved *
# ********************************************************
from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('title', 'id', 'contents', 'create_time', 'auth',
                  'source', 'type', 'occurd_time', 'source_url', 'image')

    def get_type(self, obj):
        return obj.get_type_display()


class ListNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'id', 'type', 'occurd_time', "source", 'image')
