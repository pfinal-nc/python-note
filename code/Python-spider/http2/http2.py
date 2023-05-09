# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 16:43
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : http2.py
# @Software: PyCharm

# import requests
#
# r = requests.get("https://spa16.scrape.center/")
# print(r.status_code)
# print(r.text)

# httpx 这个库 默认是不支持 h2

import httpx
client = httpx.Client(http2=True)
r = client.get("https://spa16.scrape.center/")

print(r.text)