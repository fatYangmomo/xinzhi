from django import forms
from django.views import View
import urllib.request as urllib2
import xlrd
from ..utils import (
    correct_response, err_response_with_desc,download_from_url,download_from_url_headers
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
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
			'Referer':'http://www.sse.com.cn/assortment/stock/list/share/',
		}
		download_from_url_headers(url2,send_headers,"download/file_stock/上交所A股上市公司列表.xls")
		urls = [
			{"url":url1,"name":"深交所A股上市公司列表.xlsx"},
			{"url":url3,"name":"上证50成份股列表.xls"},
			{"url":url4,"name":"沪深300成份股列表.xls"}
		]
		try:
			for url in urls:
				file_name = "download/file_stock/" + url["name"]
				download_from_url(url["url"],file_name)
		return correct_response({'data':'股份列表下载成功'})

class DownloadReport(View):
	
	def get(self,request):
		# 历史交易数据表csv
		url5 = 'http://quotes.money.163.com/service/chddata.html?code=1000001&start=20111205&end=20180717&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;VOTURNOVER;VATURNOVER;TCAP' 
		# 资产负债表xls-txt
		url6 = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/000001/ctrl/all.phtml'
		# 利润表xls-txt
		url7 = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/000002/ctrl/all.phtml'
		send_headers = {
			'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
			'Referer':'http://www.sse.com.cn/assortment/stock/list/share/',
		}
		# ***********************数据读取**********************************
		data = xlrd.open_workbook('download/file_stock/stock.xls')
		table = data.sheets()[0]
		stock_codes = table.col_values(0) # 股份代码
		stock_date = table.col_values(3) # 上市日期
		# ***********************数据读取结束**********************************

		# download_from_url('http://http://www.ajkfhafwjqh.com','123.txt')
		# ***********************获取url**********************************
		urls = [] # 历史交易数据表、资产负债表、利润表
		url_trade = [] # 历史交易数据表
		url_asset = [] # 资产负债表
		url_profit = [] # 利润表
		date_now = str(datetime.datetime.now().date())
		date_now = date_now.replace('-','')
		print(date_now)
		length = len(stock_codes)
		for i in range(0,length):
			date_old = stock_date[i].replace('-','')
			# print(date_old)
			# 历史交易数据表csv 
			url = 'http://quotes.money.163.com/service/chddata.html?code=1'+stock_codes[i]+'&start='+date_old+'&end='+date_now+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;VOTURNOVER;VATURNOVER;TCAP'
			url_trade.append({'code':stock_codes[i],'url':url})
			# 资产负债表xls-txt
			url = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/'+stock_codes[i]+'/ctrl/all.phtml'
			url_asset.append({'code':stock_codes[i],'url':url})
			# 利润表xls-txt
			url = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/'+stock_codes[i]+'/ctrl/all.phtml'
			url_profit.append({'code':stock_codes[i],'url':url})
		# ***********************获取url结束**********************************
		urls.append({'name':'trade','urls':url_trade})
		urls.append({'name':'asset','urls':url_asset})
		urls.append({'name':'profit','urls':url_profit})
		f = open('fail_url.txt','wa')
		for cate in urls:
			name = cate['name']
			urls = cate['urls']
			for code in urls:
				file_name = 'download/file_report/' + code['code'] + '_' + name + '.xls'
				res = download_from_url(code['url'], file_name)
				if res != "":
					f.write(res)
					f.write('\n')
		f.close()
		return correct_response({})
		