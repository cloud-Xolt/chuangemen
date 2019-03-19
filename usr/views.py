# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.common_viewsets import CreateOnlyModelViewSet
from usr.models import CustomUser
from usr.serializer import CustomUserSerializer


class UserViewSet(CreateOnlyModelViewSet):
    """
    create:
        Create a new user.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
