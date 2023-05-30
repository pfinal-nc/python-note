# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 14:55
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : passport.fang.com.py
# @Software: PyCharm
import execjs
import requests

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://passport.fang.com",
    "Pragma": "no-cache",
    "Referer": "https://passport.fang.com/",
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
    """获取加密密码"""
    with open('passport.fang.com.js', 'r', encoding='utf-8') as f:
        fng_js = f.read()
    encrypted_password = execjs.compile(fng_js).call('get_encrypted_password', password)
    return encrypted_password


# fang28745902136

def login(encrypted_password, username):
    """登录"""
    url = "https://passport.fang.com/login.api"
    data = {
        "uid": username,
        "pwd": encrypted_password,
        "Service": "soufun-passport-web",
        "AutoLogin": "1"
    }
    print(data)
    response = requests.post(url, headers=headers, data=data).json()
    print(response)


def main():
    """run """
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    encrypted_password = get_encrypted_password(password)
    login(encrypted_password, username)


if __name__ == '__main__':
    main()
