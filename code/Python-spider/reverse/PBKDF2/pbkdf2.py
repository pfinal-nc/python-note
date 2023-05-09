# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 14:08
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : pbkdf2.py
# @Software: PyCharm
import binascii

from Cryptodome.Hash import SHA1
from Cryptodome.Protocol.KDF import PBKDF2

text = 'I lov Python'
salt = b'12345d'

result = PBKDF2(text, salt, count=10, hmac_hash_module=SHA1)
result = binascii.hexlify(result)
print(result)
