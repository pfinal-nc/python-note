# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 09:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : www.hh1024.com.py
# @Software: PyCharm
import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "http://www.hh1024.com",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://user.hrdjyun.com/wechat/phonePwdLogin"
data = {
    "phoneNum": "11111111111",
    "pwd": "4297f44b13955235245b2497399d7a93",
    "t": 1684459773862,
    "tenant": 1,
    "sig": "4ea55e9f0cb096fd926edf86ee550d6a"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)