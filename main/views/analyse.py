from django import forms
from django.views import View
from ..utils import (
    correct_response, err_response_with_desc
)
import xlrd
import xlwt

class GenerateStock(View):
	
	def get(self,request):
		stock_data = [] # 存储股份代码、股份简称、股份全称、所属模块
		stock_code = []
		stock_attr = []
		stock_name = []
		stock_index = []
		stock_plate = []
		# 创建一个workbook 设置编码 
		workbook = xlwt.Workbook(encoding = 'ascii') 
		# 创建一个worksheet 
		worksheet = workbook.add_sheet('stock')
		# 读数据
		data = xlrd.open_workbook('download/file_stock/深交所A股上市公司列表.xlsx')
		table = data.sheets()[0]	#通过索引顺序获取
		cols_code = table.col_values(0) # 股份代码
		cols_name = table.col_values(2) # 股份全称
		cols_attr = table.col_values(6) # 股份简称
		# 初始化 股份代码、股份简称、股份全称
		stock_code = cols_code[1:]
		stock_attr = cols_attr[1:]
		stock_name = cols_name[1:]
		# 读数据
		f = open('download/file_stock/上交所A股上市公司列表.xls','r')
		lines = f.readlines()
		for line in lines[1:]:
			ln = line.split('\t')
			stock_code.append(ln[0].strip()) # 股份代码
			stock_attr.append(ln[1].strip()) # 股份简称
			stock_name.append('')			 # 股份简称
		# 初始化 指数代码、指数名称
		print('*'*30)
		print(len(stock_code))
		stock_index = ['' for x in range(0,len(stock_code))]
		stock_plate = [0 for x in range(0,len(stock_code))]
		# 读数据
		data = xlrd.open_workbook('download/file_stock/上证50成份股列表.xls')
		table = data.sheets()[0]
		index = table.col_values(1)[1] # 指数代码
		plate = 1 #指数名称-上证50
		cols_code = table.col_values(4)[1:] #股份代码
		for code in cols_code:
			pos = stock_code.index(code)
			stock_index[pos] = index # 修改指数代码
			stock_plate[pos] = stock_plate[pos] + plate # 修改指数名称
		# 读数据
		data = xlrd.open_workbook('download/file_stock/沪深300成份股列表.xls')
		table = data.sheets()[0]
		index = table.col_values(1)[1] # 指数代码
		plate = 2 #指数名称-沪深300
		cols_code = table.col_values(4)[1:] #股份代码
		for code in cols_code:
			pos = stock_code.index(code)
			stock_index[pos] = index # 修改指数代码
			stock_plate[pos] = stock_plate[pos] + plate # 修改指数名称
		# 合并数据
		stock_data.append(stock_code)
		stock_data.append(stock_attr)
		stock_data.append(stock_name)
		stock_data.append(stock_index)
		stock_data.append(stock_plate)
		# 写入数据
		length = len(stock_code)
		for i in range(length):
			for j in range(5):
				# 写入excel # 参数对应 行, 列, 值 
				worksheet.write(i,j, label = stock_data[j][i])

		# 保存 
		workbook.save('download/file_stock/stock.xls')
		return correct_response({'data':'股份列表解析成功'})

		