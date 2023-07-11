# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 11:10
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : format.py
# @Software: PyCharm

# __format__ 方法是python中用于格式化对象输出的特殊方法, 它可以让我们在使用字符串格式化方法(str.format() f-string)等

# __format__ 方法有两个参数 分别为格式字符串和格式参数. 格式字符串用于指定输出格式, 格式参数则是输出的参数值 其中,格式字符串是一个包含格式说明符的字符串可以使用大括号{}来指定要输出的参数，并在大括号中使用冒号:来指定参数的格式。

class Point:
    """Point object"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __format__(self, format_spec):
        if format_spec == 'r':
            return f"({self.y},{self.x})"
        else:
            return f"({self.x},{self.y})"


p = Point(1, 2)
print("Formatted point: {:r}".format(p))
