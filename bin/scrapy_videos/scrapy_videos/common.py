# -*- coding: utf-8 -*-
xml='''<?xml version="1.0"?><root><item><![CDATA[hello CDATA]]></item></root>'''

import requests

def get_vide_page_list(url):
    rsp = requests.get(url)
    if rsp.status_code != 200:
        raise BaseException

    tutal_page = rsp.content.split(
        '<list page="1" pagecount="')[1].split('" pagesize="')[0]
    tutal_page = int(tutal_page) + 1
    page_url_list = ["%s&t=&pg=%s&h=&ids=&wd=" % (url, index)
                     for index in xrange(1, tutal_page) ]
    return page_url_list

if __name__ == '__main__':
    print u'第7123集'[1:-1]
#     print get_vide_page_list("https://agmjcj.com/inc/api.php?ac=videolist")