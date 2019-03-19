# -*- coding: utf-8 -*-
import sys

import lxml.etree
import requests
import time
from scrapy.spiders import XMLFeedSpider

from scrapy_videos.items import AnthologyItem
from scrapy_videos.items import VideosItem

reload(sys)
sys.setdefaultencoding("utf-8")


def get_vide_page_list(url_list):
    """获取总页码"""

    page_url_list = []

    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    for url in url_list:
        rsp = requests.get(url, headers=send_headers)
        if rsp.status_code != 200:
            raise BaseException
        try:
            xml_rsp = lxml.etree.HTML(rsp.content)
            tutal_page = xml_rsp.xpath('//rss/list/@pagecount')[0]
            tutal_page = int(tutal_page) + 1
        except Exception:
            tutal_page = 300
        _url_list = ["%s&t=&pg=%s&h=&ids=&wd=" % (url, index)
                         for index in xrange(1, tutal_page) ]
        page_url_list.extend(_url_list)
    return page_url_list


class AmjVideoSpider(XMLFeedSpider):
    name = 'amj_video'
    allowed_domains = ['agmjcj.com']
    index_url = ["https://agmjcj.com/inc/api.php?ac=videolist",
                 "http://richiiwtsll.com/sapi.php?ac=videolist"]
    iterator = 'iternodes' # you can change this; see the docs

    # 此时将开始迭代的节点设置为第一个节点 rss
    itertag = 'rss' # change it accordingly

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = XMLFeedSpider.__new__(cls, *args, **kwargs)
            cls.start_urls = get_vide_page_list(cls.index_url)
        return cls._instance

    def parse_node(self, response, selector):
        video_item = VideosItem()
        anthology_item = AnthologyItem()




        try:
            video_type = selector.xpath(
                '/rss/list/video/type/text()').extract()[0].strip()
        except:
            video_type = u"其他"
        video_item["video_type"] = "/".join(video_type.split("*")) \
            if "*" in video_type else video_type

        video_item["name"] = selector.xpath(
            "/rss/list/video/name/text()").extract()[0].strip()

        try:
            video_item["last_sync_time"] = selector.xpath(
                '/rss/list/video/last/text()').extract()[0].strip()
            video_item["poster"] = selector.xpath(
                '/rss/list/video/pic/text()').extract()[0].strip()
            video_item["language"] = selector.xpath(
                '/rss/list/video/lang/text()').extract()[0].strip()
            video_item["area"] = selector.xpath(
                '/rss/list/video/area/text()').extract()[0].strip()
            video_item["year"] = selector.xpath(
                '/rss/list/video/year/text()').extract()[0].strip()
            video_item["actor"] = selector.xpath(
                '/rss/list/video/actor/text()').extract()[0].strip()
            video_item["director"] = selector.xpath(
                '/rss/list/video/director/text()').extract()[0].strip()
            video_item["des"] = selector.xpath(
                '/rss/list/video/des/text()').extract()[0].strip()
        except Exception as e:
            print e

        # 影视详情
        video_str = selector.xpath('/rss/list/video/dl/dd/text()').extract()[0].strip()
        _video_list = video_str.strip().split("#")
        for sinle_video_item in _video_list:
            sinle_video_list = sinle_video_item.split("$")
            anthology_item["video"] = video_item["name"]
            anthology_item["path"] = sinle_video_list[1].strip()

            try:
                anthology_item["episode"] = sinle_video_list[0][1:-1].strip()
                anthology_item["player"] = sinle_video_list[2].strip()
            except Exception as e:
                print e

            yield {"video_item":video_item, "anthology_item": anthology_item}
        time.sleep(5)
