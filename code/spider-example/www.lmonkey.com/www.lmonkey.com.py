# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 09:49
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : www.lmonkey.com.py
# @Software: PyCharm
import csv

import requests
from lxml import etree

headers = {
    "authority": "www.lmonkey.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.lmonkey.com/t?include=creator,column,tags&current=3",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}


# url = "https://www.lmonkey.com/t"
# params = {
#     "include": "creator,column,tags",
#     "current": "4"
# }
# response = requests.get(url, headers=headers, params=params)
#
# print(response.content.decode("utf-8"))
# print(response)

def main():
    """抓取 """
    url = "https://www.lmonkey.com/t"
    i = 1
    with  open('data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['问题名称', 'URL', '浏览量', '标签'])
        while i <= 15:
            params = {
                "include": "creator,column,tags",
                "current": i
            }
            response = requests.get(url, headers=headers, params=params)
            i += 1
            html = etree.HTML(response.content.decode("utf-8"))
            topic_list = html.xpath('//li[@class="item  itemhh"]')
            for topic in topic_list:
                topic_title = topic.xpath('./div/div[2]/div/div[1]/a/text()')[0].strip()
                topic_href = topic.xpath('./div/div[2]/div/div[1]/a/@href')[0]
                topic_watch_num = topic.xpath('./div/div[2]/div/ul/li[1]/span/text()')[0]
                topic_label = topic.xpath('./div/div[1]/div[3]/a[3]/text()')[0]
                print(topic_title, topic_href, topic_watch_num, topic_label)
                writer.writerow([topic_title, topic_href, topic_watch_num, topic_label])


if __name__ == '__main__':
    main()
