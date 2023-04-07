# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 13:38
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : baiduimg.py
# @Software: PyCharm
import json
import os.path
import random

import requests


class BdImgSearch:
    def __init__(self, key, pic_num, directory):
        self.headers = {
            "Accept": "text/plain, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Referer": "https://image.baidu.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\""
        }
        self.url = "https://image.baidu.com/search/acjson"
        self.params = {
            "tn": "resultjson_com",
            "logid": "7257790148603340277",
            "ipn": "rj",
            "ct": "201326592",
            "is": "",
            "fp": "result",
            "fr": "",
            "word": key,
            "queryWord": key,
            "cl": "2",
            "lm": "-1",
            "ie": "utf-8",
            "oe": "utf-8",
            "adpicid": "",
            "st": "-1",
            "z": "0",
            "face": "0",
            "istype": "2",
            "nc": "1",
            "pn": 30,
            "rn": "30",
            "gsm": "1e",
        }
        self.url = "https://image.baidu.com/search/acjson"
        self.max_pn = 20
        self.download_pic_url_list = []
        self.pic_num = int(pic_num)
        self.directory = directory
        self.key = key

    def random_pn_number(self):
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            # print(response.text)
            max_num = json.loads(response.text)['displayNum']
            # print('max_num',max_num)
            max_page = max_num // 30
            # print('max_page',max_page)
            if max_page > self.max_pn:
                max_page = self.max_pn
            pn = random.randint(1, max_page)
            # print('pn值,',pn)
            return pn
        except Exception as e:
            print(e)

    def random_spider(self, random_pn):
        try:
            self.params['pn'] = 30 * random_pn
            response = requests.get(self.url, headers=self.headers, params=self.params)
            res = json.loads(response.text)
            data = res['data']
            self.download_pic_url_list = [u['replaceUrl'][0]['ObjURL'] for u in data[:-1]]
        except Exception as e:
            print("没有获取到图片请重启脚本", e)

    def download_pic(self):
        d = os.path.exists(self.directory)
        if not d:
            os.mkdir(self.directory)
        try:
            download_url = random.sample(self.download_pic_url_list, k=self.pic_num)
            for i, u in enumerate(download_url):
                res = requests.get(u, headers=self.headers)
                with open("{}/{}.jpg".format(self.directory, self.key + str(i)), 'wb') as f:
                    print('正在下载{}的图片,地址为:{}'.format(self.key, u))
                    f.write(res.content)
        except Exception as e:
            print('当前URL有问题 跳过', e)

    def run(self):
        pn = self.random_pn_number()
        self.random_spider(pn)
        self.download_pic()
        print('下完了 你个老色批 静静欣赏吧!!!!')


if __name__ == '__main__':
    search = input('搜啥玩意(女优名?黑丝?白丝?萝莉?御姐?等等,出来什么我就不管了)?:')
    num = input('要多少张?太多了没有一次10-30张,老色批别太贪心!尼玛死:')
    dire = input('传个放片的目录名 请正经一点!:')
    BdImgSearch(search, num, dire).run()
