# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 16:08
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : property_demo.py
# @Software: PyCharm

# Python内置的@property装饰器就是负责把一个方法变成属性调用的

# class Student(object):
#     """ Student """
#     _score: int
####################################################################################################
# @property
# def score(self):
#     """ Score"""
#     return self._score
#
# @score.setter
# def score(self, value):
#     if not isinstance(value, int):
#         raise ValueError('score must be an integer!')
#     if value < 0 or value > 100:
#         raise ValueError('score must between 0 and 100')
#     self._score = value


# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
####################################################################################################

# @property 定义只读属性

class Student(object):
    """Student object"""

    @property
    def birth(self):
        """birth"""
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth




if __name__ == '__main__':
# s = Student()
# s.score = 60  # OK 实际转化为 s.set_score(60)
# print(s.score)
#
# s.score = 99999
# print(s.score)
