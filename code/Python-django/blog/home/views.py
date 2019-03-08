from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
# Create your views here.


def index(request):  # request是必须带的实例。类似class下方法必须带self一样
    # return HttpResponse("Hello World!!")#通过HttpResponse模块直接返回字符串到前端页面、
    return render(request, 'index.html')
