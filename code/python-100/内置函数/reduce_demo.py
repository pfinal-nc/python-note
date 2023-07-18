# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 14:03
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : reduce_demo.py
# @Software: PyCharm
from functools import reduce


# reduce 函数接受的参数和 map() 类似, 一个函数 f  一个 list 但行为 和 map 不同，reduce 传入的函数 f 必须接收两个参数, reduce() 对 list 的每个元素反复调用函数f，并返回最终结果值。
# reduce() 还可以接收第 3 个可选参数，作为计算的初始值。如果把初始值设为 100
def prod(x, y):
    """prod"""
    return x * y


if __name__ == '__main__':
    print(reduce(prod, [2, 4, 5, 7, 12]))
    # 先计算 prod(2,4) 在计算前2个结果与第三个


