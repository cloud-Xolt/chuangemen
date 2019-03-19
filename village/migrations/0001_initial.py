# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-04 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u89c6\u9891\u79cd\u7c7b', max_length=60, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]