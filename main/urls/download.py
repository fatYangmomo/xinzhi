from django.conf.urls import include,url
from ..views import DownloadStock
from ..views import DownloadReport

urlpatterns = [
	# 股份列表下载
    url(r'^stock/$',DownloadStock.as_view(),name='download_stock'),
    # 财报数据下载
    url(r'^report/$',DownloadReport.as_view(),name='download_report'),
]
