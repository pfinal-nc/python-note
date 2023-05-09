# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 13:56
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : md5.py
# @Software: PyCharm
import hashlib


def md5_test1():
    """md5 test"""
    md5 = hashlib.new('md5', 'I love python!'.encode('utf-8'))
    print(md5.hexdigest())


def md5_test2():
    """md5 test"""
    md5 = hashlib.md5()
    md5.update('I love '.encode('utf-8'))
    md5.update('python!'.encode('utf-8'))
    print(md5.hexdigest())


if __name__ == '__main__':
    md5_test1()  # 21169ee3acd4a24e1fcb4322cfd9a2b8
    md5_test2()  # 21169ee3acd4a24e1fcb4322cfd9a2b8
