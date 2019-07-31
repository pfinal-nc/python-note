# -*- coding: UTF-8 -*-

import requests
import json
import urllib
import sys
import os

class Zoomeye:

    def __init__(self, username=None, password=None):
        self.access_token = None
        self.resource = None
        if self.access_token is None:
            self._get_access_token(username, password)

    def _get_access_token(self, username, password):
        url = 'https://api.zoomeye.org/user/login'
        params = {
            'username': username,
            'password': password
        }
        response = requests.post(url, data=json.dumps(params))
        # print()
        self.access_token = str(list(json.loads(response.text).values())[0])

    def web_search(self, app, country):
        url = 'https://api.zoomeye.org/web/search'
        headers = {
            'Authorization': 'JWT ' + self.access_token
        }
        query = 'app: %s &country: %s ' % (app,country)
        
        params = {
            'query': query,
            'page': 2
        }
        response = requests.get(url, params=params, headers=headers)
        self.resource = response.text

    def save_resource(self,filename):
        with open(filename, 'w') as f:
            f.write(self.resource)        

if __name__ == "__main__":
    eye = Zoomeye('1370288056@qq.com', '')
    eye.web_search('phpmyadmin', 'China')
    eye.save_resource(os.path.dirname(sys.argv[0]) + '/phpmyadmin.txt')

