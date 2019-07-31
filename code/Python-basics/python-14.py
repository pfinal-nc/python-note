# -*- coding: UTF-8 -*-
import types
import os
from collections import Iterable


class Student(object):
    def __init__(self,score):
        self.__score = score

    def get_private_attr(self):
        return self.__score

    def set_private_attr(self,score):
        self.__score = score

lisa = Student(95)
lisa.set_private_attr(23)
print(lisa.get_private_attr())

print('=======================');
'''

类的继承和多态

'''

class Animal(object):
    def run(self):
        print('这个是啥!跑去来了')

# 这两个类继承了动物类
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog();
print(dog.run())

# 判断是一个类总的方法

print(isinstance(dog,Animal))

print('==============')

# 获取对象类型

print(type(123))

# 判断是否是整型
print(type(123)==types.IntType)

print('-----------------------------')
# dir() 获取一个对象的属性和方法
print(dir('ABC'))
print(dir(dog))
print('ABC'.__len__())
print('ABC'.lower())

print('-------------------------------')

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:1])

for i in L:
    print(i)

d = {'a': 1, 'b': 2, 'c': 3}

for j in d:
    print(j)

print('-------------------------------------------')
# 判断是否是可迭代的对象

print(isinstance('abc',Iterable))

print(list(range(1,11)))

# 列表生成
print([x*x for x in range(1,11)])

# 使用两层循环 可以生成全排列:
print([ m + n  for m in 'ABC' for n in 'XYZ']);

# 显示当前目录的文件
print([d for d in os.listdir('.')])

L = ['Hello', 'World', 18, 'Apple']
print( [s.lower()  for s in L if isinstance(s, str)==True])

