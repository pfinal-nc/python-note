# -*- coding: UTF-8 -*-

from types import MethodType

# 绑定属性

class Student(object):
    pass

s = Student()
s.name = '大爷的'
print(s.name)

# 绑定方法

def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age,s) # 给实例绑定一个方法
s.set_age(12)
print(s.age)

def set_score(self,score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
print(s.score)

# 绑定属性限制

class Demo(object):
    __slots__ = ('name','age') # 定义允许绑定的属性

D  = Demo()
D.name = '大爷得'
print(D.name)

# D.score = '么么么'
# print(D.score) # 没有允许的属性是绑定不了的


class DemoA(object):
    def __init__(self,name):
        self.name =  name
    
    def __str__(self):
        return 'name: %s' % self.name
    
print(DemoA('ABC'));

# 调用一个不存在的属性

class DemoB(object):
    def __init__(self,age):
        self.age = age
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        raise AttributeError('\'DemoB\':没有属性 \' %s\'' % attr)

DB = DemoB(23)
print(DB.age)
# print(DB.score1)

# 写一个链式调用

class Chain(object):
    def __init__(self,path=''):
        self._path = path

    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    
    def __str__(self):
        return self._path

print(Chain().status.user.timeline.list)