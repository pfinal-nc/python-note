import scrapy


class OuyeelSpider(scrapy.Spider):
    name = "ouyeel"
    allowed_domains = ["ouyeel.com"]
    start_urls = ["http://ouyeel.com/"]

    def parse(self, response):
        pass
