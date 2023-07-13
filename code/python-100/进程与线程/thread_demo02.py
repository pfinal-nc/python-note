# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 11:51
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : thread_demo02.py
# @Software: PyCharm
from threading import Lock, Thread
from time import sleep


class Account(object):
    """ Account """

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        """ deposit """
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally 中执行释放锁的操作保证正常异常锁都能释放锁
            self._lock.release()

    @property
    def balance(self):
        """ balance """
        return self._balance


class AddMoneyThread(Thread):
    """ add money thread """

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        """ run """
        self._account.deposit(self._money)


def main():
    """" main """
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()


# 在Python语言中，单线程+异步I/O的编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。协程最大的优势就是极高的执行效率，因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销。协程的第二个优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不用加锁，只需要判断状态就好了，所以执行效率比多线程高很多。