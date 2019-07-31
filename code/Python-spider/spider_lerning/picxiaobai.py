# -*- coding:utf-8 -*-
import urllib.request
import re
import random


class Pic:
    def __init__(self, page=1):
        self.siteUrl = 'http://www.picxiaobai.com/pic/index/66.html?keywords=&page=' + \
            str(page)
        self.proxy_list = [
            {"http": "58.240.53.194:8080"},
            {"http": "140.143.142.218:1080"},
            # {"http": "60.165.54.153:8060"},
            # {"http": "58.243.50.184:53281"}
        ]
        self.proxy = random.choice(self.proxy_list)

    def getContent(self):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        try:
            httpproxy_handler = urllib.request.ProxyHandler(self.proxy)
            opener = urllib.request.build_opener(httpproxy_handler)
            resource = urllib.request.Request(self.siteUrl, headers=headers)
            response = opener.open(resource)
            content = response.read().decode('utf-8')
            print(content)
            # pattern = re.compile(
            #     '<div.*?class="part">.*?(\r|\n|\\s)?.*<img\s+src="(.*)".*?>(\r|\n|\\s)+.*(\r|\n|\\s)+.*(\r|\n|\\s)+.*</div>', re.S)
            # items = re.findall(pattern, content)
            # print(items)

            # return response
        except urllib.request.URLError as e:
            if hasattr(e, 'reason'):
                print(e.reason)
                return None


pic = Pic(3)
pic.getContent()
