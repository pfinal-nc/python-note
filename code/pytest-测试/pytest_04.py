# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 14:03
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : pytest_04.py
# @Software: PyCharm
import time

import pytest

# 自动执行
# 目前为止, 所有固件的使用都是手动指定, 或者作为参数, 或者使用 usefixtures 如果让固件自动执行 可以定义时指定 autouse 参数

# 下面是两个自动计时固件,一个用于统计每个函数运行时间(function作用域) 一个用于计算测试总耗时(session 作用域):

DATE_FORMAT = "%y-%m-%d %H:%M:%S"


@pytest.fixture(scope='session', autouse=True)
def timer_session_scope():
    """ timer_session_scope """
    start = time.time()
    print('\nstart: {}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))

    yield

    finished = time.time()
    print('finished: {}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
    print('Total time cost: {:.3f}s'.format(finished - start))


@pytest.fixture(autouse=True)
def timer_function_scope():
    """timer_function_scope"""
    start = time.time()
    yield
    print(' Time cost: {:.3f}s'.format(time.time() - start))


def test_1():
    """test_1"""
    time.sleep(1)


def test_2():
    """test_2"""
    time.sleep(2)
