# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 18:18
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : python_magic_methods.py
# @Software: PyCharm

#  定义一个能够自动比较打啊熊的People 类
class People(object):
    """ People """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        return

    def __str__(self):
        return self.name + ":" + str(self.age)
