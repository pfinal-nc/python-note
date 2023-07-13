# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 15:41
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 协程.py
# @Software: PyCharm
import asyncio


#  所谓协程 可以简单的理解为多个相互协作的子程序 在同一个线程中 当一个子程序阻塞时, 可以让程序马上从一个子程序切换到另一个子程序中

# def display(num):
#     """Display """
#     time.sleep(1)
#     print(num)

#
# for num in range(10):
#     display(num)


async def display(num):
    await asyncio.sleep(1)
    print(num)


coroutines = [display(num) for num in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()

