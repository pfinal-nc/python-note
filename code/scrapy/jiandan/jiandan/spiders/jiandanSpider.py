import scrapy
from jiandan.items import JiandanItem
class jiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = []
    start_urls = ["http://jandan.net/ooxx"]

    def parse(self,response):
        item = JiandanItem()
        item['image_urls'] = response.xpath('//img//@src').extract()#提取图片链接
        yield item
        '''
        //*[@id="comments"]/div[3]/div/a[3]
        //*[@id="comments"]/div[3]/div/a[1]
        '''
        new_url = response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()
        print(new_url);
        if new_url:
            yield scrapy.Request(new_url,callback=self.parse)

