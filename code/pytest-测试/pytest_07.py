# -*- coding: utf-8 -*-
# @Time    : 2023/10/9 09:21
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : pytest_07.py
# @Software: PyCharm
# 函数用例的前后置方法


def setup_function(function):
    """setup_function"""
    print("函数用例前置方法执行")


def teardown_function(function):
    """teardown_function"""
    print("函数用例后置方法执行")


def test_01():
    print("----用例方法01---------")
