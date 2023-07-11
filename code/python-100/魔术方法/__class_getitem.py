# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 16:40
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : __class_getitem.py
# @Software: PyCharm
# __claass_getitem 魔术方法
# _class_getitem 用于在定义泛型类型时实现类型参数的协变或逆变 它是用于类型中的类方法或静态方法的
from typing import List


class A:
    def __class_getitem__(cls, item):
        print(item)
        return "abc"


print(A[0])


class MyGeneric:
    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @staticmethod
    def identity(x):
        return x

    def __class_getitem__(cls, params):
        T, = params

        class NewGeneric(cls):
            @classmethod
            def from_iterable(cls, iterable):
                return cls(*(T(x) for x in iterable))

            @staticmethod
            def identity(x):
                return T(x)

        return NewGeneric


if __name__ == '__main__':
    int_arr_type = List[int]  # type hint就是基于__class_getitem__实现的
    list1: int_arr_type = [1]
    list2: int_arr_type = []
