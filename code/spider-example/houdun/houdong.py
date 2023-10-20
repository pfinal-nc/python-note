# -*- coding: utf-8 -*-
# @Time    : 2023/10/20 14:06
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : houdong.py
# @Software: PyCharm
import json

import ddddocr
import requests
from retrying import retry

headers = {
    "authority": "www.houdunren.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.houdunren.com/login",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}


# cookies = {
#     "X_CACHE_KEY": "cbb58113db55fe18d8c9d96234eebd1f",
#     "XSRF-TOKEN": "eyJpdiI6IllxREhDb0NyNTMyZVpuL1JqRWN6UWc9PSIsInZhbHVlIjoid0xEVGpRNXhGemh4L29mOGlUSkNSRlgyVDN2RHNpZ3NmOEVLSGNibVNIKzMwODErcjZ5WlBoZHZaV09yM2kzSkVyd0QxaElrWWNONWRWSHpGWnJEek1tWGw5RVpNMTBzU0x0TmYzcTZqQnI3c0RhbjFRWGM4VjM3cjBVc3YySHoiLCJtYWMiOiJmZDI2NGQ4MTQyNTIyNDY4MDU2NDk4NzFiNGRkZDZhMjg0OTExYjIzZjA5MzE2NzI4ODllOTc3ZWYwMTcyNzYyIiwidGFnIjoiIn0%3D",
#     "hdcms_session": "eyJpdiI6IkJtUmRieE5KNmJOcjhML2dyeUtjNXc9PSIsInZhbHVlIjoiM2tuOHVPZlZuVDVhcVZDbzUyNm12T0ZIUHRWQXFlUSt5Wi9FVmsyNXlsZW8xVU9sR202UUJDTGE2cUVDTlRzelVjRndUYmlTcDVNNm1rTlZNSTVlaEMvRXRKbmlkNDNQTU1xaXczM2NvSThJQkdpbTBROFIramY2ekd3S1kxWG8iLCJtYWMiOiJhMTI1M2FkMTMwNzFhZTY2NjRlOTE3Y2E4NzBkNDZiNDk4YjA3YTJjMzM3NzRiY2Q5ZTY5YmI1Nzk3MDA5OGUyIiwidGFnIjoiIn0%3D"
# }

@retry(stop_max_attempt_number=5)
def get_captcha():
    """get_captcha"""
    url = "https://www.houdunren.com/captcha/api/math"
    response = requests.get(url, headers=headers)
    captcha_img = response.json()
    # print(response.text)
    # print(captcha_img['key'])
    print(captcha_img['img'].strip('data:image/png;base64').strip(','))
    ocr = ddddocr.DdddOcr()
    code = ocr.classification(captcha_img['img'].strip('data:image/png;base64').strip(','))
    print(code)
    if '+' in code:
        num = int(code.split('+')[0]) + int(code.split('+')[1])
    elif '-' in code:
        num = int(code.split('-')[0]) - int(code.split('-')[1])
    elif 'x' in code:
        num = int(code.split('x')[0] * int(code.split('x')[1]))
    else:
        raise Exception('Invalid code')
    return captcha_img['key'], num


if __name__ == '__main__':
    captcha_key, captcha = get_captcha()
    login_url = "https://www.houdunren.com/api/auth/login"
    data = {
        "account": "1111",
        "password": "123123",
        "password_confirmation": "",
        "captcha": captcha,
        "captcha_key": captcha_key,
        "code": ""
    }
    data = json.dumps(data, separators=(',', ':'))
    print(data)
    response = requests.post(login_url, headers=headers, data=data, cookies=cookies)
    print(response.json())
