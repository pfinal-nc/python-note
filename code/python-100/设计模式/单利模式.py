# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 17:06
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 单利模式.py
# @Software: PyCharm
import threading


# 单利模式该模式的主要目的是确保某一个类只有一个实例存在。
# 实现单例模式的几种方式
# 1. 使用模块
# 其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码

# from mysingleton import singleton

# print(singleton.foo())  # singleton 这个对象即是单例模式的对象


# 2. 使用装饰器

# def Singleton(cls):
#     """ Singleton """
#     _instance = {}
#
#     def _singleton(*args, **kwargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kwargs)
#         return _instance[cls]
#
#     return _singleton
#
#
# @Singleton
# class A(object):
#     a = 1
#
#     def __init__(self, x=0):
#         self.x = x
#
#
# a1 = A(2)
# a2 = A(3)
# print(a1.x, a2.x)

# 3. 基于 __new__
# 当实例化一个对象时, 是先执行了类的 __new__ 方法, 实例化对象, 然后再执行类的 __init__方法, 对这个对象进行初始化 可以基于这个实现单例模式

class Singleton(object):
    """ Singleton """
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
            return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)


def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
