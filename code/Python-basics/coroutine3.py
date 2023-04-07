# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 09:57
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : coroutine3.py
# @Software: PyCharm
import gevent as gevent


def work(n):
    for i in range(n):
        # 获取当前协程
        print(gevent.getcurrent(), i)
        gevent.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(work, 5)
    g2 = gevent.spawn(work, 5)
    g3 = gevent.spawn(work, 5)
    g1.join()
    g2.join()
    g3.join()
