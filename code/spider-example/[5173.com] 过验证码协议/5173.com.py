import re

import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    ".5173auth": "",
    "__utma": "12194411.1525221879.1684390422.1684390422.1684390422.1",
    "__utmb": "12194411",
    "__utmc": "12194411",
    "__utmz": "12194411.1684390422.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none)",
    "fp": "90a000d145b9f34e2a8def68419fbd3d",
    "trace_5173": "20230426000936e052473567ce9574bf",
    "C3VK": "c75252"
}
url = "https://passport.5173.com/"
session = requests.session()
response = session.get(url, headers=headers, cookies=cookies)

# print(response.text)
# print(response)
info = re.search(r'SecurityToken:"(.*?)",[\s\S]*?PasswordKey:"(.*?)",', response.text)
print(info)