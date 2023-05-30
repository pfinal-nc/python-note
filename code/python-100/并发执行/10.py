# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 15:49
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 10.py
# @Software: PyCharm
# 基于I/O多路复用+socket 非阻塞,实现并发请求
import socket

client = socket.socket()
# 将原来阻塞的位置变成非阻塞
client.setblocking(False)

# 百度创建链接
try:
    # 执行
    client.connect(('www.baidu.com', 80))
except BlockingIOError as e:
    pass

# 检测到已经链接成功
client.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')

chunk_list = []
while True:
    chunk = client.recv(8096)
    if not chunk:
        break
    chunk_list.append(chunk)

body = b''.join(chunk_list)
print(body.decode('utf-8'))
