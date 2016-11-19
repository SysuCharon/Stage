from django.conf.urls import url, include
from django.contrib import admin
from news.views import *

urlpatterns = [
    url(r'^$', newsList.as_view(), name="news_list"),
    url(r'^detail/(?P<id>[\d]+)', newsDetail.as_view(), name="news_detail")
]
