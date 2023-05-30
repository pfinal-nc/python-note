# -*- coding: UTF-8 -*-
import asyncio
from random import randint, random


class AsyncException(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        super(*args, **kwargs)

    def __str__(self):
        return self.message


async def some_coro(name):
    print(f"Coroutine {name} begin to run")
    value = random()

    delay = randint(1, 4)
    await asyncio.sleep(delay)
    if value > 0.5:
        raise AsyncException(f"Something bad happen after delay {delay} second(s)")
    print(f"Coro {name} is Done. with delay {delay} second(s)")
    return value


# asyncio.gather 用于启动一组后台任务, 等待他们完成执行, 并获取结果列表:

async def main():
    aws, results = [], [];
    for i in range(3):
        aws.append(asyncio.create_task(some_coro(f'name-{i}')))

    # results = await asyncio.gather(*aws)
    # for result in results:
    #     print(f">got :{result}")
    try:
       # results = await asyncio.gather(*aws, return_exceptions=False)  # need to unpack the list
       results = await asyncio.gather(*aws, return_exceptions=True)  # need to unpack the list
    except AsyncException as e:
        print(e)
    for result in results:
        print(f">got : {result}")
# asyncio.gather 虽然组成一个组后台任务, 但不能直接接受一个列表或集合作为参数。如果需要传入包含后台任务的列表，请解包。
# asyncio.gather 接受一个 return_excceptions参数, 当return_excecption的值为False时, 任何后台任务抛出异常,都会抛给gatherr方法的调用者, 而gather方法的结果列表是空的
# 当 return_excceptions 的值 为True时, 后台任务抛出的异常不会影响其他任务的执行, 最终会合并到结果列表中一起返回


if __name__ == '__main__':
    asyncio.run(main())
