# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 11:24
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : eq.py
# @Software: PyCharm

# __eq__ 判断两个对象是否相等
# __eq__ 方法默认情况下是比较两个对象的内存地址是否相等 即 id(self) == id(other)

class Date:
    """Date class"""

    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def __eq__(self, other):
        print("__eq__")
        return self.year == other.year and self.month == other.month and self.date == other.date

    def __ne__(self, other):
        print("__ne__")
        return self.year != other.year and self.month != other.month and self.date != other.date


if __name__ == '__main__':
    x = Date(2022, 2, 23)
    y = Date(2022, 2, 23)
    print(x == y)
    print(x != y)
