# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 11:49
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : gt.py
# @Software: PyCharm

class Date:
    """Date class"""

    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def __gt__(self, other):
        print("__gt__")
        if self.year > other.year:
            return True
        if self.month > other.month:
            return True
        if self.month == other.month:
            return self.date > other.date


# __gt__是Python中的一个魔术方法，用于实现大于（greater than）比较运算符“>”。
# 当我们使用“>”运算符来比较两个对象时，实际上是调用了其中一个对象的__gt__方法，这个方法返回True或False。
if __name__ == '__main__':
    x = Date(2022, 2, 22)
    y = Date(2022, 2, 22)

    print(x > y)
    print(x < y)
