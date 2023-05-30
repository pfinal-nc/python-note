# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 15:49
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 08.py
# @Software: PyCharm
import threading


def print_numbers():
    for i in range(10):
        print(i)


def print_letters():
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        print(letter)


# 创建线程
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# 启动线程
t1.start()
t2.start()

# 等待线程结束
t1.join()
t2.join()
