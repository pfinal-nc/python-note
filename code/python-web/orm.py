# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 11:59
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : orm.py
# @Software: PyCharm
import logging

import aiomysql

__pool = {}


def log(sql: str, args: tuple = ()) -> None:
    """log a SQL statement"""
    logging.info('SQL: %s' % sql)


async def create_pool(loop: list, **kw):
    """create pool"""
    logging.info('create database connection.......')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

    async def select(sql: str, args: tuple, size=None):
        """select"""
        log(sql, args)
        
