# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 15:14
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : dir.py
# @Software: PyCharm
# dir 返回对象的属性列表, 该方法返回的属性列表应该是对象的属性名称的迭代器

# 如果一个类灭有定义 __dir__ 方法 python会尝试调用对象的 __dict__ 属性 并返回其中所有的属性名称和方法名称

class Example:
    def __init__(self):
        self.value = 42

    def __dir__(self):
        return ['value', 'foo', 'bar']


if __name__ == '__main__':
    ex = Example()
    print(dir(ex))
