# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 17:58
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : _add.py
# @Software: PyCharm
# __add 定义对象之间加法操作的魔术方法 当使用 + 运算对两个对象执行加法操作时 Python将会查找并调用每个对象中定义的__add__方法。

class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        elif isinstance(other, (int, float)):
            return MyNumber(self.value + other)
        else:
            return NotImplemented

    def __repr__(self):
        return f"MyNumber({self.value})"


if __name__ == '__main__':
    n1 = MyNumber(1)
    n2 = MyNumber(2)
    print(n1 + n2)
    print(n1 + 5)
    print(n2 + "3")
