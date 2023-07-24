# -*- coding: utf-8 -*-
# @Time    : 2023/7/24 11:22
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 异步IO_02.py
# @Software: PyCharm
# 如何取消 可能需要很长时间才能完成的长时间运的异步操作
import asyncio
from asyncio import CancelledError


# task = asyncio.create_task(coroutine())
# result = await task
# 使用 await 语句等待任务完成, 但是,如果 coroutine 花费了很长时间, 将无法等待 await 语句完成而没有结果。
# 如果要停止这个函数, 要解决此问题，可以使用Task对象的cancel()方法取消任务。如果在取消任务后await，它会引发CancelledError异常

async def call_api(message, result=1000, delay=3):
    """ call_api()"""
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    """ main """
    task = asyncio.create_task(
        call_api('Calling API...', result=2000, delay=5)
    )

    # if not task.done():
    #     print('Cancelling the task...')
    #     task.cancel()
    #
    # try:
    #     await task
    # except CancelledError:
    #     print('Task has been cancelled.')

    # 如果每秒检查一个任务是否已经完成并在经过一段时间后取消它.
    time_elapsed = 0
    while not task.done():
        time_elapsed += 1
        await asyncio.sleep(1)
        print('Task has not completed, checking again in a second')
        if time_elapsed == 3:
            print('Cancelling the task...')
            task.cancel()
            break

    try:
        await task
    except CancelledError:
        print('Task has been cancelled')


asyncio.run(main())
