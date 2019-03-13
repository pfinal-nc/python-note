# -*- coding:utf-8 -*-
import re
import urllib.request
import os
import sys
from lxml import etree
from bs4 import BeautifulSoup
import random


class Meizi:
    def __init__(self, page):
        self.siteUrl = 'https://www.mzitu.com/xinggan/page' + str(page)

    def get_html(self):
        response = urllib.request.urlopen(self.siteUrl)
        html = response.read().decode('UTF-8')
        soup = etree.HTML(html)
        self.url_lists = soup.xpath('//*[@id="pins"]/li/a/@href')

    def get_img(self):
        for imgUrl in self.url_lists:
            page_two = 1
            response = urllib.request.urlopen(imgUrl).read().decode('utf-8')
            content = BeautifulSoup(response, 'lxml')
            title = content.find_all('h2', class_='main-title')[0].get_text()
            if os.path.exists(os.path.dirname(sys.argv[0]) + "/meizi/" + title) != True:
                os.mkdir(os.path.dirname(sys.argv[0]) + "/meizi/" + title)
            total = content.find(class_='pagenavi').find_all('a')[-2].find('span').string
            print(title + '开始下载===========>\n')
            while page_two <= int(total):
                response = urllib.request.urlopen(imgUrl + '/' + str(page_two)).read().decode('utf-8')
                soup = BeautifulSoup(response, 'lxml')
                img_url = soup.find('img').get('src')
                # print(img_url)
                f = open(os.path.dirname(sys.argv[0]) + "/meizi/" + title + '/' + title + '_' + str(page_two) + '.jpg',
                         "wb")
                f.write((urllib.request.urlopen(img_url).read()))
                print('  =======【下载 第 ' + str(page_two) + '条】=========')
                page_two += 1
                f.close()



if __name__ == "__main__":
    meizi = Meizi(1)
    meizi.get_html()
    meizi.get_img()
