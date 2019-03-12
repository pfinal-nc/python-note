# -*- coding:utf-8 -*-
import os
import urllib.request
import re
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

    def get_img_html(self, response):
        soup = BeautifulSoup(response, 'lxml')
        all_a = soup.find_all('a', class_='list-group-item')
        for i in all_a:
            # self.get_img(self.get_html(i['href']))
            soup = BeautifulSoup(self.get_html(i['href']),'lxml')
            print(soup)

if __name__ == "__main__":
    dotu = Img(1)
    dotu.get_img_html(dotu.get_html(dotu.siteUrl))
