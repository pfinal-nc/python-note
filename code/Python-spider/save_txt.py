import requests
from pyquery import PyQuery as pq

url = 'https://juejin.im/search?query=Python'

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url,headers).text
doc = pq(html)
items = doc('.content-box .title').items()
for item in items:
    # print(item.text())
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'+ item.text())
    file.close()

