# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 15:58
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : tryc.py
# @Software: PyCharm
import re
import requests
from requests.exceptions import RequestException


# 异常捕获的原则: 只做最精准的异常捕获
# 精准捕获包括:
# 1.永远只捕获那些可能会抛出异常的语句块
# 2.尽量只捕获精确的异常类型，而不是模糊的 Exception

def save_website_title(url, filename):
    try:
        resp = requests.get(url)
    except RequestException as e:
        print(f'save failed: unable to get page content: {e}')
        return False

    # 这段正则操作本身就是不应该抛出异常的，所以我们没必要使用 try 语句块
    # 假如 group 被误打成了 grop 也没关系，程序马上就会通过 AttributeError 来
    # 告诉我们。
    obj = re.search(r'<title>(.*)</title>', resp.text)
    if not obj:
        print('save failed: title tag not found in page content')
        return False
    title = obj.group(1)

    try:
        with open(filename, 'w') as fp:
            fp.write(title)
    except IOError as e:
        print(f'save failed: unable to write to file {filename}: {e}')
        return False
    else:
        return True
