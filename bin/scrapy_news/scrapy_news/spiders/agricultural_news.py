# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request

from scrapy_news.items import ScrapyNewsItem


class BaseSpider(scrapy.Spider):
    """
    获取中国农业新闻的url列表
    """

    name = 'agricultural'
    allowed_domains = ['www.farmer.com.cn']
    start_urls = ['http://www.farmer.com.cn/xwpd/btxw/']

    def parse(self, response):
        _tmp_url_list = response.xpath(
            '//div[@class="yui3-g list-list-li"]/div[@class="yui3-u"]/a[@class="vvqqq"]/@href').extract()[:100]

        agricultural_news_url_list = ["http://www.farmer.com.cn/xwpd/btxw/%s" %
                                   _tmp_url for _tmp_url in _tmp_url_list]
        for political_news_url in agricultural_news_url_list:

            # callback用法，detail是另一个方法
            yield Request(url=political_news_url, callback=self.agricultural_detail)

    def agricultural_detail(self, response):
        item = ScrapyNewsItem()
        base_contents_list = response.xpath('//div[@class="content"]/div[@class="TRS_Editor"]/div/text()').extract()
        tag_p_contents_list = response.xpath('//div[@class="content"]/div[@class="TRS_Editor"]/p/text()').extract()
        tag_image_contents_list = response.xpath('//div[@class="content"]/div[@class="TRS_Editor"]/div[@class="Custom_UnionStyle"]/p/text()').extract()
        base_contents = "\n".join(base_contents_list).strip()
        tag_p_contents = "\n".join(tag_p_contents_list).strip()
        tag_image_contents = "\n".join(tag_image_contents_list).strip()
        contents = base_contents + tag_p_contents + tag_image_contents
        if not contents:
            return
        try:
            item["image"] = response.xpath(
                '//div[@class="content"]/div[@class="TRS_Editor"]/div[@class="Custom_UnionStyle"]/p/img/@src'
            ).extract()[0]
        except:
            pass

        item["title"] = response.xpath(
            '//div[@class="zhengwen-left-container"]/h1[@class="wtitle"]/text()').extract()[0]
        item["contents"] = contents
        item["auth"] = response.xpath(u'//div[@class="content"]/div[contains(text(),"责任编辑")]/text()').extract()[0]
        item["occurd_time"] = response.xpath('//div[@class="yui3-g"]/div[@class="yui3-u"]/p[@class="wlaiyuan"]/text()').extract()[0]
        item["source_url"] = response.url
        item["source"] = u"中国农业新闻网"

        yield item
