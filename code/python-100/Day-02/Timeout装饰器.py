# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 17:28
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : Timeout装饰器.py
# @Software: PyCharm


import functools  # 下面会用到的两个库
import signal


class TimeoutError(Exception): pass  # 定义一个Exception，后面超时抛出


def timeout(seconds, error_message='Function call timed out'):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorated


@timeout(5)  # 限定下面的slowfunc函数如果在5s内不返回就强制抛TimeoutError Exception结束
def slowfunc(sleep_time):
    import time
    time.sleep(sleep_time)  # 这个函数就是休眠sleep_time秒


slowfunc(10)
