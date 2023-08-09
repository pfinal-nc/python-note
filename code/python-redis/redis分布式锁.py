# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 15:24
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : redis分布式锁.py
# @Software: PyCharm
import logging
import time

import redis

logger = logging.getLogger('service.redis_lock')

CONN = redis.Redis(host='localhost', port=6379, db=0)


def acquire_lock(lockname, identifier, wait_time=20, timeout=15):
    """ acquire lock"""
    end = time.time() + wait_time
    while end > time.time():
        if CONN.setnx(lockname, identifier):
            CONN.expire(lockname, timeout)  # set expire time
            return identifier
        time.sleep(0.001)  # wait until the lock expired or release by some thread
    return False


def release_lock(lockname, identifier):
    """ release lock"""
    pipe = CONN.pipeline()
    try:
        # watch lock once lock has been changed, break this transaction
        pipe.watch(lockname)
        if pipe.get(lockname) == identifier:
            pipe.multi()
            pipe.delete(lockname)
            pipe.execute()
            return True
        pipe.unwatch()
    except redis.exceptions.WatchError as e:
        logger.error(e)
        return False
    except Exception as e:
        logger.error(e)
        return False
    return False


if __name__ == '__main__':
    print(release_lock('h', 'a'))
