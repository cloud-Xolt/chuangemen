# -*- coding: utf-8 -*-
"""chuanmen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, \
    verify_jwt_token
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from news import views as news_view
from video import views as video_view
from usr import views as usr_view

schema_view = get_schema_view(title='API',
                              renderer_classes=[OpenAPIRenderer,
                                                SwaggerUIRenderer])

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'news', news_view.NewsViewSet)
router.register(r'video', video_view.VideoViewSet)
router.register(r'video_type', video_view.VideoTypeViewSet)
router.register(r'video_anthology', video_view.AnthologyViewSet)
router.register(r'register', usr_view.UserViewSet)

urlpatterns = [
    url(r'^docs/', schema_view, name="docs"),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api/v1/login/', obtain_jwt_token),  # 获取token
    url(r'^api-token-refresh/', refresh_jwt_token),  # 刷新Token
    url(r'^api-token-verify/', verify_jwt_token),  # 认证Token

]
