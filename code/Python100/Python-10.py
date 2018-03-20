# -*- coding: UTF-8 -*-

# 判断101-200之间有多少个素数，并输出所有素数。
from math import sqrt
from sys import stdout

h = 0
leap = 1

for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print '%-4d' % m
        h += 1
        if h % 10 == 0:
            print ''
    leap = 1
print 'The total is %d' % h      

