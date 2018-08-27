# -*- coding:utf-8 -*-

import urllib.request
response = urllib.request.urlopen('https://www.python.org')
# print(response.read())
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))