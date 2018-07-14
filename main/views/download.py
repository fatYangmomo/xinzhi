from django import forms
from django.views import View
import urllib.request as urllib2
from ..utils import (
    correct_response, err_response_with_desc
)

class DownloadStock(View):
	
	def get(self,request):
		# 深交所A股股票上市公司列表xlsx
		url1 = 'http://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1110&TABKEY=tab1&random=0.8481548239368346'
		# 上交所A股上市公司列表xls
		# http://www.sse.com.cn/assortment/stock/list/share/
		url2 = 'http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=1'
		# 上证50成份股列表地址xls
		url3 = 'http://www.csindex.com.cn/uploads/file/autofile/cons/000016cons.xls'
		# 沪深300成份股列表地址xls
		url4 = 'http://www.csindex.com.cn/uploads/file/autofile/cons/000300cons.xls'
		send_headers = {
			'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
			'Referer':'http://www.sse.com.cn/assortment/stock/list/share/',
		}
		req = urllib2.Request(url2, headers=send_headers)
		f = urllib2.urlopen(req)
		data = f.read()
		with open("download/file_stock/上交所A股上市公司列表.xls", "wb") as code:
			code.write(data)
		urls = [
			{"url":url1,"name":"深交所A股上市公司列表.xlsx"},
			{"url":url3,"name":"上证50成份股列表.xls"},
			{"url":url4,"name":"沪深300成份股列表.xls"}
		]
		for url in urls:
			f = urllib2.urlopen(url["url"])
			file_name = url["name"]
			data = f.read()
			with open("download/file_stock/"+file_name, "wb") as code:
				code.write(data)
		return correct_response({'data':'股份列表下载成功'})

# class DownloadReport(View):
	
# 	def get(self,request):
# 		# 历史交易数据表csv
# 		url5 = 'http://quotes.money.163.com/service/chddata.html?code=1002639&start=20171118&end=20180711&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP' 
# 		# 资产负债表xls-txt
# 		url6 = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/000001/ctrl/all.phtml'
# 		# 利润表xls-txt
# 		url7 = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/000002/ctrl/all.phtml'
# 		send_headers = {
# 			'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
# 			'Referer':'http://www.sse.com.cn/assortment/stock/list/share/',
# 		}
# 		urls = [
# 			{"url":url5,"name":"历史交易数据表.csv"},
# 			{"url":url6,"name":"资产负债表.xls"},
# 			{"url":url7,"name":"利润表.xls"}
# 		]
# 		for url in urls:
# 			f = urllib2.urlopen(url["url"])
# 			file_name = url["name"]
# 			data = f.read()
# 			with open("download/file_report/"+file_name, "wb") as code:
# 				code.write(data)
# 		return correct_response({})
		