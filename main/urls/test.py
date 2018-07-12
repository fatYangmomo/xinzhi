from django.conf.urls import include,url
from ..views import Test

urlpatterns = [
	# 测试
    url(r'^test/$',Test.as_view(),name='test'),
]
