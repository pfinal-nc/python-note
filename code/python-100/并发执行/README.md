python 并发编程IO模型

> 五种I/O 模型 阻塞I/O、非阻塞I/O、信号驱动I/O(不常用)、I/O多路转接、异步I/O。其中，前四个被称为同步I/O。

> 上五个模型的阻塞程度由低到高为：阻塞I/O > 非阻塞I/O > 多路转接I/O > 信号驱动I/O > 异步I/O，因此他们的效率是由低到高的

### 阻塞I/O模型

在linux中默认情况下所有 socket都是 blocking 除非特别指定,几乎所有的I/O接口都是阻塞的

如果所面临的可能同时出现的上千甚至上万次的客户端请求, "线程池"或"连接池"或许可以缓解部分压力,但是不能解决所有问题。
总之, 多线程模型可以方便高效的解决小规模的服务请求, 但面对大规模的服务请求,多线程模型也会遇到瓶颈


### 非阻塞I/O模型

在非阻塞式I/O 中, 用户进程其实是需要不断的主动问 kernel数据准备好了没有, 但是非阻塞I/O模型绝不被推荐

非阻塞,不等待, 比如创建socket对某个地址进行 connect,获取接收数据recv时默认都会等待,才执行后续操作.
如果设置setblocking(False), 以上两个过程就不再等待, 但是会报BlockingOError的错误, 只要捕获即可.

异步, 通知,执行完成之后自动执行回调函数或自动执行某些操

### 多路复用I/O模型(时间驱动)

基于事件循环的异步非阻塞框架:如Twisted框架，scrapy框架(单线程完成并发)。

检测多个socket是否已经发生变化（是否已经连接成功/是否已经获取数据）(可读/可写)IO多路复用作用？

操作系统检测socket是否发生变化，有三种模式：

select：最多1024个socket；循环去检测。
poll：不限制监听socket个数；循环去检测（水平触发）。
epoll：不限制监听socket个数；回调方式（边缘触发）。

### 异步I/O

*asyncio* 库直接内置了异步IO支持
*asyncio* 的变成模型就是一个消息循环,从asyncio 模块中直接获取一个 EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

```python
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
```

@asyncio.coroutine 把一个 generator标记为coroutine类型



