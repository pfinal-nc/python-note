# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 14:23
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : aiohttp_demo.py
# @Software: PyCharm
import asyncio
import re

import aiohttp

pattern = re.compile(r'<title>(?P<title>.*)</title>')


async def fetch_page(session, url):
    """fetch_page"""
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    """show_title"""
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(pattern.search(html).group('title'))


def main():
    """main"""
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()


if __name__ == '__main__':
    main()
