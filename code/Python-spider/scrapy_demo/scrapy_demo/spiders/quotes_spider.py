import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://learnku.com/go/c/translations?page=1',
        'https://learnku.com/go/c/translations?page=2',
    ]

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.xpath('/html/body/div[2]/div[1]/div/div[1]/div/div/div[4]/div[1]/a/span[1]::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
