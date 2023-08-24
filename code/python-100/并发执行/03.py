# -*- coding: utf-8 -*-
# @Time    : 2023/5/29 16:18
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 03.py
# @Software: PyCharm
import asyncio

# asyncio 提供了一个基于事件循环的异步编程模型, 允许使用 async和await 关键字写异步代码.
# asyncio 还提供了许多高级
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
URL = 'http://www.baidu.com'


def hello():
    """hello"""
    print("Hello world!")
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello again!")
