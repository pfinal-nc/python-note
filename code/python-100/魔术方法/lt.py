# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 13:46
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : lt.py
# @Software: PyCharm

# __lt__  是 python中的一个魔术方法,用于重载小于号 < 的行为, 该方法用于比较两个对象的大小关系 既是否小于 在python中 如果两个对象无法比较大小

class Date:
    """date class"""

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

    def __lt__(self, other):
        print("__lt__")
        if self.year < other.year:
            return True
        if self.month < other.month:
            return True
        if self.month == other.month:
            return self.date < other.date


if __name__ == '__main__':
    x = Date(2022, 2, 22)
    y = Date(2022, 2, 22)
    print(x > y)
    print(x < y)