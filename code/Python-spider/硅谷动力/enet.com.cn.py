# -*- coding: utf-8 -*-
# @Time    : 2023/5/17 15:16
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : enet.com.cn.py
# @Software: PyCharm
import csv

import requests
from lxml import etree

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Referer": "https://www.google.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}


# cookies = {
#     "XSRF-TOKEN": "eyJpdiI6ImtYNXVLb0ViVG14dndTRXpoendyaWc9PSIsInZhbHVlIjoiazJCVWErckYzenc3OTh6R242NmVlL3FEQ1I4QXRNNVJXUEVpbE5yNk1CRXJuK2lFYm1PWngwSzAyTktNaHR1WGRabS9CMU1XVEZQZzJjRzdGNXNpT0RUVmx2aWhnT01tT3RUNERhdk5hd3FFRnhxSTRIVXBQREpNajgyUm1ucGkiLCJtYWMiOiJlY2ZmZmJhYjkxMWViNWIzZjdkODQwODkwNmQ1MTY5NzRhMDBjZmVlMjc5MjJjNWVjYThkMDI3NTcxNWYxZWQzIn0%3D",
#     "enet_session": "eyJpdiI6ImVHR0FhZEdkRVY0a29GdE14V0dJL0E9PSIsInZhbHVlIjoiZGZmTUVpNGprRTNNSlVYcjlTd3dSbUx6TzRES2lJVndFOCtjbkFERVoyQW5vUnFrYk14NmIxZFE1UWoyQUZFZkloazdkZ1BaR0FuSUdYMFlCRzNiYVRieU9TTGF2ZmZCTGo2eGNQSkFiYWVQM3lYK2dYbTBRd0J4RHZRTEVNTWgiLCJtYWMiOiJiMGE2NDA1MTg2N2RhY2QyMDk5YmFkNGViOGIwYTc4MGEzNmVhZjUwNDhjNDVlMTIxY2ZhNWMwOWYyODc3NDIwIn0%3D"
# }


# print(response.text)
# print(response)

def main():
    url = "http://enet.com.cn/article/2022/0525/A202205251267187.html"
    response = requests.get(url, headers=headers, verify=False)
    html = etree.HTML(response.content.decode('utf-8'))
    tr_list = html.xpath("/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr")
    with open('data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['品牌', '影响力', '智能化', '突破性', '综合'])
        for tr in tr_list:
            row = [tr.xpath("./td[2]/text()")[0], tr.xpath("./td[3]/text()")[0], tr.xpath("./td[4]/text()")[0], tr.xpath("./td[5]/text()")[0]]
            print(row)
            writer.writerow(row)


if __name__ == '__main__':
    main()
