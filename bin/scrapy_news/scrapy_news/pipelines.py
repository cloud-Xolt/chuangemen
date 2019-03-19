# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys

from django.core.wsgi import get_wsgi_application

DJANGO_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../"))

sys.path.append(DJANGO_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chuanmen.settings")


class NewsPipeline(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            get_wsgi_application()
            from news.models import News
            cls._instance = object.__new__(cls)
            cls.News = News

        return cls._instance

    def process_item(self, item, spider):
        news_item = dict(item)
        # news_queryset = [self.News(title=news_item.get("title"),
        #                            contents=news_item.get("contents"),
        #                            auth=news_item.get("auth"),
        #                            source=news_item.get("source"),
        #                            type=spider.name
        #                            ) for news_item in new_list]
        # self.News.objects.bulk_create(news_queryset)
        self.News.objects.get_or_create(
            title=news_item.get("title"),
            defaults={
                "contents": news_item.get("contents"),
                "auth": news_item.get("auth"),
                "source": news_item.get("source"),
                "occurd_time": news_item.get("occurd_time"),
                "source_url": news_item.get("source_url"),
                "image": news_item.get("image"),
                "type": spider.name
            })

    # def close_spider(self, spider):
    #     self.client.close()
