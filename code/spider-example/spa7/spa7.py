# -*- coding: utf-8 -*-
# @Time    : 2023/10/20 14:45
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : spa7.py
# @Software: PyCharm
import base64
import json

import execjs
from pyDes import des, PAD_PKCS5


#
#     getToken(player) {
#       let key = CryptoJS.enc.Utf8.parse(this.key)
#       const {name, birthday, height, weight} = player
#       let base64Name = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(name))
#       let encrypted = CryptoJS.DES.encrypt(`${base64Name}${birthday}${height}${weight}`, key, {
#         mode: CryptoJS.mode.ECB,
#         padding: CryptoJS.pad.Pkcs7
#       })
#       return encrypted.toString()
#     }
#

def des_encrypt(key, text):
    k = des("0" * 8, padmode=PAD_PKCS5)
    k.setKey(key)
    de = k.encrypt(text, padmode=PAD_PKCS5)
    return base64.b64encode(de).decode()


player = {
    "name": '凯文-杜兰特',
    "image": 'durant.png',
    "birthday": '1988-09-29',
    "height": '208cm',
    "weight": '108.9KG'
}
# python 实现
# key = "fipFfVsZsTda94hJNKJfLoaqyqMZFFimwLt"
# secret_key = key.encode('utf-8')
# print(secret_key)
# bname = base64.b64encode(bytes(player["name"], encoding="utf-8"))
# print(str(bname, encoding="utf-8"))
#
# to_encrypt_str = "{}{}{}{}".format(str(bname, encoding="utf-8"), player["birthday"], player["height"], player["weight"])
# print(to_encrypt_str)
# print(des_encrypt(secret_key, to_encrypt_str))

node = execjs.get()
ctx = node.compile(open('spa7.js').read())
js = f"getToken({json.dumps(player, ensure_ascii=False)})"
print(js)
result = ctx.eval(js)
print(result)