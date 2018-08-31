# -*- coding:utf-8 -*-
import pickle as p
import requests
import json
# 我们要存储内容的文件名
girlfriendlistfile = 'girlfriend.data'

list_json = requests.get('https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=日本女演员&resource_id=28266&stat1=日本&stat0=女&pn=24')
member_list = list_json.json()['data'][0]['result']
print(member_list)
