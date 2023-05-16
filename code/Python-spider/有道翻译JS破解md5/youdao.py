# -*- coding: utf-8 -*-
# @Time    : 2023/5/16 16:06
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : youdao.py
# @Software: PyCharm
import requests


def youdao(word):
    """翻译"""

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://fanyi.youdao.com",
        "Pragma": "no-cache",
        "Referer": "https://fanyi.youdao.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    url = "https://dict.youdao.com/webtranslate"
    data = {
        "i": word,
        "from": "auto",
        "to": "",
        "dictResult": "true",
        "keyid": "webfanyi",
        "sign": "becc2a191091cf232cfe2b6b11129b1a",
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": "1684224354245",
        "keyfrom": "fanyi.web"
    }
    response = requests.post(url, headers=headers, data=data)

    print(response.text)
    print(response)


if __name__ == '__main__':
    result = youdao('鸡你太美')
    print(result)
