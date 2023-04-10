# -*- coding: utf-8 -*-
# @Time    : 2023/4/10 10:07
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : redisClient.py
# @Software: PyCharm
import functools
import logging
import time
import traceback
from typing import Union

from redis import StrictRedis

LOG = logging.getLogger()

REDIS_MAX_RETRY_TIMES = 3
REDIS_WAIT_TIME = 1


def retry(max_retry_times=1, wait_time=0.1):
    def _(func):
        @functools.wraps(func)
        def wrap_func(LOG=None, *l, **kwargs):
            for i in range(max_retry_times):
                try:
                    return func(*l, **kwargs)
                except ConnectionError as conn_error:
                    LOG.error(f"redis conn error:{conn_error}")
                    LOG.error(traceback.format_exc())
                    if i == (max_retry_times - 1):
                        raise Exception(
                            f"redis client command `{func.__name__}` error!")
                except Exception as e:
                    LOG.error(f"redis unknown error:{e}")
                    LOG.error(traceback.format_exc())
                    if i == (max_retry_times - 1):
                        raise Exception(
                            f"redis client command `{func.__name__}` error!")
                time.sleep(wait_time)

        return wrap_func

    return _


class RedisClient(object):

    def __init__(self, config=None) -> None:
        self.config = config
        self._connection = None

    def execute(self, cmd, *vargs):
        self.create()
        try:
            if hasattr(self, '_%s' % cmd):
                return getattr(self._connection, cmd)(*vargs)
            else:
                return getattr(self._connection, cmd)(*vargs)
        except Exception:
            self.destroy()
            raise

    def create(self):
        if self._connection is None:
            self._connection = StrictRedis(**self.config)

    def destroy(self):
        self._connection = None

    def decode(self, data: bytes):
        """bytes --> str"""
        if data is None:
            return None
        return str(data, encoding='utf-8')

    def decode_dict(self, data: dict):
        if data is None:
            return None
        return {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}

    def decode_iterable(self, data: Union[list, set, tuple]):
        if data is None:
            return None
        if isinstance(data, list):
            return list(map(self.decode, data))
        elif isinstance(data, set):
            return set(map(self.decode, data))
        elif isinstance(data, tuple):
            return tuple(map(self.decode, data))
        else:
            return list(map(self.decode, data))

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _set(self, name, value):
        return self._connection.set(name, value)

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _get(self, name):
        return self.decode(self._connection.get(name))

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _setnx(self, name, value):
        return self._connection.setnx(name, value)

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _lpush(self, name, *values):
        return self._connection.lpush(name, *values)

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _lrange(self, name, start, end):
        return self.decode_iterable(self._connection.lrange(name, start, end))

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _incr(self, name, amount=1):
        return self._connection.incr(name, amount)

    _incrby = _incr

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _hgetall(self, name):
        return self.decode_dict(self._connection.hgetall(name))

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _sadd(self, name, *values):
        return self._connection.sadd(name, *values)

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _sismember(self, name, value):
        return self._connection.sismember(name, value)

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _smembers(self, name):
        return self.decode_iterable(self._connection.smembers(name))

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _srem(self, name, *values):
        return self._connection.srem(name, *values)

    @retry(max_retry_times=REDIS_MAX_RETRY_TIMES, wait_time=REDIS_WAIT_TIME)
    def _delete(self, *names):
        return self._connection.delete(*names)
