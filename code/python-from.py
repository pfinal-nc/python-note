# -*- coding: UTF-8 -*-

import math

print(math.pi)

from math import pi
print(pi)

from math import *

print(pi)
print(cos(pi))

print('==========================')

'''
count() 方法 统计 对象中的字符串出现的次数

'''
print(['a','iplaypython.com','c','b','a'].count('a'))

# 字典

x = {'title':'python web site','url':'www.iplaypy.com'}
print(x.items())
print(x.iteritems())
print(list(x.iteritems()))