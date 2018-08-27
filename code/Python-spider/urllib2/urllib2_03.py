# -*- coding:utf-8 -*-

# 异常处理
from urllib import  request,error

# try:
#     response = request.urlopen('http://friday-go.cc/cindex.html')
# except error.URLError as e:
#     print(e.reason)

# HTTPError

# try:
#     response1 = request.urlopen('http://friday-go.cc/cindex.html')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep="\n")

try:
    response = request.urlopen('http://friday-go.cc/cindex.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep="\n=============\n")
except error.URLError as e:
    print(e.reason)
else:
    print('Request successfully')