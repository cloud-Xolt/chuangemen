# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideosItem(scrapy.Item):
    """视频信息"""

    video_type = scrapy.Field()
    name = scrapy.Field()
    poster = scrapy.Field()
    language = scrapy.Field()
    area = scrapy.Field()
    year = scrapy.Field()
    actor = scrapy.Field()
    director = scrapy.Field()
    des = scrapy.Field()
    last_sync_time = scrapy.Field()


class VideosTypeItem(scrapy.Item):
    """视频分类信息"""

    id = scrapy.Field()
    name = scrapy.Field()


class AnthologyItem(scrapy.Item):
    """视频集数地址信息"""

    video = scrapy.Field()
    episode = scrapy.Field()
    path = scrapy.Field()
    player = scrapy.Field()
