from django.conf.urls import url, include
from notice.views import *

urlpatterns = [
    url(r'^$', noticeList.as_view(), name="notice_list"),
    url(r'^detail/(?P<id>[\d]+)', noticeDetail.as_view(), name="notice_detail")
]
