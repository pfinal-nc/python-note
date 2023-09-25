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
    # s = itertools.islice(range(50), 10, 20)
    # for val in s:
    #     print(val)
    # 可以使用「itertools.islice」创建一个「islice」对象，该对象是一个迭代器，可以产生我们想要的项。但需要注意的是，该操作要使用切片之前的所有生成器项，以及「islice」对象中的所有项。

    # 跳过可迭代对象的开头
    # 有时你要处理一些不需要的行开头的文件. itertools 再次提供了一种简单的解决方案:
    string_from_file = """
    // Author: ...
// License: ...
//
// Date: ...
Actual content...

    """
    # 这段代码只打印初始注释部分之后的内容,如果我们只想舍弃可迭代对象的开头部分
    for line in itertools.dropwhile(lambda line: line.startswith('//'), string_from_file.split("\n")):
        print(line)

    # 只包含关键字参数的函数
    # 当我们使用下面的函数时, 创建仅仅需要关键字参数作为输入的函数来提供更清晰的函数定义，会很有帮助：
    # def test(*, a, b):
    #     pass
    #
    #
    # test("value for a", "value for b")
    # test(a="value", b="value 2")  # Works

    # 创建支持 with 语句的对象
    # 可以使用「__enter__」和「__exit__」来实现上下文管理协议:
