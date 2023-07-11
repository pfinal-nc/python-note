# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 11:00
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : repr str.py
# @Software: PyCharm

# __repr__ 和 __str__ 都是用于返回对象的字符串表示形式 但他们的用途不同.
# __repr__ 主要用于调试和开发 而 __str__ 则主要用于用户友好的输出

class Person:
    """Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name=%s, age=%s)" % (self.name, self.age)

    def __str__(self):
        return f"{self.name}({self.age})"


# __repr__返回一个类似于构造函数调用的字符串，用于显示对象的内部状态。而__str__则返回一个可读的字符串，用于显示对象的外部状态。

if __name__ == '__main__':
    person = Person("pfinal", 18)
    print(str(person))
    print(repr(person))
