# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 13:59
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : hash.py
# @Software: PyCharm
#  在Python中 __hash__   用于返回对象的哈希值 哈希值是一个整数，用于在字典查找中快速比较两个对象是否相等

class MyClass:
    """MyClass"""

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return self.x == other.x

    def __hash__(self):
        return hash(self.x)


if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(1)
    c = MyClass(2)

    print(a == b)
