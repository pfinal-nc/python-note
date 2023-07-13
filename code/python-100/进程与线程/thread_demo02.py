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

