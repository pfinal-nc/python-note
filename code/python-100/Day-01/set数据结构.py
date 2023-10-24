# -*- coding: utf-8 -*-
# @Time    : 2023/10/24 16:32
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : set数据结构.py
# @Software: PyCharm

# set 数据结构
# set 集合是一个非常有用的数据结构 与列表(list) 的行为类似,区别在于 set 不能包含重复值
some_list = ["a", "b", "c", "d", "e", "f", "a"]
# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
#
# print(duplicates)

# 使用set 集合
# duplicate = set([x for x in some_list if some_list.count(x) > 1])
# print(duplicate)

# 交集

# valid = set(["yellow", "red", "green", "blue", "black"])
# input_set = set(["red", "brown"])
# print(input_set.intersection(valid))


# 差集

valid = set(["yellow", "red", "green", "blue", "black"])
input_set = set(["red", "brown"])
print(input_set.difference(valid))
