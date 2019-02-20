# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os
class XiaohuaPipeline(object):
    def process_item(self, item, spider):
        detailURL=item['detailURL']
        path=item['path']
        fileName=item['fileName']
        image=requests.get(detailURL)
        f=open(path,'wb')
        f.write(image.content)
        f.close()
        print(u'正在保存图片：',detailURL)
        print(u'图片路径：',path)
        print(u'文件：',fileName)
        return item
