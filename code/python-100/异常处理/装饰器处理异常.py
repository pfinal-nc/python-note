# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 16:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 装饰器处理异常.py
# @Software: PyCharm
from functools import wraps
from typing import Dict, Any, Callable


class TryMe:
    def __init__(self):
        self.exception_: Dict[Any, Callable] = {}

    def try_(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                handler = None
                for c in self.exception_.keys():
                    if isinstance(e, c):
                        handler = c

                if handler is None:
                    raise e
                # 将异常发生的函数和异常对象传入异常处理函数
                return self.exception_[handler](func, e)

        return wrapper

    def except_(self, *exceptions):
        def decorator(f):
            for e in exceptions:
                self.exception_[e] = f
            return f

        return decorator


tryme = TryMe()


@tryme.try_
def my_function():
    print(1 / 0)
    print('hello world')


@tryme.try_
def my_function2():
    print(1 / 0)
    print('hello world')


@tryme.except_(ZeroDivisionError)
def handle_zero_division_error(func, e):
    print(func.__name__, str(e))


if __name__ == '__main__':
    my_function()
    my_function2()
