# -*- coding:utf-8 -*-

import hashlib
import os
import socket
import sys

import requests

data = []
socket.setdefaulttimeout(10)


def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest


def getmd5(url):
    src = requests.get(url).content
    md5 = get_md5_value(src)
    return md5


def init():
    file_url = os.path.dirname(sys.argv[0]) + "/dna2.txt"
    # print(file_url)
    file = open(file_url, "r+", encoding="utf-8")
    try:
        # print(file.read())
        for line in file:
            str = line.strip().split(" ")
            ls_data = {}
            if len(str) == 3:
                ls_data["url"] = str[0]
                ls_data["name"] = str[1]
                ls_data["md5"] = str[2]
                data.append(ls_data)
    finally:
        file.close()


def cms(url):
    # if url in None:
    #     print('输错了,大爷')
    #     return
    url = url.rstrip("/")
    for dataline in data:
        _url = url + dataline["url"]
        try:
            status = requests.head(_url, timeout=10).status_code
        except:
            continue

        if status == 200:
            md5 = get_md5_value(requests.get(_url).content)
            # print(md5)
            if md5 == dataline["md5"]:
                dataline["url"] = _url
                return dataline
    return False


if __name__ == "__main__":
    init()
    print(cms("http://shhjjx.com/"))
    print(cms("http://sdzhongqi.com/"))
    print(cms("http://0527art.com/"))
    print(cms("http://www.jiangnanjz.com"))
    print(cms("http://www.13422222222.com/"))
    # print(cms("https://vzeo.com/"))
    # print(cms("http://www.68ecshop.com/"))
    # print(getmd5('http://www.oilco.cn/robots.txt'))
