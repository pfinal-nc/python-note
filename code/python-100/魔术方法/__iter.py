# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 14:35
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : __iter.py
# @Software: PyCharm
from typing import Iterable


class Row:
    """Row"""
    __slots__ = ['_row', 'tags']

    def __init__(self, row=None, tags=None):
        self._row = list(row)
        self.tags = list(tags)

    def __iter__(self):
        return (col for col in self._row)


# __iter__ 返回一个 迭代器对象, 该对象是一个实现了 __next__的对象, 该方法为容器类所拥有, 类似于 迭代器模式中Aggregate 类的 createIterator 方法

# __next__ 顾铭思议 返回当前迭代器的下一个迭代器, 并且不想继续有迭代的情况下抛出一个 stopiteration的 异常,


if __name__ == '__main__':
    row = Row([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd'])
    print(isinstance(row, Iterable))
    for r in row:
        print(r)