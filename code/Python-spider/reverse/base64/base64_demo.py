# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 13:43
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : base64_demo.py
# @Software: PyCharm
import base64


def base64_encode(text):
    """base64 encode text """
    encode_data = base64.b64encode(text.encode('utf-8'))
    return encode_data


def base64_decode(text):
    """"base64 decode text """
    decode_data = base64.b64decode(text)
    return decode_data


if __name__ == '__main__':
    text = 'I love Python'
    encode_data = base64_encode(text)
    decode_data = base64_decode(encode_data)
    print('Base64 编码：', encode_data)
    print('Base64 解码：', decode_data)

# Base64 编码：b'SSBsb3ZlIFB5dGhvbiE='
# Base64 解码：b'I love Python!'
