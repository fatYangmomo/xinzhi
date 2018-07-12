from django.conf.urls import include,url

urlpatterns = [
	# 测试
    url(r'^test/',include('main.urls.test'),name='test'),
    # 数据下载
    url(r'^download/',include('main.urls.download'),name='download'),
    # 分析
    url(r'^analyse/',include('main.urls.analyse'),name='analyse'),
    # 股份
    url(r'^stock/',include('main.urls.stock'),name='stock'),
    # 财报分析
    url(r'^financial_report/',include('main.urls.financial_report'),name='financial_report'),
    # 组合
    url(r'^group/',include('main.urls.group'),name='group'),
]
