# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 18:11
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : _iadd.py
# @Software: PyCharm
# _iadd 是python 中的 一个魔术方法 用于在类中定义就地加法的实现, 即将两个对象相加  并将结果存储在第一个对象中 在 python 中 就地加法使用 += 如果类中没有实现__iadd__，则Python解释器会尝试使用__add__方法代替__iadd__方法，这样会创建一个新的对象并返回结果。

class MyList:
    def __init__(self, items):
        self.items = items

    def __iadd__(self, other):
        if isinstance(other, MyList):
            self.items.extend(other.items)
        else:
            self.items.append(other)
        return self

    def __repr__(self):
        return f'MyList({self.items})'