# -*- coding: utf-8 -*-
# @Time    : 2023/8/28 14:10
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : day04.py
# @Software: PyCharm
import asyncio


async def main():
    """ async function"""
    await asyncio.sleep(0)

# 在这段代码中，main函数和asyncio.sleep都属于Coroutine，main 是通过 asyncio.run 进行调用

asyncio.run(main())
