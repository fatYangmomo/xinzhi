from django.conf.urls import include,url
from ..views import DownloadStock

urlpatterns = [
	# 股份列表下载
    url(r'^download_stock/$',DownloadStock.as_view(),name='download_stock'),
]
