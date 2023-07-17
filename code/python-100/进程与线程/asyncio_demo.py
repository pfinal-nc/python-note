# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 10:02
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : asyncio_demo.py
# @Software: PyCharm
# asyncio 编程模型就是一个消息循环, 从 aasyncio 模块中 直接获取一个 EventLoop 的引用, 然后把 需要执行的协程扔到 EventLoop中执行  就实现了 异步IO
import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

# asyncio.coroutine 把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。

# async / aswait
# 用 aasyncio 提供的 @asyncio.coroutine 可以把一个 generator 标记为 coroutine 类型


