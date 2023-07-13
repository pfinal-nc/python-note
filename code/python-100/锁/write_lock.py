# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 09:46
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : write_lock.py
# @Software: PyCharm
# 在 python 中 原生是没有读写锁的
# 读写锁将资源拆分为读和写2种操作，读锁允许多个线程同时读取共享资源，提高并发性能。但是当需要修改共享资源的时候，只能允许一个线程修改该共享资源，并且在修改完毕前，不允许读请求，以便造成数据不一致。所以操作完毕后，开放读请求。
import threading
import time


class RWLock:
    """ RWLock """

    def __init__(self):
        # 定义写锁
        self.write = threading.Lock()
        self.Locked = False
        # 读锁个数计数
        self.readCount = 0
        # 读锁 ++
        self.readAdd = threading.Lock()

    # 读锁个数 +count
    def readCountFunc(self, count):
        """ readCount """
        self.readAdd.acquire()
        self.readCount += int(count)
        self.readAdd.release()

    # 写锁
    def writeLock(self):
        """ writeLock """
        self.Locked = True
        while True:
            if 0 == self.readCount:
                self.write.acquire()
                break

    # 释放写锁
    def writeUnlock(self):
        """ writeUnlock """
        self.write.release()
        self.Locked = False

    # 读锁
    def readLock(self):
        """ readLock """
        # 在 读的时候 要确保写没有锁
        while True:
            if self.Locked:
                continue
            else:
                self.readCountFunc(1)
                break

    # 释放读锁
    def readUnlock(self):
        """ readUnlock """
        self.readCountFunc(-1)


# 使用
testCounts = 100
rw = RWLock()


def reads():
    """ reads """
    rw.readLock()
    print("%s 在读锁状态下, 读取数据: testCounts:%s 函数睡眠3秒 " % (time.strftime("%H:%M:%S", time.localtime()), testCounts))
    time.sleep(3)
    rw.readUnlock()


def writes():
    """ waits for a test to"""
    rw.writeLock()
    global testCounts
    t = testCounts
    time.sleep(5)
    testCounts = t + 1
    print("%s 在读锁状态下, 读取数据: testCounts:%s 函数睡眠3秒 " % (time.strftime("%H:%M:%S", time.localtime()), testCounts))
    rw.writeUnlock()


def main():
    """ main """
    threads = []
    for i in range(3):
        t = threading.Thread(target=reads)
        t.start()
        threads.append(t)

    for i in range(3):
        t = threading.Thread(target=writes)
        t.start()
        threads.append(t)
    for i in range(3):
        t = threading.Thread(target=reads)
        t.start()
        threads.append(t)
    for i in threads:
        i.join()

    print("最终的值:" + str(testCounts))


if __name__ == '__main__':
    main()
