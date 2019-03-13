# -*- coding:utf-8 -*-
import sqlite3
import os
import sys
import requests
import random
import time
import json


class LgSpider:
    def __init__(self, kewords):
        self.pk = kewords
        self.url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
        self.url_start = "https://www.lagou.com/jobs/list_运维?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput="
        self.set_table()
        self.data_path = os.path.dirname(sys.argv[0]) + '/lagou.db'

    def set_table(self):
        self.conn = sqlite3.connect(os.path.dirname(sys.argv[0]) + '/lagou.db')
        try:
            sql = 'CREATE TABLE IF NOT EXISTS ' + self.pk + \
                '(ID INT PRIMARY KEY  NOT NULL,city  CHAR(50),district CHAR(255),companyFullName CHAR(255),industryField CHAR(255),education CHAR(255),salary CHAR(100));'
            self.conn.execute(sql)
            self.conn.commit()
            self.conn.close()
        except:
            return False

    def get_json(self, url, page, pk):
        data = {'first': 'false', 'pn': page, 'kd': pk}
        proxy_list = [
            {"http": "58.240.53.194:8080"},
            {"http": "140.143.142.218:1080"},
            # {"http": "60.165.54.153:8060"},
            # {"http": "58.243.50.184:53281"}
        ]
        proxy = random.choice(proxy_list)
        headers = {
            "Host": "www.lagou.com",
            'content-type': 'application/json',
            "Referer": "https://www.lagou.com/jobs/list_php",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36   "
        }
        s = requests.Session()
        s.get(self.url_start, headers=headers, timeout=3)  # 请求首页获取cookies
        cookie = s.cookies

        response = s.post(url, data, headers=headers,
                                 cookies=cookie, timeout=3)
        response.encoding = response.apparent_encoding
        contents = json.loads(response.text)
        print(contents)
        time.sleep(5)
        info_list = []
        result = contents['content']['positionResult']['result']
        for i in result:
            info = [i['city'], i['district'], i['companyFullName'], i['companyShortName'], i['industryField'], i['education'],
                    i['salary']]
            info_list.append(info)
        return info_list

    def save_data(self, data):
        conn = sqlite3.connect(self.data_path)
        c = conn.cursor()
        for item in data:
            insert_data = [item['city'], ]

    def get_content(self):
        page = 1
        info_result = []
        while page < 31:
            info = self.get_json(self.url, page, self.pk)
            info_result = info_result + info
            # print(info_result)
            page += 1
        print(info_result)
        # self.save_data(info_result)


if __name__ == "__main__":
    Lg = LgSpider('php')
    Lg.get_content()
