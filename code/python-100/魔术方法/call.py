# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 10:43
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : call.py
# @Software: PyCharm

# 在python 中 通过 class 关键字定义一个新的类时, Python 解释器会自动调用元类来实例化类对象 元类在实例对象时，python会自动调用这个实例对象的__call__ 方法
# 通过在类的 __call__() 方法中间接调用类的 __new__() 方法和 __init__() 方法，可以实现单例模式。具体而言，每次调用类的实例对象时，都会先检查已经创建的实例对象是否存在，如果存在则直接返回该实例对象，如果不存在则通过调用 __new__() 方法和 __init__() 方法来创建一个新的实例对象，并将其存储下来。由于每次都返回同一个实例对象，因此实现了单例模式。

class SingletonType(type):
    """Singleton type"""
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class MyClass(metaclass=SingletonType):
    """MyClass type"""
    pass


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(a is b)
