# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 09:00
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : des.py
# @Software: PyCharm
# 加密模式 CBC，填充方式 PAD_PKCS5
import binascii

from pyDes import des, CBC, PAD_PKCS5


def des_encrypt(key, text, iv):
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.encrypt(text, padmode=PAD_PKCS5)
    return binascii.b2a_hex(de)


def des_decrypt(key, text, iv):
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(text), padmode=PAD_PKCS5)
    return de


if __name__ == '__main__':
    secret_key = '12345678'  # 密钥
    text = 'I love Python!'  # 加密对象
    iv = secret_key  # 偏移量
    secret_str = des_encrypt(secret_key, text, iv)
    print('加密字符串：', secret_str)
    clear_str = des_decrypt(secret_key, secret_str, iv)
    print('解密字符串：', clear_str)
