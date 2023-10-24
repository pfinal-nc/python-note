# -*- coding: utf-8 -*-
# @Time    : 2023/10/24 14:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 生成器.py
# @Software: PyCharm

# 生成器也是一种迭代器, 但是整你对其迭代一次. 因为他们并没有把所有的值存在内存中,
# python 中只要它定义了可以返回一个 迭代器的 __iter__方法 或者定义了可以支持下标索引的 __getitem__方方 那么它就是一个可迭代对象。

def generator_function():
    """generator"""
    for i in range(10):
        yield i


# 计算斐波那契数列
def fibon(n):
    """fibon function"""
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def generator_function():
    for i in range(3):
        yield i


if __name__ == '__main__':
    # print(generator_function())
    # for item in generator_function():
    #     print(item)

    # for x in fibon(10):
    #     print(x)
    gen = generator_function()

    print(next(gen))
    print(next(gen))
    print(next(gen))
