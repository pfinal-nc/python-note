# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 17:22
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : __mro_entries.py
# @Software: PyCharm

# __mro_entries__ 类属性应该是一个元组，每个元素都是一个类。这些类将按照元组的顺序排列，并添加到当前类的 MRO 中。
class MyMeta:
    def __mro_entries__(self, bases):
        return (dict,)


class MyClass(MyMeta()):
    pass


print(issubclass(MyClass, MyMeta))
print(MyClass.__mro__)