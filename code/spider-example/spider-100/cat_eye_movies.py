# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 11:48
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : cat_eye_movies.py
# @Software: PyCharm

import requests
from lxml import etree

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "__mta": "19176199.1680839221304.1680839238949.1680839243486.3",
    "uuid_n_v": "v1",
    "uuid": "D72876B0D4F611EDA656FD7ECF47D229743498AC16684F60B8EB1F02E4C27BD1",
    "_csrf": "6c5d95eebe82ec25971c53dd3c70cfcc5f9af5e912b89ae7b48049005445e25d",
    "_lxsdk_cuid": "18759d30bf9c8-0322232360a67-1e525634-384000-18759d30bf9c8",
    "_lxsdk": "D72876B0D4F611EDA656FD7ECF47D229743498AC16684F60B8EB1F02E4C27BD1",
    "_lxsdk_s": "18759d30bfa-e05-0cb-d8c%7C%7C10"
}
url = "https://www.maoyan.com/board/1"
response = requests.get(url, headers=headers)
html = etree.HTML(response.content.decode("utf-8"))
title_list = [[x.xpath('.//div/div/div[1]/p[1]/a/text()')[0], x.xpath('.//div/div/div[1]/p[2]/text()')[0],
               x.xpath('.//div/div/div[1]/p[3]/text()')[0]] for x in
              html.xpath('//*[@id="app"]/div/div/div/dl/dd')]
print(title_list)
