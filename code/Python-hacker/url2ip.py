# -*- coding: UTF-8 -*-

import socket
import os
import sys
import time
import threading


def get_ip(urls):
    for openurl in urls:
        url = openurl.replace('http://', '')
        try:
            result = socket.gethostbyname_ex(socket.getfqdn(url))
            print(result)
        except:
            # time.sleep(2)
            pass


def url2ip(urllist):
    threads = []
    num = round(len(urllist) / 500)
    # print(num*500)
    for i in range(1, num):
        t = threading.Thread(target=get_ip, args=(urllist[0 * num * 500:500],))
        threads.append(t)
    # print(threads)
    for t in threads:
    #    t.setDaemon(True)
        t.start()


def get_url(file_url):
    # file_url = os.path.dirname(sys.argv[0]) + '/dna2.txt'
    # print(file_url)
    urllist = open(file_url, "r", encoding='utf-8')
    # print(urllist.read())
    url2ip(urllist.readlines())
    # urllist.close()


if __name__ == "__main__":
    file_url = os.path.dirname(sys.argv[0]) + '/school.txt'
    # print(file_url)
    get_url(file_url)
