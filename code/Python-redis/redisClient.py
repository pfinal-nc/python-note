# -*- coding: utf-8 -*-
# @Time    : 2023/4/10 10:07
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : redisClient.py
# @Software: PyCharm
from redis import StrictRedis


class RedisClient(object):

    def __init__(self, config=None) -> None:
        self.config = config
        self._connection = None

    def execute(self, cmd, *vargs):
        self.create()
        try:
            
        except Exception:

    def create(self):
        if self._connection is None:
            self._connection = StrictRedis(**self.config)
