# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 13:57
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : map_demo.py
# @Software: PyCharm
def f(x):
    return x * x


# map() 接受一个函数f 和 一个 list 并通过把函数f 一次作用在 list 的每个元素上, 得到一个新的 list 并返回
# map() 函数不会改变原有的list 而是返回一个新的 list
if __name__ == '__main__':
    print(list(map(f, [i for i in range(1, 10)])))

