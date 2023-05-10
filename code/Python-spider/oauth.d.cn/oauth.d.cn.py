# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 14:26
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : oauth.d.cn.py
# @Software: PyCharm

import execjs
import requests

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://oauth.d.cn/auth/goLogin.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}


def get_encrypted_password(password):
    """ 解密js """
    with open('oauth.js', 'r', encoding='utf-8') as f:
        weibo_js = f.read()
    encrypted_password = execjs.compile(weibo_js).call('getEncryptedPassword', password)
    return encrypted_password


def login(encrypted_password, username):
    login_url = 'https://oauth.d.cn/auth/login'
    headers = {
        'Host': 'oauth.d.cn',
        'Referer': 'https://oauth.d.cn/auth/goLogin.html',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    params = {
        'display': 'web',
        'name': username,
        'pwd': encrypted_password,
        'to': 'https%3A%2F%2Fwww.d.cn%2F'
    }
    response = requests.get(url=login_url, params=params, headers=headers).json()
    print(response)


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    encrypted_password = get_encrypted_password(password)
    login(encrypted_password, username)


if __name__ == '__main__':
    main()
