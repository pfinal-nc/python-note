# -*- coding:utf-8 -*-
import re
import urllib
import urllib.request
import os
import sys
from lxml import etree
from bs4 import BeautifulSoup
import random
import requests


class Meizi:
    def __init__(self, page):
        self.siteUrl = 'https://www.mzitu.com/xinggan/page' + str(page)

    def get_html(self):
        response = urllib.request.urlopen(self.siteUrl)
        html = response.read().decode('UTF-8')
        soup = etree.HTML(html)
        self.url_lists = soup.xpath('//*[@id="pins"]/li/a/@href')

    def get_img(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
        }
        for imgUrl in self.url_lists:
            page_two = 1
            response = urllib.request.urlopen(imgUrl).read().decode('utf-8')
            content = BeautifulSoup(response, 'lxml')
            title = content.find_all('h2', class_='main-title')[0].get_text()
            if os.path.exists(os.path.dirname(sys.argv[0]) + "/meizi/" + title) != True:
                os.mkdir(os.path.dirname(sys.argv[0]) + "/meizi/" + title)
            total = content.find(class_='pagenavi').find_all(
                'a')[-2].find('span').string
            print(title + '开始下载===========>\n')
            while page_two <= int(total):
                # print(imgUrl + '/' + str(page_two))
                s = requests.Session()
                s.get(imgUrl + '/' + str(page_two),
                      headers=headers, timeout=3)  # 请求首页获取cookies
                cookie = s.cookies
                # print(cookie)
                page_two += 1
                try:
                    handler = urllib.request.HTTPCookieProcessor(cookie)
                    opener = urllib.request.build_opener(handler)
                    response = opener.open(
                        imgUrl + '/' + str(page_two)).read().decode('utf-8')
                    soup = BeautifulSoup(response, 'lxml')
                    img_url = soup.find('img').get('src')
                    print(img_url)
                    f = open(os.path.dirname(sys.argv[0]) + "/meizi/" + title + '/' + title + '_' + str(page_two) + '.jpg',
                             "wb")
                    f.write((opener.open(img_url).read()))
                    print('  =======【下载 第 ' + str(page_two) + '条】=========')
                    f.close()
                    # print(opener.open(img_url).read().decode('utf-8'))
                except:
                    break
                # response = urllib.request.urlopen(
                #     imgUrl + '/' + str(page_two)).read().decode('utf-8')
                # # print(response)
                # soup = BeautifulSoup(response, 'lxml')
                # img_url = soup.find('img').get('src')
                # img_content = urllib.request.Request(img_url, headers=headers, cookie=cookie)
                # print(urllib.request.urlopen(img_content).read())

                # f.write((urllib.request.urlopen(img_url).read()))

                #


if __name__ == "__main__":
    meizi = Meizi(1)
    meizi.get_html()
    meizi.get_img()
