#-*- coding:utf-8 -*-
import requests
import time
from lxml import etree

# url = "https://movie.douban.com/subject/26942674/"

class Spilder(object):
    def __init__(self,url):
        self.url = url

    def crawl_details(self,url):
        data = requests.get(url).text
        # print(data)
        s = etree.HTML(data)
        # print(s)
        # //*[@id="content"]/h1/span[1]  电影名
        # //*[@id="info"]/span[1]/span[2]/a 导演
        # //*[@id="info"]/span[2]/span[2]/a 编剧
        # //*[@id="info"]/span[3]/span[2]  主演
        # //*[@id="interest_sectl"]/div[1]/div[2]/strong 评分
        file_name = s.xpath('//*[@id="content"]/h1/span[1]/text()')
        director = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()') # 导演
        Screenwriter = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()') # 编剧
        star = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')  # 主演
        score = s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()') # 评分
        # 导演不止一人
        ds = []
        for d in director:
            ds.append(d)
        # 演员不止一人
        acs = []
        for a in star:
            acs.append(a)
        # 编剧不止一人
        scr = []
        for f in Screenwriter:
            scr.append(f)
        # print(data);
        data = {'name':file_name,'director':ds,'scr':scr,'acs':acs,'score':score}
        return data
    # 获取豆瓣电影中的列表数据
    def crawl_list(self):
        data = requests.get(self.url).json()
        info = []
        for item in data['subjects']:
            # print(item['url']);
            if item['url']!=None:
                info.append(self.crawl_details(item['url']))
        return info  
        
            
