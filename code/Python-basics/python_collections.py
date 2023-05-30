# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 17:38
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : python_collections.py
# @Software: PyCharm
from collections import namedtuple

# collections 是python内建的一个集合模块 提供了许多有用的集合类
if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x, p.y)
    # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
