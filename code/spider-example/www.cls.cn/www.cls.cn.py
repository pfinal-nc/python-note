# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 15:16
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : www.cls.cn.py
# @Software: PyCharm
import time

import execjs
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=utf-8",
    "Pragma": "no-cache",
    "Referer": "https://www.cls.cn/depth?id=1000",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "HWWAFSESID": "3b70ba37e31cdcedd1",
    "HWWAFSESTIME": "1683789327151",
    "hasTelegraphRemind": "on",
    "hasTelegraphSound": "on",
    "vipNotificationState": "on",
    "isMinimize": "off",
    "hasTelegraphNotification": "off"
}
url = "https://www.cls.cn/v3/depth/list/1000"
params = {
    "app": "CailianpressWeb",
    "id": "1000",
    "last_time": "1683778668",
    "os": "web",
    "rn": "20",
    "sv": "7.7.5",
    "sign": "49b94313193abef035a4e1a32cd20ad7"
}


# response = requests.get(url, headers=headers, cookies=cookies, params=params)
#
# print(response.text)
# print(response)

def get_encrypted_sign(params):
    sign_str = f'app={params.get("app")}&os={params.get("os")}&sv={params.get("sv")}'
    with open('www.cls.js', 'r', encoding="utf-8") as f:
        cls_js = f.read()
    encrypted_sign = execjs.compile(cls_js).call('getEncryptedSign', sign_str)
    return encrypted_sign


def main():
    params = {
        "app": "CailianpressWeb",
        "id": "1000",
        "last_time": int(time.time()),
        "os": "web",
        "rn": "20",
        "sv": "7.7.5",
        "sign": ""
    }
    sign = get_encrypted_sign(params)
    params['sign'] = sign
    print(params)
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    print(response)


if __name__ == '__main__':
    """run """
    main()
