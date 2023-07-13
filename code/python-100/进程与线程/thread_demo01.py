# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 11:36
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : thread_demo01.py
# @Software: PyCharm
#  在直接使用 threading 模块的 Thread 类来创建线程,可以通过继承Thread 类的方式来创建 子弟ing一i的线程类, 然后再创建线程对象并启动线程
from random import randint
from threading import Thread
from time import sleep, time


class DownloadTask(Thread):
    """ DownloadTask """

    def __init__(self, filename=None):
        super().__init__()
        self._filename = filename

    def run(self):
        """run """
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s 下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    """ main """
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

# 因为多个线程可以共享进程的内存空间 因此要实现多个线程间的通信相对简单, 大家能想到的最直接的办法就是设置一个全局变量, 多个线程共享这个全局变量即可
# 但是当多个线程共享同一个变量的时候,很有可能产生不可控的结果从而导致程序失效甚至崩溃。如果一个资源被多个线程竞争使用，那么我们通常称之为“临界资源”，对“临界资源”的访问需要加上保护，否则资源会处于“混乱”的状态。
