# -*- coding: utf-8 -*-
# @Time    : 2023/9/25 09:54
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 常用装饰器.py
# @Software: PyCharm

def memoize(func):
    """memoize 计算缓存"""
    cache = {}

    def wrapper(*args):
        """wrapper()"""
        if args in cache:
            return cache[args]
        restult = func(*args)
        cache[args] = restult
        return restult

    return wrapper


def validate_input(func):
    def wrapper(*args, **kwargs):
        # Your data validation logic here
        if valid_data:
            return func(*args, **kwargs)
        else:
            raise ValueError("Invalid data. Please check your inputs.")

    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
