# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 15:57
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : __set_name.py
# @Software: PyCharm
# __set_name__  用于在类定义时自动设置属性的名称 它是自数据描述符的定义中使用的
# 当定义一个数据描述符时, 通常是作为类中的一个属性来定义的 而属性名称就是描述符的名称 在类定义中使用 描述符时, python 会自动调用描述符的 __set__nmae__ 方法, 并将属性名作为参数传递进去
class MyDescriptor:
    def __set_name__(self, owner, name):
        print(owner, name)
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value


class MyClass:
    x = MyDescriptor()


if __name__ == '__main__':
    MyClass()
