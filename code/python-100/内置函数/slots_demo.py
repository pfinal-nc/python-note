# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 15:53
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : slots_demo.py
# @Software: PyCharm

# 正常情况下, 定义了一个 class  创建一个 class的实例后, 可以给该实例 绑定任何属性 和方法
class Student(object):
    """student"""
    __slots__ = ('name', 'age')  # 用 tuple 定义允许绑定的属性名称
    pass


def set_score(self, score):
    self.score = score


Student.set_score = set_score  # 给对象绑定一个方法

if __name__ == '__main__':
    s = Student()
    # s.name = 'Michael'  # 动态给实例绑定一个属性
    # print(s.name)
    # s.set_score(1000)
    # print(s.score)
    s.name = 'PFinal'  # 绑定属性'name'
    s.age = 25  # 绑定属性 'age'
    # s.score = 99  限定了 2个  如果多绑定就会报错

