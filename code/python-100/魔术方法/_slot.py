# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 15:46
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : _slot.py
# @Software: PyCharm
# __solt__ 方法是一种类变量 他可以用来限制类实例的属性
# 使用 __solt__ 变量的主要优点是可以提高实例访问的速度和减少内存消耗, __slots__ 变量制定了实现可以拥有的属性, 所以在访问实例属性时


class Person:
    """Person"""
    __slots__ = {'name', 'age'}

    def __init__(self, name, age):
        """
        Person的初始化函数
        """
        self.name = name
        self.age = age

