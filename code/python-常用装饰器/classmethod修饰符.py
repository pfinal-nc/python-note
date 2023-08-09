# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 18:09
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : classmethod修饰符.py
# @Software: PyCharm

# class test_classmoethod(object):
#     @classmethod
#     def printd(cls, a, b): # classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，
#         """ printd """
#         c = a + b
#         print(c)
#
#
# if __name__ == '__main__':
#     # c = test_classmoethod()  # 不想做实例化这一步，可以在 def printd(self,a ,b)上面加上@classmethod，
#     # c.printd(3, 5)
#     test_classmoethod.printd(3, 5)

class A(object):
    """A"""
    a = 1

    def def1(self):
        """def1"""
        print('def1')

    @classmethod
    def def2(cls):
        print('def2')
        print(cls.a)
        cls().def1()
