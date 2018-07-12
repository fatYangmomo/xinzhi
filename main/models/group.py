__all__ = ['Group']

from django.db import models
from datetime import datetime

# 组合表
class Group(models.Model):

	class Meta():  # Meta 可用于定义数据表名，排序方式等。
	    verbose_name="group" #指明一个易于理解和表示的单词形式的对象。
	    db_table = "group" #声明数据表的名。

	# ID
	id = models.IntegerField(primary_key=True,verbose_name=u"ID")
	# 组合名称
	group_name = models.CharField(max_length=32,verbose_name=u"组合名称")

	def __str__(self):
		info="[id:%s,group_name:%s]"%(self.id,self.group_name)
		return info