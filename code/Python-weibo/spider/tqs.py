# -*- coding: utf-8 -*-
import json
import random
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "http://tb.pfinal.club/ajax-list?page=" + str(random.randint(1, 100))

class TqsParse(Spider):
    def __init__(self):
        super(TqsParse, self).__init__(HOME_URL)

    def get_weibo_message(self):
        msg=''
        json_text = self.download_text()
        items = self.getItems(json_text)
        count = len(items)
        # print(count)
        if count > 0:
            index = random.randint(0, count - 1)
            msg = items[index]
            #print(msg["text"])
        return WeiboMessage(msg["text"],msg["images"])
        # return json_text  

    def getItems(self, jsonStr):
        items = []
        nodes = json.loads(jsonStr)
        results = nodes["data"]
        for node in results: 
            msg = node["name"] + '【优惠券领取】'
            url = "http://tb.pfinal.club/"
            item = "%s %s" % (msg, url)
            items.append({"text":item,"images":[node["z_img"],node["z_img"],node["z_img"]]})
        return items