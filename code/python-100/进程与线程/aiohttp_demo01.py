# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 15:07
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : aiohttp_demo01.py
# @Software: PyCharm
import asyncio
import json
import os

import aiofile
import aiohttp


async def download_picture(session, url):
    """ download_picture"""
    filename = url[url.rfind('/') + 1:]
    async with session.get(url, ssl=False) as response:
        if response.status == 200:
            data = await response.read()
            async with aiofile.async_open(f'images/beauty/{filename}', 'wb') as file:
                await file.write(data)


async def fetch_json():
    """ fetch_json"""
    async with aiohttp.ClientSession() as session:
        for page in range(3):
            async with session.get(
                    url=f'https://image.so.com/zjl?ch=beauty&sn={page * 30}',
                    ssl=False
            ) as response:
                if response.status == 200:
                    json_str = await response.text()
                    result = json.loads(json_str)
                    for pic_dict in result['list']:
                        await download_picture(session, pic_dict['qhimg_url'])


def main():
    """ main """
    if not os.path.exists('images/beauty'):
        os.makedirs('images/beauty')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_json())
    loop.close()


if __name__ == '__main__':
    main()
