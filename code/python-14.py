# -*- coding: UTF-8 -*-

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