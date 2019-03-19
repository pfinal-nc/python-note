# -*- coding: UTF-8 -*-

import socket
import os
import sys
import time
import threading


def get_ip(url):
    try:
        result = socket.gethostbyname_ex(socket.getfqdn(url))
        print(result)
    except:
        # time.sleep(2)
        pass


def url2ip(urllist):
    threads = []
    print(len(urllist))
    # for openurl in urllist:
    #     url = openurl.replace('http://', '')
    #     t = threading.Thread(target=get_ip, args=(url,))
    #     threads.append(t)
    #     # print(socket.has_ipv6)
    #     # url = openurl.replace('http://', '')
    #     # # print(url)
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()


def get_url(file_url):
    # file_url = os.path.dirname(sys.argv[0]) + '/dna2.txt'
    # print(file_url)
    urllist = open(file_url, "r+", encoding='utf-8')
    # print(urllist)
    url2ip(urllist)
    # urllist.close()


if __name__ == "__main__":
    file_url = os.path.dirname(sys.argv[0]) + '/school.txt'
    get_url(file_url)
