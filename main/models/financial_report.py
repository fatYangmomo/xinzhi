__all__ = ['FinancialReport']

from django.db import models
from datetime import datetime
from .group import Group

# 财报表
class FinancialReport(models.Model):

	class Meta():  # Meta 可用于定义数据表名，排序方式等。
	    verbose_name="financial_report" #指明一个易于理解和表示的单词形式的对象。
	    db_table = "financial_report" #声明数据表的名。

	# 股份代码
	stock_code = models.CharField(primary_key=True,max_length=10,verbose_name=u"股份代码")
	# 股份名称
	stock_name = models.CharField(max_length=50,verbose_name=u"股份名称")
	# 报告日期
	report_date = models.CharField(max_length=10,null=True,verbose_name=u"报告日期")
	# 总股本
	capital = models.DecimalField(max_digits=20, decimal_places=2,null=True,verbose_name=u"总股本")
	# 营业收入
	business_receipts = models.DecimalField(max_digits=20, decimal_places=2,null=True,verbose_name=u"营业收入")
	# 净利润
	profits = models.DecimalField(max_digits=20, decimal_places=2,null=True,verbose_name=u"净利润")
	# 营业收入增长率
	business_ratio = models.DecimalField(max_digits=5, decimal_places=2,null=True,verbose_name=u"营业收入增长率")
	# 净利润增长率
	profits_ratio = models.DecimalField(max_digits=5, decimal_places=2,null=True,verbose_name=u"净利润增长率")
	# 每股净资产
	share_asset = models.DecimalField(max_digits=20, decimal_places=2,null=True,verbose_name=u"每股净资产")
	# 净资产收益率
	asset_ratio = models.DecimalField(max_digits=5, decimal_places=2,null=True,verbose_name=u"净资产收益率")
	# 每股收益
	share_profit = models.DecimalField(max_digits=20, decimal_places=2,null=True,verbose_name=u"每股收益")
	# 当前价格
	current_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,verbose_name=u"当前价格")
	# 市盈率
	shiying_ratio = models.DecimalField(max_digits=5, decimal_places=2,null=True,verbose_name=u"市盈率")
	# 市净率
	shijing_ratio = models.DecimalField(max_digits=20, decimal_places=2,null=True,verbose_name=u"市净率")


	# 所属板块
	# 1：上证50
	# 2：沪深300
	# 3：上证50，沪深300
	# 4：MSCI
	# 5：上证50，MSCI
	# 6：沪深300，MSCI
	# 7： 上证50，沪深300，MSCI
	plate = models.CharField(max_length=10,null=True,verbose_name=u"所属板块")
	# 所属组合
	group = models.ForeignKey(Group,on_delete=models.CASCADE)

	# 收盘价
	closing_price = models.DecimalField(max_digits=20, decimal_places=2,null=True,verbose_name=u"收盘价")
	# 前收盘
	front_close = models.DecimalField(max_digits=20, decimal_places=2,null=True,verbose_name=u"前收盘")

	def __str__(self):
		info="[stock_code:%s,stock_name:%s]"%(self.stock_code,self.stock_name)
		return info