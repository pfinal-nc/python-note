# -*- coding: utf-8 -*-
# @Time    : 2023/8/3 11:20
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 装饰器02.py
# @Software: PyCharm
# 装饰器本质 就是一个闭包函数  在不修改原函数及其调用方式的情况下对原函数功能进行扩展
# import time
#
#
# # 装饰带一个参数的函数
#
# def timer(func):
#     """timer function"""
#
#     def inner(a):
#         """ inner function"""
#         start = time.time()
#         func(a)
#         print(time.time() - start)
#     return inner
#
# @timer
# def f(a):
#     """f function"""
#     print(a)
#
#
# f("hello")
import time
from functools import wraps

# 为了使用装饰器不用时更好的回收而不是一个一个去注释  引入带参数的装饰器

FLAGE = True


def timmer_out(flag):
    def timmer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if flag:
                start = time.time()
                ret = func(*args, **kwargs)
                print(time.time() - start)
                return ret
            else:
                return func(*args, **kwargs)

        return inner

    return timmer


@timmer_out(FLAGE)
# timmer_out(FLAGE)
# 也相当于执行  timmer_out(FLAGE)--->>返回timmer———————>>@timmer(wahaha = timmer(wahaha))
def wahaha():
    """ wahaha """
    time.sleep(0.1)  # 不休息的话函数执行的太快难以计算时间
    print('wahahahahahaha')


wahaha()


@timmer_out(False)
def erguotou():
    time.sleep(0.1)  # 不休息的话函数执行的太快难以计算时间
    print('erguotoutoutou')


erguotou()

print(wahaha.__name__)
print(wahaha.__doc__)

# 装饰器原则
# 1.开放封闭原则  对于任何一个程序来说，不可能在设计之初就已想好了所有的功能并且未来不做任何更新和修改
# 2. 对修改是封闭
