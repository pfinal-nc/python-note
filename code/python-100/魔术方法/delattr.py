# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 14:59
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : delattr.py
# @Software: PyCharm
# __delattr__ 用于删除对象属性时被调用

class Example:
    """
    Example
    """

    def __init__(self, ):
        """
        Example的初始化函数
        """
        self.value = 42

    def __delattr__(self, name):
        if name == 'value':
            del self.__dict__[name]
        else:
            raise AttributeError(f"cannot delete attribute '{name}'")


if __name__ == '__main__':
    ex = Example()
    del ex.value
    print(ex.__dict__)
    del ex.other

# 在这示例中定义了一个 example 它有一个 value 属性,在 __delattr__ 方法中, 受限检查要删除的属性名称是否是 value
# 如果是 直接删除该属性, 抛出一个 attributeeroor 异常 表示不能删除该属性, 实现了对 value属性的访问控制 如果在 __delattr__ 方法中又删除了其他属性, 就会再次调用 __delattr__
# 从而导致 递归调用, 为了避免这个调用,通常在 __delattr__ 方法中使用 del self.__dict__[name]

