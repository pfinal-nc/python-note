# -*- coding:utf-8 -*-
import sqlite3
import os
import sys
import requests
import random


class LgSpider:
    def __init__(self, kewords):
        self.pk = kewords
        self.url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
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
        cookie = {
            "Cookie": " _ga=GA1.2.432750973.1550042291; user_trace_token=20190213151806-821f8f7b-2f5f-11e9-818a-5254005c3644; LGUID=20190213151806-821f9481-2f5f-11e9-818a-5254005c3644; index_location_city=%E4%B8%8A%E6%B5%B7; LG_LOGIN_USER_ID=94a64b4fbd1a74412c5a9a7678eb378f294417647814d5b5; JSESSIONID=ABAAABAAAIAACBI842C0781A3F2F7C51134B796BD95011E; _gid=GA1.2.1382980678.1552446497; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550042292,1550120598,1550733380,1552446497; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168e5b86dbe114-0fca7c07944258-323b5b03-2073600-168e5b86dbf205%22%2C%22%24device_id%22%3A%22168e5b86dbe114-0fca7c07944258-323b5b03-2073600-168e5b86dbf205%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpc_baidu_pc%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; TG-TRACK-CODE=index_search; SEARCH_ID=0ee88abfd82f450cba0b0163b25c4662; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552451906; LGSID=20190313123822-d51d53c0-4549-11e9-9484-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_php%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_php%3Fcity%3D%25E4%25B8%258A%25E6%25B5%25B7%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; LGRID=20190313123822-d51d559e-4549-11e9-9484-5254005c3644",
        }
        json = requests.post(url, data, headers=headers,
                             cookies=cookie, proxies=proxy)
        print(json)
        info_list = []
        result = json['content']['positionResult']['result']
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
