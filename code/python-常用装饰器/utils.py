# -*- coding: utf-8 -*-
# @Time    : 2023/8/4 14:23
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : utils.py
# @Software: PyCharm
import time
import warnings

from matplotlib import pyplot as plt


def timer(func):
    """timer"""

    def wrapper(*args, **kwargs):
        """wrapper"""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result

    return wrapper


def memoize(func):
    """memoize"""
    cache = {}

    def wrapper(*args):
        """"wrapper"""
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


def validate_input(func):
    """数据验证"""

    def wrapper(*args, **kwargs):
        """wrapper"""
        # TODO valid_status  做参数验证
        valid_status = True
        if valid_status:
            return func(*args, **kwargs)
        else:
            raise ValueError("Invalid data. Please check your inputs.")

    return wrapper


def log_results(func):
    """日志输出"""

    def wrapper(*args, **kwargs):
        """ wrapper"""
        result = func(*args, **kwargs)
        with open("./results.log", "a") as log_file:
            log_file.write(f"{func.__name__} - Result: {result}\n")
        return result

    return wrapper


def suppress_errors(func):
    """ 优雅的错误处理 """

    def wrapper(*args, **kwargs):
        """ wrapper"""
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            return None

    return wrapper


def validate_output(func):
    """ 过滤返回结果 """

    def wrapper(*args, **kwargs):
        """ wrapper """
        result = func(*args, **kwargs)
        if validate_output(result):
            return result
        else:
            raise ValueError("Invalid output. Please check your function logic.")

    return wrapper


def visualize_results(func):
    """ 输出格式化 """

    def wrapper(*args, **kwargs):
        """ wrapper """
        result = func(*args, **kwargs)
        plt.figure()  # 自动生成漂亮的可视化结果
        # Your visualization code here
        plt.show()
        return result

    return wrapper


def debug(func):
    """debug """

    def wrapper(*args, **kwargs):
        """ wrapper """
        print(f"Debugging {func.__name__} - args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


def deprecated(func):
    """ deprecated 处理废弃的函数  """

    def wrapper(*args, **kwargs):
        """ wrapper """
        warnings.warn(f"{func.__name__} is deprecated and will be removed in future versions.", DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper



