# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 14:08
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 枚举.py
# @Software: PyCharm

# 枚举 是python内置函数, 用处很难再简单的一行中说明
# for counter, value in enumerate(some_list):
#      print(counter, value)

# enumerate 也接受一些可选参数, 这使它更有用
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

counter_list = list(enumerate(my_list, 1))
print(counter_list)