# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    "Referer": "https://www.meizitu.com/",  # 加入referer 为下载的域名网站
}

class PaimgPipeline(ImagesPipeline):
# get_media_requests(item, info)
# 在工作流程中可以看到，管道会得到图片的URL并从项目中下载。
# 为了这么做，你需要重写 get_media_requests() 方法，并对各个图片URL返回一个Request:
#    
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            # 这里把item传过去，因为后面需要用item里面的name作为文件名
            yield Request(image_url, meta={'item': item}, headers=headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]  # 倒数第一个元素
        filenames = "full/%s/%s" % (item['name'], image_guid)
        # print(filename)
        return filenames

   def thumb_path(self, request, thumb_id, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]  # 倒数第一个元素
        # thumb_id就是setting文件中定义的big small
        filenames = "thumbil/%s/%s/%s" % (thumb_id, item['name'], image_guid)
        return filenames
