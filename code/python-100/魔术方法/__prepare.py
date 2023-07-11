# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 17:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : __prepare.py
# @Software: PyCharm
# __prepare__ 方法中新引入的一个元类方法, 在类定义之前被调用, 用于创建用于存储类属性的字典.
# 定义一个新的类时, python 首先会寻找 元类并调用它的 __prepare__ 方法。该方法返回的字典会被用来存储类属性。
import collections


class MyMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        # 创建一个 OrderedDict 对象作为字典 并返回它
        return collections.OrderedDict()


class MyClass(metaclass=MyMeta):
    a = 1
    b = 2
    c = 3


print(MyClass.__dict__)
