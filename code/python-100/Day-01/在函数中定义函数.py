# -*- coding: utf-8 -*-
# @Time    : 2023/10/24 16:44
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 在函数中定义函数.py
# @Software: PyCharm

def hi(name="pfinal"):
    """hi"""
    print("now you are inside the hi() function")

    def greet():
        """greet"""
        return "now you are inside the greet() function"

    def welcome():
        """ welcome """
        return "now you are inside the welcome() function"

    print(greet())
    print(welcome())
    print("now you are inside the welcome() function")

hi()
