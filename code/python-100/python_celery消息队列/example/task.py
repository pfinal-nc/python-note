# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 10:21
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : task.py
# @Software: PyCharm
from celery import Celery

app = Celery('azima', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')


# 第一个参数为当前模块的名称，只有在 __main__ 模块中定义任务时才会生产名称
# 第二个参数为中间人（Broker）的链接 URL ，
# 创建了一个名称为 add 的任务，返回的俩个数字的和。

@app.task
def add(x, y):
    """ add a task"""
    return x + y

