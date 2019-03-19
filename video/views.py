# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.filters import DjangoFilterBackend, SearchFilter
from rest_framework.response import Response

from common.filter_pagination import StandardResultsSetPagination
from video.models import VideoType, Video, Anthology
from video.serializers import VideoSerializer, VideoTypeSerializer, \
    AnthologySerializer, AnthologyListSerializer


class VideoTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a video type instance.

    list:
        Return all video types.
    """

    queryset = VideoType.objects.all()
    serializer_class = VideoTypeSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('name',)  # 过滤的字段
    search_fields = ('name',)  # 搜索的字段


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a video instance.

    list:
        Return all videos, ordered by last update time.
    """

    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('video_type__id', 'name', "video_type__name")  # 过滤的字段
    search_fields = ('name', 'video_type__name')  # 搜索的字段


class AnthologyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a video anthology instance.

    list:
        Return all anthology types.
    """

    queryset = Anthology.objects.all()
    serializer_class = AnthologySerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('video__id', 'episode',)  # 过滤的字段

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AnthologyListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AnthologyListSerializer(queryset, many=True)
        return Response(serializer.data)
