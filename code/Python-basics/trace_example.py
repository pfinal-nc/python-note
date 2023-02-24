# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 19:35
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : trace_example.py
# @Software: PyCharm
import functools
import profile


@functools.lru_cache(maxsize=None)
def fib(n):
    # from literateprograms.org
    # http://bit.ly/hlOQ5m
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq


# profile.run('print(fib_seq(20)); print()')
if __name__ == '__main__':
    profile.runctx(
        'print(fib_seq(n)); print()',
        globals(),
        {'n': 20},
    )