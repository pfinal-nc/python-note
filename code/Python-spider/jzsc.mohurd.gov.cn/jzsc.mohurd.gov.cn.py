# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 13:55
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : jzsc.mohurd.gov.js.cn.py
# @Software: PyCharm
import json

import execjs
import requests

# api


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://jzsc.mohurd.gov.cn/supervise/list",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "accessToken": "",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "timeout": "30000"
}

url = "https://jzsc.mohurd.gov.cn/APi/webApi/artcleApi/getPageList"


def get_encrypted_data(page):
    """Returns"""
    params = {
        # "itemCode": "jsbpp_news_bfwjnew",
        "pg": f"{page}",
        "pgsz": "15"
    }

    response = requests.get(url, headers=headers, params=params)
    return response.text


def get_decrypted_data(encrypt_data):
    """解密"""
    with open('jzsc.mohurd.gov.js', 'r', encoding='utf-8') as f:
        jzsc_mohurd_js = f.read()

    decrypted_data = execjs.compile(jzsc_mohurd_js).call('getDecryptedData', encrypt_data)
    return json.loads(decrypted_data)


if __name__ == '__main__':
    encrypted_data = get_encrypted_data(1)
    decrypted_data = get_decrypted_data(encrypted_data)
    print(decrypted_data)
