import datetime

import scrapy

from scrapy_demo.items import ScrapyDemoItem


class CdhptxwSpider(scrapy.Spider):
    """Spider"""
    name = "cdhptxw"
    allowed_domains = ["cdhptxw.com"]
    pagesize = 1
    url = 'https://www.cdhptxw.com/mryt/list_{}.html'
    start_urls = ["https://www.cdhptxw.com/mryt/"]

    def parse(self, response):
        """

        :param response:
        """
        li_list = response.xpath('/html/body/section/div[2]/div/article')
        end_day = '2022-11-21 00:00:00'
        item_day = ''
        for li in li_list:
            title = li.xpath('.//header/h2/a/text()').get()
            category = li.xpath('.//header/a/text()').get()
            detail_url = li.xpath('.//header/h2/a/@href').get()
            # 封装数据
            item = ScrapyDemoItem()
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item['category'] = category
            item['title'] = title
            item['created_at'] = str(date)
            item['updated_at'] = str(date)
            item['webname'] = '问天票据'
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})
            # yield item
        # 构造下一页的请求
        self.pagesize += 1
        url = self.url.format(self.pagesize)
        if len(li_list) > 0:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_detail(self, response):
        """Parse a detail"""
        detail_content = source_name = ''
        item = response.request.meta['item']
        ctime = response.xpath('/html/body/section/div[2]/div/header/div/time/text()').get()
        if ctime:
            item['pushddate'] = ctime + ':00'
        content_html = response.xpath('/html/body/section/div[2]/div/article')
        print(response)

