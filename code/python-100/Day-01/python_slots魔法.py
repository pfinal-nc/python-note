# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 09:47
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : python_slots魔法.py
# @Software: PyCharm

# 在Python中，每个类都有实例属性。默认情况下 python用一个字典来保存一个对象的实例属性 使用__slots__来告诉Python不要使用字典，而且只给一个固定集合的属性分配空间。

# class MyClass:
#     def __init__(self, name, identifier):
#         self.name = name
#         self.identifier = identifier
#         self.set_up()
#         ....

# class MyClass(object):
#     __solts__ = ['name', 'identifier']
#     def __init__(self, name, identifier):
#         self.name = name
#         self.identifier = identifier
#         self.set_up()
#         ....
# 内存减轻负担。通过这个技巧，有些人已经看到内存占用率几乎40%~50%的减少。
