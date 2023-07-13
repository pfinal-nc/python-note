# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 11:01
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : process_thread.py
# @Software: PyCharm
from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    """ sub_task() """
    global counter
    while counter < 10:
        print(string, end=' ', flush=True)
        counter += 1
        sleep(0.01)


def main():
    """ main() """
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main()
