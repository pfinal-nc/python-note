# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 11:15
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 线程池.py
# @Software: PyCharm
import time
from concurrent.futures import ThreadPoolExecutor


def spider(page):
    """ spider """
    time.sleep(page)
    print(f"crawle task{page} finished")
    return page


with ThreadPoolExecutor(max_workers=5) as t:  # 创建一个最大
    task1 = t.submit(spider, 1)
    task2 = t.submit(spider, 2)  # 通过submit提交执行的函数到线程池中
    task3 = t.submit(spider, 3)

    print(f"task1: {task1.done()}")  # 通过 done 来判断线程是否完成
    print(f"task2: {task2.done()}")
    print(f"task3: {task3.done()}")

    time.sleep(2.5)
    print(f"task1: {task1.done()}")
    print(f"task2: {task2.done()}")
    print(f"task3: {task3.done()}")

    print(task1.result())  # 通过 result 来获取返回值

# 1. 使用 with 语句, 通过 ThreadPoolExecutor 构造实例, 同时传入 max_workers 参数来设置现场池中最多能同时运行的线程数目
# 2. 使用 submit 函数 来提交线程需要执行的任务到线程池中，并返回该任务的句柄（类似于文件、画图），注意 submit() 不是阻塞的，而是立即返回。
# 3. 通过使用 done() 方法判断该任务是否结束。
