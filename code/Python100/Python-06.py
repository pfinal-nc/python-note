# -*- coding: UTF-8 -*-

# 题目：斐波那契数列。

# 方法一

def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b =b,a+b
    return a
print(fib(10))

def fibB(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs=[1,1]
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print(fibB(10))