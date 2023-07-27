# -*- coding: utf-8 -*-
# @Time    : 2023/7/24 13:43
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 并发运行.py
# @Software: PyCharm


# 使用 asyncio.create_task 函数并发运行多个任务

# 模拟长时间运行的操作
# 要模拟长时间运行的操作, 可以使用 asyncio 包的 sleep() 协程, 该 sleep() 函数延迟指定的秒数
# await asyncio.sleep(seconds)
# 因为 sleep() 是协程, 所以需要使用 await 关键字,
#
# async def call_api(message, result=1000, delay=3):
#     """ call_api(message, result, delay)"""
#     print(message)
#     await asyncio.sleep(delay)
#     return result


# call_api 是协程, 它显示一条消息 暂停指定的秒数(默认为三秒)  然后返回结果
#
# async def main():
#     """main"""
#     start = time.perf_counter()
#
#     price = await call_api('Get stock price of GOOG...', 300)
#     print(price)
#
#     price = await call_api('Get stock price of APPL...', 400)
#     print(price)
#
#     end = time.perf_counter()
#     print(f'It took {round(end - start, 0)} second(s) to complete.')
#
#
# asyncio.run(main())

# python 中任务是协程的包装器 它安排携程尽快在事件循环上运行
# 调度和执行以阻塞方式发生,可以创建任务并在任务运行时立即执行其他代码

