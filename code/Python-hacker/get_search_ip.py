# -*- coding: UTF-8 -*-
import os
import sys
import json
import requests

file = open(os.path.dirname(sys.argv[0]) + '/phpmyadmin.txt','r+',encoding='utf-8')
content = json.loads(file.read())
matches_list = content.get('matches')
ips = []
for item in matches_list:
    ips.append(item.get('ip')[0])

urls = []
for ip in ips:
    url = 'http://%s/phpmyadmin/index.php' % ip
    response = requests.get(url)
    if response.status_code == 200:
        urls.append(url)
    # urls.append()

print(urls)
