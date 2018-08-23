# -*- coding:utf-8 -*-

import json
import scrapy
from douyu.items import DouyuItem
class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains=['douyucdn.cn',]
    offset=0
    base_url='http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls=[base_url+str(offset),]

    def parse(self,response):

        content = response.text
        data = json.loads(content)['data']

        for i in data:
            image_url = i['vertical_src']
            nickname = i['nickname']
            item = DouyuItem()
            item['image_urls']=[image_url]
            item['nickname']=nickname
            yield item

        if self.offset < 2300:
            self.offset+=20
            yield scrapy.Request(url=self.base_url+str(self.offset),callback=self.parse)
