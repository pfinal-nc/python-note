#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import itertools

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
user_input = "This\nstring has\tsome whitespaces...\r\n"


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

character_map = {
    ord('\n'): ' ',
    ord('\t'): ' ',
    ord('\r'): None
}

# 迭代器切片
# 如果对迭代器进行切片操作, 会返回一个TypeError 提示生成器对象没有下标

if __name__ == '__main__':
    # a()
    # print(count)
    # print(user_input.translate(character_map))
    s = itertools.islice(range(50), 10, 20)
    for val in s:
        print(val)
    # 可以使用「itertools.islice」创建一个「islice」对象，该对象是一个迭代器，可以产生我们想要的项。但需要注意的是，该操作要使用切片之前的所有生成器项，以及「islice」对象中的所有项。
