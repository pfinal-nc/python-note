# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 09:11
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : coroutine1.py
# @Software: PyCharm
import time


def work1():
    while True:
        print("------work1------")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("------work2------")
        yield
        time.sleep(0.5)


def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)


if __name__ == '__main__':
    main()
