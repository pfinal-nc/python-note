# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 17:41
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : __isinstancecheck.py
# @Software: PyCharm
"""
__isinstancecheck__ 是一个特殊方法，用于自定义对象是否为某个类或其子类的实例。如果定义了这个方法，那么在使用 isinstance() 函数检查对象是否为某个类或其子类的实例时，会调用这个方法，返回值为 True 或 False。
__subclasscheck__ 是一个特殊方法，用于自定义对象是否为某个类的子类。如果定义了这个方法，那么在使用 issubclass() 函数检查对象是否为某个类的子类时，会调用这个方法，返回值为 True 或 False。

"""


class Meta(type):
    """Class Meta"""

    def __instancecheck__(self, instance):
        print("instance check")
        return True

    def __subclasscheck__(self, subclass):
        print("subclass check")
        if subclass is int:
            return True
        return False


class A(metaclass=Meta):
    pass


a = A()

print(isinstance(123, A))

print(issubclass(int, A))
