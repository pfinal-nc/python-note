# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 09:13
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 3des.py
# @Software: PyCharm
from Cryptodome import Random
from Cryptodome.Cipher import DES3


# 需要 补位， str不是16的倍数  那就补

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)


def des_encrypt(key, text, iv):
    # 加密模式 OFB
    cipher_encrypt = DES3.new(add_to_16(key), DES3.MODE_OFB, iv)
    encrypted_text = cipher_encrypt.encrypt(text.encode("utf-8"))
    return encrypted_text


def des_decrypt(key, text, iv):
    # 加密模式 OFB
    cipher_decrypt = DES3.new(add_to_16(key), DES3.MODE_OFB, iv)
    decrypted_text = cipher_decrypt.decrypt(text)
    return decrypted_text


if __name__ == '__main__':
    key = '12345678'  # 密钥，16 位
    text = 'I love Python!'  # 加密对象
    iv = Random.new().read(DES3.block_size)  # DES3.block_size == 8
    secret_str = des_encrypt(key, text, iv)
    print('加密字符串：', secret_str)
    clear_str = des_decrypt(key, secret_str, iv)
    print('解密字符串：', clear_str)
