# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class News(models.Model):
    NEWS_TYPE = (
        ("entertainment", u"娱乐"),
        ("economic", u"财经"),
        ("political ", u"时政"),
        ("agricultural ", u"农业"),
        ("recruitment", u"招聘")
    )

    title = models.CharField(max_length=100, help_text=u"新闻标题")
    contents = models.TextField(help_text=u"新闻内容")
    image = models.URLField(help_text=u"图片地址", null=True)
    create_time = models.DateTimeField(auto_now_add=True,
                                       help_text=u"新闻创建时间")
    occurd_time = models.CharField(max_length=50, help_text=u"新闻发生时间")
    auth = models.CharField(max_length=50, help_text=u"新闻作者")
    source = models.CharField(max_length=100, help_text=u"新闻来源")
    source_url = models.URLField(help_text=u"新闻来源地址", null=True)
    type = models.CharField(max_length=50, choices=NEWS_TYPE,
                            help_text=u"新闻类别")

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-occurd_time',)
