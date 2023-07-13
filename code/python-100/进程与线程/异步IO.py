# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 13:54
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 异步IO.py
# @Software: PyCharm
import asyncio


def num_generator(m, n):
    """ num_generator """
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """ 素数过滤器 """
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)
        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """ 平方映射器 """
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)

    return squares


def main():
    """main function"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
    main()
