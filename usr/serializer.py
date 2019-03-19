#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework import serializers

from usr.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'scope', 'headImage', 'description')
