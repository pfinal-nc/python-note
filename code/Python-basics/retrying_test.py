# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 09:30
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : retrying_test.py
# @Software: PyCharm
import random

from retrying import retry


@retry
def do_something_retry():
    if random.randint(0, 10) > 1:
        print(f'this is a test!')
        raise IOError('raise exception!')
    else:
        return "Nice！"


print(do_something_retry())
