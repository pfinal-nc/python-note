# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 09:53
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : tenhou.net.py
# @Software: PyCharm
import execjs


def main():
    """Construct"""
    params = {
        "q": "3369m237p2379s67z5z"
    }
    with open('tenhou.net.js', 'r', encoding='utf-8') as f:
        tenhou_js = f.read()
    data = execjs.compile(tenhou_js).call('fa', params["q"])
    print(data)


if __name__ == '__main__':
    main()
