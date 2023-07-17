# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 11:24
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : socket_server.py
# @Software: PyCharm
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen()


def handle_sock(sock, addr):
    """ handle sock"""
    while True:
        data = sock.recv(1024)
        print(data.decode('utf8'))
        re_data = input("请输入内容")
        sock.send(re_data.encode("utf8"))


# 获取从客户端返送的数据
# 一次获取 1k的数据

while True:
    sock, addr = server.accept()

    # 用线程去处理新接受的连接(用户)
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()


