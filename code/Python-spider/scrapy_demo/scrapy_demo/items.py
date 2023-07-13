# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    """ScrapyDemoItem"""
    # define the fields for your item here like:
    # name = scrapy.Field()
    webname = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    source_name = scrapy.Field()
    pushddate = scrapy.Field()
    content = scrapy.Field()
    created_at = scrapy.Field()  # 创建时间
    updated_at = scrapy.Field()  # 更新时间
