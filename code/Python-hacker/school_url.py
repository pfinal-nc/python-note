# -*- coding:utf-8 -*-

import requests
import sys
import os
from bs4 import BeautifulSoup
import tldextract

url = 'http://www.hao123.com/edu'

headers = {
    'Host': 'www.hao123.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Referer': 'http://www.hao123.com/exam/wangzhi'
}

area_url_list = []
school_url = []


def get_area_url_list():
    global area_url_list
    try:
        response = requests.get(url=url, headers=headers)
        # print(response)
    except Exception as e:
        print(e)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.select("[href^='http://www.hao123.com/eduhtm']")
    # print(div)
    for tag in div[1:-2]:
        area_url = tag.get('href')
        area_url_list.append(area_url)


def get_school_url():
    global school_url
    for area_url in area_url_list:
        try:
            response = requests.get(url=area_url, headers=headers, timeout=3)
            # print(response.text)
        except Exception as e:
            continue
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.select("a[href^=http://]")
        # print(div)
        for tag in div[60:-5]:
            # print(tag.get('href'))
            tagget_url = str(tag.get('href'))
            school_url.append(tagget_url)


def filter_scholl_url():
    global school_url
    tmplist = []
    for url in school_url:
        if 'baike' not in url:
            ext = tldextract.extract(url)
            tmplist.append('http://' + '.'.join(ext[0:3]))
    school_url = tmplist
    # print(tmplist)


def save_scholl_url(filename):
    count = 0
    with open(filename, 'w') as f:
        for url in school_url:
            f.writelines(url+'\n')
            count += 1


if __name__ == "__main__":
    get_area_url_list()
    get_school_url()
    filter_scholl_url()
    save_scholl_url(os.path.dirname(sys.argv[0]) + '/school.txt')
