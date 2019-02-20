# import requests
from requests import  Request,Session
# 代理设置

# proxies = {
#     "http": "http://10.10.1.10:3128",
#     "https": "http://10.10.1.10:1080",
# }
# requests.get("https://www.taobao.com", proxies=proxies)

# 设置超时
# r = requests.get('https://www.taobao.com',timeout=1)
# print(r.status_code)

# Prepared Request
url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)