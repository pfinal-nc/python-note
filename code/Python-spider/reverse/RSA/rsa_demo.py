# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 10:09
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : rsa_demo.py.py
# @Software: PyCharm

import rsa as rsa


def rsa_encrypt(pu_key, t):
    """Encrypt"""
    return rsa.encrypt(t.encode("utf-8"), pu_key)


def rsa_decrypt(pr_key, t):
    """私钥解密"""
    return rsa.decrypt(t, pr_key).decode("utf-8")


if __name__ == "__main__":
    public_key, private_key = rsa.newkeys(512)  # 生成公钥、私钥
    print('公钥：', public_key)
    print('私钥：', private_key)
    text = 'I love Python!'  # 加密对象
    encrypted_str = rsa_encrypt(public_key, text)
    print('加密字符串：', encrypted_str)
    decrypted_str = rsa_decrypt(private_key, encrypted_str)
    print('解密字符串：', decrypted_str)
