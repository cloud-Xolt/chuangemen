# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    description = models.TextField(max_length=256, default="", blank=True)
    headImage = models.ImageField(upload_to='./', null=True,
                                  blank=True)
    scope = models.IntegerField(default=100)
    # token = models.CharField(max_length=100)

    objects = UserManager()
