# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 16:38
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : merry_example.py
# @Software: PyCharm
from merry import Merry

merry = Merry()
merry.logger.disabled = True


# _try 装饰器监听异常
@merry._try
def example(num1, num2, path):
    result = num1 / num2
    with open(path, 'r') as file:
        file.read()


# _except 异常处理
@merry._except(ZeroDivisionError)
def process_zero_division_error(e):
    print('zero_division_error', e)


@merry._except(TypeError)
def process_type_error(e):
    print("type_error", e)


@merry._except(FileNotFoundError)
def process_file_not_found_error(e):
    print('file_not_found_error', e)


@merry._except(Exception)
def process_exception(e):
    print('exception', type(e), e)


if __name__ == '__main__':
    example(1, 0, 'test.txt')
    example(1, 'a', 'test.txt')
    example(1, 2, 'test.txt')