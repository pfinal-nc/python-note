# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 14:41
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 05.py
# @Software: PyCharm
# 线程的一个关键特性是每个线程都是独立运行不可预测。如果程序中的其他线程需要通过判断某个线程的状态来确定自己下一步的操作，这时线程同步问题就会变得非常棘手
import time
from threading import Event, Thread


def countdown(n, started_evt):
    print("countdown, starting")
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


started_evt = Event()

print("countdown")
t = Thread(target=countdown, args=(10, started_evt))
t.start()

started_evt.wait()
print("countdown is running")

# event 对象最好单次使用,就是说，创建一个event对象,让某个线程等待这个对象，一旦这个对象被设置为真，尽管可以通过 clear() 方法来重置 event 对象，但是很难确保安全地清理 event 对象并对它重新赋值。很可能会发生错过事件、死锁或者其他问题（特别是，你无法保证重置 event 对象的代码会在线程再次等待这个 event 对象之前执行）。如果一个线程需要不停地重复使用 event 对象，你最好使用 Condition 对象来代替。

