# import scrapy
# from scrapy.crawler import CrawlerProcess
#
# class TextSpider(scrapy.Spider):
#     name = 'text_spider'
#
#     def __init__(self, url='', *args, **kwargs):
#         super(TextSpider, self).__init__(*args, **kwargs)
#         self.start_urls = [url]
#
#     def parse(self, response):
#         page_text = response.xpath('//text()').extract()
#         page_text = '\n'.join(text.strip() for text in page_text if text.strip())
#         return page_text
#
#
# def run_text_spider(url):
#     process = CrawlerProcess(settings={
#         'LOG_LEVEL': 'INFO',
#         'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#     })
#
#     process.crawl(TextSpider, url=url)
#     process.start()
#
#


import scrapy
from scrapy.crawler import CrawlerProcess


class TextSpider(scrapy.Spider):
    name = "text"

    def __init__(self, start_url, *args, **kwargs):
        super(TextSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]


def run_text_spider(url) -> str:
    process = CrawlerProcess(settings={
        'LOG_LEVEL': 'INFO',
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    })

    result = ''

    class ResultSpider(TextSpider):
        def parse(self, response):
            nonlocal result
            result = response.xpath('//text()').extract()
            result = '\n'.join(text.strip() for text in result if text.strip())

    process.crawl(ResultSpider, start_url=url)
    process.start()
    return result
