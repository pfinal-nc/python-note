# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 10:35
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : newAndinit.py
# @Software: PyCharm

#  __new__ 和 __init__
#  __new__是从一个class建立一个object的过程。 而__init__是有了这个object之后，给这个object初始化的过程

class A:
    """ A class"""

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print("__init__")


# 单例模式是指在整个应用程序中，某个类只能有一个实例存在，且该实例可以被任何模块访问到。这种模式的应用场景包括数据库连接池、日志对象等需要全局唯一性的对象。
# 单例模式 常用到 __new__
# super() 函数是用于调用父类(超类)的一个方法。
# super() 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
# 但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
class Singletoon:
    """简单的单利模式"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__':
    a = A()
