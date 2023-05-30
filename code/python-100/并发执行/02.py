# -*- coding: utf-8 -*-
# @Time    : 2023/5/29 14:50
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 02.py
# @Software: PyCharm
import asyncio
from random import random, randint


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


async def main():
    aws, results = [], []
    for i in range(3):
        aws.append(asyncio.create_task(some_coro(f'name-{i}')))

    results = await asyncio.wait_for(asyncio.gather(*aws), timeout=2)
    for result in results:
        print(f"Coroutine {result}")