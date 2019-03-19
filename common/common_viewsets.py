#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateOnlyModelViewSet(mixins.CreateModelMixin,
                             GenericViewSet):
    """
    A viewset that provides default `create()` actions.
    """
    pass
