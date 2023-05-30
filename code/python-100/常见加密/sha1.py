# -*- coding: utf-8 -*-
# @Time    : 2023/5/29 15:38
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : sha1.py
# @Software: PyCharm
import hashlib


# sha1 加密方式
def sha1(data):
    sha1 = hashlib.sha1()
    sha1.update(data.encode('utf-8'))
    return sha1.hexdigest()


# sha256算法
def sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

