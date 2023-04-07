# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 12:38
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : baidu_fanyi.py
# @Software: PyCharm
import execjs
import requests as requests


def get_sign(param):
    node = execjs.get()
    with open('sign.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code)
    sign = ctx.call("getSign", param)
    return sign


def spider(eng):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Acs-Token": "1680842229314_1680842250446_Cmts9HfphZfrPsHC3TUz9vKq2yQJc1uQwVsMTzV/u9wIMCBxIWLSjeT8xmwPDB7RNy8atyrCGBxNPQtO7lGA/pApiZBknMzZAKiZ6wosIxFxnPi2FPaMeq+V7wiPZ5YLyz7J0uYXKdg6p3jbTLqfIfdt4N8uvIgOOd9vl8IR7S/+78yj1pZuMY5ZsP6ElYteHJYjjqh6/MS3e/fgStdgoL3YovZ/tyfA91jdCYqS+17fCFeyUkhEq7x4BF3OK1Y6iXoajl3k/09AydlP7qdT+aupkEkePR4JmgNcbYKCczLt/MGBMxA364xzuzOgkUYQdgvoDY8Lk9/Unfeb/wrfhR1drr+qcygiAU6y6aIGiYFHmOC/7Po/9jlEIBQtlzBq8SfiukkH4Fo37fF9OyAVj/oIxJ5lID8Huo6bDZbdYFzdnmIXXVT+IAppqKnDZuiFIDx6AFJbsld6B6KEgBhjKg==",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://fanyi.baidu.com",
        "Referer": "https://fanyi.baidu.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    cookies = {
        "APPGUIDE_10_0_2": "1",
        "REALTIME_TRANS_SWITCH": "1",
        "FANYI_WORD_SWITCH": "1",
        "HISTORY_SWITCH": "1",
        "SOUND_SPD_SWITCH": "1",
        "SOUND_PREFER_SWITCH": "1",
        "BAIDUID_BFESS": "4C34023BD322B6B59B2235C4F0F4B426:FG=1",
        "BDUSS": "jNaVGYzZUlSeVhpdVB6RW1WeklzdnUwUFhLM2ZmLWFrdC14eGNEQ25NQU5kVkprSVFBQUFBJCQAAAAAAAAAAAEAAABAyoIubGl1eGlhbzc2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3oKmQN6Cpkf",
        "BDUSS_BFESS": "jNaVGYzZUlSeVhpdVB6RW1WeklzdnUwUFhLM2ZmLWFrdC14eGNEQ25NQU5kVkprSVFBQUFBJCQAAAAAAAAAAAEAAABAyoIubGl1eGlhbzc2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3oKmQN6Cpkf",
        "PSTM": "1680580679",
        "BIDUPSID": "73938F10879D52437B9823C60BA02B21",
        "ZFY": "s1mhXybcHt:AB4:AgnH8ysoazNXNmake4oxg0pNSB8IAk:C",
        "BDRCVFR[feWj1Vr5u3D]": "I67x6TjHwwYf0",
        "delPer": "0",
        "PSINO": "2",
        "BCLID": "11330255794450637110",
        "BCLID_BFESS": "11330255794450637110",
        "BDSFRCVID": "lgIOJeC627hKMYOfamVKUOUVteQk_-6TH6aoNdhvVkdG7EGFWJDAEG0PnU8g0KubRh6TogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5",
        "BDSFRCVID_BFESS": "lgIOJeC627hKMYOfamVKUOUVteQk_-6TH6aoNdhvVkdG7EGFWJDAEG0PnU8g0KubRh6TogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5",
        "H_BDCLCKID_SF": "tbADoCK2JKt3jRjd5bO2qRIJMfcKbJQKaDQ03Ru8Kb7VbIoo5fnkbfJBDGJ3BMrlaDcKWlOOQl7lS4be2h0aXT-7yajK25kqJjCO0Uoc2xb4sx3_QbJpQT8rhR_OK5OiJIrNBIQmab3vOIJNXpO1MUtzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjtDJJAD_Ktbf-3bfTrmMtQ_KtFtK2T22-usyHvT2hcH0KLKfnjnDjJDb4_DLpbPWhQpbgbG_p5l-fb1MRjvMqJb3nki2h-eqx692Nc4bq5TtUt5JKnTDMRh-x-B3-QyKMnitIT9-pno0hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuj5LbD5QyDaAsbPtX-TKX3buQQR5r8pcNLTDK5JIr-H0fKtoLBDQP2M5CbpbvqpcoylO1j4_eDPn32lOpLjch5l3tQfjUqh5jDh3mXjksD-RtWCrhJ2vy0hvctn5cShncLUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2b6QhDNLqJ5_ftnAsL-35HtbEHJrlMtr2q4tehHRQB-n9WDTm_Do5KRO0HlcI-tcBMlLg3JjJQbOJBI72-pPKKR7_oDohXTjtLPPOW-n3LfQE3mkjbIOyfn02OP5PQnjxLt4syP4jKxRnWI3mKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCF5hIDljj8bD5Pq-f7J-n8XMDb0WRj-bRj_jRTphCTjhPrMhMJAWMT-0bFH_bncBxTceRjz3xRlXpLZ5MoIah4LJHn7_JjOBJbsfxQcbMtbQf-z3P6R3xQxtNRX-CnjtpvhHxodjlOobUPUDMo9LUvW02cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-DDxj6uK3f",
        "H_BDCLCKID_SF_BFESS": "tbADoCK2JKt3jRjd5bO2qRIJMfcKbJQKaDQ03Ru8Kb7VbIoo5fnkbfJBDGJ3BMrlaDcKWlOOQl7lS4be2h0aXT-7yajK25kqJjCO0Uoc2xb4sx3_QbJpQT8rhR_OK5OiJIrNBIQmab3vOIJNXpO1MUtzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjtDJJAD_Ktbf-3bfTrmMtQ_KtFtK2T22-usyHvT2hcH0KLKfnjnDjJDb4_DLpbPWhQpbgbG_p5l-fb1MRjvMqJb3nki2h-eqx692Nc4bq5TtUt5JKnTDMRh-x-B3-QyKMnitIT9-pno0hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuj5LbD5QyDaAsbPtX-TKX3buQQR5r8pcNLTDK5JIr-H0fKtoLBDQP2M5CbpbvqpcoylO1j4_eDPn32lOpLjch5l3tQfjUqh5jDh3mXjksD-RtWCrhJ2vy0hvctn5cShncLUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2b6QhDNLqJ5_ftnAsL-35HtbEHJrlMtr2q4tehHRQB-n9WDTm_Do5KRO0HlcI-tcBMlLg3JjJQbOJBI72-pPKKR7_oDohXTjtLPPOW-n3LfQE3mkjbIOyfn02OP5PQnjxLt4syP4jKxRnWI3mKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCF5hIDljj8bD5Pq-f7J-n8XMDb0WRj-bRj_jRTphCTjhPrMhMJAWMT-0bFH_bncBxTceRjz3xRlXpLZ5MoIah4LJHn7_JjOBJbsfxQcbMtbQf-z3P6R3xQxtNRX-CnjtpvhHxodjlOobUPUDMo9LUvW02cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-DDxj6uK3f",
        "H_PS_PSSID": "38185_36556_38409_38470_38344_38436_38396_38468_38290_37922_38356_26350_22157_38282_37881",
        "BA_HECTOR": "25810h048k0la405agak8l141i2v4cd1n",
        "ab_sr": "1.0.1_ZDYzMTAxZDdmMmQwYTNjODFjMjJkOGJmZGIzYWEzYjQwMDJjMzc3YjU4YWZjNjA4YjdiYjQ1MDE5ZmU2NTFlZTk5ZWVlZTA5MzA1YjgzMTc4YWE3N2RlMzM5YzM0MjljYmVhNjlmYjk0OThjMWNlOTVmMjkzMTBjZDQxNWE0NTk2ZTJhMTkzOTc1OGM3MDMwNDI1ZmNjZmYyMDA0YWQxZjllYzk3ZjE0MjhkMTE3MDk4YTAwYzRkMjczN2ZiOGY1"
    }
    url = "https://fanyi.baidu.com/v2transapi"
    params = {
        "from": "zh",
        "to": "en"
    }
    data = {
        "from": "zh",
        "to": "en",
        "query": eng,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": get_sign(eng),
        "token": "d7c4ac6e34d72a16c9a8bc7535c3d7e2",
        "domain": "common"
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    import json
    a = json.loads(response.text)
    res = a['trans_result']['data'][0]['dst']
    print("翻译结果:", res)


if __name__ == '__main__':
    while True:
        eng = input('输入中文:')
        spider(eng)
        q = input('是否继续?y/n')
        if q == 'y':
            continue
        elif q == 'n':
            break
        else:
            print('请输入y/n')
