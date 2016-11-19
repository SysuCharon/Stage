from django.conf.urls import url
from django.contrib import admin
from team.views import *


urlpatterns = [
    url(r'^$', memberList.as_view(), name="member_list"),
    url(r'^detail/(?P<id>[\d]+)', memberDetail.as_view(), name="member_detail")
]
