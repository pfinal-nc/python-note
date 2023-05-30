# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 11:36
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 04.py
# @Software: PyCharm
import time
from threading import Thread


# threading 库可以再单独的线程中 执行任何的在pyton中可以调用的对象, Thread 对象并将要执行的对象以 target参数的形式提供给对象

# threading 库可以在单独的线程中执行任何的在 Python 中可以调用的对象。可以创建一个 Thread 对象并将执行的对象以target参数形式提供给该对象
# Python中的线程会在一个单独的系统级线程中执行（比如说一个 POSIX 线程或者一个 Windows 线程），这些线程将由操作系统来全权管理
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# t = Thread(target=countdown, args=(10,))
# t.start()
# 对于需要长时间运行的线程或者需要一直运行的后台任务,  使用后台线程,后台线程无法等待，不过，这些线程会在主线程终止时自动销毁。
t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
