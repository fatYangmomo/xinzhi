__all__ = ['Stock']

from django.db import models
from datetime import datetime

# 股份表
class Stock(models.Model):

	class Meta():  # Meta 可用于定义数据表名，排序方式等。
	    verbose_name="stock" #指明一个易于理解和表示的单词形式的对象。
	    db_table = "stock" #声明数据表的名。

	# 股份代码
	stock_code = models.CharField(primary_key=True,max_length=10,verbose_name=u"股份代码")
	# 股份名称
	stock_name = models.CharField(max_length=50,verbose_name=u"股份名称")
	# 所属板块
	plate = models.CharField(max_length=10,null=True,verbose_name=u"所属板块")

	def __str__(self):
		info="[stock_code:%s,stock_name:%s]"%(self.stock_code,self.stock_name)
		return info