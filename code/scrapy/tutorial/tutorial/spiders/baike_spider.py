# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from tutorial.items import TutorialItem

from scrapy.contrib.spiders import CrawlSpider, Rule 
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

i=0
not_data = 0 #统计未采集到的条数
class BaikeSpider(CrawlSpider): 

   name = "baike" 
   #减慢爬取速度 为1s
   # download_delay = 1
   allowed_domains = ['baike.baidu.com'] 
   start_urls = [ 
       "http://baike.baidu.com/fenlei/互联网"
   ]

   

   rules =[
        Rule(SgmlLinkExtractor(allow=('/?limit=30&index=([\w]+)&offset=([\d]+)\#gotoList', ),)),
        Rule(SgmlLinkExtractor(allow=('/view/', ), 
          restrict_xpaths=('//div[@class="list"]')),
          callback='parse_item',
          ),
   ]

   def parse_item(self, response):
    global i,not_data
    i+= 1 #记录抓取条数
    print(i)
    item = BaikeItem() 
    sel = HtmlXPathSelector(response) 
    baike_url = str(response.url)
    baike_name = sel.xpath('//div[@id="sec-content0"]/h1/span[@class="lemmaTitleH1"]/text()').extract() 
    baike_desc = sel.xpath('//div[@class="card-summary-content"]/div[@class="para"]/text()').extract()[0]


    if not baike_name:
      not_data+=1 #记录未抓取到的条数
      print(not_data)


    if not baike_desc:
      baike_desc = '未抓取到'
      

    item['title'] = [n.encode('utf-8') for n in baike_name] 
    item['link'] = baike_url.encode('utf-8') 
    item['desc'] = baike_desc
   
    yield item