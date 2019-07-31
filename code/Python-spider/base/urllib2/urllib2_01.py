# -*- coding:utf-8 -*-
import socket
import urllib.parse
import urllib.request
import urllib.error
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())

# timeout 参数

# response1 = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# print(response1.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('Time out')
