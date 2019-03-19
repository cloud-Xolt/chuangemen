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
