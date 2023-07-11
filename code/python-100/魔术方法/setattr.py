# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 14:27
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : setattr.py
# @Software: PyCharm

# __setattr__ 方法是 python 中的一个特殊方法, 用于设置对象属性时被调用, 当使用赋值语句或setattr() 函数来设置一个对象的属性时, python 会调用该对象的 _setattr__ 方法来进行赋值操作

class Example:
    """Example class"""

    def __setattr__(self, name, value):
        if name == 'value':
            self.__dict__[name] = value
        else:
            raise AttributeError(f"cannot set attribute '{name}'")


if __name__ == '__main__':
    ex = Example()
    ex.value = 42
    print(ex.value)
