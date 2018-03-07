# -*- coding: UTF-8 -*-

class Student(object):
    def __init__(self,name,obj):
        self.name = name
        self.obj = obj

    def get_grade(self):
        if self.obj.score >=90:
            return 'A';
        elif self.obj.score >= 80:
            return 'B';
        else:
            return 'C';

class Score(object):
    def __init__(self,args):
        self.score = args

lisa = Student('Lisa',Score(85))
print(lisa.name,lisa.get_grade())

'''
私有属性的访问
'''

class  Private(object):
    def __init__(self,name,size):
        self.__name = name
        self.__size = size

mode = Private('大爷',22)
print(mode.__name);