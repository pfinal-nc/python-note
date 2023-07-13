# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 11:32
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : thread_demo.py
# @Software: PyCharm
from random import randint
from threading import Thread
from time import sleep, time


def download(filename):
    """ download """
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    """ main """
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()
