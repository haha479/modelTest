# encoding:utf-8
from django.shortcuts import render
from models import *
# Create your views here.

# 显示书的页面
def index(request):
	#　获取所有的书
	book_info = BookInfo.objects.all()
	content = {"book_list":book_info}

	return render(request,'tempTest/index.html',content)


#　显示对应书的作者页面
def show(request,id):
	#通过url接收的id来获取是哪本书
	book = BookInfo.objects.get(pk=id)
	# 获取一本书对应的所有作者
	hero = book.heroinfo_set.all()
	#将对应书的所有作者传给网页
	content = {"hero_list":hero}
	return render(request,'tempTest/show.html', content)