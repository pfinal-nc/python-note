import hashlib
import random
import time

import execjs
import requests

translate_url = 'https://dict.youdao.com/webtranslate'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'


def get_translation_result(parameters):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://fanyi.youdao.com",
        "Pragma": "no-cache",
        "Referer": "https://fanyi.youdao.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    cookies = {
        "OUTFOX_SEARCH_USER_ID": "1574753563@180.168.160.38"
    }
    response = requests.post(url=translate_url, cookies=cookies, headers=headers, data=parameters)
    print(response.text)
    # result = response.json()['translateResult'][0][0]['tgt']
    # return result


def get_parameters_by_python(query, translate_from, translate_to):
    lts = str(int(time.time() * 1000))  # 以毫秒为单位的 13 位时间戳
    salt = lts + str(random.randint(0, 9))  # 13 位时间戳+随机数字，生成 salt 值
    sign = "fanyideskweb" + query + salt + "Y2FYu%TNSbMCxc3t2u^XT"  # 拼接字符串组成 sign
    sign = hashlib.md5(sign.encode()).hexdigest()  # 将 sign 进行 MD5 加密，生成最终 sign 值
    parameters = {
        'i': query,
        'from': translate_from,
        'to': translate_to,
        "domain": "0",
        "dictResult": "true",
        "keyid": "webfanyi",
        "sign": sign,
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": "1684236145023",
        "keyfrom": "fanyi.web"
    }
    return parameters


def get_parameters_by_javascript(query, translate_from, translate_to):
    with open('youdao.js', 'r', encoding='utf-8') as f:
        youdao_js = f.read()
    params = execjs.compile(youdao_js).call('getEncryptedParams')  # 通过 JavaScript 代码获取各个参数
    print(params)
    parameters = {
        'i': query,
        'from': translate_from,
        'to': translate_to,
        "domain": 0,
        "dictResult": "true",
        "keyid": "webfanyi",
        'sign': params['sign'],
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        'mysticTime': params["t"],
        'keyfrom': 'fanyi.web'
    }
    return parameters


def main():
    query = input('请输入要翻译的文字：')
    # 原始语言，目标语言，默认自动处理
    translate_from = 'auto'
    translate_to = ''
    # 通过 Python 获取加密参数或者通过 JavaScript 获取参数，二选一
    param = get_parameters_by_javascript(query, translate_from, translate_to)
    print(param)
    # param = get_parameters_by_javascript(query, translate_from, translate_to)
    result = get_translation_result(param)
    print('翻译的结果为：', result)


if __name__ == '__main__':
    main()
