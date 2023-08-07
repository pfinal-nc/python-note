# -*- coding: utf-8 -*-
# @Time    : 2023/8/7 16:40
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : lambda_demo.py
# @Software: PyCharm
from functools import reduce

# lambda 是匿名函数，也就是没有名字的函数

my_sum = lambda x, y: x + y
print(my_sum(1, 2))

# map() 接收两个参数 func (函数) 和 seq (序列，例如list) map 返回一个迭代器 使用map 相当于使用一个for 循环
l = [11, 22, 33, 44, 55]
print(list(map(lambda x: x + 100, l)))

# filter() 函数和 map 函数一样也是接收两个参数 func () 和seq, filter 函数类似实现了一个过滤功能, 它过滤序列中的所有元素 返回
a = [30, 11, 22, 33, 44, 55]
print(list(filter(lambda x: x > 33, a)))

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 3, 4]

print(list(filter(lambda a: a in y, x)))

# reduce 同样接收两个参数: func 函数 和 seq   reducec 最后返回的不是一个迭代器, 它返回一个值
# reduce 首先将序列中的前两个元素，传入 func 中, 再将得到的结果和第三个元素一起传入 func, ..., 这样一直计算到最后
reduce_res = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(reduce_res)

# 三元运算 配合 lambda表达式 和reduce 求列表里面值最大的元素
l = [30, 11, 77, 8, 25, 65, 4]

result = reduce(lambda x, y: x if x > y else y, l)

print(result)

# zip 函数接收 一个或多个可迭代对象作为参数 最后返回一个迭代器:

x = ["a", "b", "c", "d", "e", "f"]
y = [1, 2, 3]
a = list(zip(x, y))  # 合包
print(a)

b = list(zip(*a))  # 解包
print(b)

# zip(x，y)
