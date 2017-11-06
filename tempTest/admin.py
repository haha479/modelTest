# encoding:utf-8
from django.contrib import admin
from models import *

# Register your models here.

#定义一个类,用来关联注册,可以继承两个类
class HeroInfoInline(admin.StackedInline):
	#关联的类
	model = HeroInfo
	#关联的个数
	extra = 3

#创建管理类,用来自定义管理页面中的显示
class BookInfoadmin(admin.ModelAdmin):
	#指定字段排序
	list_display  = ['pk','btitle', 'bpub_date']
	#过滤器,出现在右边
	list_filter = ['btitle']
	#搜索过滤,出现再上方
	search_fields = ['btitle']
	#分页(值是等于一页放下多少条数据)
	list_per_page = 1

	#添加修改页
	fieldsets = [
		('base',{'fields':['btitle']}),
		('super',{'fields':['bpub_date']})
	]

	#嵌入(可以嵌入多个,这里只对应了一个作者)
	inlines = [HeroInfoInline]

# 注册用户()
admin.site.register(BookInfo,BookInfoadmin)
admin.site.register(HeroInfo)

