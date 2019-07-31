import requests
import spider
obj = spider.Spilder(r'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0')
data = obj.crawl_list()
print(data)