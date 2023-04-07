# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 09:54
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : coroutine2.py
# @Software: PyCharm
import time

import time
import greenlet


# 任务1
def work1():
    for i in range(5):
        print("work1...")
        time.sleep(0.2)
        # 切换到协程2里面执行对应的任务
        g2.switch()


# 任务2
def work2():
    for i in range(5):
        print("work2...")
        time.sleep(0.2)
        # 切换到第一个协程执行对应的任务
        g1.switch()


if __name__ == '__main__':
    # 创建协程指定对应的任务
    g1 = greenlet.greenlet(work1)
    g2 = greenlet.greenlet(work2)

    # 切换到第一个协程执行对应的任务
    g1.switch()