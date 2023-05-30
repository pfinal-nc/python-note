# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 16:11
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 09.py
# @Software: PyCharm
import time
from multiprocessing import Process


def task(name,n):
    print('task is running', name)
    time.sleep(n)
    print('task is over', name)


if __name__ == '__main__':
    # p1 = Process(target=task, kwargs={'name': 'jason123'})
    # p1.start() # 异步 告诉操作系统创建一个新的进程, 并在该进程中执行task函数
    # 进程join方法
    p1 = Process(target=task, args=('jason1', 1))
    p2 = Process(target=task, args=('jason1', 2))
    p3 = Process(target=task, args=('jason1', 3))
    start_time = time.time()
    p1.start()
    p1.join()
