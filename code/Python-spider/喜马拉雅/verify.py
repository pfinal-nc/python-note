# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 19:14
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : verify.py
# @Software: PyCharm
import ddddocr as ddddocr
import requests as requests

headers = {
    "authority": "mobile.ximalaya.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://www.ximalaya.com",
    "pragma": "no-cache",
    "referer": "https://www.ximalaya.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}


def verify_slide():
    """"Check"""
    params = {
        "bpId": 139,
        "sessionId": "xm_lhg5lr9ofy9fqk"
    }
    url = "https://mobile.ximalaya.com/captcha-web/check/slide/get"
    params = {
        "bpId": "139",
        "sessionId": "xm_lhg5lr9ofy9fqk"
    }
    response = requests.get(url, headers=headers, params=params).json()
    data = response['data']
    print(response)
    # 保存2张图片
    image_url_list = {"fg": data["fgUrl"], "bg": data["bgUrl"]}
    for k, v in image_url_list.items():
        rr = requests.get(v, headers=headers)
        with open(f"{k}.png", "wb") as f:
            f.write(rr.content)
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    with open('fg.png', 'rb') as f:
        fg_bytes = f.read()
    with open('bg.png', 'rb') as f:
        bg_bytes = f.read()
    res = det.slide_match(fg_bytes, bg_bytes, simple_target=True)
    print(res)


if __name__ == '__main__':
    verify_slide()
