#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

count = 1


def a():
    """a"""
    count: str = 'a函数里面'  # 如果不事先声明，那么函数b中的nonlocal就会报错

    def b():
        nonlocal count
        print(count)
        count = 2

    b()
    print(count)


# 第一行的额count 和 a() 函数中的count 是两个变量 而 a() 函数中的 count 变量只是在该函数内部起作用 因为它是一个局部变量。
# nonlocal 只能在封装函数中使用, 在外部函数先进行声明，这样在b()函数中的count与a()中的count是同一个变量。

if __name__ == '__main__':
    a()
    print(count)
