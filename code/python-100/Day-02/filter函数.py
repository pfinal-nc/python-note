# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 14:41
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : filter函数.py
# @Software: PyCharm
# 在 python 中 filter 函数是一种内置的高阶函数,它能够接受一个函数和一个迭代器, 然后返回一个新的迭代器, 这个新的迭代器仅包含使给定函数返回 True的原始元素.

def is_event(n):
    """is event"""
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_event, numbers)

print(list(even_numbers))

# 使用匿名函数与 filter 函数
# 使用匿名函数 作为 filter 函数的第一个参数

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)
# 在 filter 函数调用中 定义了一个匿名函数, 这个匿名函数接受一个数字并检查它是哦否是偶数
# filter 函数也可以处理更复杂的数据结构可以使用.filter函数来筛选出满足某些条件的字典。

data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]
old_people = filter(lambda x: x['age'] > 30, data)
print(list(old_people))

# 使用推导式

even_numbers = {n for n in numbers if n % 2 == 0}
print(even_numbers)

