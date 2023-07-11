# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 14:13
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : getattr.py
# @Software: PyCharm
# __getattr__ 是 python 中的一个 特殊方法, 用于在访问一个不存在的属性时被调用

class Example:
    """Example"""

    def __init__(self):
        self.data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")


if __name__ == '__main__':
    ex = Example()
    print(ex.a)
    print(ex.b)
    print(ex.c)