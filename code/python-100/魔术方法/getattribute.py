# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 14:18
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : getattribute.py
# @Software: PyCharm
# __getattribute__ 是 Python 中的一个特殊方法，用于在访问对象属性时被调用。当我们使用点号（.）或 getattr() 函数来访问一个对象的属性时，Python 会调用该对象的 __getattribute__ 方法来获取属性的值

class Exaample:
    """Example class"""

    def __init__(self):
        self.data = {'a': 1, 'b': 2, 'c': 3}

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            if name in self.data:
                return self.data[name]
            else:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
