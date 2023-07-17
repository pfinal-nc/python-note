# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 11:31
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : socket_client.py
# @Software: PyCharm
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    re_data = input("请输入内容:")
    client.send(re_data.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))
