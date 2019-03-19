# -*- coding: utf-8 -*-
import scrapy
import sys

from scrapy_videos.items import VideosTypeItem

reload(sys)
sys.setdefaultencoding("utf-8")


class AmjVideoTypeSpider(scrapy.Spider):
    name = 'amj_video_type'
    allowed_domains = ['agmjcj.com']
    start_urls = ['https://agmjcj.com/inc/api.php?ac=videolist',
                  'http://richiiwtsll.com/sapi.php?ac=videolist']

    def parse(self, response):
        video_type_obj = VideosTypeItem()
        video_type_item = response.xpath('//ty')
        for _ietm in video_type_item:
            name_item = _ietm.xpath('text()').extract()[0].strip()
            if "*" in name_item:
                name_item =  "/".join(name_item.split("*"))
            video_type_obj["name"] = name_item
            # video_type_obj["id"] = _ietm.xpath('@id').extract()[0].strip()
            yield video_type_obj
