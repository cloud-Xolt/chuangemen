# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys

from django.core.wsgi import get_wsgi_application

reload(sys)
sys.setdefaultencoding("utf-8")

DJANGO_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../"))

sys.path.append(DJANGO_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chuanmen.settings")


class ScrapyVideosPipeline(object):

    def __init__(self):
        self.video_obj = ""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            get_wsgi_application()
            from video.models import Video, VideoType, Anthology
            cls._instance = object.__new__(cls)
            cls.video = Video
            cls.video_type = VideoType
            cls.anthology = Anthology
            cls.video_type.objects.get_or_create(
                name=u"其他")

        return cls._instance

    def process_item(self, item, spider):
        if spider.name == 'amj_video':

            video_dic = item.get("video_item")
            this_video_type = self.video_type.objects.get(
                name=video_dic.get("video_type"))

            self.video_obj, _ = self.video.objects.get_or_create(
                name=video_dic.get("name"),
                defaults={
                    "last_sync_time": video_dic.get("last_sync_time"),
                    "video_type": this_video_type,
                    "poster": video_dic.get("poster"),
                    "language": video_dic.get("language"),
                    "area": video_dic.get("area"),
                    "year": video_dic.get("year"),
                    "actor": video_dic.get("actor"),
                    "director": video_dic.get("director"),
                    "des": video_dic.get("des")
                })

            anthology_dic = item.get("anthology_item")
            self.anthology.objects.get_or_create(
                video=self.video_obj,
                episode=anthology_dic.get("episode"),
                defaults={
                    "path": anthology_dic.get("path"),
                    "player": anthology_dic.get("player")
                })
        elif spider.name == 'amj_video_type':
            self.video_type.objects.get_or_create(
                name=item.get("name"))
        else:
            print "%s 不存在！" % spider.name
