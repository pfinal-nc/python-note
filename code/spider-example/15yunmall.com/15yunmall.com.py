# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 15:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 15yunmall.com.py
# @Software: PyCharm
import ddddocr
import execjs
import requests
from lxml import etree

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://www.15yunmall.com",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://www.15yunmall.com/pc/login/index",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
session = requests.session()
index_url = 'http://www.15yunmall.com/pc/login/index'
code_url = 'http://www.15yunmall.com/very/code.html'
login_url = 'http://www.15yunmall.com/pc/login/check'


def get_csrf_token_cookie():
    """

    @return:
    """
    response = session.get(url=index_url, headers=headers)
    tree = etree.HTML(response.text)
    csrf_token = tree.xpath("//input[@name='_csrfToken']/@value")[0]
    cookies = response.cookies.get_dict()
    # print(csrf_token, cookies)
    return csrf_token, cookies


def get_very_code(cookies):
    response = session.get(url=code_url, cookies=cookies, headers=headers)
    with open('code.png', 'wb') as f:
        f.write(response.content)
    ocr = ddddocr.DdddOcr()
    from PIL import Image
    image = Image.open('code.png')
    # res =  ocr.classification(image)
    # print(res)
    # return res
    image.show()
    very_code = input('请输入验证码: ')
    return very_code


def get_encrypted_password(password):
    """Get the encrypted"""
    with open('15yunmall.com.js', 'r', encoding="utf-8") as f:
        yunmall_js = f.read()
    encrypted_password = execjs.compile(yunmall_js).call('getEncryptedPassword', password)
    return encrypted_password


def login(csrf_token, very_code, cookies, username, encrypted_password):
    """Login  the user"""
    data = {
        'u[loginType]': 'name',
        'u[phone]': username,
        'u[password]': encrypted_password,
        'u[veryCode]': very_code,
        'u[token]': '',
        '_csrfToken': csrf_token
    }
    header_info = {
        'X-Requested-With': 'XMLHttpRequest',
    }
    headers.update(header_info)
    response = session.post(url=login_url, data=data, cookies=cookies, headers=headers)
    response.encoding = 'utf-8-sig'
    response_code = response.text
    # print(response_code)
    status_code = {
        '31': '恭喜，登陆成功。',
        '32': '登陆失败。',
        '33': '用户名或密码错误。',
        '35': '该用户已被管理员锁定。',
        '311': '该账号已绑定设备，请在绑定的设备登陆。',
        '20001': '验证码填写错误!'
    }
    try:
        print(status_code[response_code])
    except KeyError:
        print('请求超时！')


if __name__ == '__main__':
    """run """
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    encrypted_password = get_encrypted_password(password)
    csrf_token, cookies = get_csrf_token_cookie()
    very_code = get_very_code(cookies)
    login(csrf_token, very_code, cookies, username, encrypted_password)
