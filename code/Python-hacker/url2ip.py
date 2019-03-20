# -*- coding: UTF-8 -*-

import socket
import os
import sys
import time
import threading

ip_info = []


def get_ip(urls):
    for openurl in urls:
        url = openurl.replace('http://', '')
        try:
            result = socket.gethostbyname(socket.getfqdn(url))
            save_ip(os.path.dirname(sys.argv[0]) + '/school_ip.txt',result)
            # print(result)
            # ip_info.append(result)
        except:
            # time.sleep(2)
            pass


def url2ip(urllist):
    threads = []
    num = round(len(urllist) / 100)
    # print(num*500)
    for i in range(1, num):
        t = threading.Thread(target=get_ip, args=(urllist[0 * i * 100:100],))
        threads.append(t)
    # print(threads)
    for t in threads:
        # t.setDaemon(True)
        t.start()
    # print(ip_info)


def get_url(file_url):
    # file_url = os.path.dirname(sys.argv[0]) + '/dna2.txt'
    # print(file_url)
    urllist = open(file_url, "r", encoding='utf-8')
    # print(urllist.read())
    url2ip(urllist.readlines())
    # urllist.close()


def save_ip(filename, content):
    # global ip_info
    # print(ip_info)
    count = 0
    with open(filename, 'a') as f:
        f.writelines(content+'\n')
        count += 1


if __name__ == "__main__":
    file_url = os.path.dirname(sys.argv[0]) + '/school.txt'
    # print(file_url)
    get_url(file_url)
    # print(ip_info)
    # save_ip(os.path.dirname(sys.argv[0]) + '/school_ip.txt')
