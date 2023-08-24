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


#
# @asyncio.coroutine
# def hello():
#     """hello"""
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1)
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# @asyncio.coroutine 把一个 generator 标记为 coroutine类型, 然后 我们就把这个 coroutine 扔到 eventloop 中执行
# hello() 会首先打印出 hello world!
# 然后 yield from 语法可以让我们方便地调用另一个generator 由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
# asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

# @asyncio.coroutine
# def hello():
#     """hello"""
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。

@asyncio.coroutine
def wget(host):
    """wget(host)"""
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
