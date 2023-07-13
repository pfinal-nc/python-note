# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 11:01
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : process_thread.py
# @Software: PyCharm
from multiprocessing import Process
from random import randint
from time import sleep, time


def download_task(filename):
    """ download a task"""
    print('开始下载 %s ...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s 下载完成! 耗费了 %d 秒' % (filename, time_to_download))


def main():
    """main"""
    # start = time()
    # download_task('Python从入门到住院.pdf')
    # download_task('Peking Hot.avi')
    # end = time()
    # print('总共耗费了%.2f秒.' % (end - start))
    # 启用多进程
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
