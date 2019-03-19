#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        self.crawler_process.crawl("amj_video_type", **opts.__dict__)
        self.crawler_process.crawl("amj_video", **opts.__dict__)
        self.crawler_process.start()
