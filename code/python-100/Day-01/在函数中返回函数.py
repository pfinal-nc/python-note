# -*- coding: utf-8 -*-
# @Time    : 2023/10/24 16:48
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 在函数中返回函数.py
# @Software: PyCharm

# 从函数中返回函数

# def hi(name="pfinal"):
#     """hi"""
#
#     def greet():
#         """greet"""
#         return "now you are in greet() function"
#
#     def welcome():
#         """welcome"""
#         return "now you are in welcome() function"
#
#     if name == "pfinal":
#         return greet
#     else:
#         return welcome


#
# a = hi()
# print(a)
#
# print(hi()())

#  将函数作为参数传给另一个函数

def hi():
    """hi"""
    return "hi pfinalclub"


def doSomethingBeforeHi(func):
    """ do something before"""
    print("do something before")
    print(func())


doSomethingBeforeHi(hi)