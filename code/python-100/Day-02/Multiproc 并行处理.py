# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 18:05
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : Multiproc 并行处理.py
# @Software: PyCharm
import time


def square(num):
    time.sleep(1)  # 模拟耗时的计算操作
    return num ** 2


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 普通的for 循环
    start_time = time.time()
    results = []
    for num in numbers:
        results.append(square(num))
