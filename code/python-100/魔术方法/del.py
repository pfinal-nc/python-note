# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 10:53
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : del.py
# @Software: PyCharm

# __del__() 是 delete的缩写,这是析构魔术方法。当一块空间没有了任何引用时 默认执行
# __del__ 回收这个类地址
# 注意：程序自动调用__del__()方法，不需要我们手动调用

class A:
    """A class that"""

    def __del__(self):
        print("__del__")


if __name__ == '__main__':
    o = A()
    x = o
    del o
# __del__和关键字del是没有关系的 del是Python的一个关键字，用于删除变量或对象的引用。
# __del__()方法是一个特殊方法，用于在对象被销毁时执行一些清理任务。
