# -*- coding: utf-8 -*-
# @Time    : 2023/3/13 09:54
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : property.py
# @Software: PyCharm


class Exam(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        self._score = value


obj = Exam(60)
obj.score = 200
print(obj.score)