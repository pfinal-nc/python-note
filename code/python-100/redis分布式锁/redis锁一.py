# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 11:36
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : redis锁一.py
# @Software: PyCharm
import math
import time
import uuid

from redis.exceptions import WatchError


# 如果 redis 大于 2.6版本,加锁的过程可以进行简化


def acquire_lock_with_timeout(conn, lock_name, acquire_timeout=3, lock_timeout=2):
    """ 基于 redis 实现的分布式锁 """
    identifier = str(uuid.uuid4())
    lockname = f'lock:{lock_name}'
    lock_timeout = int(math.ceil(lock_timeout))
    end = time.time() + acquire_timeout

    while time.time() < end:
        # 如果不存在这个锁则加锁并设置过期时间，避免死锁
        if conn.set(lockname, identifier, ex=lock_timeout, nx=True):
            return identifier

        time.sleep(0.001)

    return False


def release_lock(conn, lockname, identifier):
    """ 释放锁 """
    # python 中 redis 事务是通过pipline 的封装实现的
    with conn.pipeline() as pipe:
        lockname = 'lock:' + lockname
        while True:
            try:
                # watch 锁, multi 后如果该 key 被其他客户端改变, 事务操作会抛出 WatchError 异常
                pipe.watch(lockname)
                iden = pipe.get(lockname)
                if iden and iden.decode('utf-8') == identifier:
                    # 事务开始
                    pipe.multi()
                    pipe.delete(lockname)
                    pipe.execute()
                    return True
                pipe.unwatch()
                break
            except WatchError:
                pass
        return False
