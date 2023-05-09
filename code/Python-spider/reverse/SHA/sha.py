# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 14:27
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : sha.py
# @Software: PyCharm
import hashlib


def sha1_test1():
    """sha1 test1"""
    sha1 = hashlib.new('sha1', 'I love python!'.encode('utf-8'))
    print(sha1.hexdigest())


def sha1_test2():
    """sha1 test2"""
    sha1 = hashlib.sha1()
    sha1.update('I love python!'.encode('utf-8'))
    print(sha1.hexdigest())


if __name__ == '__main__':
    sha1_test1()
    sha1_test2()
