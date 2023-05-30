import json

import execjs
import requests


def get_sign():
    node = execjs.get()
    with open('sign.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code)
    sign = ctx.call('run')
    return sign[0], sign[1]


def decode_data(data):
    node1 = execjs.get()
    with open('decode.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node1.compile(js_code)
    text = ctx.call('run', data)
    return text


def spider(k):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://fanyi.youdao.com",
        "Referer": "https://fanyi.youdao.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    cookies = {
        "OUTFOX_SEARCH_USER_ID_NCOO": "6976087.043106277",
        "P_INFO": "null",
        "__yadk_uid": "RKjQ2qahP2CGQbOhjIqPZopA1dwOAble",
        "rollNum": "true",
        "OUTFOX_SEARCH_USER_ID": "1495422171@180.168.160.38",
        "advertiseCookie": "advertiseValue",
        "___rl__test__cookies": "1680846871097"
    }
    url = "https://dict.youdao.com/webtranslate"
    sign, mysticTime = get_sign()
    data = {
        "i": str(k),
        "from": "auto",
        "to": "",
        "dictResult": "true",
        "keyid": "webfanyi",
        "sign": sign,
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": mysticTime,
        "keyfrom": "fanyi.web"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    return response.text


if __name__ == '__main__':
    while True:
        eng = input('输入英文,别的别瞎JB输入：')
        encode_txt = spider(eng)
        res = json.loads(decode_data(encode_txt))['dictResult']['ce']['word']['trs']
        for i in res:
            print(i)
