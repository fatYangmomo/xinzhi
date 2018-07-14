from django.conf.urls import include,url
from ..views import GenerateStock

urlpatterns = [
	# 股份列表解析，生成股份列表
    url(r'^stock/$',GenerateStock.as_view(),name='analyse_stock'),
    
]
