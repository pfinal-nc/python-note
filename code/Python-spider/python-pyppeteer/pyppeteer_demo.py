# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 11:46
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : pyppeteer_demo.py
# @Software: PyCharm
import asyncio

from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://top.baidu.com/board?tab=realtime')
    # 等待元素加载
    await page.waitForXPath('//div[@class="c-single-text-ellipsis"]')
    element_j = await page.J('.c-single-text-ellipsis')
    element_jj = await page.JJ('.c-single-text-ellipsis')
    # 打印元素的文本信息
    print(await (await element_j.getProperty('textContent')).jsonValue())
    for element in element_jj:
        # 打印元素的文本信息
        print(await (await element.getProperty('textContent')).jsonValue())

    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
