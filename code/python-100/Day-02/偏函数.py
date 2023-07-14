# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 15:46
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 偏函数.py
# @Software: PyCharm
# 偏函数是固定一个函数的一些参数, 然后生产一个新的函数的行为, 偏函数的概念可以用简化函数的复杂性
from functools import partial


def multiple(x, y):
    return x * y


# 使用偏函数来创建一个新的函数，比如 double(x)，这个函数将 y 参数固定为 2：
# 使用 functools 模块中的 partial 函数来创建偏函数
double = partial(multiple, y=2)
print(double(3))


# partial 函数接受一个函数作为第一个参数, 然后接受任意数量的位置 参数或关键字参数

def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2)
print(square(3))


# 偏函数的应用场景
# 偏函数在许多应用场景中 ,在复杂爱应用中, 可能需要床架按一些特定的功能函数来处理特定的任务, 这些任务只是更大的任务的一部分. 通过使用偏函数,可以很容易地创建特定的函数
# 无需复制或修改现有的函数实现

def process_data(data, data_type):
    """process_data"""
    if data_type == 'text':
        return data.lower()
    elif data_type == 'number':
        return data * 2
    else:
        return str(data)


process_text_data = partial(process_data, data_type='text')
process_number_data = partial(process_data, data_type='number')

print(process_text_data('Hello World'))
print(process_number_data(5))
