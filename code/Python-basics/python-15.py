# -*- coding: UTF-8 -*-
# 生成器
L = [x*x for x in range(10)]
print(L)

g= (x * x for x in range(10))
print(tuple(g))

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # yield b
        a,b = b,a + b
        n = n + 1 
    return 'done'
# 函数

def add(x,y,f):
    return f(x) + f(y)

print(add(10,-10,abs))

# map
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(r)

# 利用map 整型转字符串
print(map(str,[1,2,3,4,5,6,12]))

# reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s];

print(reduce(lambda x, y: x*y, map(char2num,'123')));

# filter 用来过滤

def is_odd(n):
   return n % 2 == 1
print(filter(is_odd,[10,70,80,1,35,23]))




