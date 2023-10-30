# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 09:34
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : main.py
# @Software: PyCharm
import hashlib
import json
import re
import time

import requests

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://www.autoreport.cn",
    "Pragma": "no-cache",
    "Referer": "https://www.autoreport.cn/newslist/a1147/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "cid": "601",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "x-city-id": "2401",
    "x-ip-address": "180.168.160.38",
    "x-platform": "phone",
    "x-sign": "eae15d3be0da65a9ddb1583617607d8e",
    "x-timestamp": "1698283204517",
    "x-user-guid": ""
}

res = requests.get('https://www.autoreport.cn/newslist/a1147/', headers=headers)
stageTime = re.findall(r',stageTime="(.*?)"', res.text)[0]

print(stageTime)

url = "https://mgw.yiche.com/site_api/article/api/get_article_list"
data = {
    "cid": "601",
    "param": {
        "pageIndex": 2,
        "pageSize": 18,
        "appIds": "101",
        "type": "0",
        "clientType": 0,
        "recommendGrade": "0",
        "categoryIds": "145,7",
        "copyright": "original",
        "stageTime": stageTime
    }
}
data = json.dumps(data, separators=(',', ':'))
dt = int(time.time() * 1000)

d_str = 'cid=601&param={"pageIndex":%s,"pageSize":18,"appIds":"101","type":"0","clientType":0,"recommendGrade":"0","categoryIds":"145,7","copyright":"original","stageTime":"%s"}DB2560A6EBC65F37A0484295CD4EDD25%s' % (
    2, stageTime, str(dt))
m = hashlib.md5()
# frida hook app拿到的字符串
b = d_str.encode(encoding='utf-8')
m.update(b)
sign = m.hexdigest()
headers['x-sign'] = sign
headers['x-timestamp'] = str(dt)
#
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)
