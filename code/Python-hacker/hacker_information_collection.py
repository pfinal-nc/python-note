# -*- coding:utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
import re
import json
import socket
import urllib.request
start = time.time()


def chax():
    lid = input('请输入你要查询的域名:')
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    pattern = re.compile(r'http://|https://')
    lid = re.sub(pattern, '', lid).rsplit('/')[0]
    try:
        ip = socket.gethostbyname(lid)
        print('[+]IP解析记录')
        print('    IP地址:%s' % ip)
    except Exception as e:
        print("this URL 2 IP ERROR ")

    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={}&co=&resource_id=6006&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json'
    req = urllib.request.Request(url=url.format(ip))
    response = urllib.request.urlopen(req).read() 
    start = '/**/op_aladdin_callback('.__len__()
    ip_info = json.loads(response[start:-2].decode('gbk'));
    print('    IPhost地址:' + ip_info['data'][0]['location'])
    print('[+]子域名查询')
    scan_domain(lid)


        # print('[+]IP解析记录')
    # gf = rb.content.decode()
    # dict_json = json.loads(gf)
    # print(dict_json)
    # for v in dict_json['data']:
    #     print('\nIP:【'+ v['ip'] + '】\nSIGN:【' + v['sign'] + '】\n' )
    # gf1 = BeautifulSoup(rb1.content, 'html.parser')
    # print('[+]子域名查询')
    # for v in gf1.find_all('p'):
    #      link2 = v.get_text()
    #      print(link2)
    # gf2 = BeautifulSoup(rb2.content, 'html.parser')
    # print('[+]备案查询')
    # for s in gf2.find_all('p'):
    #     link3 = s.get_text()
    #     print(link3)
    # gf3 = BeautifulSoup(rb3.content, 'html.parser')
    # print('[+]whois查询')
    # for k in gf3.find_all('p'):
    #     link4 = k.get_text()
    #     print(link4)

if __name__ == "__main__":
    chax()
    end = time.time()
    print('查询耗时:', end - start)
