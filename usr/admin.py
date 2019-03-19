# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from usr.models import CustomUser

admin.site.register(CustomUser)
