#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import sys

from django.core.wsgi import get_wsgi_application

from bin.live_broadcast.sour_constant import SOURCE

reload(sys)
sys.setdefaultencoding("utf-8")

DJANGO_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../"))

sys.path.append(DJANGO_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chuanmen.settings")


class LiveSource(object):
    """初始化直播信息到数据库"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            get_wsgi_application()
            from video.models import Video, VideoType, Anthology
            cls._instance = object.__new__(cls)
            cls.video = Video
            cls.video_type = VideoType
            cls.anthology = Anthology
            cls.live_video, _ = cls.video_type.objects.get_or_create(
                name=u"直播")

        return cls._instance

    def get_source_iteration(self):
        for video_name, video_path_list in SOURCE.items():
            for video_path in video_path_list:
                yield video_name, video_path

    def insert_into_db(self):
        for video_name, video_path in self.get_source_iteration():
            video_qwet, _ = self.video.objects.get_or_create(
                video_type=self.live_video, name=video_name)
            self.anthology.objects.get_or_create(video=video_qwet,
                                                 path=video_path)


if __name__ == "__main__":
    live = LiveSource()
    live.insert_into_db()