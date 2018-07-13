from django import forms
from django.views import View
import urllib.request
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
		# 历史交易数据表csv
		url5 = 'http://quotes.money.163.com/service/chddata.html?code=1002639&start=20171118&end=20180711&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP' 
		# 资产负债表xls
		url6 = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/000001/ctrl/all.phtml'
		# 利润表xls
		url7 = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/000002/ctrl/all.phtml'
		f = urllib.request.urlopen(url1) 
		data = f.read()
		with open("download/file_stock/深交所A股股票上市公司列表.xlsx", "wb") as code:
			code.write(data)
		return correct_response({})
		