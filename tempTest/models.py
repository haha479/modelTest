# encoding:utf-8
from __future__ import unicode_literals

from django.db import models

class BookInfo(models.Model):
	#下面定义的类属性是为了映射数据库的表结构
	btitle = models.CharField(max_length=20)
	bpub_date = models.DateTimeField()
	def __str__(self):
		return self.btitle.encode("utf-8")

class HeroInfo(models.Model):
	hname = models.CharField(max_length=10)
	hgender = models.BooleanField()
	hcontent = models.CharField(max_length=1000)
	hbook = models.ForeignKey(BookInfo)
	def __str__(self):
		return self.hname.encode("utf-8")




