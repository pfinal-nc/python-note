# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 13:52
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : all_demo.py
# @Software: PyCharm

# all 如果 iterable 的所有元素均为 True 或 iterable 为空 则返回 True
def all(iterable):
    """all(iterable)"""
    for element in iterable:
        if not element:
            return False
        return True


