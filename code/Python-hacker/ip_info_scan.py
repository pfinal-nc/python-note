# -*- coding:utf-8 -*-
import requests
import json


class IpInfoScan:
    def __init__(self, ip):
        self.siteUrl = 'http://ip-api.com/json/'
        self.ip = ip
        self.params = {
            'lang': 'zh-CN'
        }

    def scan(self):
        ip_content = requests.get(self.siteUrl + self.ip, params=self.params)
        data = json.loads(ip_content.text)
        return data


if __name__ == "__main__":
    ip_scan = IpInfoScan('58.211.137.13')
    ip_scan.scan()
