# -*- coding: utf-8 -*-
from django.core.paginator import InvalidPage, EmptyPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):

    page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 100
