#!/usr/bin/python3
# 文件名: using_sys.py

import sys


# print('命令行参数如下:')
# for i in sys.argv:
#   print(i)

# print('\n\nPython 路径为：', sys.path, '\n');

def power(x,n):
	s = 1;
	while n>0:
		n = n-1;
		s = s*x;
	return s;

print(power(5,2));

# 函数的默认参数
def enroll(name,gender,age=6,city='上海'):
	print('name:',name);
	print('gender',gender);
	print('age',age);
	print('city',city);
# 给默认参数
enroll('大爷','得的')
# 给默认参数传递新的值
enroll('大爷','得的',10)
# 给后一个默认参数赋值
enroll('大爷','得的',city='我了个去')

def add_end(L=[]):
    L.append('END')
    for i in L:
        print(i)
    return L

print(add_end([1]));


# 可变参数的函数

def calc(numbers):
    sum=0
    for n in numbers:
        sum = sum + n * n
    return sum

total = calc([1,2,3,4])
total1 = calc((1,2,3,4))
print(total)
print(total1)

# 可变参数的函数

def calc_a(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 因为参数 是 *numbers 所以 可以传递任何参数
total_01 = calc_a(1,2,3);
total_02 = calc_a();
print(total_01)
print(total_02)


