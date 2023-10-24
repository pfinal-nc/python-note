# -*- coding: utf-8 -*-
# @Time    : 2023/10/24 11:20
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 魔法函数.py
# @Software: PyCharm

# python 定义类时中 以双下划线开头，以双下划线结尾函数为魔法函数
# 魔法函数可以定义类的特性
# 魔法函数时解释器提供的功能
# 魔法函数只能使用 python 提供的魔法函数,不能自定义

class Company:
    """Company"""

    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, index):
        return self.employee[index]


company = Company(['alex', 'linda', 'catherine', 'pfinal'])
employee = company.employee

for item in employee:
    print(item)

# for 首先去找 __iter__ 没有时优化去找 __getitem__
for item in company:
    print(item)
