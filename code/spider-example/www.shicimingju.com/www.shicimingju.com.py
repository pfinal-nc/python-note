# -*- coding: utf-8 -*-
# @Time    : 2023/5/16 15:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : www.shicimingju.com.py
# @Software: PyCharm
import requests
from lxml import etree

headers = {
    "authority": "www.shicimingju.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    # "referer": "https://www.shicimingju.com/category/all_2",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}


def parse_data(shi_data):
    """parse_data"""
    html = etree.HTML(shi_data)
    # TODO:拿到作者


def run_url():
    """run_url"""
    i = 1
    while True:
        if i >= 10:
            break
        url = "https://www.shicimingju.com/category/all_%s" % i
        response = requests.get(url, headers=headers)
        parse_data(response.content.decode("utf-8"))
        i += 1
