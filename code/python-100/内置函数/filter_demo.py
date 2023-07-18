# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 14:19
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : filter_demo.py
# @Software: PyCharm

# filter() 函数是 python 内置的另一个有用的高阶函数, filter() 函数接受一个函数 f 和 一个  list 这个函数 f 的作用 是对每个元素进行判断, 返回True 或 False
# filter() 根据 判断结果自动过滤掉不符合条件的元素, 返回由符合条件元素组成新 list

def is_odd(x):
    """is odd"""
    if x % 2 == 1:
        return x


if __name__ == '__main__':
    print(list(filter(is_odd, [1, 4, 6, 7, 9, 12, 17])))
    # 利用 filter()
