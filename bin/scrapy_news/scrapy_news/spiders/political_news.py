# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request

from scrapy_news.items import ScrapyNewsItem


class BaseSpider(scrapy.Spider):
    """
    获取腾讯时政新闻的url列表
    """

    name = 'political'
    allowed_domains = ['news.qq.com']
    start_urls = ['https://news.qq.com/newsgn/x_qitazonghe_more.htm']

    def parse(self, response):
        _tmp_url_list = response.xpath('//a[@class="rlk1"]/@href').extract()[:100]

        political_news_url_list = ["https://news.qq.com%s" % _tmp_url
                              for _tmp_url in _tmp_url_list]
        for political_news_url in political_news_url_list:

            # callback用法，detail是另一个方法
            yield Request(url=political_news_url, callback=self.political_detail)

    def political_detail(self, response):
        item = ScrapyNewsItem()
        item["title"] = response.xpath('//div[@class="hd"]/h1/text()').extract()[0]
        content_list = response.xpath('//div[@class="Cnt-Main-Article-QQ"]/p[@class="text"]/text()').extract()
        political_contents = "\n".join(content_list).strip()
        if not political_contents:
            return

        item["contents"] = political_contents
        item["auth"] = response.xpath('//div[@class="qq_editor"]/text()').extract()[0]
        item["occurd_time"] = response.xpath('//div[@class="a_Info"]/span[@class="a_time"]/text()').extract()[0]
        item["source_url"] = response.url
        try:
            item["source"] = response.xpath('//div[@class="a_Info"]/span[@class="a_source"]/a/text()').extract()[0]
        except Exception:
            item["source"] = response.xpath('//div[@class="a_Info"]/span[@class="a_source"]/text()').extract()[0]

        yield item
