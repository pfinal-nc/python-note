# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 09:51
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : rc4.py
# @Software: PyCharm
import base64

from Cryptodome.Cipher import ARC4


def rc4_encrypt(key, t):
    """Encrypt"""
    enc = ARC4.new(key.encode('utf8'))
    res = enc.encrypt(t.encode('utf-8'))
    res = base64.b64encode(res)
    return res


def rc4_decrypt(key, t):
    """Decrypt"""
    data = base64.b64encode(t)
    enc = ARC4.new(key.encode('utf8'))
    res = enc.decrypt(data)
    return res


if __name__ == '__main__':
    secret_key = '12345678'  # 密钥
    text = 'I love Python!'  # 加密对象
    encrypted_str = rc4_encrypt(secret_key, text)
    print('加密字符串：', encrypted_str)
    decrypted_str = rc4_decrypt(secret_key, encrypted_str)
    print('解密字符串：', decrypted_str)
