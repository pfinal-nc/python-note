# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 18:00
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 14.py
# @Software: PyCharm
import os
import time
from multiprocessing import current_process, Process


# 子进程的任务
def func(name):
    print(f'{name} start')
    time.sleep(2)
    print(f'func {current_process().pid}，current——process获取进程号')
    print(f'func {os.getpid()}，OS获取进程号')
    print(f'{name} end')


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):  # start 会自动调用run
        func(self.name)


if __name__ == '__main__':
    p = MyProcess('zhuang')
    p.start()  # p.run()只有通过start开启的才是子进程，通过run开启的不是子进程
    print('主进程结束')
