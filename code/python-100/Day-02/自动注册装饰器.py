# -*- coding: utf-8 -*-
# @Time    : 2023/8/3 09:49
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 自动注册装饰器.py
# @Software: PyCharm

# 这个装饰器会在装饰函数时自动将函数添加到一个列表或字典中, 这样就可以在程序的其他地方访问到这个列表或字典,知道有哪些函数被装饰过
def register_decorator(func_list: list) -> object:
    """ register decor
    @rtype: object
    """

    def decorator(func):
        """ decorator function"""
        func_list.append(func)
        return func

    return decorator


# 自动注册函数
registered_functions = []


@register_decorator(registered_functions)
def foo() -> None:
    """foo function"""
    pass


@register_decorator(registered_functions)
def bar() -> None:
    """baa  function"""
    pass


print(registered_functions)
