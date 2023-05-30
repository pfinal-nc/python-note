# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 16:59
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : demo.py
# @Software: PyCharm

import asyncio

import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
