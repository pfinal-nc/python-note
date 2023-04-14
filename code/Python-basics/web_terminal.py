# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 09:53
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : web_terminal.py
# @Software: PyCharm
import requests

url = "https://api.newrank.cn/api/sync/weixin/account/articles_content"

payload='account=gh_256cabfe335b&from=2023-03-04%2000%3A00%3A00&to=2023-04-04%2000%3A00%3A00&page=1&size=20'
headers = {
  'Key': '0691bc14880a46848e6511817',
  'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
