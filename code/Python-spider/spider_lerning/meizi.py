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
            while page_two < 10:
                f = open(os.path.dirname(
                    sys.argv[0]) + "/meizi/" + random.random() + '.jpg', "wb")
                f.write((urllib.request.urlopen(imgUrl + '/' + page_two)).read())
                page_two += 1
                f.close()

if __name__ == "__main__":
    meizi = Meizi(1)
    meizi.get_html()
    meizi.get_img()
