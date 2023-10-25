# -*- coding: utf-8 -*-
# @Time    : 2023/10/24 16:57
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : Mutation.py
# @Software: PyCharm

# foo = ["hi"]
# print(foo)
#
# bar = foo
# bar += ['bye']
# print(foo)

#  每当将一个变量赋值为另一个可变类型的变量时, 对这个数据的任意改动 同事反映到这个变量上 新变量只不过是老变量的一个副本

# def add_to(num, target=[]):
#     """add to"""
#     target.append(num)
#     return target
#
#
# print(add_to(1))
# print(add_to(2))
# print(add_to(3))

def add_to(num, target=None):
    """add to"""
    if target is None:
        target = []
    target.append(num)
    return target


print(add_to(1))
print(add_to(2))
print(add_to(3))