# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


# Register your models here.
from video.models import VideoType, Video, Anthology

admin.site.register(VideoType)
admin.site.register(Video)
admin.site.register(Anthology)
