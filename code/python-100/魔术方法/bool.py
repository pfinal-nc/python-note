# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 14:09
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : bool.py
# @Software: PyCharm
#  bool 它是在类中实现定义实例转化为布尔值的方式

class MyClass:
    """MyClass"""

    def __init__(self, num):
        self.num = num

    def __bool__(self):
        return self.num > 0

# MyClass 类的 __bool__ 方法返回 self.num > 0 的结果, 这表示 当 num 大于 0时
