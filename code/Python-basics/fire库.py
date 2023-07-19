# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 16:32
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : fire库.py
# @Software: PyCharm
import fire
import requests


# Fire 优化cli 运行 python
def hello(name='World'):
    """hello """
    return "Hello %s!" % name


# 类的支持 当 fire 这个库不仅仅支持给 方法添加命令行的支持, 还支持给一个类添加命令行的支持

class Calculator(object):
    """calculates"""

    def double(self, number):
        """double"""
        return 2 * number


def scrape(url, timeout=10):
    response = requests.get(url, timeout=timeout)
    print(response.text)


if __name__ == '__main__':
    # fire.Fire(hello)
    # fire.Fire(Calculator)
    fire.Fire(scrape)
