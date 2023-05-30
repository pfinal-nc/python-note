# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 11:25
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : spider-02.py
# @Software: PyCharm

import requests
from lxml import etree

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Authorization": "Basic YWRtaW46YWRtaW4=",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Referer": "https://scrape.center/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://ssr3.scrape.center/"
response = requests.get(url, headers=headers)
html = etree.HTML(response.content.decode("utf-8"))
title_list = [x.xpath('.//div/div[2]/a/h2/text()')[0] for x in
              html.xpath('//*[@id="index"]/div[1]/div[1]/div')]
print(title_list)