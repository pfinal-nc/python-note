# -*- coding: utf-8 -*-
# @Time    : 2023/10/24 16:01
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : map filter 和 reduce.py
# @Software: PyCharm
from functools import reduce

# Map 会将一个函数映射到一个输入列表的所有元素上
items = [1, 2, 3, 4, 5]

# squared = []
# for i in items:
#     squared.append(i ** 2)

# map 可以用一个简单的方式来实现
# square = list(map(lambda x: x ** 2, items))
# print(square)

# def multiply(x):
#     """multip"""
#     return (x * x)
#
#
# def add(x):
#     return (x + x)
#
#
# funcs = [multiply, add]
# for i in range(5):
#     value = map(lambda x: x(i), funcs)
#     print(list(value))

# filter 过滤列表中的元素, 并且返回一个由所有符合要求的元素所构成的列表 既函数映射到钙元素时返回值为True
# number_List = range(-5, 5)
# less_than_zero = list(filter(lambda x: x < 0, number_List))
# print(list(less_than_zero))
# filter 类似于一个 for 循环 但它是一个内置函数 并且更快

# reduce
# 当需要对一个列表进行一些计算并返回结果时, reduce 是个非常有用的函数.

product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)

