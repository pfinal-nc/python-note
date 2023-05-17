# -*- coding: utf-8 -*-
# @Time    : 2023/5/17 14:13
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : www.qimingpian.com.py
# @Software: PyCharm
import execjs
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.qimingpian.com",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://vipapi.qimingpian.cn/DataList/productListVip"


def get_data():
    """get data"""
    data = {
        "time_interval": "",
        "tag": "",
        "tag_type": "",
        "province": "",
        "lunci": "",
        "page": "1",
        "num": "20",
        "unionid": ""
    }
    response = requests.post(url, headers=headers, data=data).json()
    return response['encrypt_data']


def parse_data(encrypt_data):
    with open('qimingpian.js', 'r', encoding='utf-8') as f:
        qimingpian_js = f.read()
    dencrypt_data = execjs.compile(qimingpian_js).call('getData', encrypt_data)  # 通过 JavaScript 代码获取各个参数
    print(dencrypt_data)
    return dencrypt_data


def main():
    encrypt_data = get_data()
    dencrypt_data = parse_data(encrypt_data)
    print(dencrypt_data)


if __name__ == '__main__':
    main()
