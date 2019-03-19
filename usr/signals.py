#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db.models.signals import post_save
from django.contrib.auth.models import User

from usr.models import CustomUser


def create_user_detail(sender, instance, signal, *args, **kwargs):
    print sender, instance, signal, args, kwargs

    if kwargs['created']:
        u = CustomUser()
        u.__dict__.update(instance.__dict__)
        u.save()


post_save.connect(create_user_detail, sender=User)
