# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 17:52
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : hmac_demo.py
# @Software: PyCharm
import hmac


def hamc_test1():
    """hamc_test"""
    message = b'I love python!'
    key = b'secret'
    md5 = hmac.new(key, message, digestmod='MD5')
    print(md5.hexdigest())


def hamc_test2():
    """hamc_test"""
    key = 'secret'.encode('utf8')
    sha1 = hmac.new(key, digestmod='sha1')
    sha1.update('I love '.encode('utf8'))
    sha1.update('Python!'.encode('utf8'))
    print(sha1.hexdigest())


if __name__ == '__main__':
    hamc_test2()
    hamc_test1()
