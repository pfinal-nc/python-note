# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 13:53
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 异步IO_01.py
# @Software: PyCharm
import asyncio


# 异步并发的概念
# 对于其他并发模型大多数采取的都是线性的方式编写。 并且依赖于语言运行时系统或操作系统的底层线程或进程来适当地改变上下文, 而基于asyncio 的应用要求代码显示的处理上下文切换
# asyncio 提供的框架以事件循环(event loop)为中心, 程序开启一个无限的循环, 程序会把一些函数注册到事件循环上。当满足事件发生的时候, 调用相应的协程函数

# 事件循环
# 事件循环是一种处理多并发量的有效方式, 定义事件循环来简化使用轮询方法来监控事件，通俗的说法就是「当A发生时，执行B」。事件循环使用回调方法来知道事件的发生。它是asyncio提供的「中央处理设备」，支持如下操作：
# 与事件循环交互的应用要显示地注册将运行的代码，让事件循环在资源可用时向应用代码发出必要的调用。

# Future
# future 是一个数据结构,表示还未完成的工作结果, 事件循环可以监视 Future 对象是否完成. 从而允许应用的一部分等待另一部分完成一些工作

# Task
# task 是 future的一个子类, 知道如何包装和管理一个协程的执行。任务所需的资源可用时，事件循环会调度任务允许，并生成一个结果，从而可以由其他协程消费。

# 使用 asyncio 也就意味着你需要一直写异步方法。

# 要调用异步函数，必须使用await关键字

# 不能在同步函数里使用await，否则会出错


# 启动一个协程
#  一般异步方法被称之为协程。asyncio 事件循环可以通过多种不同的方法启动一个协程。一般对于入口函数, 最简单的方法就是使用 run_until_complete() 并将协程直接传入这个方法

# async def fool():
#     """fool"""
#     print("这是一个协程")
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         print("开始运行协程")
#         coro = fool()
#         print("进入事件循环")
#         loop.run_until_complete(coro)
#     finally:
#         print("关闭事件循环")
#         loop.close()

# 得到一个事件循环的应用也就是定义的对象 loop 可以使用默认的事件循环.
# 也可以实例化一个特定的循环类, 使用了默认循环 run_until_complete 方法用这个协程启动循环,协程返回时这个方法将停止循环。
# run_until_complete的参数是一个futrue对象。当传入一个协程，其内部会自动封装成task，其中task是Future的子类。

# 从协程中返回值 将上面的代码 改写

# async def foo():
#     """foo """
#     print("这是一个协程")
#     return "返回值"
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         print("开始运行协程")
#         coro = foo()
#         result = loop.run_until_complete(coro)
#         print(f"run_until_complete可以获取协程的{result}，默认输出None")
#     finally:
#         print("关闭时间循环")
#         loop.close()

# run_until_complete 可以获取协程的返回值, 如果没有给定返回值, 则像函数一样, 默认返回None

# 协程调用协程
# 一个协程可以启动另外一个协程, 从而可以任务根据工作内容, 封装到不同的协程中, 可以在携程中使用 await 关键字 链式的调度协程, 来形成一个协程任务流

# async def result1():
#     """ result1 """
#     print("这是result1协程")
#     return "result1"
#
#
# async def result2(arg):
#     """result2 """
#     print("这是 result2协程")
#     return f"result2接受了一个参数,{arg}"
#
#
# async def main():
#     """main"""
#     print("主协程")
#     print("等待result1协程运行")
#     res1 = await result1()
#     print("等待result2协程运行")
#     res2 = await result2(res1)
#     return res1, res2
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         result = loop.run_until_complete(main())
#         print(f"获取返回值:{result}")
#     finally:
#         print("关闭事件循环")
#         loop.close()

# 协程中调用普通函数
# 在协程中可以通过一些方法去调用普通的函数. 可以使用的关键字有call_soon,call_later，call_at。

# call_soon
# 通过 字面意思理解调用立即返回
# loop.call_soon(callback, *args, context=None)
# 在下一个迭代的时间循环中 立刻调用回调函数, 大部分的回调函数支持位置参数,而不支持关键字参数. 如果是想要使用关键字参数，则推荐使用functools.aprtial()对方法进一步包装.可选关键字context允许指定要运行的回调的自定义contextvars.Context
# 使用上下文就可以在一些场景下隐式地传递变量，比如数据库连接session等，而不需要在所有方法调用显示地传递这些变量。

# def callback(args, *, kwargs="default"):
#     """Callback"""
#     print(f"普通函数做为回调函数,获取参数:{args},{kwargs}")
#
#
# async def main(loop):
#     """main"""
#     print("注册callback")
#     loop.call_soon(callback, 1)
#     wrapped = functools.partial(callback, kwargs="not defalut")
#     loop.call_soon(wrapped, 2)
#     await asyncio.sleep(0.2)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(main(loop))
#     finally:
#         loop.close()

#  有时候不想立即调用一个函数, 此时可以 call_later延时去调用一个函数

# call_later 就是事件循环在delay多长时间之后才执行callback函数.
# loop.call_later(delay, callback, *args, context=None),

# def callback(n):
#     """ callback """
#     print(f"callback {n} invoked")
#
#
# async def main(loop):
#     """main"""
#     print("注册callbacks")
#     loop.call_later(0.2, callback, 1)
#     loop.call_later(0.1, callback, 2)
#     loop.call_soon(callback, 3)
#     await asyncio.sleep(0.4)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(main(loop))
#     finally:
#         loop.close()

# call_soon 会在 call_later 之前执行, 和它的位置在哪无关
# call_later 的第一个参数越小, 越先执行


# call_at
# loop.call_at(when, callback, *args, context=None)
# call_at 第一个参数的含义代表的是一个单调时间, 它和我们平时说的系统时间有点差异, 这里的时间指的是事件循环内部时间 可以通过loop.time() 获取, 然后可以在此基础上进行操作
# # 后面的参数和前面的两个方法一样, 实际上 call_later 内部就是调用的 call_at
#
# def call_back(n, loop):
#     """call_back"""
#     print(f"callback {n} 运行时间点{loop.time()}")
#
#
# async def main(loop):
#     """main"""
#     now = loop.time()
#     print("当前的内部时间", now)
#     print("循环时间", now)
#     print("注册callback")
#     loop.call_at(now + 0.1, call_back, 1, loop)
#     loop.call_at(now + 0.2, call_back, 2, loop)
#     loop.call_soon(call_back, 3, loop)
#     await asyncio.sleep(1)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         print("进入事件循环")
#         loop.run_until_complete(main(loop))
#     finally:
#         print("关闭循环")
#         loop.close()

# Future
#  表示 还没完成的工作结果, 事件循环可以通过监视一个 future 对象 的状态来指定它已经完成. future 对象有几个状态:
#  Pending
#  Running
#  Done
#  Cancelled
#  创建future 的时候, task 为 pending 事件循环调用执行的时候当然就是 running 调用完毕自然就是 done, 如果需要停止事件循环, 就需要把task取消, 状态 cancel.


# def foo(future, result):
#     """ foo """
#     print(f"此时future的状态:{future}")
#     print(f"设置future 的结果:{result}")
#     future.set_result(result)
#     print(f"此时future 的状态:{future}")
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         all_done = asyncio.Future()
#         loop.call_soon(foo, all_done, "Future is done!")
#         print("进入事件循环")
#         result =
#     finally:
#         print("关闭事件循环")
#         loop.close()
