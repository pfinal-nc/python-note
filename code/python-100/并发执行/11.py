# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 17:26
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 11.py
# @Software: PyCharm
import asyncio

@asyncio.coroutine
def hello():
    print("Hello")
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("hello again")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
