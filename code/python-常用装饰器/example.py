# -*- coding: utf-8 -*-
# @Time    : 2023/8/4 14:26
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : example.py
# @Software: PyCharm
import time

from utils import timer, memoize, log_results, validate_output, debug, deprecated


@timer
def testTimer():
    time.sleep(1)
    print('测试timer 装饰器')


testTimer()


@memoize
def fibonacci(n):
    """Fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

    # fibonacci(2)


@log_results
@timer
def calculate_metrics(data):
    """Calculates metrics"""
    print('================================')
    return data


calculate_metrics([1, 2, 3, 4])


@validate_output
def clean_data(data):
    """clean_data """
    print('================================')


@debug
def complex_data_processing(data, threshold=0.5):
    """ complex_data_processing """
    print('================================')


complex_data_processing([1, 2])


@deprecated
def old_data_processing(data):
    # Your old data processing code here
    print(data)


old_data_processing([1, 2])


# 多个装饰器
def foo1(func):
    print("d1")

    def inner1():
        print("inner1")
        return "<i>{}</i>".format(func())

    return inner1


def foo2(func):
    print("d2")

    def inner2():
        print("inner2")
        return "<b>{}</b>".format(func())

    return inner2


@foo1
@foo2
def f1():
    """f1"""
    return "Hello Andy"


ret = f1()  # 调用f1() ==> inner1()  ==> <i>inner2()</i>  ==> <i><b>inner1()</b></i> ==> <i><b>Hello Andy</b></i>
print(ret)
