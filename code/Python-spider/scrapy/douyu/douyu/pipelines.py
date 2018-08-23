# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import pymysql
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

class DouyuPipeline(ImagesPipeline):
    # 获取配置文件中配置的图片存储路径
    IMAGES_STORE=get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        # 修改图片保存名称为主播昵称
        os.rename(self.IMAGES_STORE + image_paths[0], self.IMAGES_STORE + 'full/' + item["nickname"] + ".jpg")
        item['image_paths'] = self.IMAGES_STORE+'full/'+item["nickname"]

        return item