# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.filters import DjangoFilterBackend, SearchFilter
from rest_framework.response import Response

from common.filter_pagination import StandardResultsSetPagination
from news.models import News
from news.serializers import NewsSerializer, ListNewsSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a news instance.

    list:
        Return all news, ordered by most recently joined.
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('type',)  # 过滤的字段
    search_fields = ('title',)  # 搜索的字段

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ListNewsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ListNewsSerializer(queryset, many=True)
        return Response(serializer.data)
