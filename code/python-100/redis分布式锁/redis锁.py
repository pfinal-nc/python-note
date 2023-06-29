# -*- encoding: utf-8 -*-
"""
@Filename :redis锁.py
@Description :
@Datatime :2023/06/05 09:51:47
@Author :PFinal南丞
@Email :lampxiezi@163.com
"""
import math
import time
import uuid

from redis.exceptions import WatchError


def acquire_lock_with_timeout(conn, lock_name, acquire_timeout=3, lock_timeout=2):
    """
    基于redis分布式锁

    """
    identifier = str(uuid.uuid4())
    lockname = f'lock:{lock_name}'
    lock_time = int(math.ceil(lock_timeout))
    end = time.time() + acquire_timeout

    while time.time() < end:
        # 如果不存在这个规则加锁并设置过期时间,避免死锁
        if conn.setnx(lockname, identifier):
            conn.expire(lockname, lock_name)
            return identifier
        # 如果存在锁, 且这个锁没有过期时间则为其设置过期时间,避免死锁
        elif conn.ttl(lockname) == -1:
            conn.expire(lockname, lock_timeout)
        time.sleep(0.001)
    return False


# 加锁过程
# 1. 首先需要为锁生成一个唯一的标识, 这里使用 uuid
# 2. 然后使用 setnx 设置锁, 如果该锁名之前不存在其他客户端的锁则加锁成功, 接着设置锁的过期时间防止死锁并返回锁的唯一标示
# 3. 如果设置失败先判断一下锁名所在的锁是否有过期时间,因为 setnx 和 expire 两个命令执行不是原子性的, 可能会出现加锁成功但是设置超时时间失败出现死锁, 如果不存在就给锁重新设置过期时间,存在就不给锁重新设置过期时间,存在就不断循环知道加锁时间超时加锁失败


def release_lock(conn, lockname, identifier):
    """ 释放锁 """
    # python 中 redis 事务是通过pipeline 的封装实现的
    with conn.pipeline() as pipe:
        lockname = 'lock:' + lockname
        while True:
            try:
                # watch 锁, multi 后如果该 key 被其他客户端改变,
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

# 解锁过程
# 1. 首先整个解锁操作需要一个Redis 的事务中进行;
# 2. 使用 watch 监听锁, 防止解锁时出现删除其他人的锁;
# 3. 查询锁名所在的标识是否与本次解锁的标识相同
# 4. 人如果相同则在事务中删除这个锁, 如果删除过程中自动失效过期又被其他客户端拿到, 因为设置了 watch 就会删除失败,这样就不会出现删除了其他客户端锁的情况

