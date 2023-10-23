# -*- coding: utf-8 -*-
# @Time    : 2023/10/20 17:45
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : get_phone_code.py
# @Software: PyCharm
import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.php.cn",
    "Pragma": "no-cache",
    "Referer": "https://www.php.cn/account/login.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "Hm_lvt_c0e685c8743351838d2a7db1c49abd56": "1697377670",
    "phpcndatauser_from": "www.php.cn%2F",
    "PHPSESSID": "g2sb1qvhf4rlb4ev570mdd3lp2"
}
url = "https://www.php.cn/index.php/account/get_code_token/"
data = {
    "phone": "17721213677"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)

