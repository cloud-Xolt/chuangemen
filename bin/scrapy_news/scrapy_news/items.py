# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyNewsItem(scrapy.Item):
    title = scrapy.Field()
    contents = scrapy.Field()
    image = scrapy.Field()
    auth = scrapy.Field()
    occurd_time = scrapy.Field()
    source_url = scrapy.Field()
    source = scrapy.Field()
