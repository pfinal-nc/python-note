# -*- coding: utf-8 -*-
# @Time    : 2023/10/24 11:36
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : arg和kwargs.py
# @Software: PyCharm

# *args 和 **kwargs 主要用于函数定义,可以将不定数量的参数传递给一个函数
# 预先并不知道, 函数是使用者会传递多少个参数给你, 所以在这个场景下使用两个关键字 *args是用来发送一个非键值对的可变数量的参数列表

# def test_var_args(f_arg, *argv):
#     print("first normal arg:", f_arg)
#     for arg in argv:
#         print("another arg through *argv:", arg)
#
#
# test_var_args('yasoob', 'python', 'eggs', 'test')

# **kwargs 允许将不定长度的键值对, 作为参数传递给一个函数, 想要在一个函数里处理带名字的参数, 应该使用 **kwargs

def greet_me(**kwargs):
    """greet_me"""
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="yasoob")
