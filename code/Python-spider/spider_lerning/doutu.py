# -*- coding:utf-8 -*-
import os,sys
import urllib.request
import re
import time
import threading
import requests

from bs4 import BeautifulSoup
from lxml import etree


class Img:
    def __init__(self, page=1):
        self.siteUrl = 'https://www.doutula.com/article/list/?page=' + \
            str(page)

    def get_html(self, url):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        return response

    def get_img(self, html):
        soup = etree.HTML(html)
        items = soup.xpath('//div[@class="artile_des"]')
        # print(items)
        for item in items:
            imgurl_list = item.xpath('table/tbody/tr/td/a/img/@onerror')
            for i in imgurl_list:
                th = threading.Thread(target=self.save_img, args=(i,))
                th.start()

    def get_img_html(self, response):
        soup = BeautifulSoup(response, 'lxml')
        all_a = soup.find_all('a', class_='list-group-item')
        for i in all_a:
            # self.get_img(self.get_html(i['href']))
            content = self.get_html(i['href']).read().decode('utf-8')
            self.get_img(content)

    def save_img(self, img_url):
        img_url = img_url.split('=')[-1][1:-2].replace('jp', 'jpg')
        print(u'正在下载'+img_url)
        img_content = requests.get(img_url).content
        # print(img_content)
        with open(os.path.dirname(sys.argv[0])+'/doutu/%s.jpg' % img_url.split('/')[-1], 'wb') as f:
            f.write(img_content)
if __name__ == "__main__":
    for i in range(1,11):
        dotu = Img(i)
        dotu.get_img_html(dotu.get_html(dotu.siteUrl))
