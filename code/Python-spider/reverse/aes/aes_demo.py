# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 09:34
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : aes_demo.py
# @Software: PyCharm
import base64

from Cryptodome.Cipher import AES


def add_to_16(value):
    """Add a value to"""
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)


# 加密方法

def aes_encrypt(key, t, iv):
    """Aes encrypt"""
    aes = AES.new(add_to_16(key), AES.MODE_CBC, add_to_16(iv))
    encrypt_aes = aes.encrypt(add_to_16(t))
    encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码 返回
    return encrypt_text


# 解密方法

def aes_decrypt(key, t, iv):
    aes = AES.new(add_to_16(key), AES.MODE_CBC, add_to_16(iv))  # 初始化加密器
    base64_decrypted = base64.decodebytes(t.encode(encoding='utf-8'))  # 优先逆向解密 base64 成 bytes
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')  # 执行解密密并转码返回str
    return decrypted_text


if __name__ == '__main__':
    secret_key = '12345678'  # 密钥
    text = 'I love Python!'  # 加密对象
    iv = secret_key  # 初始向量
    encrypted_str = aes_encrypt(secret_key, text, iv)
    print('加密字符串：', encrypted_str)
    decrypted_str = aes_decrypt(secret_key, encrypted_str, iv)
    print('解密字符串：', decrypted_str)
