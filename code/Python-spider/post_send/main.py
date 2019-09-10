# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pfinal'
__mtime__ = '2019/9/9'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from send import send
import multiprocessing as mp
from multiprocessing import Pool
import time


def run_send(name):
    print('开始进程 %s...\n' % name)
    res = send.send_message()
    print(res)


if __name__ == '__main__':
    mp_list = Pool(4)
    for i in range(10000):
        mp_list.apply_async(run_send, args=(i,))
    print("-- start --\n")
    mp_list.close()
    mp_list.join()
#
