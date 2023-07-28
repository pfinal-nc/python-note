# -*- coding: utf-8 -*-
# @Time    : 2023/7/28 15:45
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : therading_lock.py
# @Software: PyCharm
import random
import threading
import time

yangs = []
dao = threading.Lock()


def kill_yang(yang):
    """kill_yang """
    with dao:
        time.sleep(random.randint(1, 10))
        yangs.append(yang)
        print(yangs)
        return yangs


def kill():
    """kill"""
    # 定义10个人 按顺序割羊
    for i in range(0, 10):
        th = threading.Thread(target=kill_yang, args=(i + 1,))
        th.start()


if __name__ == '__main__':
    kill()
