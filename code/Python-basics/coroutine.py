# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 09:02
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : coroutine.py
# @Software: PyCharm
import asyncio


async def execute():
    print("Executing PFinal", )


coro = execute()
loop = asyncio.get_event_loop()
task = loop.create_task(coro)
print("Task", task)
loop.run_until_complete(task)
print("Task", task)
# loop.close()
