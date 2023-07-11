# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 15:52
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : subclass.py
# @Software: PyCharm
# __init_subclass__ 方法定义在父类中, 用于自定义子类的创建过程,可以控制子类的行为

class Base:
    def __init_subclass__(cls, **kwargs):
        cls.x = {}
        cls.name = kwargs.get("name")


class A(Base, name="Jack"):
    pass


print(A.x)
print(A.name)
