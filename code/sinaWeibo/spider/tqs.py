# -*- coding: utf-8 -*-
import json
from __future__ import absolute_import
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "http://tb.pfinal.club/ajax-list"

class GetTaoBaoParse(Spider) {
    def __init__(self):
        super(MiaopaParser, self).__init__(HOME_URL)

    def get_weibo_message(self):
        json_text = self.download_text()
        items = self.getItems(json_text)

    def getItems(self, jsonStr):
        nodes = json.loads(jsonStr)
        print(nodes)
}