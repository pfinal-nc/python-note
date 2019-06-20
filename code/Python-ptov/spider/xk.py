# -*- coding:utf-8 -*-
import requests
import config
import json
import os
import random
import logging


class SpiderXk:
    def __init__(self):
        # super(SpiderXk, self).__init__()
        self.session = requests.session()
        self.home_url = config.PIC_HOST_SEARCH_URL
        self.session.headers['User-Agent'] = config.USER_AGENT

    def get_user_list(self):
        offset = 0
        cup = 'G'
        user_List = self.get_user_json()
        user_info = user_List['artists']
        user_offset = user_List['offset']
        user_list_id = self.get_user_pic(user_info)
        self.get_pic_list(user_list_id)

    def get_user_json(self, cup='G', offset=0, ):
        user_List = self.session.post(self.home_url, {'offset': offset, 'cup': cup})
        return json.loads(user_List.text)

    def get_user_pic(self, user_info):
        user_ids = [];
        if len(user_info) <= 0:
            return False
        for user in user_info:
            if user['name_cn']:
                name_dir = os.getcwd() + '/image/' + user['name_cn']
                user_ids.append([user['id'], name_dir])
            else:
                dir_name = '没名字_' + user['id']
                name_dir = os.getcwd() + '/image/' + dir_name
                user_ids.append([user['id'], name_dir])
            # 创建目录
        return user_ids

    def doweload_pic(self, name, pic_url):
        pic_name = name.replace('/', '\\') + '\\' + str(random.randint(1, 10000)) + '.jpg'
        # print(pic_name)
        pic_url = pic_url.replace('\\', '').replace('//', 'http://')
        # print(self.session.get(pic_url).content)
        try:
            r = self.session.get(pic_url)
            img = r.content
            with open(pic_name, 'wb') as f:
                f.write(img)
            print(pic_name + '下载成功')
            return True
        except Exception as e:
            print(e)
            return False

    def get_pic_list(self, user):
        if len(user) < 0:
            return False
        for val in user:
            # print(val[1])
            if os.path.exists(val[1]) == False:
                os.makedirs(val[1])
            res = self.session.post(config.ATLAS_URL, data={'id': val[0]})
            albums_list = json.loads(res.text)
            root_album = albums_list['root_album']
            if len(albums_list['albums']) > 0:
                for alb in albums_list['albums']:
                    if self.doweload_pic(val[1], root_album + alb['cover']) is False:
                        continue
            if len(os.listdir(val[1])) <= 0:
                os.removedirs(val[1])
