# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 17:46
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 13.py
# @Software: PyCharm
"""
current_process().pid 可以获取当前进程的进程PID
os.getpid() 也可以获取当前进程的进程是PID
"""
import os
import time
from multiprocessing import current_process, Process


# 子进程的任务
def func(name):
    print(f'{name} start')
    time.sleep(2)
    print(f'func {current_process().pid}, current_process获取进程号')
    print(f'func {os.getpid()}, os 获取进程号')
    print(f'{name} end')


if __name__ == '__main__':
    #  创建子进程,
    p = Process(target=func, args=('zhuang',))
    # 开启进程
    p.start()
    # 执行当前文件就是主进程
    print(f'current_procecss获取进程号 {current_process().pid},主进程结束')
    print(f'os获取进程号{os.getpid()},主进程结束')
